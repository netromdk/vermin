import ast
import re

from .rules import MOD_MEM_REQS, KWARGS_REQS
from .config import Config
from .printing import nprint, vvprint, vvvprint
from .utility import dotted_name, reverse_range

STRFTIME_DIRECTIVE_REGEX = re.compile(r"(%\w)")

class SourceVisitor(ast.NodeVisitor):
  def __init__(self):
    super(SourceVisitor, self).__init__()
    self.__import = False
    self.__modules = []
    self.__members = []
    self.__printv2 = False
    self.__printv3 = False
    self.__format = False  # TODO: Maybe remove this because it's in builtin functions in rules?
    self.__longv2 = False
    self.__bytesv3 = False
    self.__fstrings = False
    self.__bool_const = False
    self.__function_name = None
    self.__kwargs = []
    self.__depth = 0
    self.__strftime_directives = []

    # Imported members of modules, like "exc_clear" of "sys".
    self.__import_mem_mod = {}

    # Name -> name resolutions.
    self.__name_res = {}

    # User-defined symbols to be ignored.
    self.__user_defs = []

  def modules(self):
    return self.__modules

  def members(self):
    return self.__members

  def printv2(self):
    return self.__printv2

  def printv3(self):
    return self.__printv3

  def format(self):
    return self.__format

  def longv2(self):
    return self.__longv2

  def bytesv3(self):
    return self.__bytesv3

  def fstrings(self):
    return self.__fstrings

  def bool_const(self):
    return self.__bool_const

  def kwargs(self):
    return self.__kwargs

  def strftime_directives(self):
    return self.__strftime_directives

  def user_defined(self):
    return self.__user_defs

  def __add_module(self, module):
    if module in self.__user_defs:
      vvvprint("Ignoring module '{}' because it's user-defined!".format(module))
      return

    if module not in self.__modules:
      self.__modules.append(module)

  def __add_member(self, member):
    """Add member if fully-qualified name is known."""
    if member in self.__user_defs:
      vvvprint("Ignoring member '{}' because it's user-defined!".format(member))
      return

    if member in MOD_MEM_REQS:
      self.__members.append(member)

  def __add_kwargs(self, function, keyword):
    if function in self.__user_defs:
      vvvprint("Ignoring function '{}' because it's user-defined!".format(function))
      return

    fn_kw = (function, keyword)
    if fn_kw in KWARGS_REQS and fn_kw not in self.__kwargs:
      self.__kwargs.append(fn_kw)

  def __add_strftime_directive(self, group):
    self.__strftime_directives.append(group)

  def __add_user_def(self, name):
    if name not in self.__user_defs:
      self.__user_defs.append(name)

    # Remove any modules and members that were added before any known user-definitions. Do it in
    # reverse so the indices are kept while traversing!
    for ud in self.__user_defs:
      for i in reverse_range(self.__modules):
        if self.__modules[i] == ud:
          vvvprint("Ignoring module '{}' because it's user-defined!".format(ud))
          del(self.__modules[i])

      for i in reverse_range(self.__members):
        if self.__members[i] == ud:
          vvvprint("Ignoring member '{}' because it's user-defined!".format(ud))
          del(self.__members[i])

  def __add_user_def_node(self, node):
    """Add user-defined name from node, like ast.Name, ast.arg or str."""
    if isinstance(node, str):
      self.__add_user_def(node)
    if isinstance(node, ast.Name) and hasattr(node, "id"):
      self.__add_user_def(node.id)
    elif hasattr(node, "arg"):
      self.__add_user_def(node.arg)

  def __add_name_res(self, source, target):
    self.__name_res[source] = target

  def __get_attribute_name(self, node):
    """Retrieve full attribute name path, like ["ipaddress", "IPv4Address"] from:
    Attribute(value=Name(id='ipaddress', ctx=Load()), attr='IPv4Address', ctx=Load())
    """
    full_name = []
    for attr in ast.walk(node):
      if isinstance(attr, ast.Attribute):
        if hasattr(attr, "attr"):
          full_name.insert(0, attr.attr)
        if hasattr(attr, "value") and hasattr(attr.value, "id"):
          full_name.insert(0, attr.value.id)
    return full_name

  def __add_name_res_assign_node(self, node):
    if not hasattr(node, "value"):
      return

    value_name = None

    # If rvalue is a Call.
    if isinstance(node.value, ast.Call):
      if isinstance(node.value.func, ast.Name):
        value_name = node.value.func.id
      elif isinstance(node.value.func, ast.Attribute):
        value_name = dotted_name(self.__get_attribute_name(node.value.func))

    # If rvalue is an Attribute list
    elif isinstance(node.value, ast.Attribute):
      value_name = dotted_name(self.__get_attribute_name(node.value))

    if value_name is None:
      return

    targets = []
    if hasattr(node, "targets"):
      targets = node.targets
    elif hasattr(node, "target"):
      targets.append(node.target)
    for target in targets:
      if isinstance(target, ast.Name):
        target_name = target.id
        self.__add_name_res(target_name, value_name)

  def generic_visit(self, node):
    self.__depth += 1
    if Config.get().print_visits():
      nprint("| " * self.__depth + ast.dump(node))
    super(SourceVisitor, self).generic_visit(node)
    self.__depth -= 1

  def visit_Import(self, node):
    self.__import = True
    self.generic_visit(node)
    self.__import = False

  def visit_ImportFrom(self, node):
    if node.module is None:
      return

    self.__add_module(node.module)

    # Remember module members and full module paths, like "ABC" member of module "abc" and "abc.ABC"
    # module.
    for name in node.names:
      if name.name == "*":
        # Ignore star import.
        pass
      elif name.name is not None:
        self.__import_mem_mod[name.name] = node.module
        comb_name = "{}.{}".format(node.module, name.name)
        self.__add_module(comb_name)
        self.__add_member(comb_name)
        self.__add_member(name.name)

  def visit_alias(self, node):
    if self.__import:
      self.__add_module(node.name)
      self.__add_member(node.name)

  def visit_Name(self, node):
    if node.id == "long":
      self.__longv2 = True
      vvprint("long is a v2 feature")

  def visit_Print(self, node):
    self.__printv2 = True
    self.generic_visit(node)

  def visit_Call(self, node):
    if hasattr(node, "func"):
      func = node.func
      if hasattr(func, "id"):
        self.__function_name = func.id
        self.__add_member(func.id)
        if func.id == "print":
          self.__printv3 = True
      elif hasattr(func, "attr"):
        attr = func.attr
        if attr == "format" and hasattr(func, "value") and isinstance(func.value, ast.Str):
          vvprint("`\"..\".format(..)` requires [2.6, 3.0]")
          self.__format = True
        elif (attr == "strftime" or attr == "strptime") and hasattr(node, "args"):
          for arg in node.args:
            if hasattr(arg, "s"):
              for directive in STRFTIME_DIRECTIVE_REGEX.findall(arg.s):
                self.__add_strftime_directive(directive)
      if isinstance(func, ast.Attribute):
        self.__function_name = dotted_name(self.__get_attribute_name(func))
    self.generic_visit(node)
    self.__function_name = None

  def visit_Attribute(self, node):
    full_name = self.__get_attribute_name(node)
    if len(full_name) > 0:
      for mod in self.__modules:
        if full_name[0] == mod:
          self.__add_module(dotted_name(full_name))
        elif mod.endswith(full_name[0]):
          self.__add_member(dotted_name([mod, full_name[1:]]))
      self.__add_member(dotted_name(full_name))

      if full_name[0] in self.__name_res:
        res = self.__name_res[full_name[0]]
        if res in self.__import_mem_mod:
          mod = self.__import_mem_mod[res]
          self.__add_member(dotted_name([mod, res, full_name[1:]]))

        # Try as a fully-qualified name.
        else:
          self.__add_member(dotted_name([res, full_name[1:]]))

  def visit_keyword(self, node):
    if self.__function_name is not None:
      self.__add_kwargs(self.__function_name, node.arg)

      if self.__function_name in self.__import_mem_mod:
        mod = self.__import_mem_mod[self.__function_name]
        self.__add_kwargs(dotted_name([mod, self.__function_name]), node.arg)

      # When having "ElementTree.tostringlist", for instance, and include mapping "{'ElementTree':
      # 'xml.etree'}" then try piecing them together to form a match.
      exp_name = self.__function_name.split(".")
      if exp_name[0] in self.__import_mem_mod:
        mod = self.__import_mem_mod[exp_name[0]]
        self.__add_kwargs(dotted_name([mod, self.__function_name]), node.arg)

      # Lookup indirect names via variables.
      if exp_name[0] in self.__name_res:
        res = self.__name_res[exp_name[0]]
        if res in self.__import_mem_mod:
          mod = self.__import_mem_mod[res]
          self.__add_kwargs(dotted_name([mod, res, exp_name[1:]]), node.arg)

        # Try as FQN.
        else:
          self.__add_kwargs(dotted_name([res, exp_name[1:]]), node.arg)

  def visit_Bytes(self, node):
    self.__bytesv3 = True

  def visit_JoinedStr(self, node):
    self.__fstrings = True

  # Mark variable names as aliases.
  def visit_Assign(self, node):
    for target in node.targets:
      self.__add_user_def_node(target)
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

  def visit_AugAssign(self, node):
    self.__add_user_def_node(node.target)
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

  def visit_AnnAssign(self, node):
    self.__add_user_def_node(node.target)
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

  def visit_FunctionDef(self, node):
    self.__add_user_def(node.name)
    self.generic_visit(node)

  def visit_ClassDef(self, node):
    self.__add_user_def(node.name)
    self.generic_visit(node)

  def visit_NameConstant(self, node):
    if node.value is True or node.value is False:
      self.__bool_const = True
      vvvprint("True/False constant requires v2.2+.")

  # Ignore unused nodes as a speed optimization.

  def visit_Load(self, node):
    pass

  def visit_Store(self, node):
    pass

  def visit_Pass(self, node):
    pass

  def visit_Num(self, node):
    pass

  def visit_Not(self, node):
    pass

  def visit_Add(self, node):
    pass

  def visit_Sub(self, node):
    pass

  def visit_Mult(self, node):
    pass

  def visit_Div(self, node):
    pass

  def visit_BitAnd(self, node):
    pass

  def visit_Or(self, node):
    pass

  def visit_BitOr(self, node):
    pass

  def visit_Eq(self, node):
    pass

  def visit_NotEq(self, node):
    pass

  def visit_Lt(self, node):
    pass

  def visit_Gt(self, node):
    pass

  def visit_In(self, node):
    pass

  def visit_Is(self, node):
    pass

  def visit_Continue(self, node):
    pass

  def visit_Break(self, node):
    pass

  def visit_Mod(self, node):
    pass
