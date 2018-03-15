import ast
import re

from .rules import MOD_MEM_REQS, KWARGS_REQS
from .config import Config
from .printing import nprint, vvprint

STRFTIME_DIRECTIVE_REGEX = re.compile(r"(%\w)")

class SourceVisitor(ast.NodeVisitor):
  def __init__(self):
    super(SourceVisitor, self).__init__()
    self.__import = False
    self.__modules = []
    self.__members = []
    self.__printv2 = False
    self.__printv3 = False
    self.__format = False
    self.__longv2 = False
    self.__bytesv3 = False
    self.__fstrings = False
    self.__function_name = None
    self.__kwargs = []
    self.__depth = 0
    self.__strftime_directives = []

    # Imported members of modules, like "exc_clear" of "sys".
    self.__import_mem_mod = {}

    # Name -> name resolutions.
    self.__name_res = {}

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

  def kwargs(self):
    return self.__kwargs

  def strftime_directives(self):
    return self.__strftime_directives

  def __add_module(self, module):
    if module not in self.__modules:
      self.__modules.append(module)

  def __add_member(self, member):
    """Add member if fully-qualified name is known."""
    if member in MOD_MEM_REQS:
      self.__members.append(member)

  def __add_kwargs(self, function, keyword):
    fn_kw = (function, keyword)
    if fn_kw in KWARGS_REQS:
      (mod, mins) = KWARGS_REQS[fn_kw]
      if mod in self.__modules:
        self.__kwargs.append(fn_kw)

  def __add_strftime_directive(self, group):
    self.__strftime_directives.append(group)

  def __add_name_res(self, source, target):
    self.__name_res[source] = target

  def __add_name_res_assign_node(self, node):
    if not hasattr(node, "value"):
      return
    if not isinstance(node.value, ast.Call):
      return

    value_name = None
    if isinstance(node.value.func, ast.Name):
      value_name = node.value.func.id
    elif isinstance(node.value.func, ast.Attribute):
      full_name = []
      for attr in ast.walk(node.value.func):
        if isinstance(attr, ast.Attribute):
          if hasattr(attr, "attr"):
            full_name.insert(0, attr.attr)
          if hasattr(attr, "value") and hasattr(attr.value, "id"):
            full_name.insert(0, attr.value.id)
      value_name = ".".join(full_name)

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
        if func.id == "print":
          self.__printv3 = True
      elif hasattr(func, "attr"):
        attr = func.attr
        if attr == "format" and hasattr(func, "value") and isinstance(func.value, ast.Str):
          vvprint("`\"..\".format(..)` requires [2.7, 3.0]")
          self.__format = True
        elif (attr == "strftime" or attr == "strptime") and hasattr(node, "args"):
          for arg in node.args:
            if hasattr(arg, "s"):
              for directive in STRFTIME_DIRECTIVE_REGEX.findall(arg.s):
                self.__add_strftime_directive(directive)
    self.generic_visit(node)
    self.__function_name = None

  def visit_Attribute(self, node):
    # Retrieve full attribute name path, like "ipaddress.IPv4Address" from:
    # Attribute(value=Name(id='ipaddress', ctx=Load()), attr='IPv4Address', ctx=Load())
    if hasattr(node, "value"):
      full_name = []
      for attr in ast.walk(node):
        if isinstance(attr, ast.Attribute):
          if hasattr(attr, "attr"):
            full_name.insert(0, attr.attr)
          if hasattr(attr, "value") and hasattr(attr.value, "id"):
            full_name.insert(0, attr.value.id)
      if len(full_name) > 0:
        for mod in self.__modules:
          if full_name[0] == mod:
            self.__add_module(".".join(full_name))
          elif mod.endswith(full_name[0]):
            self.__add_member(mod + "." + full_name[-1])
        self.__add_member(".".join(full_name))

        if full_name[0] in self.__name_res:
          res = self.__name_res[full_name[0]]
          if res in self.__import_mem_mod:
            mod = self.__import_mem_mod[res]
            self.__add_member("{}.{}.{}".format(mod, res, full_name[-1]))

          # Try as a fully-qualified name.
          else:
            self.__add_member("{}.{}".format(res, full_name[-1]))

    # When a function is called like "os.path.ismount(..)" it is an attribute list where the "first"
    # (this one) is the function name. Stop visiting here.
    if hasattr(node, "attr"):
      self.__function_name = node.attr

  def visit_keyword(self, node):
    if self.__function_name is not None:
      self.__add_kwargs(self.__function_name, node.arg)

  def visit_Bytes(self, node):
    self.__bytesv3 = True

  def visit_JoinedStr(self, node):
    self.__fstrings = True

  # Mark variable names as user-defined.
  def visit_Assign(self, node):
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

  def visit_AugAssign(self, node):
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

  def visit_AnnAssign(self, node):
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

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
