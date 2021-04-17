import ast
import re
import sys
import os
from collections import deque

from .rules import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS, STRFTIME_REQS, BYTES_REQS,\
  ARRAY_TYPECODE_REQS, CODECS_ERROR_HANDLERS, CODECS_ERRORS_INDICES, CODECS_ENCODINGS,\
  CODECS_ENCODINGS_INDICES, BUILTIN_GENERIC_ANNOTATION_TYPES, DICT_UNION_SUPPORTED_TYPES,\
  DICT_UNION_MERGE_SUPPORTED_TYPES, DECORATOR_USER_FUNCTIONS
from .utility import dotted_name, reverse_range, combine_versions, remove_whitespace

STRFTIME_DIRECTIVE_REGEX = re.compile(r"%(?:[-\.\d#\s\+])*(\w)")
BYTES_DIRECTIVE_REGEX = STRFTIME_DIRECTIVE_REGEX

def is_int_node(node):
  return (isinstance(node, ast.Num) and isinstance(node.n, int)) or \
    (isinstance(node, ast.UnaryOp) and isinstance(node.operand, ast.Num) and
     isinstance(node.operand.n, int))

def is_neg_int_node(node):
  return (isinstance(node, ast.Num) and isinstance(node.n, int) and node.n < 0) or \
    (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub) and
     isinstance(node.operand, ast.Num) and isinstance(node.operand.n, int))

def is_none_node(node):
  if isinstance(node, ast.Name) and node.id == 'None':
    return True
  if hasattr(ast, 'NameConstant') and isinstance(node, ast.NameConstant) and node.value is None:
    return True
  if hasattr(ast, 'Constant') and isinstance(node, ast.Constant) and node.value is None:
    return True
  return False

# Generalized unpacking, or starred expressions, are allowed when used with assignment targets prior
# to 3.5. That means that generalized unpacking expressions are only on the right-hand side of the
# assignment, they're ctx=ast.Load for 3.5+ but ctx=ast.Store are allowed prior to 3.5.
def is_valid_star_unpack(node):
  return hasattr(ast, "Starred") and isinstance(node, ast.Starred) and\
    isinstance(node.ctx, ast.Load)

def trim_fstring_value(value):  # pragma: no cover
  # HACK: Since parentheses are stripped of the AST, we'll just remove all those deduced or directly
  # available such that the self-doc f-strings can be compared.
  return remove_whitespace(value, ["\\(", "\\)"])

class SourceVisitor(ast.NodeVisitor):
  def __init__(self, config, path=None):
    super(SourceVisitor, self).__init__()

    assert config is not None, "Config must be specified!"
    self.__config = config
    self.__parsable = (self.__config.format().name() == "parsable")

    self.__path = "<unknown>" if path is None else path
    if self.__parsable and not sys.platform.startswith("win32"):
      for c in (":", "\n"):
        assert c not in self.__path, "Path '{}' cannot contain '{}'".format(self.__path, c)

    self.__is_init_file = (os.path.basename(self.__path) == "__init__.py")

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
    self.__final_annotations = False
    self.__literal_annotations = False
    self.__coroutines = False
    self.__async_generator = False
    self.__async_comprehension = False
    self.__async_for = False
    self.__seen_yield = 0
    self.__seen_await = 0
    self.__await_in_comprehension = False
    self.__named_exprs = False
    self.__kw_only_args = False
    self.__pos_only_args = False
    self.__yield_from = False
    self.__raise_cause = False
    self.__raise_from_none = False
    self.__dict_comp = False
    self.__mat_mult = False
    self.__continue_in_finally = False
    self.__seen_for = 0
    self.__seen_while = 0
    self.__try_finally = []
    self.__mod_inverse_pow = False
    self.__function_name = None
    self.__function_name_stack = deque()
    self.__kwargs = []
    self.__user_func_decorators = []
    self.__depth = 0
    self.__line = 1
    self.__strftime_directives = []
    self.__bytes_directives = []
    self.__codecs_error_handlers = []
    self.__codecs_encodings = []
    self.__with_statement = False
    self.__generalized_unpacking = False
    self.__unpacking_assignment = False
    self.__bytes_format = False
    self.__bytearray_format = False
    self.__seen_except_handler = False
    self.__seen_raise = False
    self.__dict_union = False
    self.__dict_union_merge = False
    self.__builtin_generic_type_annotations = False
    self.__function_decorators = False
    self.__class_decorators = False
    self.__relaxed_decorators = False
    self.__module_dir_func = False
    self.__module_getattr_func = False
    self.__builtin_types = {"dict", "set", "list", "unicode", "str", "int", "float", "long",
                            "bytes"}
    self.__codecs_encodings_kwargs = ("encoding", "data_encoding", "file_encoding")

    # Imported members of modules, like "exc_clear" of "sys".
    self.__import_mem_mod = {}

    # Name -> name resolutions.
    self.__name_res = {}

    # Name -> type resolutions.
    self.__name_res_type = {}

    # User-defined symbols to be ignored.
    self.__user_defs = set()

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

    # Default to disabling fstring self-doc detection since the built-in AST cannot distinguish
    # `f'{a=}'` from `f'a={a}'`, for instance, because it optimizes some information away. And this
    # incorrectly marks some source code as using fstring self-doc when only using general fstring.
    self.__fstring_self_doc_enabled = self.__config.has_feature("fstring-self-doc")

    # Used for incompatible versions texts.
    self.__info_versions = {}

    self.__mod_rules = MOD_REQS(self.__config)
    self.__mod_mem_reqs_rules = MOD_MEM_REQS(self.__config)

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

  def user_function_decorators(self):
    return self.__user_func_decorators

  def annotations(self):
    return self.__annotations

  def var_annotations(self):
    return self.__var_annotations

  def final_annotations(self):
    return self.__final_annotations

  def literal_annotations(self):
    return self.__literal_annotations

  def coroutines(self):
    return self.__coroutines

  def async_generator(self):
    return self.__async_generator

  def async_comprehension(self):
    return self.__async_comprehension

  def await_in_comprehension(self):
    return self.__await_in_comprehension

  def async_for(self):
    return self.__async_for

  def kw_only_args(self):
    return self.__kw_only_args

  def pos_only_args(self):
    return self.__pos_only_args

  def strftime_directives(self):
    return self.__strftime_directives

  def bytes_directives(self):
    return self.__bytes_directives

  def user_defined(self):
    return list(self.__user_defs)

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

  def raise_from_none(self):
    return self.__raise_from_none

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

  def generalized_unpacking(self):
    return self.__generalized_unpacking

  def unpacking_assignment(self):
    return self.__unpacking_assignment

  def bytes_format(self):
    return self.__bytes_format

  def bytearray_format(self):
    return self.__bytearray_format

  def dict_union(self):
    return self.__dict_union

  def dict_union_merge(self):
    return self.__dict_union_merge

  def builtin_generic_type_annotations(self):
    return self.__builtin_generic_type_annotations

  def function_decorators(self):
    return self.__function_decorators

  def class_decorators(self):
    return self.__class_decorators

  def relaxed_decorators(self):
    return self.__relaxed_decorators

  def module_dir_func(self):
    return self.__module_dir_func

  def module_getattr_func(self):
    return self.__module_getattr_func

  def __add_versions_entity(self, mins, versions, info=None, vvprint=False, entity=None):
    if info is not None:
      if versions in self.__info_versions:
        self.__info_versions[versions].append(info)
      else:
        self.__info_versions[versions] = [info]
      if vvprint:
        self.__vvprint(info, entity=entity, versions=versions)
    return combine_versions(mins, versions, self.__config, self.__info_versions)

  def minimum_versions(self):
    mins = [(0, 0), (0, 0)]

    if self.printv2():
      # Must be like this, not `combine_versions(2.0, None)`, since in py2 all print statements call
      # `visit_Print()` but in py3 it's just a regular function via
      # `Call(func=Name(id="print"..)..)`. Otherwise it will say not compatible with 3 when run on
      # py3. The reason for now using `combine_versions(2.0, 3.0)` is that in py2 we cannot
      # distinguish `print x` from `print(x)` - the first fails in py3 but not the second form.
      mins[0] = (2, 0)  # pragma: no cover

    if self.printv3():
      # print() is used so often that we only want to show it once, and with no line.
      self.__vvprint("print(expr)", line=-1, versions=[(2, 0), (3, 0)])
      mins = self.__add_versions_entity(mins, ((2, 0), (3, 0)))

    if self.format27():
      mins = self.__add_versions_entity(mins, ((2, 7), (3, 0)), "`\"..{}..\".format(..)`")

    if self.longv2():
      # `long` is also in `MOD_MEM_REQS`, which means it will trigger below, so we don't put an
      # entity description here.
      mins = self.__add_versions_entity(mins, ((2, 0), None))

    if self.bytesv3():
      # Since byte strings are a `str` synonym as of 2.6+, (2, 6) is returned instead of None.
      # Ref: https://github.com/netromdk/vermin/issues/32
      mins = self.__add_versions_entity(mins, ((2, 6), (3, 0)), "'bytes' type")

    if self.fstrings():
      mins = self.__add_versions_entity(mins, (None, (3, 6)), "fstrings")

    if self.fstrings_self_doc():  # pragma: no cover
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "self-documenting fstrings")

    if self.bool_const():  # pragma: no cover
      mins = self.__add_versions_entity(mins, ((2, 2), (3, 0)), "'bool' constant")

    if self.annotations():
      mins = self.__add_versions_entity(mins, (None, (3, 0)), "annotations")

    if self.var_annotations():
      mins = self.__add_versions_entity(mins, (None, (3, 6)), "variable annotations")

    if self.final_annotations():
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "Final annotations")

    if self.literal_annotations():
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "Literal annotations")

    if self.coroutines():
      mins = self.__add_versions_entity(mins, (None, (3, 5)), "coroutines")

    if self.async_generator():
      mins = self.__add_versions_entity(mins, (None, (3, 6)), "async generators")

    # NOTE: While async comprehensions and await in comprehensions should be in 3.6, they were first
    # put into 3.7 for some reason!

    if self.async_comprehension():
      mins = self.__add_versions_entity(mins, (None, (3, 7)), "async comprehensions")

    if self.await_in_comprehension():
      mins = self.__add_versions_entity(mins, (None, (3, 7)), "await in comprehension")

    if self.async_for():
      mins = self.__add_versions_entity(mins, (None, (3, 6)), "async for-loop")

    if self.named_expressions():
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "named expressions")

    if self.kw_only_args():
      mins = self.__add_versions_entity(mins, (None, (3, 0)), "keyword-only arguments")

    if self.pos_only_args():
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "position only arguments")

    if self.yield_from():
      mins = self.__add_versions_entity(mins, (None, (3, 3)), "yield from")

    if self.raise_cause():
      mins = self.__add_versions_entity(mins, (None, (3, 0)), "exception cause")

    if self.raise_from_none():
      mins = self.__add_versions_entity(mins, (None, (3, 3)), "raise ... from None")

    if self.dict_comprehension():
      mins = self.__add_versions_entity(mins, ((2, 7), (3, 0)), "dict comprehension")

    if self.infix_matrix_multiplication():
      mins = self.__add_versions_entity(mins, (None, (3, 5)), "infix matrix multiplication")

    if self.continue_in_finally():
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "'continue' in 'finally'")

    if self.modular_inverse_pow():
      mins = self.__add_versions_entity(mins, (None, (3, 8)), "modular inverse 'pow()'")

    if self.with_statement():
      mins = self.__add_versions_entity(mins, ((2, 5), (3, 0)), "'with' statement")

    if self.generalized_unpacking():
      mins = self.__add_versions_entity(mins, (None, (3, 5)), "generalized unpacking")

    if self.unpacking_assignment():
      mins = self.__add_versions_entity(mins, (None, (3, 0)), "unpacking assignment")

    if self.bytes_format():
      # Since byte strings are a `str` synonym as of 2.6+, and thus also supports `%` formatting,
      # (2, 6) is returned instead of None.
      mins = self.__add_versions_entity(mins, ((2, 6), (3, 5)), "bytes format")

    if self.bytearray_format():
      mins = self.__add_versions_entity(mins, (None, (3, 5)), "bytearray format")

    if self.dict_union():
      mins = self.__add_versions_entity(mins, (None, (3, 9)), "dict union")
    if self.dict_union_merge():
      mins = self.__add_versions_entity(mins, (None, (3, 9)), "dict union merge")

    if self.builtin_generic_type_annotations():
      mins = self.__add_versions_entity(mins, (None, (3, 9)), "builtin generic type annotations")

    if self.function_decorators():
      mins = self.__add_versions_entity(mins, ((2, 4), (3, 0)), "function decorators")

    if self.class_decorators():
      mins = self.__add_versions_entity(mins, ((2, 6), (3, 0)), "class decorators")

    if self.relaxed_decorators():
      mins = self.__add_versions_entity(mins, (None, (3, 9)), "relaxed decorators")

    for directive in self.strftime_directives():
      if directive in STRFTIME_REQS:
        vers = STRFTIME_REQS[directive]
        mins = self.__add_versions_entity(mins, vers, "strftime directive '{}'".format(directive),
                                          vvprint=True, entity=directive)

    for directive in self.bytes_directives():
      if directive in BYTES_REQS:
        vers = BYTES_REQS[directive]
        mins = self.__add_versions_entity(mins, vers, "bytes directive '{}'".format(directive),
                                          vvprint=True, entity=directive)

    for typecode in self.array_typecodes():
      if typecode in ARRAY_TYPECODE_REQS:
        vers = ARRAY_TYPECODE_REQS[typecode]
        mins = self.__add_versions_entity(mins, vers, "array typecode '{}'".format(typecode),
                                          vvprint=True, entity=typecode)

    for name in self.codecs_error_handlers():
      if name in CODECS_ERROR_HANDLERS:
        vers = CODECS_ERROR_HANDLERS[name]
        mins = self.__add_versions_entity(mins, vers, "codecs error handler name '{}'".format(name),
                                          vvprint=True, entity=name)

    for encoding in self.codecs_encodings():
      for encs in CODECS_ENCODINGS:
        if encoding.lower() in encs:
          vers = CODECS_ENCODINGS[encs]
          mins = self.__add_versions_entity(mins, vers, "codecs encoding '{}'".format(encoding),
                                            vvprint=True, entity=encoding)

    mods = self.modules()
    for mod in mods:
      if mod in self.__mod_rules:
        vers = self.__mod_rules[mod]
        mins = self.__add_versions_entity(mins, vers, "'{}' module".format(mod), vvprint=True,
                                          entity=mod)

    mems = self.members()
    for mem in mems:
      if mem in self.__mod_mem_reqs_rules:
        vers = self.__mod_mem_reqs_rules[mem]
        mins = self.__add_versions_entity(mins, vers, "'{}' member".format(mem), vvprint=True,
                                          entity=mem)

    kwargs = self.kwargs()
    for fn_kw in kwargs:
      if fn_kw in KWARGS_REQS:
        vers = KWARGS_REQS[fn_kw]
        mins = self.__add_versions_entity(mins, vers, "'{}({})'".format(fn_kw[0], fn_kw[1]),
                                          vvprint=True, entity=fn_kw)

    for user_func_deco in self.user_function_decorators():
      if user_func_deco in DECORATOR_USER_FUNCTIONS:
        vers = DECORATOR_USER_FUNCTIONS[user_func_deco]
        mins = self.__add_versions_entity(mins, vers, "'{}' user function decorator".
                                          format(user_func_deco), vvprint=True,
                                          entity=user_func_deco)
    return mins

  def output_text(self):
    # Throw away dups and sort.
    self.__output_text = self.__config.format().sort_output_lines(list(set(self.__output_text)))

    text = "\n".join(self.__output_text)
    if len(text) > 0:
      text += "\n"
    return text

  def set_no_lines(self, lines):
    self.__no_lines = lines

  def no_lines(self):
    return self.__no_lines

  def __nprint(self, msg):
    if not self.__config.quiet():  # pragma: no cover
      self.__output_text.append(msg)

  def __verbose_print(self, msg, level, entity=None, line=None, versions=None):  # pragma: no cover
    fmt = self.__config.format()
    config_level = self.__config.verbose()
    if fmt.skip_output_line() or config_level < level:
      return

    col = None

    # Line/column numbers start at level 3+ or for parsable format.
    entity = entity if config_level > 2 else None
    if entity is not None and entity in self.__line_col_entities:
      (line, col) = self.__line_col_entities[entity]

    if line == -1:
      line = None
    elif line is None and config_level > 2:
      line = self.__line

    msg = fmt.format_output_line(msg, self.__path, line, col, versions)
    self.__output_text.append(msg)

  def __vprint(self, msg, entity=None):  # pragma: no cover
    self.__verbose_print(msg, 1, entity)

  def __vvprint(self, msg, entity=None, line=None, versions=None):  # pragma: no cover
    self.__verbose_print(msg, 2, entity, line, versions)

  def __vvvprint(self, msg, entity=None, line=None, versions=None):  # pragma: no cover
    self.__verbose_print(msg, 3, entity, line, versions)

  def __vvvvprint(self, msg, entity=None, line=None, versions=None):  # pragma: no cover
    self.__verbose_print(msg, 4, entity, line, versions)

  def __add_module(self, module, line=None, col=None):
    if module in self.__user_defs:  # pragma: no cover
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

    if member in self.__mod_mem_reqs_rules:
      self.__members.append(member)
      self.__add_line_col(member, line, col)

  def __add_kwargs(self, function, keyword, line=None, col=None):
    if function in self.__user_defs:  # pragma: no cover
      self.__vvvvprint("Ignoring function '{}' because it's user-defined!".format(function))
      return

    if self.__config.is_excluded_kwarg(function, keyword):
      self.__vvprint("Excluding kwarg: {}({})".format(function, keyword))
      return

    fn_kw = (function, keyword)
    if fn_kw not in self.__kwargs:
      self.__kwargs.append(fn_kw)
      self.__add_line_col(fn_kw, line, col)

  def __add_user_func_deco(self, ufd, line=None, col=None):
    if ufd in self.__user_defs:
      self.__vvvvprint("Ignoring user function decorator '{}' because it's user-defined!".
                       format(ufd))
      return

    if self.__config.is_excluded(ufd):
      self.__vvprint("Excluding user function decorator: {}".format(ufd))
      return

    if ufd in DECORATOR_USER_FUNCTIONS:
      self.__user_func_decorators.append(ufd)
      self.__add_line_col(ufd, line, col)

  def __add_strftime_directive(self, group, line=None, col=None):
    self.__strftime_directives.append(group)
    self.__add_line_col(group, line, col)

  def __add_bytes_directive(self, group, line=None, col=None):
    self.__bytes_directives.append(group)
    self.__add_line_col(group, line, col)

  def __add_codecs_error_handler(self, func, node):
    if func in CODECS_ERRORS_INDICES:
      idx = CODECS_ERRORS_INDICES[func]

      # Check indexed arguments.
      if 0 <= idx < len(node.args):
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
        if kw.arg == "errors" and hasattr(kw.value, "s"):
          name = kw.value.s
          if self.__config.is_excluded_codecs_error_handler(name):
            self.__vvprint("Excluding codecs error handler: {}".format(name))
            continue
          self.__codecs_error_handlers.append(name)
          self.__add_line_col(name, node.lineno)

  def __add_codecs_encoding(self, func, node):
    if func in CODECS_ENCODINGS_INDICES:
      for idx in CODECS_ENCODINGS_INDICES[func]:
        # Check indexed arguments.
        if 0 <= idx < len(node.args):
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
          if kw.arg in self.__codecs_encodings_kwargs and hasattr(kw.value, "s"):
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
    self.__user_defs.add(name)

  def __add_user_def_node(self, node):
    if isinstance(node, ast.Name) and hasattr(node, "id"):
      self.__add_user_def(node.id)

  def __add_name_res(self, source, target):
    self.__name_res[source] = target

  def __add_name_res_type(self, source, target):
    self.__name_res_type[source] = target

  def __is_builtin_type(self, name):
    return name in self.__builtin_types

  def __resolve_module_name(self, name):
    return self.__module_as_name[name] if name in self.__module_as_name\
      else name

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
          full_name.append(attr.attr)
        if hasattr(attr, "value") and hasattr(attr.value, "id"):
          full_name.append(self.__resolve_module_name(attr.value.id))
      elif isinstance(attr, ast.Call):
        if hasattr(attr, "func") and hasattr(attr.func, "id"):
          full_name.append(attr.func.id)
      elif not primi_type and isinstance(attr, ast.Dict):
        if len(full_name) == 0 or (full_name[0] != "dict" and len(full_name) == 1):
          full_name.append("dict")
      elif not primi_type and isinstance(attr, ast.Set):
        if len(full_name) == 0 or (full_name[0] != "set" and len(full_name) == 1):
          full_name.append("set")
      elif not primi_type and isinstance(attr, ast.List):
        if len(full_name) == 0 or (full_name[0] != "list" and len(full_name) == 1):
          full_name.append("list")
      elif not primi_type and isinstance(attr, ast.Str):
        # pylint: disable=undefined-variable
        if sys.version_info.major == 2 and isinstance(attr.s, unicode):  # novm
          name = "unicode"  # pragma: no cover
        else:
          name = "str"
        if len(full_name) == 0 or (full_name[0] != name and len(full_name) == 1):
          full_name.append(name)
      elif not primi_type and isinstance(attr, ast.Num):
        t = type(attr.n)
        name = None
        if t == int:
          name = "int"
        elif t == float:
          name = "float"
        if sys.version_info.major == 2 and t == long:  # novm # pylint: disable=undefined-variable
          name = "long"  # pragma: no cover
        if name is not None and len(full_name) == 0 or \
          (full_name[0] != name and len(full_name) == 1):
          full_name.append(name)
      elif not primi_type and hasattr(ast, "Bytes") and isinstance(attr, ast.Bytes):
        if len(full_name) == 0 or (full_name[0] != "bytes" and len(full_name) == 1):
          full_name.append("bytes")
    full_name.reverse()
    return full_name

  def __add_name_res_assign_node(self, node):
    if not hasattr(node, "value"):
      return  # pragma: no cover

    value_name = None
    type_name = None

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
      # pylint: disable=undefined-variable
      if sys.version_info.major == 2 and isinstance(node.value.s, unicode):  # novm
        value_name = "unicode"  # pragma: no cover
      else:
        value_name = "str"
    elif isinstance(node.value, ast.Num):
      t = type(node.value.n)
      if t == int:
        value_name = "int"
      elif sys.version_info.major == 2 and t == long:  # novm # pylint: disable=undefined-variable
        value_name = "long"  # pragma: no cover
      elif t == float:
        value_name = "float"
    elif hasattr(ast, "Bytes") and isinstance(node.value, ast.Bytes):
      value_name = "bytes"

    # When a type name is used, and not a type instance.
    elif isinstance(node.value, ast.Name):
      type_name = node.value.id

    if value_name is None and type_name is None:
      return

    targets = []
    if hasattr(node, "targets"):
      targets = node.targets
    elif hasattr(node, "target"):
      targets.append(node.target)
    for target in targets:
      if isinstance(target, ast.Name):
        target_name = target.id
        if value_name is not None:
          self.__add_name_res(target_name, value_name)
        elif type_name is not None:
          self.__add_name_res_type(target_name, type_name)

  def __add_line_col(self, entity, line, col=None):
    if line is not None:
      self.__line_col_entities[entity] = (line, col)

  def __add_array_typecode(self, typecode, line=None, col=None):
    if typecode not in self.__array_typecodes:
      self.__array_typecodes.append(typecode)
      self.__add_line_col(typecode, line, col)

  def __is_no_line(self, line):
    return line in self.__no_lines

  def __after_visit_all(self):
    # Remove any modules and members that were added before any known user-definitions. Do it in
    # reverse so the indices are kept while traversing!
    for ud in self.__user_defs:
      for i in reverse_range(self.__modules):
        if self.__modules[i] == ud:  # pragma: no cover
          self.__vvvvprint("Ignoring module '{}' because it's user-defined!".format(ud))
          del(self.__modules[i])

      for i in reverse_range(self.__members):
        if self.__members[i] == ud:  # pragma: no cover
          self.__vvvvprint("Ignoring member '{}' because it's user-defined!".format(ud))
          del(self.__members[i])

  # Entry point of source visitor.
  def tour(self, node):
    self.visit(node)
    self.__after_visit_all()

  def generic_visit(self, node):
    if hasattr(node, "lineno"):
      self.__line = node.lineno
    self.__depth += 1
    if self.__config.print_visits():
      self.__nprint("| " * self.__depth + ast.dump(node))  # pragma: no cover
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

  def visit_ImportFrom(self, node):
    if node.module is None:
      return  # pragma: no cover

    # Ignore modules that aren't top-level, such as `.typing` and `..typing` that are relative and
    # might be files in local packages.
    if hasattr(node, "level") and node.level > 0:
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

    # Names used within `except ..:` or `raise ..` should be detected as members being used.
    if self.__seen_except_handler or self.__seen_raise:
      self.__add_member(node.id, node.lineno, node.col_offset)

  def visit_Print(self, node):  # pragma: no cover
    self.__printv2 = True
    self.generic_visit(node)

  def visit_Starred(self, node):
    # Unpacking assignment is when a starred expression `*` is used on the left-hand side of an
    # assignment, like `*a, b = [1, 2, 3]`.
    if isinstance(node.ctx, ast.Store):
      self.__unpacking_assignment = True
      self.__vvprint("unpacking assignment", versions=[None, (3, 0)])
    self.generic_visit(node)

  def __check_generalized_unpacking(self, node):
    def has_gen_unp():
      self.__generalized_unpacking = True
      self.__vvprint("generalized unpacking", versions=[None, (3, 5)])

    # Call arguments and keywords: Check if more than one unpacking is used or if unpacking is used
    # before the end. This is so because in 3.4, unpacking in function call parameter list is only
    # allowed at the end of the parameter list, and only one unpacking is allowed.
    if isinstance(node, ast.Call):
      def check_gen_unp(pos, total):
        val = len(pos) > 1 or any(p < total - 1 for p in pos)
        if val:
          has_gen_unp()
        return val

      if hasattr(node, "args") and hasattr(ast, "Starred"):
        total = len(node.args)
        pos = []
        for i in range(total):
          if is_valid_star_unpack(node.args[i]):
            pos.append(i)
        if check_gen_unp(pos, total):
          return

      if hasattr(node, "keywords"):
        total = len(node.keywords)
        pos = []
        for i in range(total):
          kw = node.keywords[i]
          if kw.arg is None and kw.value is not None:
            pos.append(i)
        if check_gen_unp(pos, total):
          return

    # Any unpacking in tuples, sets, or lists is generalized unpacking.
    elif isinstance(node, (ast.Tuple, ast.Set, ast.List)) and hasattr(ast, "Starred"):
      if any(is_valid_star_unpack(elt) for elt in node.elts):
        has_gen_unp()
        return

    # Any unpacking in dicts is generalized unpacking.
    elif isinstance(node, ast.Dict):
      if any(key is None and value is not None
             for (key, value) in zip(node.keys, node.values)):
        has_gen_unp()

  def __push_function_name(self, name):
    self.__function_name = name
    self.__function_name_stack.append(name)

  def __pop_function_name(self):
    self.__function_name = self.__function_name_stack.pop() \
      if len(self.__function_name_stack) > 0 else None

  def visit_Call(self, node):
    if self.__is_no_line(node.lineno):
      return

    if hasattr(node, "func"):
      func = node.func

      if hasattr(func, "id"):
        self.__push_function_name(func.id)
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
              # "array" = 5 + 1 = 6
              self.__add_array_typecode(arg.s, node.lineno, node.col_offset + 6)
        elif func.id == "pow" and len(node.args) == 3:
          # Check if the second of three arguments of pow() is negative.
          if is_int_node(node.args[0]) and is_neg_int_node(node.args[1]) and \
             is_int_node(node.args[2]):
            self.__mod_inverse_pow = True
            self.__vvprint("modular inverse pow()", versions=[None, (3, 8)])
      elif hasattr(func, "attr"):
        attr = func.attr
        if attr == "format" and hasattr(func, "value") and isinstance(func.value, ast.Str) and \
           "{}" in func.value.s:
          self.__vvprint("`\"..{}..\".format(..)`", versions=[(2, 7), (3, 0)])
          self.__format27 = True
        elif attr in ("strftime", "strptime") and hasattr(node, "args"):
          for arg in node.args:
            if hasattr(arg, "s"):
              for directive in STRFTIME_DIRECTIVE_REGEX.findall(arg.s):
                self.__add_strftime_directive(directive, node.lineno)

      if isinstance(func, ast.Attribute):
        self.__push_function_name(dotted_name(self.__get_attribute_name(func)))
        self.__check_codecs_function(self.__function_name, node)
        if self.__function_name == "array.array":
          for arg in node.args:
            if isinstance(arg, ast.Str) and hasattr(arg, "s"):
              # "array.array" = 5 + 1 + 5 + 1 = 12
              self.__add_array_typecode(arg.s, node.lineno, node.col_offset + 12)

    self.__check_generalized_unpacking(node)
    self.generic_visit(node)
    self.__pop_function_name()

  def visit_Attribute(self, node):
    full_name = self.__get_attribute_name(node)
    line = node.lineno
    if len(full_name) > 0:
      dotted = dotted_name(full_name)
      for mod in self.__modules:
        if full_name[0] == mod:
          self.__add_module(dotted, line)
        elif full_name[0] in self.__import_mem_mod:
          self.__add_member(dotted_name([self.__import_mem_mod[full_name[0]], full_name]), line)
      self.__add_member(dotted, line)

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
    for func_name in self.__function_name_stack:
      # kwarg related.
      exp_name = func_name.split(".")

      # Check if function is imported from module.
      if func_name in self.__import_mem_mod:
        mod = self.__import_mem_mod[func_name]
        self.__add_kwargs(dotted_name([mod, func_name]), node.arg, self.__line)

      # When having "ElementTree.tostringlist", for instance, and include mapping "{'ElementTree':
      # 'xml.etree'}" then try piecing them together to form a match.
      elif exp_name[0] in self.__import_mem_mod:
        mod = self.__import_mem_mod[exp_name[0]]
        self.__add_kwargs(dotted_name([mod, func_name]), node.arg, self.__line)

      # Lookup indirect names via variables.
      elif exp_name[0] in self.__name_res:
        res = self.__name_res[exp_name[0]]
        if res in self.__import_mem_mod:
          mod = self.__import_mem_mod[res]
          self.__add_kwargs(dotted_name([mod, res, exp_name[1:]]), node.arg, self.__line)

        # Try as FQN.
        else:
          self.__add_kwargs(dotted_name([res, exp_name[1:]]), node.arg, self.__line)

      # Only add direct function if not found via module/class/member.
      else:
        self.__add_kwargs(func_name, node.arg, self.__line)

  def visit_Bytes(self, node):
    self.__bytesv3 = True
    self.__vvprint("byte string (b'..') or `str` synonym", versions=[(2, 6), (3, 0)])

    if hasattr(node, "s"):
      for directive in BYTES_DIRECTIVE_REGEX.findall(str(node.s)):
        self.__add_bytes_directive(directive, node.lineno)

  def __is_dict(self, node):
    """Checks if node is a dict either by direct instance, name, constructor, function/lambda body,
    or subscript index value."""
    if isinstance(node, ast.Dict):
      return True
    if isinstance(node, ast.Name) and\
       node.id in self.__name_res and self.__name_res[node.id] == "dict":
      return True
    if isinstance(node, ast.Call):
      if isinstance(node.func, ast.Name) and node.func.id == "dict":
        return True
      if isinstance(node.func, ast.Lambda) and self.__is_dict(node.func.body):
        return True
    elif isinstance(node, ast.Subscript):
      n = None
      if isinstance(node.slice, ast.Index) and isinstance(node.slice.value, ast.Num):
        n = node.slice.value.n
      elif hasattr(ast, "Constant") and isinstance(node.slice, ast.Constant):
        n = node.slice.value
      if isinstance(n, int):
        for tup in ast.iter_fields(node.value):
          if (tup[0] == "elts" or tup[0] == "values") and n < len(tup[1]) and\
             self.__is_dict(tup[1][n]):
            return True
    return False

  def __resolve_full_name(self, name):
    """Tries to resolve name into a fully dotted name. Takes name as a string, ast.Name or
ast.Call(func=ast.Name)."""
    if isinstance(name, ast.Name):
      name = name.id
    elif isinstance(name, ast.Call) and isinstance(name.func, ast.Name):
      name = name.func.id
    elif isinstance(name, ast.Attribute):
      name = dotted_name(self.__get_attribute_name(name))
    name = self.__name_res[name] if name in self.__name_res else name
    if name in self.__module_as_name:
      return self.__module_as_name[name]
    if name in self.__import_mem_mod:
      return dotted_name([self.__import_mem_mod[name], name])
    return name

  def visit_BinOp(self, node):
    # Examples:
    #   BinOp(left=Bytes(s=b'%4x'), op=Mod(), right=Num(n=10))
    #   BinOp(left=Call(func=Name(id='bytearray', ctx=Load()), args=[Bytes(s=b'%x')], keywords=[]),
    #         op=Mod(), right=Num(n=10))
    if (hasattr(ast, "Bytes") and isinstance(node.left, ast.Bytes))\
       and isinstance(node.op, ast.Mod):
      self.__bytes_format = True
      self.__vvprint("bytes `%` formatting or `str` synonym", versions=[(2, 6), (3, 5)])

    if (isinstance(node.left, ast.Call) and isinstance(node.left.func, ast.Name) and
         node.left.func.id == "bytearray") and isinstance(node.op, ast.Mod):
      self.__bytearray_format = True
      self.__vvprint("bytearray `%` formatting", versions=[None, (3, 5)])

    # Example:
    # BinOp(left=Dict(keys=[Constant(value='a')], values=[Constant(value=1)]),
    #       op=BitOr(),
    #       right=Dict(keys=[Constant(value='b')], values=[Constant(value=2)]))
    if isinstance(node.op, ast.BitOr):
      def has_du():
        self.__dict_union = True
        self.__vvprint("dict union (dict | dict)", line=node.lineno, versions=[None, (3, 9)])

      left_dict = self.__is_dict(node.left)
      right_dict = self.__is_dict(node.right)
      left_special = self.__resolve_full_name(node.left) in DICT_UNION_SUPPORTED_TYPES
      right_special = self.__resolve_full_name(node.right) in DICT_UNION_SUPPORTED_TYPES
      if (left_dict or left_special) and (right_dict or right_special):
        has_du()

    self.generic_visit(node)

  def visit_Constant(self, node):
    # From 3.8, Bytes(s=b'%x') is represented as Constant(value=b'%x', kind=None) instead.
    if hasattr(node, "value") and isinstance(node.value, bytes):
      self.__bytesv3 = True
      self.__vvprint("byte string (b'..') or `str` synonym", versions=[(2, 6), (3, 0)])

      for directive in BYTES_DIRECTIVE_REGEX.findall(str(node.value)):
        self.__add_bytes_directive(directive, node.lineno)

  def __extract_fstring_value(self, node):  # pragma: no cover
    value = []
    is_call = False
    for n in ast.walk(node):
      if isinstance(n, ast.Name):
        value.append(n.id)

      elif hasattr(ast, "Constant") and isinstance(n, ast.Constant):
        v = str(n.value)
        if isinstance(n.value, str):
          v = "\"{}\"".format(v)
        value.append(v)

      elif isinstance(n, ast.Add):
        value.append("+")

      elif isinstance(n, ast.Sub):
        value.append("-")

      elif isinstance(n, ast.Div):
        value.append("/")

      elif isinstance(n, ast.FloorDiv):
        value.append("//")

      elif isinstance(n, ast.Mult):
        value.append("*")

      elif hasattr(ast, "MatMult") and isinstance(n, ast.MatMult):
        value.append("@")

      elif isinstance(n, ast.Mod):
        value.append("%")

      elif isinstance(n, ast.Pow):
        value.append("**")

      elif isinstance(n, ast.BitXor):
        value.append("^")

      elif isinstance(n, ast.BitOr):
        value.append("|")

      elif isinstance(n, ast.BitAnd):
        value.append("&")

      elif isinstance(n, ast.Not):
        value.append("not ")

      elif isinstance(n, ast.USub):
        value.append("-")

      elif isinstance(n, ast.UAdd):
        value.append("+")

      elif isinstance(n, ast.Invert):
        value.append("~")

      elif isinstance(n, ast.LShift):
        value.append("<<")

      elif isinstance(n, ast.RShift):
        value.append(">>")

      elif isinstance(n, ast.In):
        value.append("in ")

      elif isinstance(n, ast.NotIn):
        value.append("not in ")

      elif isinstance(n, ast.Is):
        value.append(" is ")

      elif isinstance(n, ast.IsNot):
        value.append(" is not ")

      elif isinstance(n, ast.Or):
        value.append(" or ")

      elif isinstance(n, ast.And):
        value.append(" and ")

      elif isinstance(n, ast.Eq):
        value.append(" == ")

      elif isinstance(n, ast.NotEq):
        value.append(" != ")

      elif isinstance(n, ast.LtE):
        value.append(" <= ")

      elif isinstance(n, ast.GtE):
        value.append(" >= ")

      elif isinstance(n, ast.Gt):
        value.append(" > ")

      elif isinstance(n, ast.Lt):
        value.append(" < ")

      elif hasattr(ast, "comprehension") and isinstance(n, ast.comprehension):
        target = self.__extract_fstring_value(n.target)
        iter_ = self.__extract_fstring_value(n.iter)
        value.append("{} in {}".format(target, iter_))
        break

      elif isinstance(n, ast.Attribute):
        value += self.__get_attribute_name(n)
        break

      elif isinstance(n, ast.keyword):
        val = self.__extract_fstring_value(n.value)
        value.append("{}={}".format(n.arg, val))
        break

      elif isinstance(n, ast.Call):
        is_call = True
        if len(n.args) == 0 and len(n.keywords) == 0:
          value.append("{}()".format(self.__extract_fstring_value(n.func)))
          break

      elif isinstance(n, ast.BinOp):
        left = self.__extract_fstring_value(n.left)
        op = self.__extract_fstring_value(n.op)
        right = self.__extract_fstring_value(n.right)
        value.append(left + op + right)
        break

      elif isinstance(n, ast.UnaryOp):
        op = self.__extract_fstring_value(n.op)
        operand = self.__extract_fstring_value(n.operand)
        value.append(op + operand)
        break

      elif isinstance(n, ast.BoolOp):
        op = self.__extract_fstring_value(n.op)
        vals = [self.__extract_fstring_value(v) for v in n.values]
        value.append(op.join(vals))
        break

      elif isinstance(n, ast.IfExp):
        test = self.__extract_fstring_value(n.test)
        body = self.__extract_fstring_value(n.body)
        orelse = self.__extract_fstring_value(n.orelse)
        value.append("{} if {} else {}".format(body, test, orelse))
        break

      elif isinstance(n, ast.Tuple):
        elts = [self.__extract_fstring_value(elt) for elt in n.elts]
        value.append("({})".format(",".join(elts)))
        break

      elif isinstance(n, ast.List):
        elts = [self.__extract_fstring_value(elt) for elt in n.elts]
        value.append("[{}]".format(",".join(elts)))
        break

      elif isinstance(n, ast.Set):
        elts = [self.__extract_fstring_value(elt) for elt in n.elts]
        value.append("{" + ",".join(elts) + "}")
        break

      elif isinstance(n, ast.Dict):
        keys = [self.__extract_fstring_value(key) for key in n.keys]
        vals = [self.__extract_fstring_value(val) for val in n.values]
        kvs = ",".join(["{}:{}".format(k, v) for (k, v) in zip(keys, vals)])
        value.append("{" + kvs + "}")
        break

      elif isinstance(n, ast.Index):
        val = self.__extract_fstring_value(n.value)
        value.append(val)
        break

      elif hasattr(ast, "ListComp") and isinstance(n, ast.ListComp):
        elt = self.__extract_fstring_value(n.elt)
        gens = [self.__extract_fstring_value(gen) for gen in n.generators]
        value.append("[{} for {}]".format(elt, " ".join(gens)))
        break

      elif hasattr(ast, "SetComp") and isinstance(n, ast.SetComp):
        elt = self.__extract_fstring_value(n.elt)
        gens = [self.__extract_fstring_value(gen) for gen in n.generators]
        value.append("{" + "{} for {}".format(elt, " ".join(gens)) + "}")
        break

      elif hasattr(ast, "DictComp") and isinstance(n, ast.DictComp):
        key = self.__extract_fstring_value(n.key)
        val = self.__extract_fstring_value(n.value)
        gens = [self.__extract_fstring_value(gen) for gen in n.generators]
        value.append("{" + "{}:{} for {}".format(key, val, " ".join(gens)) + "}")
        break

      elif hasattr(ast, "GeneratorExp") and isinstance(n, ast.GeneratorExp):
        elt = self.__extract_fstring_value(n.elt)
        gens = [self.__extract_fstring_value(gen) for gen in n.generators]
        value.append("({} for {})".format(elt, " ".join(gens)))
        break

      elif isinstance(n, ast.Compare):
        left = self.__extract_fstring_value(n.left)
        ops = [self.__extract_fstring_value(op) for op in n.ops]
        comps = [self.__extract_fstring_value(comp) for comp in n.comparators]
        value.append(left + "".join(["{} {}".format(op, comp) for (op, comp) in zip(ops, comps)]))
        break

      elif isinstance(n, ast.Subscript):
        val = self.__extract_fstring_value(n.value)
        slice_ = self.__extract_fstring_value(n.slice)
        value.append("{}[{}]".format(val, slice_))
        break

    if is_call:
      return "(".join(value) + ")" * (len(value) - 1)  # "a(b(c()))"
    return ".".join(value)  # "a" or "a.b"..

  def visit_JoinedStr(self, node):
    self.__fstrings = True
    self.__vvprint("f-strings", versions=[None, (3, 6)])
    if self.__fstring_self_doc_enabled and hasattr(node, "values"):  # pragma: no cover
      total = len(node.values)
      for i in range(total):
        val = node.values[i]
        # A self-referencing f-string will be at the end of the Constant, like "..stuff..expr=", and
        # the next value will be a FormattedValue(value=..) with Names or nested Calls with Names
        # inside, for instance.
        if isinstance(val, ast.Constant) and hasattr(val, "value") and \
           isinstance(val.value, str) and val.value.strip().endswith("=") and i + 1 < total:
            next_val = node.values[i + 1]
            if isinstance(next_val, ast.FormattedValue):
              fstring_value =\
                trim_fstring_value(self.__extract_fstring_value(next_val.value))
              if len(fstring_value) > 0 and\
                trim_fstring_value(val.value).endswith(fstring_value + "="):
                  self.__fstrings_self_doc = True
                  self.__vvprint("self-documenting fstrings", versions=[None, (3, 8)])
                  break

    self.generic_visit(node)

  # Mark variable names as aliases.
  def visit_Assign(self, node):
    if self.__is_no_line(node.lineno):
      return
    for target in node.targets:
      self.__add_user_def_node(target)
    self.__add_name_res_assign_node(node)
    self.generic_visit(node)

  def visit_AugAssign(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__add_user_def_node(node.target)
    self.__add_name_res_assign_node(node)

    # Example:
    # AugAssign(target=Name(id='d', ctx=Store()),
    #           op=BitOr(),
    #           value=Dict(keys=[Constant(value='b')], values=[Constant(value=2)]))
    if isinstance(node.op, ast.BitOr) and self.__is_dict(node.value):
      full_name = self.__resolve_full_name(node.target)
      if full_name in DICT_UNION_MERGE_SUPPORTED_TYPES or self.__is_dict(node.target):
        self.__dict_union_merge = True
        self.__vvprint("dict union merge (dict var |= dict)", line=node.lineno,
                       versions=[None, (3, 9)])

    self.generic_visit(node)

  def visit_AnnAssign(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__add_user_def_node(node.target)
    self.__add_name_res_assign_node(node)
    if self.__config.eval_annotations():
      self.generic_visit(node)
    self.__annotations = True
    self.__var_annotations = True
    self.__vvprint("variable annotations", versions=[None, (3, 6)])
    if hasattr(node, "annotation"):
      ann = node.annotation
      if (isinstance(ann, ast.Name) and ann.id == "Final") or \
         (isinstance(ann, ast.Subscript) and hasattr(ann.value, "id") and
           ann.value.id == "Final"):
        self.__final_annotations = True
        self.__vvprint("final variable annotations", versions=[None, (3, 8)])
      elif (isinstance(ann, ast.Name) and ann.id == "Literal") or \
         (isinstance(ann, ast.Subscript) and hasattr(ann.value, "id") and
           ann.value.id == "Literal"):
        self.__literal_annotations = True
        self.__vvprint("literal variable annotations", versions=[None, (3, 8)])

  def __check_relaxed_decorators(self, node):
    # Checking for relaxed decorators, i.e. decorators that aren't a dotted name (name or attribute)
    # or a function call. `Load()` is also ignored since they occur all over the place for
    # non-relaxed decorators, too.
    for decorator in node.decorator_list:
      if self.__is_no_line(decorator.lineno):
        continue
      # If decorator is a function call, then only look in the body branch, not arguments and
      # such.
      for n in ast.walk(decorator if not isinstance(decorator, ast.Call) else decorator.func):
        if not isinstance(n, (ast.Name, ast.Attribute, ast.Load)):
          self.__relaxed_decorators = True
          self.__vvprint("relaxed decorators", line=decorator.lineno, versions=[None, (3, 9)])
          break

  def __check_user_func_decorators(self, node):
    # Checking for user function decorators, i.e. decorators that aren't used as function calls but
    # names, and they take the docorated function as argument in the decorator.
    for decorator in node.decorator_list:
      if self.__is_no_line(decorator.lineno):
        continue
      # Not ast.Call.
      if isinstance(decorator, (ast.Name, ast.Attribute)):
        if isinstance(decorator, ast.Name):
          name = decorator.id
        elif isinstance(decorator, ast.Attribute):
          name = dotted_name(self.__get_attribute_name(decorator))
        if name in self.__import_mem_mod:
          name = dotted_name([self.__import_mem_mod[name], name])
        elif name in self.__module_as_name:
          name = self.__module_as_name[name]
        self.__add_user_func_deco(name, line=decorator.lineno)

  def __handle_FunctionDef(self, node):
    if self.__is_no_line(node.lineno):
      return False

    self.__add_user_def(node.name)

    # Module-level `__dir__()` is supported by `dir()` and `__getattr__(name)` through lookup since
    # 3.7 but it isn't a version requirement because it has always been possible to define such
    # functions.
    args = node.args
    if self.__depth == 1 and self.__is_init_file and\
       (not hasattr(args, "posonlyargs") or len(args.posonlyargs) == 0) and\
       (not hasattr(args, "kwonlyargs") or len(args.kwonlyargs) == 0) and\
       (not hasattr(args, "kwarg") or args.kwarg is None):
      if node.name == "__dir__" and len(args.args) == 0:
        self.__module_dir_func = True
        self.__vvprint("module `__dir__()` supported by `dir()` since 3.7", line=node.lineno)
      elif node.name == "__getattr__" and len(args.args) == 1:
        self.__module_getattr_func = True
        self.__vvprint("module `__getattr__(name)` supported through lookup since 3.7",
                       line=node.lineno)

    if getattr(node, "decorator_list", None):
      decos = node.decorator_list
      # Exclude only if all decorators are excluded, otherwise the function decorator version
      # requirement should still be in effect.
      if not all(self.__is_no_line(deco.lineno) for deco in decos):
        deco_line = [deco.lineno for deco in decos if not self.__is_no_line(deco.lineno)][0]
        self.__function_decorators = True
        self.__vvprint("function decorators", line=deco_line, versions=[(2, 4), (3, 0)])
        self.__check_relaxed_decorators(node)
        self.__check_user_func_decorators(node)

    self.generic_visit(node)

    def has_ann():
      self.__annotations = True
      self.__vvprint("annotations", line=node.lineno, versions=[None, (3, 0)])

    # Check if the return annotation is set
    if hasattr(node, "returns") and node.returns:
      has_ann()
      return True

    def has_lit_ann():
      if self.__config.eval_annotations():
        self.__literal_annotations = True
        self.__vvprint("literal variable annotations", line=node.lineno, versions=[None, (3, 8)])

    for arg in node.args.args:
      if not hasattr(arg, "annotation") or not arg.annotation:
        continue

      has_ann()

      ann = arg.annotation
      if (isinstance(ann, ast.Name) and ann.id == "Literal") or \
         (isinstance(ann, ast.Subscript) and
         hasattr(ann.value, "id") and ann.value.id == "Literal"):
        has_lit_ann()
        break

      attr_name = dotted_name(self.__get_attribute_name(ann))
      if attr_name in ("Literal", "typing.Literal"):
        has_lit_ann()
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
      self.__vvprint("coroutines (async)", line=node.lineno, versions=[None, (3, 5)])
      if self.__seen_yield > seen_yield and self.__seen_await > seen_await:
        self.__async_generator = True
        self.__vvprint("async generators (await and yield in same func)",
                       line=node.lineno, versions=[None, (3, 6)])

      # Reset to seen awaits/yields before async function.
      self.__seen_await = seen_await
      self.__seen_yield = seen_yield

  def visit_Await(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__coroutines = True
    self.__vvprint("coroutines (await)", versions=[None, (3, 5)])
    self.__seen_await += 1
    self.generic_visit(node)

  def visit_ClassDef(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__add_user_def(node.name)
    if getattr(node, "decorator_list", None):
      decos = node.decorator_list
      # Exclude only if all decorators are excluded, otherwise the class decorator version
      # requirement should still be in effect.
      if not all(self.__is_no_line(deco.lineno) for deco in decos):
        deco_line = [deco.lineno for deco in decos if not self.__is_no_line(deco.lineno)][0]
        self.__class_decorators = True
        self.__vvprint("class decorators", line=deco_line, versions=[(2, 6), (3, 0)])
        self.__check_relaxed_decorators(node)
    self.generic_visit(node)

  def visit_NameConstant(self, node):
    if node.value is True or node.value is False:  # pragma: no cover
      self.__bool_const = True
      self.__vvvprint("True/False constant", versions=[(2, 2), (3, 0)])

  def visit_NamedExpr(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__named_exprs = True
    self.__vvprint("named expressions", versions=[None, (3, 8)])
    self.generic_visit(node)

  def visit_arguments(self, node):
    if hasattr(node, "kwonlyargs") and len(node.kwonlyargs) > 0:
      self.__kw_only_args = True
      self.__vvprint("keyword-only parameters", versions=[None, (3, 0)])
    if hasattr(node, "posonlyargs") and len(node.posonlyargs) > 0:
      self.__pos_only_args = True
      self.__vvprint("positional-only parameters", versions=[None, (3, 8)])
    self.generic_visit(node)

  def visit_YieldFrom(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__yield_from = True
    self.__vvprint("`yield from`", versions=[None, (3, 3)])
    self.generic_visit(node)

  def visit_Yield(self, node):
    if self.__is_no_line(node.lineno):
      return
    self.__seen_yield += 1
    self.generic_visit(node)

  def visit_Raise(self, node):
    if self.__is_no_line(node.lineno):
      return
    if hasattr(node, "cause") and node.cause is not None:
      self.__raise_cause = True
      self.__vvprint("exception cause", line=node.lineno, versions=[None, (3, 0)])
      if is_none_node(node.cause):
        self.__raise_from_none = True
        self.__vvprint("raise ... from None", line=node.lineno, versions=[None, (3, 3)])
    seen_raise = self.__seen_raise
    self.__seen_raise = True
    self.generic_visit(node)
    self.__seen_raise = seen_raise

  def visit_ExceptHandler(self, node):
    if self.__is_no_line(node.lineno):
      return
    seen_except = self.__seen_except_handler
    self.__seen_except_handler = True
    self.generic_visit(node)
    self.__seen_except_handler = seen_except

  def visit_DictComp(self, node):
    self.__dict_comp = True
    self.__vvprint("dict comprehensions", versions=[(2, 7), (3, 0)])
    self.generic_visit(node)

  def visit_MatMult(self, node):
    self.__mat_mult = True
    self.__vvprint("infix matrix multiplication", versions=[None, (3, 5)])
    self.generic_visit(node)

  def visit_comprehension(self, node):
    if hasattr(node, "is_async") and node.is_async == 1:
      self.__async_comprehension = True
      self.__vvprint("async comprehensions", versions=[None, (3, 7)])

    seen_await = self.__seen_await
    self.generic_visit(node)
    if self.__seen_await > seen_await:
      self.__await_in_comprehension = True
      self.__vvprint("await in comprehensions", versions=[None, (3, 7)])

    # Reset to seen awaits before comprehension.
    self.__seen_await = seen_await

  def visit_Continue(self, node):
    # Only accept continue in try-finally if no intermediary loops have been encountered.
    if len(self.__try_finally) > 0:
      (seen_for, seen_while) = self.__try_finally[-1]
      if seen_for == self.__seen_for and seen_while == self.__seen_while:
        self.__continue_in_finally = True
        self.__vvprint("continue in finally block", line=node.lineno, versions=[None, (3, 8)])

  def visit_With(self, node):
    if self.__config.lax() or self.__is_no_line(node.lineno):
      return
    self.__with_statement = True
    self.__vvprint("`with`", line=node.lineno, versions=[(2, 5), (3, 0)])
    self.generic_visit(node)

  def visit_Dict(self, node):
    self.__check_generalized_unpacking(node)
    self.generic_visit(node)

  def visit_Tuple(self, node):
    self.__check_generalized_unpacking(node)
    self.generic_visit(node)

  def visit_List(self, node):
    self.__check_generalized_unpacking(node)
    self.generic_visit(node)

  def visit_Set(self, node):
    self.__check_generalized_unpacking(node)
    self.generic_visit(node)

  def visit_Subscript(self, node):
    if self.__is_no_line(node.lineno):
      return
    if isinstance(node.value, (ast.Name, ast.Attribute)):
      def match(name):
        if self.__config.eval_annotations():
          if name in self.__user_defs:
            self.__vvvvprint("Ignoring type '{}' because it's user-defined!".format(name))
          else:
            self.__builtin_generic_type_annotations = True
            self.__vvprint("builtin generic type annotation ({}[..])".format(name),
                           versions=[None, (3, 9)])
      if isinstance(node.value, ast.Name):
        coll_name = node.value.id
      else:
        coll_name = dotted_name(self.__get_attribute_name(node.value))
      if coll_name in BUILTIN_GENERIC_ANNOTATION_TYPES:
        match(coll_name)
      elif coll_name in self.__import_mem_mod:
        full_coll_name = dotted_name([self.__import_mem_mod[coll_name], coll_name])
        if full_coll_name in BUILTIN_GENERIC_ANNOTATION_TYPES:
          match(full_coll_name)
      elif coll_name in self.__name_res_type and\
           self.__name_res_type[coll_name] in BUILTIN_GENERIC_ANNOTATION_TYPES:
        match(self.__name_res_type[coll_name])
    self.generic_visit(node)

  # Lax mode and comment-excluded lines skip conditional blocks if enabled.

  def visit_If(self, node):
    if not self.__config.lax() and not self.__is_no_line(node.lineno):
      self.generic_visit(node)

  def visit_IfExp(self, node):
    if not self.__config.lax() and not self.__is_no_line(node.lineno):
      self.generic_visit(node)

  def __handle_for(self, node):
    if not self.__config.lax() and not self.__is_no_line(node.lineno):
      self.__seen_for += 1

      # Check if any value of the for-iterable is a dictionary, then associate for-target variable
      # with a ditionary type such that sub-levels of the for-loop can use it for dict union merge
      # detection.
      old_name_res = self.__name_res
      if hasattr(node.target, "id"):
        for tup in ast.iter_fields(node.iter):
          if tup[0] == "elts" or tup[0] == "values":
            if any(self.__is_dict(elm) for elm in tup[1]):
              self.__name_res[node.target.id] = "dict"
              break

      self.generic_visit(node)
      self.__seen_for -= 1
      self.__name_res = old_name_res

  def visit_For(self, node):
    self.__handle_for(node)

  def visit_AsyncFor(self, node):
    if self.__config.lax() or self.__is_no_line(node.lineno):
      return
    self.__async_for = True
    self.__vvprint("async for-loops", line=node.lineno, versions=[None, (3, 6)])
    self.__handle_for(node)

  def visit_While(self, node):
    if not self.__config.lax() and not self.__is_no_line(node.lineno):
      self.__seen_while += 1
      self.generic_visit(node)
      self.__seen_while -= 1

  def __handle_Try(self, node):
    if not self.__config.lax() and not self.__is_no_line(node.lineno):
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
    self.__handle_Try(node)  # pragma: no cover

  def visit_TryFinally(self, node):
    self.__handle_Try(node)  # pragma: no cover

  def visit_BoolOp(self, node):
    if not self.__config.lax() and not self.__is_no_line(node.lineno):
      self.generic_visit(node)

  # Ignore unused nodes as a speed optimization.

  def visit_alias(self, node):
    pass  # pragma: no cover

  def visit_Load(self, node):
    pass  # pragma: no cover

  def visit_Store(self, node):
    pass  # pragma: no cover

  def visit_Pass(self, node):
    pass  # pragma: no cover

  def visit_Num(self, node):
    pass  # pragma: no cover

  def visit_Not(self, node):
    pass  # pragma: no cover

  def visit_Add(self, node):
    pass  # pragma: no cover

  def visit_Sub(self, node):
    pass  # pragma: no cover

  def visit_Mult(self, node):
    pass  # pragma: no cover

  def visit_Div(self, node):
    pass  # pragma: no cover

  def visit_BitAnd(self, node):
    pass  # pragma: no cover

  def visit_Or(self, node):
    pass  # pragma: no cover

  def visit_BitOr(self, node):
    pass  # pragma: no cover

  def visit_Eq(self, node):
    pass  # pragma: no cover

  def visit_NotEq(self, node):
    pass  # pragma: no cover

  def visit_Lt(self, node):
    pass  # pragma: no cover

  def visit_Gt(self, node):
    pass  # pragma: no cover

  def visit_In(self, node):
    pass  # pragma: no cover

  def visit_Is(self, node):
    pass  # pragma: no cover

  def visit_Break(self, node):
    pass  # pragma: no cover

  def visit_Mod(self, node):
    pass  # pragma: no cover
