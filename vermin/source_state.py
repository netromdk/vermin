import sys
import os
from collections import deque

from .rules import MOD_REQS, MOD_MEM_REQS, KWARGS_REQS

class SourceState:
  """Source file visitation state."""

  def __init__(self, config, path=None, source=None):
    assert config is not None, "Config must be specified!"
    self.config = config
    self.parsable = config.format().name() == "parsable"

    self.path = "<unknown>" if path is None else path

    if isinstance(source, bytes):
      self.source = source.decode(errors="replace")
    else:
      self.source = source

    if self.parsable and not sys.platform.startswith("win32"):
      for c in (":", "\n"):
        assert c not in self.path, "Path '{}' cannot contain '{}'".format(self.path, c)

    self.is_init_file = os.path.basename(self.path) == "__init__.py"

    self.depth = 0
    self.line = 1
    self.lines = None

    # List of lines of output text.
    self.output_text = []

    # Line/column of entities for vvv-printing.
    self.line_col_entities = {}

    self.modules = []
    self.members = []
    self.printv2 = False
    self.printv3 = False
    self.format27 = False  # If format is used so that it requires 2.7+, like '{}' etc.
    self.longv2 = False
    self.bytesv3 = False
    self.fstrings = False
    self.fstrings_self_doc = False
    self.bool_const = False
    self.annotations = False
    self.var_annotations = False
    self.final_annotations = False
    self.literal_annotations = False
    self.coroutines = False
    self.async_generator = False
    self.async_comprehension = False
    self.async_for = False
    self.seen_yield = 0
    self.seen_await = 0
    self.await_in_comprehension = False
    self.named_exprs = False
    self.kw_only_args = False
    self.pos_only_args = False
    self.nonlocal_stmt = False
    self.yield_from = False
    self.raise_cause = False
    self.raise_from_none = False
    self.set_literals = False
    self.set_comp = False
    self.dict_comp = False
    self.mat_mult = False
    self.continue_in_finally = False
    self.seen_for = 0
    self.seen_while = 0
    self.try_finally = []
    self.mod_inverse_pow = False
    self.function_name = None
    self.function_name_stack = deque()
    self.kwargs = []
    self.user_func_decorators = []
    self.strftime_directives = []
    self.bytes_directives = []
    self.codecs_error_handlers = []
    self.codecs_encodings = []
    self.with_statement = False
    self.async_with_statement = False
    self.multi_withitem = False
    self.with_parentheses = False
    self.generalized_unpacking = False
    self.unpacking_assignment = False
    self.ellipsis_out_of_slices = False
    self.bytes_format = False
    self.bytearray_format = False
    self.dict_union = False
    self.dict_union_merge = False
    self.builtin_generic_type_annotations = False
    self.function_decorators = False
    self.class_decorators = False
    self.relaxed_decorators = False
    self.module_dir_func = False
    self.module_getattr_func = False
    self.pattern_matching = False
    self.union_types = False
    self.builtin_types = {"dict", "set", "list", "unicode", "str", "int", "float", "long", "bytes"}
    self.codecs_encodings_kwargs = ("encoding", "data_encoding", "file_encoding")
    self.super_no_args = False
    self.except_star = False
    self.metaclass_class_keyword = False

    # `type X = SomeType`.
    self.type_alias_statement = False

    # Imported members of modules, like "exc_clear" of "sys".
    self.import_mem_mod = {}

    # Name -> name resolutions.
    self.name_res = {}

    # Name -> type resolutions. Is a dictionary of sets.
    self.name_res_type = {}

    # User-defined symbols to be ignored.
    self.user_defs = set()

    # Typecodes for use with `array.array(typecode, [init..])`.
    self.array_typecodes = []

    # Module as-name -> name.
    self.module_as_name = {}

    # Lines that should be ignored if they have the comment "novermin" or "novm".
    self.no_lines = set()

    # Default to disabling fstring self-doc detection since the built-in AST cannot distinguish
    # `f'{a=}'` from `f'a={a}'`, for instance, because it optimizes some information away. And this
    # incorrectly marks some source code as using fstring self-doc when only using general fstring.
    self.fstring_self_doc_enabled = self.config.has_feature("fstring-self-doc")

    # Default to disabling union types detection because it sometimes fails to report it correctly
    # due to using heuristics.
    self.union_types_enabled = self.config.has_feature("union-types")

    # Used for incompatible versions texts.
    self.info_versions = {}

    # Keep track of all Ellipsis nodes in slices for detecting Ellipsis out of slices.
    self.ellipsis_nodes_in_slices = set()

    # Might be using generic/literal annotations that require `--eval-annotations` to work.
    self.maybe_annotations = False

    self.mod_rules = MOD_REQS(self.config)
    self.mod_mem_reqs_rules = MOD_MEM_REQS(self.config)
    self.kwargs_reqs_rules = KWARGS_REQS(self.config)
