import ast
import re
import sys

from .rules import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS, STRFTIME_REQS, ARRAY_TYPECODE_REQS, \
  CODECS_ERROR_HANDLERS, CODECS_ERRORS_INDICES, CODECS_ENCODINGS, CODECS_ENCODINGS_INDICES
from .config import Config
from .utility import dotted_name, reverse_range, combine_versions

STRFTIME_DIRECTIVE_REGEX = re.compile(r"(%\w)")

class SourceVisitor(ast.NodeVisitor):
  def __init__(self, config=None):
    super(SourceVisitor, self).__init__()
    if config is None:
      self.__config = Config.get()
    else:
      self.__config = config

    self.__modules = []
    self.__members = []
    self.__printv2 = False
    self.__printv3 = False
    self.__format27 = False  # If format is used so that it requires 2.7+, like '{}' etc.
    self.__longv2 = False
    self.__bytesv3 = False
    self.__fstrings = False
    self.__fstrings_self_doc = False
    self.__bool_const = False
    self.__annotations = False
    self.__var_annotations = False
    self.__coroutines = False
    self.__async_generator = False
    self.__async_comprehension = False
    self.__seen_yield = 0
    self.__seen_await = 0
    self.__await_in_comprehension = False
    self.__named_exprs = False
    self.__pos_only_args = False
    self.__yield_from = False
    self.__raise_cause = False
    self.__dict_comp = False
    self.__mat_mult = False
    self.__continue_in_finally = False
    self.__seen_for = 0
    self.__seen_while = 0
    self.__try_finally = []
    self.__mod_inverse_pow = False
    self.__function_name = None
    self.__kwargs = []
    self.__depth = 0
    self.__line = 1
    self.__strftime_directives = []
    self.__codecs_error_handlers = []
    self.__codecs_encodings = []
    self.__with_statement = False

    # Imported members of modules, like "exc_clear" of "sys".
    self.__import_mem_mod = {}

    # Name -> name resolutions.
    self.__name_res = {}

    # User-defined symbols to be ignored.
    self.__user_defs = []

    # List of lines of output text.
    self.__output_text = []

    # Line/column of entities for vvv-printing.
    self.__line_col_entities = {}

    # Typecodes for use with `array.array(typecode, [init..])`.
    self.__array_typecodes = []

    # Module as-name -> name.
    self.__module_as_name = {}

    # Lines that should be ignored if they have the comment "novermin" or "novm".
    self.__no_lines = set()

  def modules(self):
    return self.__modules

  def members(self):
    return self.__members

  def printv2(self):
    return self.__printv2

  def printv3(self):
    return self.__printv3

  def format27(self):
    return self.__format27

  def longv2(self):
    return self.__longv2

  def bytesv3(self):
    return self.__bytesv3

  def fstrings(self):
    return self.__fstrings

  def fstrings_self_doc(self):
    return self.__fstrings_self_doc

  def bool_const(self):
    return self.__bool_const

  def named_expressions(self):
    return self.__named_exprs

  def kwargs(self):
    return self.__kwargs

  def annotations(self):
    return self.__annotations

  def var_annotations(self):
    return self.__var_annotations

  def coroutines(self):
    return self.__coroutines

  def async_generator(self):
    return self.__async_generator

  def async_comprehension(self):
    return self.__async_comprehension

  def await_in_comprehension(self):
    return self.__await_in_comprehension

  def pos_only_args(self):
    return self.__pos_only_args

  def strftime_directives(self):
    return self.__strftime_directives

  def user_defined(self):
    return self.__user_defs

  def array_typecodes(self):
    return self.__array_typecodes

  def codecs_error_handlers(self):
    return self.__codecs_error_handlers

  def codecs_encodings(self):
    return self.__codecs_encodings

  def yield_from(self):
    return self.__yield_from

  def raise_cause(self):
    return self.__raise_cause

  def dict_comprehension(self):
    return self.__dict_comp

  def infix_matrix_multiplication(self):
    return self.__mat_mult

  def continue_in_finally(self):
    return self.__continue_in_finally

  def modular_inverse_pow(self):
    return self.__mod_inverse_pow

  def with_statement(self):
    return self.__with_statement

  def minimum_versions(self):
    mins = [0, 0]

    if self.printv2():
      # Must be like this, not `combine_versions(2.0, None)`, since in py2 all print statements call
      # `visit_Print()` but in py3 it's just a regular function via
      # `Call(func=Name(id="print"..)..)`. Otherwise it will say not compatible with 3 when run on
      # py3. The reason for now using `combine_versions(2.0, 3.0)` is that in py2 we cannot
      # distinguish `print x` from `print(x)` - the first fails in py3 but not the second form.
      mins[0] = 2.0

    if self.printv3():
      # print() is used so often that we only want to show it once, and with no line.
      self.__vvprint("print(expr) requires 2+ or 3+", line=-1)
      mins = combine_versions(mins, (2.0, 3.0))

    if self.format27():
      mins = combine_versions(mins, (2.7, 3.0))

    if self.longv2():
      mins = combine_versions(mins, (2.0, None))

    if self.bytesv3():
      mins = combine_versions(mins, (None, 3.0))

    if self.fstrings():
      mins = combine_versions(mins, (None, 3.6))

    if self.fstrings_self_doc():
      mins = combine_versions(mins, (None, 3.8))

    if self.bool_const():
      mins = combine_versions(mins, (2.2, 3.0))

    if self.annotations():
      mins = combine_versions(mins, (None, 3.0))

    if self.var_annotations():
      mins = combine_versions(mins, (None, 3.6))

    if self.coroutines():
      mins = combine_versions(mins, (None, 3.5))

    if self.async_generator():
      mins = combine_versions(mins, (None, 3.6))

    # NOTE: While async comprehensions and await in comprehensions should be in 3.6, they were first
    # put into 3.7 for some reason!

    if self.async_comprehension():
      mins = combine_versions(mins, (None, 3.7))

    if self.await_in_comprehension():
      mins = combine_versions(mins, (None, 3.7))

    if self.named_expressions():
      mins = combine_versions(mins, (None, 3.8))

    if self.pos_only_args():
      mins = combine_versions(mins, (None, 3.8))

    if self.yield_from():
      mins = combine_versions(mins, (None, 3.3))

    if self.raise_cause():
      mins = combine_versions(mins, (None, 3.3))

    if self.dict_comprehension():
      mins = combine_versions(mins, (2.7, 3.0))

    if self.infix_matrix_multiplication():
      mins = combine_versions(mins, (None, 3.5))

    if self.continue_in_finally():
      mins = combine_versions(mins, (None, 3.8))

    if self.modular_inverse_pow():
      mins = combine_versions(mins, (None, 3.8))

    if self.with_statement():
      mins = combine_versions(mins, (2.5, 3.0))

    for directive in self.strftime_directives():
      if directive in STRFTIME_REQS:
        vers = STRFTIME_REQS[directive]
        self.__vvprint("strftime directive '{}' requires {}".
                       format(directive, vers), directive)
        mins = combine_versions(mins, vers)

    for typecode in self.array_typecodes():
      if typecode in ARRAY_TYPECODE_REQS:
        vers = ARRAY_TYPECODE_REQS[typecode]
        self.__vvprint("array typecode '{}' requires {}".format(typecode, vers), typecode)
        mins = combine_versions(mins, vers)

    for name in self.codecs_error_handlers():
      if name in CODECS_ERROR_HANDLERS:
        vers = CODECS_ERROR_HANDLERS[name]
        self.__vvprint("codecs error handler name '{}' requires {}".format(name, vers), name)
        mins = combine_versions(mins, vers)

    for encoding in self.codecs_encodings():
      for encs in CODECS_ENCODINGS:
        if encoding.lower() in encs:
          vers = CODECS_ENCODINGS[encs]
          self.__vvprint("codecs encoding '{}' requires {}".format(encoding, vers), encoding)
          mins = combine_versions(mins, vers)

    mods = self.modules()
    for mod in mods:
      if mod in MOD_REQS:
        vers = MOD_REQS[mod]
        self.__vvprint("'{}' requires {}".format(mod, vers), mod)
        mins = combine_versions(mins, vers)

    mems = self.members()
    for mem in mems:
      if mem in MOD_MEM_REQS:
        vers = MOD_MEM_REQS[mem]
        self.__vvprint("'{}' requires {}".format(mem, vers), mem)
        mins = combine_versions(mins, vers)

    kwargs = self.kwargs()
    for fn_kw in kwargs:
      if fn_kw in KWARGS_REQS:
        vers = KWARGS_REQS[fn_kw]
        self.__vvprint("'{}({})' requires {}".format(fn_kw[0], fn_kw[1], vers), fn_kw)
        mins = combine_versions(mins, vers)

    return mins

  def output_text(self):
    text = "\n".join(self.__output_text)
    if len(text) > 0:
      text += "\n"
    return text

  def set_no_lines(self, lines):
    self.__no_lines = lines

  def no_lines(self):
    return self.__no_lines

  def __nprint(self, msg):
    if not self.__config.quiet():
      self.__output_text.append(msg)

  def __verbose_print(self, msg, level, entity=None, line=None):
    config_level = self.__config.verbose()
    if self.__config.quiet() or config_level < level:
      return

    col = None

    # Line/column numbers start at level 3+.
    entity = entity if config_level > 2 else None
    if entity is not None and entity in self.__line_col_entities:
      (line, col) = self.__line_col_entities[entity]

    if line == -1:
      line = None
    elif line is None and config_level > 2:
      line = self.__line

    if line is not None:
      if col is not None:
        msg = "L{} C{}: ".format(line, col) + msg
      else:
        msg = "L{}: ".format(line) + msg
    self.__output_text.append(msg)

  def __vprint(self, msg, entity=None):
    self.__verbose_print(msg, 1, entity)

  def __vvprint(self, msg, entity=None, line=None):
    self.__verbose_print(msg, 2, entity, line)

  def __vvvprint(self, msg, entity=None, line=None):
    self.__verbose_print(msg, 3, entity, line)

  def __vvvvprint(self, msg, entity=None, line=None):
    self.__verbose_print(msg, 4, entity, line)

  def __add_module(self, module, line=None, col=None):
    if module in self.__user_defs:
      self.__vvvvprint("Ignoring module '{}' because it's user-defined!".format(module))
      return

    if self.__config.is_excluded(module):
      self.__vvprint("Excluding module: {}".format(module))
      return

    if module not in self.__modules:
      self.__modules.append(module)
      self.__add_line_col(module, line, col)

  def __add_member(self, member, line=None, col=None):
    """Add member if fully-qualified name is known."""
    if member in self.__user_defs:
      self.__vvvvprint("Ignoring member '{}' because it's user-defined!".format(member))
      return

    if self.__config.is_excluded(member):
      self.__vvprint("Excluding member: {}".format(member))
      return

    if member in MOD_MEM_REQS:
      self.__members.append(member)
      self.__add_line_col(member, line, col)

  def __add_kwargs(self, function, keyword, line=None, col=None):
    if function in self.__user_defs:
      self.__vvvvprint("Ignoring function '{}' because it's user-defined!".format(function))
      return

    if self.__config.is_excluded_kwarg(function, keyword):
      self.__vvprint("Excluding kwarg: {}({})".format(function, keyword))
      return

    fn_kw = (function, keyword)
    if fn_kw in KWARGS_REQS and fn_kw not in self.__kwargs:
      self.__kwargs.append(fn_kw)
      self.__add_line_col(fn_kw, line, col)

  def __add_strftime_directive(self, group, line=None, col=None):
    self.__strftime_directives.append(group)
    self.__add_line_col(group, line, col)

  def __add_codecs_error_handler(self, func, node):
    if func in CODECS_ERRORS_INDICES:
      idx = CODECS_ERRORS_INDICES[func]

      # Check indexed arguments.
      if idx >= 0 and idx < len(node.args):
        arg = node.args[idx]
        if hasattr(arg, "s"):
          name = arg.s
          if self.__config.is_excluded_codecs_error_handler(name):
            self.__vvprint("Excluding codecs error handler: {}".format(name))
          else:
            self.__codecs_error_handlers.append(name)
            self.__add_line_col(name, node.lineno)

      # Check for "errors" keyword arguments.
      for kw in node.keywords:
        if kw.arg == "errors":
          value = kw.value
          if hasattr(value, "s"):
            name = kw.value.s
            if self.__config.is_excluded_codecs_error_handler(name):
              self.__vvprint("Excluding codecs error handler: {}".format(name))
              continue
            self.__codecs_error_handlers.append(name)
            self.__add_line_col(name, node.lineno)

  def __add_codecs_encoding(self, func, node):
    if func in CODECS_ENCODINGS_INDICES:
      kwargs = ("encoding", "data_encoding", "file_encoding")
      for idx in CODECS_ENCODINGS_INDICES[func]:
        # Check indexed arguments.
        if idx >= 0 and idx < len(node.args):
          arg = node.args[idx]
          if hasattr(arg, "s"):
            name = arg.s
            if self.__config.is_excluded_codecs_encoding(name):
              self.__vvprint("Excluding codecs encoding: {}".format(name))
              continue
            self.__codecs_encodings.append(name)
            self.__add_line_col(name, node.lineno)

        # Check for "encoding", "data_encoding", "file_encoding" keyword arguments.
        for kw in node.keywords:
          if kw.arg in kwargs:
            value = kw.value
            if hasattr(value, "s"):
              name = kw.value.s
              if self.__config.is_excluded_codecs_encoding(name):
                self.__vvprint("Excluding codecs encoding: {}".format(name))
                continue
              self.__codecs_encodings.append(name)
              self.__add_line_col(name, node.lineno)

  def __check_codecs_function(self, func, node):
    self.__add_codecs_error_handler(func, node)
    self.__add_codecs_encoding(func, node)

  def __add_user_def(self, name):
    if name not in self.__user_defs:
      self.__user_defs.append(name)

    # Remove any modules and members that were added before any known user-definitions. Do it in
    # reverse so the indices are kept while traversing!
    for ud in self.__user_defs:
      for i in reverse_range(self.__modules):
        if self.__modules[i] == ud:
          self.__vvvvprint("Ignoring module '{}' because it's user-defined!".format(ud))
          del(self.__modules[i])

      for i in reverse_range(self.__members):
        if self.__members[i] == ud:
          self.__vvvvprint("Ignoring member '{}' because it's user-defined!".format(ud))
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

  def __get_name(self, node):
    full_name = []
    if isinstance(node, ast.Attribute):
      if hasattr(node, "attr"):
        full_name.insert(0, node.attr)
      if hasattr(node, "value") and hasattr(node.value, "id"):
        full_name.insert(0, node.value.id)
    elif isinstance(node, ast.Name):
      if hasattr(node, "id"):
        full_name.insert(0, node.id)
    return full_name

  def __is_builtin_type(self, name):
    return name in {"dict", "set", "list", "unicode", "str", "int", "float", "long", "bytes"}

  def __get_attribute_name(self, node):
    """Retrieve full attribute name path, like ["ipaddress", "IPv4Address"] from:
    `Attribute(value=Name(id='ipaddress', ctx=Load()), attr='IPv4Address', ctx=Load())`
    Or ["Fraction", "as_integer_ratio"] from:
    `Attribute(value=Call(func=Name(id='Fraction', ctx=Load()), args=[Num(n=42)], keywords=[]),
               attr='as_integer_ratio', ctx=Load())`
    """
    full_name = []
    primi_type = False
    for attr in ast.walk(node):
      if len(full_name) > 0 and self.__is_builtin_type(full_name[0]):
        primi_type = True
      if isinstance(attr, ast.Attribute):
        if hasattr(attr, "attr"):
          full_name.insert(0, attr.attr)
        if hasattr(attr, "value") and hasattr(attr.value, "id"):
          full_name.insert(0, attr.value.id)
      elif isinstance(attr, ast.Call):
        if hasattr(attr, "func") and hasattr(attr.func, "id"):
          full_name.insert(0, attr.func.id)
      elif not primi_type and isinstance(attr, ast.Dict):
        if len(full_name) == 0 or (full_name[0] != "dict" and len(full_name) == 1):
          full_name.insert(0, "dict")
      elif not primi_type and isinstance(attr, ast.Set):
        if len(full_name) == 0 or (full_name[0] != "set" and len(full_name) == 1):
          full_name.insert(0, "set")
      elif not primi_type and isinstance(attr, ast.List):
        if len(full_name) == 0 or (full_name[0] != "list" and len(full_name) == 1):
          full_name.insert(0, "list")
      elif not primi_type and isinstance(attr, ast.Str):
        if sys.version_info.major == 2 and type(attr.s) == unicode:
          name = "unicode"
        else:
          name = "str"
        if len(full_name) == 0 or (full_name[0] != name and len(full_name) == 1):
          full_name.insert(0, name)
      elif not primi_type and isinstance(attr, ast.Num):
        t = type(attr.n)
        name = None
        if t == int:
          name = "int"
        elif t == float:
          name = "float"
        if sys.version_info.major == 2 and t == long:  # novm
          name = "long"
        if name is not None and len(full_name) == 0 or \
          (full_name[0] != name and len(full_name) == 1):
          full_name.insert(0, name)
      elif not primi_type and hasattr(ast, "Bytes") and isinstance(attr, ast.Bytes):
        if len(full_name) == 0 or (full_name[0] != "bytes" and len(full_name) == 1):
          full_name.insert(0, "bytes")
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

    elif isinstance(node.value, ast.Dict):
      value_name = "dict"
    elif isinstance(node.value, ast.Set):
      value_name = "set"
    elif isinstance(node.value, ast.List):
      value_name = "list"
    elif isinstance(node.value, ast.Str):
      if sys.version_info.major == 2 and type(node.value.s) == unicode:
        value_name = "unicode"
      else:
        value_name = "str"
    elif isinstance(node.value, ast.Num):
      t = type(node.value.n)
      if t == int:
        value_name = "int"
      elif sys.version_info.major == 2 and t == long:  # novm
        value_name = "long"
      elif t == float:
        value_name = "float"
    elif hasattr(ast, "Bytes") and isinstance(node.value, ast.Bytes):
      value_name = "bytes"

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

  def __add_line_col(self, entity, line, col=None):
    if line is not None and col is None:
      self.__line_col_entities[entity] = (line, None)
    elif line is not None and col is not None:
      self.__line_col_entities[entity] = (line, col)

  def __add_array_typecode(self, typecode, line=None, col=None):
    if typecode not in self.__array_typecodes:
      self.__array_typecodes.append(typecode)
      self.__add_line_col(typecode, line, col)

  def __is_no_line(self, line):
    return line in self.__no_lines

  def __is_int(self, node):
    return (isinstance(node, ast.Num) and type(node.n) == int) or \
      (isinstance(node, ast.UnaryOp) and isinstance(node.operand, ast.Num) and
       type(node.operand.n) == int)

  def __is_neg_int(self, node):
    return (isinstance(node, ast.Num) and type(node.n) == int and node.n < 0) or \
      (isinstance(node, ast.UnaryOp) and type(node.op) == ast.USub and
       isinstance(node.operand, ast.Num) and type(node.operand.n) == int)

  def generic_visit(self, node):
    if hasattr(node, "lineno"):
      self.__line = node.lineno
    self.__depth += 1
    if self.__config.print_visits():
      self.__nprint("| " * self.__depth + ast.dump(node))
    super(SourceVisitor, self).generic_visit(node)
    self.__depth -= 1

  def visit_Import(self, node):
    if self.__is_no_line(node.lineno):
      return

    for name in node.names:
      line = node.lineno
      col = node.col_offset + 7  # "import" = 6 + 1
      self.__add_module(name.name, line, col)
      self.__add_member(name.name, line, col)
      if hasattr(name, "asname") and name.asname is not None:
        self.__module_as_name[name.asname] = name.name
    self.generic_visit(node)

  def visit_ImportFrom(self, node):
    if node.module is None:
      return

    if self.__is_no_line(node.lineno):
      return

    from_col = 5  # "from" = 4 + 1
    self.__add_module(node.module, node.lineno, node.col_offset + from_col)

    # Remember module members and full module paths, like "ABC" member of module "abc" and "abc.ABC"
    # module.
    for name in node.names:
      if name.name == "*":
        # Ignore star import.
        pass
      elif name.name is not None:
        self.__import_mem_mod[name.name] = node.module
        comb_name = "{}.{}".format(node.module, name.name)
        line = node.lineno
        col = node.col_offset + from_col
        self.__add_module(comb_name, line, col)
        self.__add_member(comb_name, line, col)
        self.__add_member(name.name, line, col)
      if hasattr(name, "asname") and name.asname is not None:
        self.__module_as_name[name.asname] = node.module + "." + name.name

  def visit_Name(self, node):
    if node.id == "long":
      if self.__config.is_excluded("long"):
        self.__vvprint("Excluding long type")
      else:
        self.__longv2 = True
        self.__vvprint("long is a v2 feature")

  def visit_Print(self, node):
    self.__printv2 = True
    self.generic_visit(node)

  def visit_Call(self, node):
    if self.__is_no_line(node.lineno):
      return

    if hasattr(node, "func"):
      func = node.func
      if hasattr(func, "id"):
        self.__function_name = func.id
        self.__add_member(func.id, node.lineno, node.col_offset)

        if func.id in self.__import_mem_mod:
          name = self.__import_mem_mod[func.id] + "." + func.id
          self.__check_codecs_function(name, node)
        elif func.id in self.__module_as_name:
          name = self.__module_as_name[func.id]
          self.__check_codecs_function(name, node)

        if func.id == "print":
          self.__printv3 = True
        elif func.id == "array" or\
             (func.id in self.__module_as_name and self.__module_as_name[func.id] == "array.array"):
          for arg in node.args:
            if isinstance(arg, ast.Str) and hasattr(arg, "s"):
              self.__add_array_typecode(arg.s, node.lineno, node.col_offset + 6)  # "array" = 5 + 1
        elif func.id == "pow" and len(node.args) == 3:
          # Check if the second of three arguments of pow() is negative.
          if self.__is_int(node.args[0]) and self.__is_neg_int(node.args[1]) and \
             self.__is_int(node.args[2]):
            self.__mod_inverse_pow = True
            self.__vvprint("modular inverse pow() requires 3.8+")
      elif hasattr(func, "attr"):
        attr = func.attr
        if attr == "format" and hasattr(func, "value") and isinstance(func.value, ast.Str) and \
           "{}" in func.value.s:
          self.__vvprint("`\"..{}..\".format(..)` requires (2.7, 3.0)")
          self.__format27 = True
        elif (attr == "strftime" or attr == "strptime") and hasattr(node, "args"):
          for arg in node.args:
            if hasattr(arg, "s"):
              for directive in STRFTIME_DIRECTIVE_REGEX.findall(arg.s):
                self.__add_strftime_directive(directive, node.lineno)
      if isinstance(func, ast.Attribute):
        self.__function_name = dotted_name(self.__get_attribute_name(func))
        self.__check_codecs_function(self.__function_name, node)

    # Visit arguments and keywords.
    if hasattr(node, "args"):
      for arg in node.args:
        self.generic_visit(arg)
    if hasattr(node, "keywords"):
      for kw in node.keywords:
        self.generic_visit(kw)

    self.generic_visit(node)
    self.__function_name = None

  def visit_Attribute(self, node):
    full_name = self.__get_attribute_name(node)
    line = node.lineno
    if len(full_name) > 0:
      for mod in self.__modules:
        if full_name[0] == mod:
          self.__add_module(dotted_name(full_name), line)
        elif mod.endswith(full_name[0]):
          self.__add_member(dotted_name([mod, full_name[1:]]), line)
      self.__add_member(dotted_name(full_name), line)

      if full_name[0] in self.__name_res:
        res = self.__name_res[full_name[0]]
        if res in self.__import_mem_mod:
          mod = self.__import_mem_mod[res]
          self.__add_member(dotted_name([mod, res, full_name[1:]]), line)

        # Try as a fully-qualified name.
        else:
          self.__add_member(dotted_name([res, full_name[1:]]), line)
    self.generic_visit(node)

  def visit_keyword(self, node):
    if self.__function_name is not None:
      self.__add_kwargs(self.__function_name, node.arg, self.__line)

      if self.__function_name in self.__import_mem_mod:
        mod = self.__import_mem_mod[self.__function_name]
        self.__add_kwargs(dotted_name([mod, self.__function_name]), node.arg, self.__line)

      # When having "ElementTree.tostringlist", for instance, and include mapping "{'ElementTree':
      # 'xml.etree'}" then try piecing them together to form a match.
      exp_name = self.__function_name.split(".")
      if exp_name[0] in self.__import_mem_mod:
        mod = self.__import_mem_mod[exp_name[0]]
        self.__add_kwargs(dotted_name([mod, self.__function_name]), node.arg, self.__line)

      # Lookup indirect names via variables.
      if exp_name[0] in self.__name_res:
        res = self.__name_res[exp_name[0]]
        if res in self.__import_mem_mod:
          mod = self.__import_mem_mod[res]
          self.__add_kwargs(dotted_name([mod, res, exp_name[1:]]), node.arg, self.__line)

        # Try as FQN.
        else:
          self.__add_kwargs(dotted_name([res, exp_name[1:]]), node.arg, self.__line)

  def visit_Bytes(self, node):
    self.__bytesv3 = True
    self.__vvprint("byte strings (b'..') require 3+")

  def visit_Constant(self, node):
    if hasattr(node, "value") and type(node.value) == bytes:
      self.__bytesv3 = True
      self.__vvprint("byte strings (b'..') require 3+")

  def visit_JoinedStr(self, node):
    self.__fstrings = True
    self.__vvprint("f-strings require 3.6+")
    if hasattr(node, "values"):
      for val in node.values:
        if type(val) == ast.Constant and hasattr(val, "value") and \
           type(val.value) == str and val.value.endswith("="):
            self.__fstrings_self_doc = True
            self.__vvprint("self-documenting fstrings require 3.8+")

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
    self.__annotations = True
    self.__var_annotations = True
    self.__vvprint("variable annotations require 3.6+")

  def __handle_FunctionDef(self, node):
    if self.__is_no_line(node.lineno):
      return False

    self.__add_user_def(node.name)
    self.generic_visit(node)

    # Check if the return annotation is set
    if hasattr(node, "returns") and node.returns:
      self.__annotations = True
      self.__vvprint("annotations require 3+")
      return True
    # Then we are going to check the args
    if not hasattr(node, "args") or not hasattr(node.args, "args"):
      return True
    for arg in node.args.args:
      if hasattr(arg, "annotation") and arg.annotation:
        self.__annotations = True
        self.__vvprint("annotations require 3+")
        break
    return True

  def visit_FunctionDef(self, node):
    seen_yield = self.__seen_yield
    if self.__handle_FunctionDef(node):
      # Reset to seen yields before function.
      self.__seen_yield = seen_yield

  def visit_AsyncFunctionDef(self, node):
    seen_await = self.__seen_await
    seen_yield = self.__seen_yield
    if self.__handle_FunctionDef(node):
      self.__coroutines = True
      self.__vvprint("coroutines require 3.5+ (async)", line=node.lineno)
      if self.__seen_yield > seen_yield and self.__seen_await > seen_await:
        self.__async_generator = True
        self.__vvprint("async generators require 3.6+ (await and yield in same func)",
                       line=node.lineno)

      # Reset to seen awaits/yields before async function.
      self.__seen_await = seen_await
      self.__seen_yield = seen_yield

  def visit_Await(self, node):
    self.__coroutines = True
    self.__vvprint("coroutines require 3.5+ (await)")
    self.__seen_await += 1
    self.generic_visit(node)

  def visit_ClassDef(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__add_user_def(node.name)
    self.generic_visit(node)

  def visit_NameConstant(self, node):
    if node.value is True or node.value is False:
      self.__bool_const = True
      self.__vvvprint("True/False constant requires v2.2+.")

  def visit_NamedExpr(self, node):
    self.__named_exprs = True
    self.__vvprint("named expressions require 3.8+")
    self.generic_visit(node)

  def visit_arguments(self, node):
    if hasattr(node, "posonlyargs") and len(node.posonlyargs) > 0:
      self.__pos_only_args = True
      self.__vvprint("positional-only parameters require 3.8+")
    self.generic_visit(node)

  def visit_YieldFrom(self, node):
    self.__yield_from = True
    self.__vvprint("`yield from` requires 3.3+")
    self.generic_visit(node)

  def visit_Yield(self, node):
    self.__seen_yield += 1
    self.generic_visit(node)

  def visit_Raise(self, node):
    if hasattr(node, "cause") and node.cause is not None:
      self.__raise_cause = True
      self.__vvprint("exception cause requires 3.3+", line=node.lineno)
    self.generic_visit(node)

  def visit_DictComp(self, node):
    self.__dict_comp = True
    self.__vvprint("dict comprehensions require (2.7, 3.0)")
    self.generic_visit(node)

  def visit_MatMult(self, node):
    self.__mat_mult = True
    self.__vvprint("infix matrix multiplication requires 3.5+")
    self.generic_visit(node)

  def visit_comprehension(self, node):
    if hasattr(node, "is_async") and node.is_async == 1:
      self.__async_comprehension = True
      self.__vvprint("async comprehensions require 3.7+")

    seen_await = self.__seen_await
    self.generic_visit(node)
    if self.__seen_await > seen_await:
      self.__await_in_comprehension = True
      self.__vvprint("await in comprehensions require 3.7+")

    # Reset to seen awaits before comprehension.
    self.__seen_await = seen_await

  def visit_Continue(self, node):
    # Only accept continue in try-finally if no intermediary loops have been encountered.
    if len(self.__try_finally) > 0:
      (seen_for, seen_while) = self.__try_finally[-1]
      if seen_for == self.__seen_for and seen_while == self.__seen_while:
        self.__continue_in_finally = True
        self.__vvprint("continue in finally block requires 3.8+", line=node.lineno)

  # Lax mode and comment-excluded lines skip conditional blocks if enabled.

  def visit_If(self, node):
    if not self.__config.lax_mode() and not self.__is_no_line(node.lineno):
      self.generic_visit(node)

  def visit_IfExp(self, node):
    if not self.__config.lax_mode() and not self.__is_no_line(node.lineno):
      self.generic_visit(node)

  def visit_For(self, node):
    if not self.__config.lax_mode() and not self.__is_no_line(node.lineno):
      self.__seen_for += 1
      self.generic_visit(node)
      self.__seen_for -= 1

  def visit_While(self, node):
    if not self.__config.lax_mode() and not self.__is_no_line(node.lineno):
      self.__seen_while += 1
      self.generic_visit(node)
      self.__seen_while -= 1

  def __handle_Try(self, node):
    if not self.__config.lax_mode() and not self.__is_no_line(node.lineno):
      if hasattr(node, "finalbody"):
        self.__try_finally.append((self.__seen_for, self.__seen_while))
        for stm in node.finalbody:
          self.visit(stm)
        if len(self.__try_finally) > 0:
          self.__try_finally.pop()
      self.generic_visit(node)

  def visit_Try(self, node):
    self.__handle_Try(node)

  def visit_TryExcept(self, node):
    self.__handle_Try(node)

  def visit_TryFinally(self, node):
    self.__handle_Try(node)

  def visit_BoolOp(self, node):
    if not self.__config.lax_mode() and not self.__is_no_line(node.lineno):
      self.generic_visit(node)

  def visit_With(self, node):
    self.__with_statement = True
    self.__vvprint("`with` requires 2.5+")
    self.generic_visit(node)

  # Ignore unused nodes as a speed optimization.

  def visit_alias(self, node):
    pass

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

  def visit_Break(self, node):
    pass

  def visit_Mod(self, node):
    pass
