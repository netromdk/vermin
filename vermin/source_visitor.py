import ast
import re

from .rules import MOD_MEM_REQS, KWARGS_REQS
from .config import Config
from .printing import nprint, vvprint, vvvprint
from .utility import reverse_range

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
    self.__star_imports = []
    self.__function_name = None
    self.__kwargs = []
    self.__depth = 0
    self.__strftime_directives = []
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
    """Add member if required module is imported and not be user-defined."""
    if member in self.__user_defs:
      vvvprint("Ignoring member '{}' because it's user-defined!".format(member))
      return

    if self.__member_mod_visited(member):
      self.__members.append(member)

  def __add_star_import(self, module):
    self.__star_imports.append(module)

  def __add_kwargs(self, function, keyword):
    if function not in self.__user_defs:
      fn_kw = (function, keyword)
      if fn_kw in KWARGS_REQS:
        (mod, mins) = KWARGS_REQS[fn_kw]
        if mod in self.__modules or mod in self.__star_imports:
          self.__kwargs.append(fn_kw)

  def __member_mod_visited(self, member):
    """Checks if module of member is imported/visited."""
    if member in MOD_MEM_REQS:
      for (mod, vers) in MOD_MEM_REQS[member]:
        if mod in self.__modules or mod in self.__star_imports:
          return True
    return False

  def __add_strftime_directive(self, group):
    self.__strftime_directives.append(group)

  def __add_user_def_node(self, node):
    """Add user-defined name from node, like ast.Name, ast.arg or str."""
    if isinstance(node, str):
      self.__add_user_def(node)
    if isinstance(node, ast.Name) and hasattr(node, "id"):
      self.__add_user_def(node.id)
    elif hasattr(node, "arg"):
      self.__add_user_def(node.arg)

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
        self.__add_star_import(node.module)
      elif name.name is not None:
        self.__add_module(node.module + "." + name.name)
        self.__add_member(name.name)

  def visit_alias(self, node):
    if self.__import:
      self.__add_module(node.name)

      # If the import path has several levels then remember last member, like "ABC" of "abc.ABC".
      elms = node.name.split(".")
      if len(elms) >= 2:
        self.__add_member(elms[-1])

  def visit_Name(self, node):
    if node.id == "long":
      self.__longv2 = True
      vvprint("long is a v2 feature")
    self.__add_member(node.id)

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
        if full_name[0] in self.__modules:
          self.__add_module(".".join(full_name))

    # When a function is called like "os.path.ismount(..)" it is an attribute list where the "first"
    # (this one) is the function name. Stop visiting here.
    if hasattr(node, "attr"):
      self.__function_name = node.attr

      # Also add as a possible module member, like `B` in `class A(B)`.
      self.__add_member(node.attr)

  def visit_keyword(self, node):
    if self.__function_name is not None:
      self.__add_kwargs(self.__function_name, node.arg)

  def visit_Bytes(self, node):
    self.__bytesv3 = True

  def visit_JoinedStr(self, node):
    self.__fstrings = True

  def visit_FunctionDef(self, node):
    self.__add_user_def(node.name)
    self.generic_visit(node)

  def visit_ClassDef(self, node):
    self.__add_user_def(node.name)
    self.generic_visit(node)

  # Mark argument names as user-defined.
  def visit_arguments(self, node):
    for arg in node.args:
      self.__add_user_def_node(arg)
    if node.vararg is not None:
      self.__add_user_def_node(node.vararg)
    self.generic_visit(node)

  # Mark variable names as user-defined.
  def visit_Assign(self, node):
    for target in node.targets:
      self.__add_user_def_node(target)
    self.generic_visit(node)

  def visit_AugAssign(self, node):
    self.__add_user_def_node(node.target)
    self.generic_visit(node)

  def visit_AnnAssign(self, node):
    self.__add_user_def_node(node.target)
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
