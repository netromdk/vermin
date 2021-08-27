from .testutils import VerminTest, current_version

class VerminKwargsTests(VerminTest):
  def test_name_of_ImportError(self):
    self.assertOnlyIn((3, 3), self.detect("ImportError(name=None)"))

  def test_path_of_ImportError(self):
    self.assertOnlyIn((3, 3), self.detect("ImportError(path=None)"))

  def test_filename2_of_OSError(self):
    self.assertOnlyIn((3, 4), self.detect("OSError(filename2=None)"))

  def test_encoding_of_bytearray_decode(self):
    self.assertOnlyIn((3, 2), self.detect("bytearray.decode(encoding=None)"))

  def test_errors_of_bytearray_decode(self):
    self.assertOnlyIn((3, 2), self.detect("bytearray.decode(errors=None)"))

  def test_bytes_per_sep_of_bytearray_hex(self):
    self.assertOnlyIn((3, 8), self.detect("bytearray.hex(bytes_per_sep=None)"))

  def test_sep_of_bytearray_hex(self):
    self.assertOnlyIn((3, 8), self.detect("bytearray.hex(sep=None)"))

  def test_delete_of_bytearray_translate(self):
    self.assertOnlyIn((3, 6), self.detect("bytearray.translate(delete=None)"))

  def test_encoding_of_bytes_decode(self):
    self.assertOnlyIn((3, 2), self.detect("bytes.decode(encoding=None)"))

  def test_errors_of_bytes_decode(self):
    self.assertOnlyIn((3, 2), self.detect("bytes.decode(errors=None)"))

  def test_bytes_per_sep_of_bytes_hex(self):
    self.assertOnlyIn((3, 8), self.detect("bytes.hex(bytes_per_sep=None)"))

  def test_sep_of_bytes_hex(self):
    self.assertOnlyIn((3, 8), self.detect("bytes.hex(sep=None)"))

  def test_delete_of_bytes_translate(self):
    self.assertOnlyIn((3, 6), self.detect("bytes.translate(delete=None)"))

  def test_bytes_per_sep_of_memoryview_hex(self):
    self.assertOnlyIn((3, 8), self.detect("memoryview.hex(bytes_per_sep=None)"))

  def test_sep_of_memoryview_hex(self):
    self.assertOnlyIn((3, 8), self.detect("memoryview.hex(sep=None)"))

  def test_key_of_sorted(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("sorted(key=None)"))

  def test_reverse_of_sorted(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("sorted(reverse=None)"))

  def test_fillchar_of_str_ljust(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("s = str()\ns.ljust(fillchar=None)"))
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("str.ljust(fillchar=None)"))

  def test_chars_of_str_lstrip(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("str.lstrip(chars=None)"))

  def test_fillchar_of_str_rjust(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("str.rjust(fillchar=None)"))

  def test_chars_of_str_rstrip(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("str.rstrip(chars=None)"))

  def test_chars_of_str_strip(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("str.strip(chars=None)"))

  def test_weights_of_statistics_harmonic_mean(self):
    self.assertOnlyIn((3, 10), self.detect("""
from statistics import harmonic_mean
harmonic_mean(weights=None)
"""))

  def test_start_of_sum(self):
    self.assertOnlyIn((3, 8), self.detect("sum(start=None)"))

  def test_inheritable_of_dup2_from_os(self):
    self.assertOnlyIn((3, 4), self.detect("import os\nv = os.dup2(inheritable=True)"))
    self.assertOnlyIn((3, 4), self.detect("from os import dup2\nv = dup2(inheritable=True)"))

  def test_dir_fd_of_open_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.open(dir_fd=None)"))

  def test_dir_fd_of_access_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.access(dir_fd=None)"))

  def test_effective_ids_of_access_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.access(effective_ids=None)"))

  def test_follow_symlinks_of_access_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.access(follow_symlinks=None)"))

  def test_follow_symlinks_of_chflags_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.chflags(follow_symlinks=None)"))

  def test_dir_fd_of_chmod_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.chmod(dir_fd=None)"))

  def test_follow_symlinks_of_chmod_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.chmod(follow_symlinks=None)"))

  def test_dir_fd_of_chown_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.chown(dir_fd=None)"))

  def test_follow_symlinks_of_chown_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.chown(follow_symlinks=None)"))

  def test_src_dir_fd_of_link_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.link(src_dir_fd=None)"))

  def test_dst_dir_fd_of_link_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.link(dst_dir_fd=None)"))

  def test_follow_symlinks_of_link_from_os(self):
    self.assertOnlyIn((3, 3), self.detect("import os\nv = os.link(follow_symlinks=None)"))

  def test_maxtasksperchild_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
      "import multiprocessing\nmultiprocessing.Pool(maxtasksperchild=3)"))

  def test_daemon_of_Process_from_multiprocessing(self):
    self.assertOnlyIn((3, 3),
                      self.detect("import multiprocessing\nmultiprocessing.Process(daemon=None)"))

  def test_compact_of_PrettyPrinter_from_pprint(self):
    self.assertOnlyIn((3, 4), self.detect("import pprint\npprint.PrettyPrinter(compact=True)"))

  def test_compact_of_pformat_from_pprint(self):
    self.assertOnlyIn((3, 4), self.detect("import pprint\npprint.pformat(compact=True)"))

  def test_compact_of_pprint_from_pprint(self):
    self.assertOnlyIn((3, 4), self.detect("import pprint\npprint.pprint(compact=True)"))

  def test_delta_of_assertAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
      "from unittest import TestCase\nTestCase.assertAlmostEqual(delta=1)"))

  def test_delta_of_assertNotAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase.assertNotAlmostEqual(delta=1)"))

  def test_fold_of_datetime_from_datetime(self):
    self.assertOnlyIn((3, 6), self.detect("from datetime import datetime\ndatetime(fold=1)"))

  def test_tzinfo_of_combine_from_datetime(self):
    self.assertOnlyIn((3, 6), self.detect(
      "from datetime import datetime\ndatetime.combine(tzinfo=1)"))

  def test_fold_of_replace_from_datetime(self):
    self.assertOnlyIn((3, 6), self.detect(
      "from datetime import datetime\ndatetime.replace(fold=1)"))

  def test_timespec_of_isoformat_from_datetime(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from datetime import datetime\ndatetime.isoformat(timespec=1)"))

  def test_fold_of_replace_from_datetime_time(self):
    self.assertOnlyIn((3, 6), self.detect("from datetime import time\ntime.replace(fold=1)"))

  def test_timespec_of_isoformat_from_datetime_time(self):
    self.assertOnlyIn((3, 6), self.detect("from datetime import time\ntime.isoformat(timespec=1)"))

  def test_domain_of_Filter_from_tracemalloc(self):
    self.assertOnlyIn((3, 6), self.detect("import tracemalloc\ntracemalloc.Filter(domain=1)"))

  def test_compact_of_TracebackException_from_traceback(self):
    self.assertOnlyIn((3, 10), self.detect("""
from traceback import TracebackException
TracebackException(compact=1)
"""))

  def test_max_length_of_decompress_from_bz2_BZ2Decompressor(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from bz2 import BZ2Decompressor\n"
                                  "d = BZ2Decompressor()\n"
                                  "d.decompress(max_length=1)"))

  def test_maxlen_of_deque_from_collections(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import collections\ncollections.deque(maxlen=1)"))

  def test_rename_of_namedtuple_from_collections(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("import collections\ncollections.namedtuple(rename=True)"))

  def test_module_of_namedtuple_from_collections(self):
    self.assertOnlyIn((3, 6), self.detect(
      "import collections\ncollections.namedtuple(module=None)"))

  def test_defaults_of_namedtuple_from_collections(self):
    self.assertOnlyIn((3, 7), self.detect(
      "import collections\ncollections.namedtuple(defaults=None)"))

  def test_m_of_ChainMap_new_child_from_collections(self):
    self.assertOnlyIn((3, 4), self.detect(
      "import collections\ncollections.ChainMap.new_child(m=None)"))

  def test_stop_of_index_from_collections_abc_ByteString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections.abc import ByteString\n"
                                  "x = ByteString()\n"
                                  "x.index(stop=None)"))

  def test_start_of_index_from_collections_abc_ByteString(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections.abc import ByteString\n"
                                  "x = ByteString()\n"
                                  "x.index(start=None)"))

  def test_stop_of_index_from_collections_abc_MutableSequence(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections.abc import MutableSequence\n"
                                  "x = MutableSequence()\n"
                                  "x.index(stop=None)"))

  def test_start_of_index_from_collections_abc_MutableSequence(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections.abc import MutableSequence\n"
                                  "x = MutableSequence()\n"
                                  "x.index(start=None)"))

  def test_stop_of_index_from_collections_abc_Sequence(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections.abc import Sequence\n"
                                  "x = Sequence()\n"
                                  "x.index(stop=None)"))

  def test_start_of_index_from_collections_abc_Sequence(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from collections.abc import Sequence\n"
                                  "x = Sequence()\n"
                                  "x.index(start=None)"))

  def test_use_last_error_of_CDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import ctypes\nctypes.CDLL(use_last_error=True)"))

  def test_use_errno_of_CDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.CDLL(use_errno=True)"))

  def test_use_last_error_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import ctypes\nctypes.OleDLL(use_last_error=True)"))

  def test_use_errno_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.OleDLL(use_errno=True)"))

  def test_use_last_error_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import ctypes\nctypes.WinDLL(use_last_error=True)"))

  def test_use_errno_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.WinDLL(use_errno=True)"))

  def test_use_last_error_of_CFUNCTYPE_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("import ctypes\nctypes.CFUNCTYPE(use_last_error=True)"))

  def test_use_errno_of_CFUNCTYPE_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "import ctypes\nctypes.CFUNCTYPE(use_errno=True)"))

  def test_offset_of_byref_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import ctypes\nctypes.byref(offset=3)"))

  def test_autojunk_of_SequenceMatcher_from_difflib(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("import difflib\ndifflib.SequenceMatcher(autojunk=True)"))

  def test_charset_of_make_file_from_difflib(self):
    self.assertOnlyIn((3, 5), self.detect("from difflib import HtmlDiff\n"
                                          "HtmlDiff.make_file(charset=True)"))

  def test_use_builtin_types_of_SimpleXMLRPCServer_from_xmlrpc_server(self):
    self.assertOnlyIn((3, 3), self.detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                                          "SimpleXMLRPCServer(use_builtin_types=True)"))

  def test_use_builtin_types_of_CGIXMLRPCRequestHandler_from_xmlrpc_server(self):
    self.assertOnlyIn((3, 3), self.detect("from xmlrpc.server import CGIXMLRPCRequestHandler\n"
                                          "CGIXMLRPCRequestHandler(use_builtin_types=True)"))

  def test_use_builtin_types_of_DocXMLRPCServer_from_xmlrpc_server(self):
    self.assertOnlyIn((3, 3), self.detect("from xmlrpc.server import DocXMLRPCServer\n"
                                          "DocXMLRPCServer(use_builtin_types=True)"))

  def test_typed_of_lru_cache_from_functools(self):
    self.assertOnlyIn((3, 3), self.detect("import functools\nfunctools.lru_cache(typed=3)"))

  def test_key_of_nlargest_from_heapq(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import heapq\nheapq.nlargest(key=3)"))

  def test_key_of_nsmallest_from_heapq(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import heapq\nheapq.nsmallest(key=3)"))

  def test_key_of_merge_from_heapq(self):
    self.assertOnlyIn((3, 5), self.detect("import heapq\nheapq.merge(key=3)"))

  def test_reverse_of_merge_from_heapq(self):
    self.assertOnlyIn((3, 5), self.detect("import heapq\nheapq.merge(reverse=True)"))

  def test_follow_wrapped_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.signature(follow_wrapped=True)"))

  def test_eval_str_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 10), self.detect("import inspect\ninspect.signature(eval_str=True)"))

  def test_globals_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 10), self.detect("import inspect\ninspect.signature(globals=True)"))

  def test_locals_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 10), self.detect("import inspect\ninspect.signature(locals=True)"))

  def test_globalns_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 10), self.detect("""
from inspect import Signature
Signature.from_callable(globalns=True)
"""))

  def test_localns_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 10), self.detect("""
from inspect import Signature
Signature.from_callable(localns=True)
"""))

  def test_write_through_of_TextIOWrapper_from_io(self):
    self.assertOnlyIn((3, 3), self.detect("import io\nio.TextIOWrapper(write_through=True)"))

  def test_func_of_accumulate_from_itertools(self):
    self.assertOnlyIn((3, 3), self.detect("import itertools\nitertools.accumulate(func=None)"))

  def test_step_of_count_from_itertools(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("import itertools\nitertools.count(step=None)"))

  def test_object_pairs_hook_of_load_from_json(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect(
      "import json\njson.load(object_pairs_hook=None)"))

  def test_object_pairs_hook_of_JSONDecoder_from_json(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("import json\njson.JSONDecoder(object_pairs_hook=None)"))

  def test_func_of_makeRecord_from_logging_Logger(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import Logger\nLogger.makeRecord(func=None)"))

  def test_extra_of_makeRecord_from_logging_Logger(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import Logger\nLogger.makeRecord(extra=None)"))

  def test_func_of_LogRecord_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import LogRecord\nLogRecord(func=None)"))

  def test_extra_of_debug_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("import logging\nlogging.debug(extra=None)"))

  def test_stack_info_of_debug_from_logging(self):
    self.assertOnlyIn((3, 2), self.detect("import logging\nlogging.debug(stack_info=None)"))

  def test_style_of_Formatter_from_logging(self):
    self.assertOnlyIn((3, 2), self.detect("import logging\nlogging.Formatter(style=None)"))

  def test_annotate_of_dis_from_pickletools(self):
    self.assertOnlyIn((3, 2), self.detect("import pickletools\npickletools.dis(annotate=None)"))

  def test_posix_of_split_from_shlex(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import shlex\nshlex.split(posix=None)"))

  def test_punctuation_chars_of_shlex_from_shlex(self):
    self.assertOnlyIn((3, 6), self.detect("import shlex\nshlex.shlex(punctuation_chars=None)"))

  def test_allow_none_of_SimpleXMLRPCServer_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                                  "SimpleXMLRPCServer(allow_none=True)"))

  def test_encoding_of_SimpleXMLRPCServer_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                                  "SimpleXMLRPCServer(encoding=True)"))

  def test_bind_and_active_of_SimpleXMLRPCServer_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                                  "SimpleXMLRPCServer(bind_and_active=True)"))

  def test_allow_none_of_CGIXMLRPCRequestHandler_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from SimpleXMLRPCServer import CGIXMLRPCRequestHandler\n"
                                  "CGIXMLRPCRequestHandler(allow_none=True)"))

  def test_encoding_of_CGIXMLRPCRequestHandler_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from SimpleXMLRPCServer import CGIXMLRPCRequestHandler\n"
                                  "CGIXMLRPCRequestHandler(encoding=True)"))

  def test_allow_dotted_names_of_register_instance_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                                  "srv = SimpleXMLRPCServer()\n"
                                  "srv.register_instance(allow_dotted_names=True)"))
    self.assertOnlyIn((3, 0),
                      self.detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                                  "srv = SimpleXMLRPCServer()\n"
                                  "srv.register_instance(allow_dotted_names=True)"))

  def test_ciphers_of_wrap_socket_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("import ssl\nssl.wrap_socket(ciphers=None)"))

  def test_password_of_load_cert_chain_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.load_cert_chain(password=None)"))

  def test_cadata_of_load_verify_locations_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from ssl import SSLContext\n"
                                  "ctx = SSLContext()\n"
                                  "ctx.load_verify_locations(cadata=None)"))

  def test_encoding_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 6), self.detect("import subprocess\nsubprocess.run(encoding=None)"))

  def test_errors_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 6), self.detect("import subprocess\nsubprocess.run(errors=None)"))

  def test_encoding_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 6), self.detect(
      "import subprocess\nsubprocess.check_output(encoding=None)"))

  def test_errors_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 6), self.detect(
      "import subprocess\nsubprocess.check_output(errors=None)"))

  def test_text_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("import subprocess\nsubprocess.check_output(text=None)"))

  def test_pass_fds_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(pass_fds=True)"))

  def test_restore_signals_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(restore_signals=True)"))

  def test_start_new_session_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(start_new_session=True)"))

  def test_encoding_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 6), self.detect("import subprocess\nsubprocess.Popen(encoding=None)"))

  def test_errors_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 6), self.detect("import subprocess\nsubprocess.Popen(errors=None)"))

  def test_text_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("import subprocess\nsubprocess.Popen(text=None)"))

  def test_timeout_of_wait_from_subprocess_Popen(self):
    self.assertOnlyIn((3, 3), self.detect("from subprocess import Popen\nPopen.wait(timeout=None)"))

  def test_timeout_of_communicate_from_subprocess_Popen(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from subprocess import Popen\nPopen.communicate(timeout=None)"))

  def test_timeout_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 3), self.detect("import subprocess\nsubprocess.call(timeout=None)"))

  def test_timeout_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 3), self.detect("import subprocess\nsubprocess.check_call(timeout=None)"))

  def test_timeout_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 3), self.detect(
      "import subprocess\nsubprocess.check_output(timeout=None)"))

  def test_input_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 4), self.detect("import subprocess\nsubprocess.check_output(input=None)"))

  def test_exclude_of_add_from_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from tarfile import TarFile\ntf = TarFile()\ntf.add(exclude=None)"))

  def test_filter_of_add_from_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect(
      "from tarfile import TarFile\ntf = TarFile()\ntf.add(filter=None)"))

  def test_format_of_tobuf_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from tarfile import TarInfo\ntf = TarInfo()\ntf.tobuf(format=None)"))

  def test_encoding_of_tobuf_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarInfo\n"
                                  "tf = TarInfo()\n"
                                  "tf.tobuf(encoding=None)"))

  def test_errors_of_tobuf_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
      "from tarfile import TarInfo\ntf = TarInfo()\ntf.tobuf(errors=None)"))

  def test_members_of_list_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 5), self.detect(
      "from tarfile import TarFile\ntf = TarFile()\ntf.list(members=None)"))

  def test_numeric_owner_of_extractall_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from tarfile import TarFile\n"
                                  "tf = TarFile()\n"
                                  "tf.extractall(numeric_owner=None)"))

  def test_set_attrs_of_extract_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from tarfile import TarFile\n"
                                  "tf = TarFile()\n"
                                  "tf.extract(set_attrs=None)"))

  def test_numeric_owner_of_extract_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from tarfile import TarFile\n"
                                  "tf = TarFile()\n"
                                  "tf.extract(numeric_owner=None)"))

  def test_module_globals_of_warn_explicit_from_warnings(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("import warnings\nwarnings.warn_explicit(module_globals=None)"))

  def test_line_of_formatwarning_from_warnings(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("import warnings\nwarnings.formatwarning(line=None)"))

  def test_source_of_warn_explicit_from_warnings(self):
    self.assertOnlyIn((3, 6),
                      self.detect("import warnings\nwarnings.warn_explicit(source=None)"))

  def test_source_of_warn_from_warnings(self):
    self.assertOnlyIn((3, 6),
                      self.detect("import warnings\nwarnings.warn(source=None)"))

  def test_short_empty_elements_of_tostring_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.tostring(short_empty_elements=None)"))

  def test_xml_declaration_of_tostring_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.tostring(xml_declaration=None)"))

  def test_default_namespace_of_tostring_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.tostring(default_namespace=None)"))

  def test_short_empty_elements_of_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.tostringlist(short_empty_elements=None)"))

  def test_xml_declaration_of_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.tostringlist(xml_declaration=None)"))

  def test_default_namespace_of_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.tostringlist(default_namespace=None)"))

  def test_short_empty_elements_of_write_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from xml.etree import ElementTree\n"
                                  "ElementTree.write(short_empty_elements=None)"))

  def test_use_datetime_of_ServerProxy_from_xmlrpclib_ServerProxy(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from xmlrpclib import ServerProxy\n"
                                  "ServerProxy(use_datetime=None)"))

  def test_context_of_ServerProxy_from_xmlrpclib_ServerProxy(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from xmlrpclib import ServerProxy\n"
                                  "ServerProxy(context=None)"))

  def test_use_datetime_of_loads_from_xmlrpclib(self):
    self.assertOnlyIn((2, 5),
                      self.detect("import xmlrpclib\n"
                                  "xmlrpclib.loads(use_datetime=None)"))

  def test_pwd_of_read_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.read(pwd=None)"))

  def test_compress_type_of_writestr_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from zipfile import ZipFile\n"
                                  "zf = ZipFile()\n"
                                  "zf.writestr(compress_type=None)"))
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from zipfile import ZipFile\n"
                                  "ZipFile().writestr(compress_type=None)"))

  def test_filterfunc_of_writepy_from_zipfile_PyZipFile(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from zipfile import PyZipFile\n"
                                  "zf = PyZipFile()\n"
                                  "zf.writepy(filterfunc=None)"))

  def test_optimize_of_PyZipFile_from_zipfile(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from zipfile import PyZipFile\n"
                                  "PyZipFile(optimize=None)"))

  def test_unsafe_of_Mock_from_unittest_mock(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from unittest.mock import Mock\n"
                                  "Mock(unsafe=False)"))

  def test_with_pip_of_EnvBuilder_from_venv(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from venv import EnvBuilder\n"
                                  "EnvBuilder(with_pip=False)"))

  def test_upgrade_deps_of_EnvBuilder_from_venv(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from venv import EnvBuilder\n"
                                  "EnvBuilder(upgrade_deps=False)"))

  def test_with_pip_of_create_from_venv(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from venv import create\n"
                                  "create(with_pip=False)"))

  def test_prompt_of_EnvBuilder_from_venv(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from venv import EnvBuilder\n"
                                  "EnvBuilder(prompt=False)"))

  def test_flags_of_compile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("compile(flags=None)"))

  def test_dont_inherit_of_compile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("compile(dont_inherit=None)"))

  def test_optimize_of_compile(self):
    self.assertOnlyIn((3, 2), self.detect("compile(optimize=None)"))

  def test_start_of_enumerate(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("enumerate(start=None)"))

  def test_key_of_max(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("max(key=None)"))

  def test_default_of_max(self):
    self.assertOnlyIn((3, 4), self.detect("max(default=None)"))

  def test_key_of_min(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("min(key=None)"))

  def test_default_of_min(self):
    self.assertOnlyIn((3, 4), self.detect("min(default=None)"))

  def test_level_of___import__(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("__import__(level=None)"))

  def test_opener_of_open(self):
    self.assertOnlyIn((3, 3), self.detect("open(opener=None)"))

  @VerminTest.skipUnlessVersion(3)
  def test_flush_of_print(self):
    # `print()` is not a function in v2.
    self.assertOnlyIn((3, 3), self.detect("print(flush=None)"))

  def test_policy_of_email_mime_base_MIMEBase(self):
    self.assertOnlyIn((3, 6), self.detect(
      "from email.mime.base import MIMEBase\nMIMEBase(policy=None)"))

  def test_policy_of_email_mime_multipart_MIMEMultipart(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from email.mime.multipart import MIMEMultipart\n"
                                  "MIMEMultipart(policy=None)"))

  def test_policy_of_email_mime_application_MIMEApplication(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from email.mime.application import MIMEApplication\n"
                                  "MIMEApplication(policy=None)"))

  def test_policy_of_email_mime_audio_MIMEAudio(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from email.mime.audio import MIMEAudio\nMIMEAudio(policy=None)"))

  def test_policy_of_email_mime_image_MIMEImage(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from email.mime.image import MIMEImage\nMIMEImage(policy=None)"))

  def test_policy_of_email_mime_message_MIMEMessage(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from email.mime.message import MIMEMessage\n"
                                  "MIMEMessage(policy=None)"))

  def test_policy_of_email_mime_text_MIMEText(self):
    self.assertOnlyIn((3, 6), self.detect(
      "from email.mime.text import MIMEText\nMIMEText(policy=None)"))

  def test_domain_of_email_utils_make_msgid(self):
    self.assertOnlyIn((3, 2), self.detect(
      "import email.utils\nemail.utils.make_msgid(domain=None)"))

  def test_charset_of_email_utils_formatdate(self):
    self.assertOnlyIn((3, 3), self.detect(
      "import email.utils\nemail.utils.formatdate(charset=None)"))

  def test_strict_of_email_message_from_string(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("import email\nemail.message_from_string(strict=None)"))

  def test_strict_of_email_message_from_file(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("import email\nemail.message_from_file(strict=None)"))

  def test_policy_of_email_parser_BytesFeedParser(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.parser import BytesFeedParser\n"
                                  "BytesFeedParser(policy=None)"))

  def test_policy_of_email_parser_FeedParser(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.parser import FeedParser\n"
                                  "FeedParser(policy=None)"))

  def test_policy_of_email_generator_BytesGenerator(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.generator import BytesGenerator\n"
                                  "BytesGenerator(policy=None)"))

  def test_policy_of_email_generator_Generator(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.generator import Generator\n"
                                  "Generator(policy=None)"))

  def test_linesep_of_email_generator_Generator_flatten(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from email.generator import Generator\n"
                                  "g=Generator()\ng.flatten(linesep=None)"))

  def test_linesep_of_email_header_Header_encode(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from email.header import Header\n"
                                  "g=Header()\ng.encode(linesep=None)"))

  def test_base_of_math_log(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("import math\nmath.log(base=None)"))

  def test_exit_ok_of_path_mkdir(self):
    self.assertOnlyIn(
        (3, 5), self.detect("from pathlib import Path\np=Path('foo')\np.mkdir(exist_ok=True)"))

  def test_strict_of_path_resolve(self):
    self.assertOnlyIn(
        (3, 6), self.detect("from pathlib import Path\np=Path('foo')\np.resolve(strict=True)"))

  def test_follow_symlinks_of_path_chmod(self):
    self.assertOnlyIn((3, 10), self.detect("""
from pathlib import Path
p=Path('foo')
p.chmod(follow_symlinks=True)
"""))

  def test_follow_symlinks_of_path_stat(self):
    self.assertOnlyIn((3, 10), self.detect("""
from pathlib import Path
p=Path('foo')
p.stat(follow_symlinks=True)
"""))

  def test_newline_of_path_write_text(self):
    self.assertOnlyIn((3, 10), self.detect("""
from pathlib import Path
p=Path('foo')
p.write_text(newline=True)
"""))

  def test_optimization_of_importlib_util_cache_from_source(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from importlib.util import cache_from_source\n"
                                  "cache_from_source(optimization=None)"))

  def test_allow_abbrev_of_argparse_ArgumentParser(self):
    self.assertOnlyIn((3, 5), self.detect(
      "import argparse\nargparse.ArgumentParser(allow_abbrev=True)"))

  def test_exit_on_error_of_argparse_ArgumentParser(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import argparse\nargparse.ArgumentParser(exit_on_error=True)"))

  def test_skip_of_bdb_Bdb(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("import bdb\nbdb.Bdb(skip=True)"))

  def test_backtick_of_binascii_b2a_uu(self):
    self.assertOnlyIn((3, 7), self.detect("import binascii\nbinascii.b2a_uu(backtick=True)"))

  def test_newline_of_binascii_b2a_base64(self):
    self.assertOnlyIn((3, 6), self.detect("import binascii\nbinascii.b2a_base64(newline=True)"))

  def test_encoding_of_cgi_parse_multipart(self):
    self.assertOnlyIn((3, 7), self.detect("import cgi\ncgi.parse_multipart(encoding='utf-8')"))

  def test_errors_of_cgi_parse_multipart(self):
    self.assertOnlyIn((3, 7), self.detect("import cgi\ncgi.parse_multipart(errors='utf-8')"))

  def test_separator_of_cgi_parse_multipart(self):
    self.assertOnlyIn((3, 10), self.detect("import cgi\ncgi.parse_multipart(separator='-')"))

  def test_exitmsg_of_code_interact(self):
    self.assertOnlyIn((3, 6), self.detect("import code\ncode.interact(exitmsg='hello')"))

  def test_legacy_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 2), self.detect(
      "import compileall\ncompileall.compile_dir(legacy='hello')"))

  def test_optimize_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 2), self.detect(
      "import compileall\ncompileall.compile_dir(optimize='hello')"))

  def test_invalidation_mode_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 7),
                      self.detect("import compileall\n"
                                  "compileall.compile_dir(invalidation_mode='hello')"))

  def test_stripdir_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_dir(stripdir=None)"))

  def test_prependdir_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_dir(prependdir=None)"))

  def test_limit_sl_dest_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_dir(limit_sl_dest=None)"))

  def test_hardlink_dupes_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_dir(hardlink_dupes=None)"))

  def test_legacy_of_compileall_compile_path(self):
    self.assertOnlyIn((3, 2), self.detect(
      "import compileall\ncompileall.compile_path(legacy='hello')"))

  def test_optimize_of_compileall_compile_path(self):
    self.assertOnlyIn((3, 2),
                      self.detect("import compileall\ncompileall.compile_path(optimize='hello')"))

  def test_invalidation_mode_of_compileall_compile_path(self):
    self.assertOnlyIn((3, 7),
                      self.detect("import compileall\n"
                                  "compileall.compile_path(invalidation_mode='hello')"))

  def test_invalidation_mode_of_compileall_compile_file(self):
    self.assertOnlyIn((3, 7),
                      self.detect("import compileall\n"
                                  "compileall.compile_file(invalidation_mode='hello')"))

  def test_stripdir_of_compileall_compile_file(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_file(stripdir=None)"))

  def test_prependdir_of_compileall_compile_file(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_file(prependdir=None)"))

  def test_limit_sl_dest_of_compileall_compile_file(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_file(limit_sl_dest=None)"))

  def test_hardlink_dupes_of_compileall_compile_file(self):
    self.assertOnlyIn((3, 9),
                      self.detect("import compileall\n"
                                  "compileall.compile_file(hardlink_dupes=None)"))

  def test_chunksize_of_concurrent_futures_Executor_map(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from concurrent.futures import Executor\n"
                                  "Executor().map(chunksize=123)"))

  def test_cancel_futures_of_concurrent_futures_Executor_shutdown(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from concurrent.futures import Executor\n"
                                  "Executor().shutdown(cancel_futures=True)"))

  def test_thread_name_prefix_of_concurrent_futures_ThreadPoolExecutor(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from concurrent.futures import ThreadPoolExecutor\n"
                                  "ThreadPoolExecutor(thread_name_prefix='123')"))

  def test_initializer_of_concurrent_futures_ThreadPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from concurrent.futures import ThreadPoolExecutor\n"
                                  "ThreadPoolExecutor(initializer='123')"))

  def test_initargs_of_concurrent_futures_ThreadPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from concurrent.futures import ThreadPoolExecutor\n"
                                  "ThreadPoolExecutor(initargs=0)"))

  def test_mp_context_of_concurrent_futures_ProcessPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from concurrent.futures import ProcessPoolExecutor\n"
                                  "ProcessPoolExecutor(mp_context='123')"))

  def test_initializer_of_concurrent_futures_ProcessPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from concurrent.futures import ProcessPoolExecutor\n"
                                  "ProcessPoolExecutor(initializer='123')"))

  def test_initargs_of_concurrent_futures_ProcessPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from concurrent.futures import ProcessPoolExecutor\n"
                                  "ProcessPoolExecutor(initargs=0)"))

  def test_rounds_of_crypt_mksalt(self):
    self.assertOnlyIn((3, 7), self.detect("import crypt\ncrypt.mksalt(rounds=8)"))

  def test_file_of_dis_show_code(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.show_code(file=8)"))

  def test_file_of_dis_dis(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.dis(file=8)"))

  def test_depth_of_dis_dis(self):
    self.assertOnlyIn((3, 7), self.detect("import dis\ndis.dis(depth=8)"))

  def test_file_of_dis_distb(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.distb(file=8)"))

  def test_file_of_dis_disco(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.disco(file=8)"))

  def test_file_of_dis_disassemble(self):
    self.assertOnlyIn((3, 4), self.detect("import dis\ndis.disassemble(file=8)"))

  def test_mtime_of_gzip_compress(self):
    self.assertOnlyIn((3, 8), self.detect("import gzip\ngzip.compress(mtime=8)"))

  def test_encoding_of_gzip_open(self):
    self.assertOnlyIn((3, 3), self.detect("import gzip\ngzip.open(encoding='utf-8')"))

  def test_errors_of_gzip_open(self):
    self.assertOnlyIn((3, 3), self.detect("import gzip\ngzip.open(errors=True)"))

  def test_newline_of_gzip_open(self):
    self.assertOnlyIn((3, 3), self.detect("import gzip\ngzip.open(newline=None)"))

  def test_encoding_of_str_decode(self):
    self.assertOnlyIn((2, 7), self.detect("'test'.decode(encoding=None)"))

  def test_errors_of_str_decode(self):
    self.assertOnlyIn((2, 7), self.detect("'test'.decode(errors=None)"))

  def test_encoding_of_str_encode(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("'test'.encode(encoding=None)"))

  def test_errors_of_str_encode(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("'test'.encode(errors=None)"))

  def test_filter_of_zipapp_create_archive(self):
    self.assertOnlyIn((3, 7), self.detect("import zipapp\nzipapp.create_archive(filter=None)"))

  def test_compressed_of_zipapp_create_archive(self):
    self.assertOnlyIn((3, 7), self.detect("import zipapp\nzipapp.create_archive(compressed=True)"))

  def test_timeout_of_smtplib_SMTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("import smtplib\nsmtplib.SMTP(timeout=1)"))

  def test_timeout_of_smtplib_LMTP(self):
    self.assertOnlyIn((3, 9), self.detect("import smtplib\nsmtplib.LMTP(timeout=1)"))

  def test_source_address_of_smtplib_SMTP(self):
    self.assertOnlyIn((3, 3), self.detect("import smtplib\nsmtplib.SMTP(source_address=1)"))

  def test_source_address_of_smtplib_SMTP_SSL(self):
    self.assertOnlyIn((3, 3), self.detect("import smtplib\nsmtplib.SMTP_SSL(source_address=1)"))

  def test_context_of_smtplib_SMTP_SSL(self):
    self.assertOnlyIn((3, 3), self.detect("import smtplib\nsmtplib.SMTP_SSL(context=1)"))

  def test_context_of_smtplib_SMTP_starttls(self):
    self.assertOnlyIn((3, 3), self.detect("import smtplib\nsmtplib.SMTP.starttls(context=1)"))

  def test_text_of_subprocess_run(self):
    self.assertOnlyIn((3, 7), self.detect("import subprocess\nsubprocess.run(text=True)"))

  def test_capture_output_of_subprocess_run(self):
    self.assertOnlyIn((3, 7), self.detect("import subprocess\nsubprocess.run(capture_output=1)"))

  def test_lpAttributeList_of_subprocess_STARTUPINFO(self):
    self.assertOnlyIn((3, 7),
                      self.detect("import subprocess\nsubprocess.STARTUPINFO(lpAttributeList=1)"))

  def test_allow_no_value_of_ConfigParser_from_ConfigParser(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from ConfigParser import ConfigParser\n"
                                  "ConfigParser(allow_no_value=None)"))

  def test_dict_type_of_ConfigParser_from_ConfigParser(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from ConfigParser import ConfigParser\n"
                                  "ConfigParser(dict_type=None)"))

  def test_allow_no_value_of_RawConfigParser_from_ConfigParser(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from ConfigParser import RawConfigParser\n"
                                  "RawConfigParser(allow_no_value=None)"))

  def test_dict_type_of_RawConfigParser_from_ConfigParser(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from ConfigParser import RawConfigParser\n"
                                  "RawConfigParser(dict_type=None)"))

  def test_allow_no_value_of_SafeConfigParser_from_ConfigParser(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from ConfigParser import SafeConfigParser\n"
                                  "SafeConfigParser(allow_no_value=None)"))

  def test_dict_type_of_SafeConfigParser_from_ConfigParser(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from ConfigParser import SafeConfigParser\n"
                                  "SafeConfigParser(dict_type=None)"))

  def test_useTk_of_Tk_from_Tkinter(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from Tkinter import Tk\n"
                                  "Tk(useTk=None)"))

  def test_encodings_of_FileType_from_argparse(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from argparse import FileType\n"
                                  "FileType(encodings=None)"))

  def test_errors_of_FileType_from_argparse(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from argparse import FileType\n"
                                  "FileType(errors=None)"))

  def test_feature_version_of_parse_from_ast(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from ast import parse\n"
                                  "parse(feature_version=None)"))

  def test_type_comments_of_parse_from_ast(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from ast import parse\n"
                                  "parse(type_comments=None)"))

  def test_name_of_Task_from_asyncio(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import Task\n"
                                  "Task(name=None)"))

  def test_name_of_create_task_from_asyncio(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import create_task\n"
                                  "create_task(name=None)"))

  def test_ssl_handshake_timeout_of_open_connection_from_asyncio(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import open_connection\n"
                                  "open_connection(ssl_handshake_timeout=None)"))

  def test_ssl_handshake_timeout_of_open_unix_connection_from_asyncio(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import open_unix_connection\n"
                                  "open_unix_connection(ssl_handshake_timeout=None)"))

  def test_ssl_handshake_timeout_of_start_server_from_asyncio(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import start_server\n"
                                  "start_server(ssl_handshake_timeout=None)"))

  def test_start_serving_of_start_server_from_asyncio(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import start_server\n"
                                  "start_server(start_serving=None)"))

  def test_ssl_handshake_timeout_of_start_unix_server_from_asyncio(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import start_unix_server\n"
                                  "start_unix_server(ssl_handshake_timeout=None)"))

  def test_start_serving_of_start_unix_server_from_asyncio(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import start_unix_server\n"
                                  "start_unix_server(start_serving=None)"))

  def test_bytes_per_sep_of_b2a_hex_from_binascii(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from binascii import b2a_hex\n"
                                  "b2a_hex(bytes_per_sep=None)"))

  def test_sep_of_b2a_hex_from_binascii(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from binascii import b2a_hex\n"
                                  "b2a_hex(sep=None)"))

  def test_bytes_per_sep_of_hexlify_from_binascii(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from binascii import hexlify\n"
                                  "hexlify(bytes_per_sep=None)"))

  def test_sep_of_hexlify_from_binascii(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from binascii import hexlify\n"
                                  "hexlify(sep=None)"))

  def test_base_of_log_from_cmath(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from cmath import log\n"
                                  "log(base=None)"))

  def test_stdin_of_Cmd_from_cmd(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from cmd import Cmd\n"
                                  "Cmd(stdin=None)"))

  def test_stdout_of_Cmd_from_cmd(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from cmd import Cmd\n"
                                  "Cmd(stdout=None)"))

  def test_allow_no_value_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(allow_no_value=None)"))

  def test_comment_prefixes_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(comment_prefixes=None)"))

  def test_converters_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(converters=None)"))

  def test_default_section_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(default_section=None)"))

  def test_delimiters_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(delimiters=None)"))

  def test_empty_lines_in_values_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(empty_lines_in_values=None)"))

  def test_interpolation_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(interpolation=None)"))

  def test_strict_of_ConfigParser_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "ConfigParser(strict=None)"))

  def test_lineno_of_DuplicateSectionError_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import DuplicateSectionError\n"
                                  "DuplicateSectionError(lineno=None)"))

  def test_source_of_DuplicateSectionError_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import DuplicateSectionError\n"
                                  "DuplicateSectionError(source=None)"))

  def test_source_of_ParsingError_from_configparser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ParsingError\n"
                                  "ParsingError(source=None)"))

  def test_winmode_of_CDLL_from_ctypes(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from ctypes import CDLL\n"
                                  "CDLL(winmode=None)"))

  def test_winmode_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from ctypes import OleDLL\n"
                                  "OleDLL(winmode=None)"))

  def test_winmode_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from ctypes import WinDLL\n"
                                  "WinDLL(winmode=None)"))

  def test_jump_of_stack_effect_from_dis(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from dis import stack_effect\n"
                                  "stack_effect(jump=None)"))

  def test_encoding_of_DocFileSuite_from_doctest(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from doctest import DocFileSuite\n"
                                  "DocFileSuite(encoding=None)"))

  def test_extraglobs_of_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import DocTestSuite\n"
                                  "DocTestSuite(extraglobs=None)"))

  def test_globs_of_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import DocTestSuite\n"
                                  "DocTestSuite(globs=None)"))

  def test_optionflags_of_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import DocTestSuite\n"
                                  "DocTestSuite(optionflags=None)"))

  def test_setUp_of_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import DocTestSuite\n"
                                  "DocTestSuite(setUp=None)"))

  def test_tearDown_of_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import DocTestSuite\n"
                                  "DocTestSuite(tearDown=None)"))

  def test_test_finder_of_DocTestSuite_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import DocTestSuite\n"
                                  "DocTestSuite(test_finder=None)"))

  def test_pm_of_debug_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import debug\n"
                                  "debug(pm=None)"))

  def test_encoding_of_testfile_from_doctest(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from doctest import testfile\n"
                                  "testfile(encoding=None)"))

  def test_exclude_empty_of_testmod_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import testmod\n"
                                  "testmod(exclude_empty=None)"))

  def test_extraglobs_of_testmod_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import testmod\n"
                                  "testmod(extraglobs=None)"))

  def test_optionflags_of_testmod_from_doctest(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from doctest import testmod\n"
                                  "testmod(optionflags=None)"))

  def test_raise_on_error_of_testmod_from_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from doctest import testmod\n"
                                  "testmod(raise_on_error=None)"))

  def test_policy_of_message_from_binary_file_from_email(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email import message_from_binary_file\n"
                                  "message_from_binary_file(policy=None)"))

  def test_policy_of_message_from_bytes_from_email(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email import message_from_bytes\n"
                                  "message_from_bytes(policy=None)"))

  def test_policy_of_message_from_file_from_email(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email import message_from_file\n"
                                  "message_from_file(policy=None)"))

  def test_policy_of_message_from_string_from_email(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email import message_from_string\n"
                                  "message_from_string(policy=None)"))

  def test_start_of_Enum_from_enum(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from enum import Enum\n"
                                  "Enum(start=None)"))

  def test_mode_of_FileInput_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from fileinput import FileInput\n"
                                  "FileInput(mode=None)"))

  def test_openhook_of_FileInput_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from fileinput import FileInput\n"
                                  "FileInput(openhook=None)"))

  def test_encoding_of_FileInput_from_fileinput(self):
    self.assertOnlyIn((3, 10), self.detect("""
from fileinput import FileInput
FileInput(encoding=None)
"""))

  def test_errors_of_FileInput_from_fileinput(self):
    self.assertOnlyIn((3, 10), self.detect("""
from fileinput import FileInput
FileInput(errors=None)
"""))

  def test_errors_of_hook_encoded_from_fileinput(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from fileinput import hook_encoded\n"
                                  "hook_encoded(errors=None)"))

  def test_encoding_of_hook_compressed_from_fileinput(self):
    self.assertOnlyIn((3, 10), self.detect("""
from fileinput import hook_compressed
hook_compressed(encoding=None)
"""))

  def test_errors_of_hook_compressed_from_fileinput(self):
    self.assertOnlyIn((3, 10), self.detect("""
from fileinput import hook_compressed
hook_compressed(errors=None)
"""))

  def test_mode_of_input_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from fileinput import input\n"
                                  "input(mode=None)"))

  def test_openhook_of_input_from_fileinput(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from fileinput import input\n"
                                  "input(openhook=None)"))

  def test_encoding_of_input_from_fileinput(self):
    self.assertOnlyIn((3, 10), self.detect("""
from fileinput import input
input(encoding=None)
"""))

  def test_errors_of_input_from_fileinput(self):
    self.assertOnlyIn((3, 10), self.detect("""
from fileinput import input
input(errors=None)
"""))

  def test_source_address_of_FTP_from_ftplib(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from ftplib import FTP\n"
                                  "FTP(source_address=None)"))

  def test_timeout_of_FTP_from_ftplib(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from ftplib import FTP\n"
                                  "FTP(timeout=None)"))

  def test_context_of_FTP_TLS_from_ftplib(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from ftplib import FTP_TLS\n"
                                  "FTP_TLS(context=None)"))

  def test_source_address_of_FTP_TLS_from_ftplib(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from ftplib import FTP_TLS\n"
                                  "FTP_TLS(source_address=None)"))

  def test_generation_of_collect_from_gc(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from gc import collect\n"
                                  "collect(generation=None)"))

  def test_generation_of_get_objects_from_gc(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from gc import get_objects\n"
                                  "get_objects(generation=None)"))

  def test_stream_of_getpass_from_getpass(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from getpass import getpass\n"
                                  "getpass(stream=None)"))

  def test_codeset_of_install_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import install\n"
                                  "install(codeset=None)"))

  def test_names_of_install_from_gettext(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from gettext import install\n"
                                  "install(names=None)"))

  def test_codeset_of_translation_from_gettext(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from gettext import translation\n"
                                  "translation(codeset=None)"))

  def test_recursive_of_glob_from_glob(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from glob import glob\n"
                                  "glob(recursive=None)"))

  def test_dir_fd_of_glob_from_glob(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from glob import glob\n"
                                  "glob(dir_fd=None)"))

  def test_root_dir_of_glob_from_glob(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from glob import glob\n"
                                  "glob(root_dir=None)"))

  def test_dir_fd_of_iglob_from_glob(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from glob import iglob\n"
                                  "iglob(dir_fd=None)"))

  def test_root_dir_of_iglob_from_glob(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from glob import iglob\n"
                                  "iglob(root_dir=None)"))

  def test_mtime_of_GzipFile_from_gzip(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from gzip import GzipFile\n"
                                  "GzipFile(mtime=None)"))

  def test_source_address_of_HTTPConnection_from_httplib(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from httplib import HTTPConnection\n"
                                  "HTTPConnection(source_address=None)"))

  def test_timeout_of_HTTPConnection_from_httplib(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from httplib import HTTPConnection\n"
                                  "HTTPConnection(timeout=None)"))

  def test_context_of_HTTPSConnection_from_httplib(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from httplib import HTTPSConnection\n"
                                  "HTTPSConnection(context=None)"))

  def test_source_address_of_HTTPSConnection_from_httplib(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from httplib import HTTPSConnection\n"
                                  "HTTPSConnection(source_address=None)"))

  def test_timeout_of_HTTPSConnection_from_httplib(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from httplib import HTTPSConnection\n"
                                  "HTTPSConnection(timeout=None)"))

  def test_ssl_context_of_IMAP4_SSL_from_imaplib(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from imaplib import IMAP4_SSL\n"
                                  "IMAP4_SSL(ssl_context=None)"))

  def test_timeout_of_IMAP4_SSL_from_imaplib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from imaplib import IMAP4_SSL\n"
                                  "IMAP4_SSL(timeout=None)"))

  def test_timeout_of_IMAP4_from_imaplib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4(timeout=None)"))

  def test_timeout_of_IMAP4_open_from_imaplib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().open(timeout=None)"))

  def test_opener_of_FileIO_from_io(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from io import FileIO\n"
                                  "FileIO(opener=None)"))

  def test_initial_of_accumulate_from_itertools(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from itertools import accumulate\n"
                                  "accumulate(initial=None)"))

  def test_module_globals_of_getline_from_linecache(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from linecache import getline\n"
                                  "getline(module_globals=None)"))

  def test_monetary_of_format_from_locale(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("import locale\n"
                                  "locale.format(monetary=None)"))

  def test_monetary_of_format_string_from_locale(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from locale import format_string\n"
                                  "format_string(monetary=None)"))

  def test_delay_of_FileHandler_from_logging(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging import FileHandler\n"
                                  "FileHandler(delay=None)"))

  def test_validate_of_Formatter_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Formatter\n"
                                  "Formatter(validate=None)"))

  def test_defaults_of_Formatter_from_logging(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from logging import Formatter\n"
                                  "Formatter(defaults=None)"))

  def test_datefmt_of_basicConfig_from_logging(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(datefmt=None)"))

  def test_filemode_of_basicConfig_from_logging(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(filemode=None)"))

  def test_filename_of_basicConfig_from_logging(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(filename=None)"))

  def test_force_of_basicConfig_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(force=None)"))

  def test_format_of_basicConfig_from_logging(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(format=None)"))

  def test_handlers_of_basicConfig_from_logging(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(handlers=None)"))

  def test_level_of_basicConfig_from_logging(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(level=None)"))

  def test_stream_of_basicConfig_from_logging(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(stream=None)"))

  def test_style_of_basicConfig_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(style=None)"))

  def test_extra_of_critical_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import critical\n"
                                  "critical(extra=None)"))

  def test_stack_info_of_critical_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import critical\n"
                                  "critical(stack_info=None)"))

  def test_stacklevel_of_critical_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import critical\n"
                                  "critical(stacklevel=None)"))

  def test_stacklevel_of_debug_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import debug\n"
                                  "debug(stacklevel=None)"))

  def test_extra_of_error_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import error\n"
                                  "error(extra=None)"))

  def test_stack_info_of_error_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import error\n"
                                  "error(stack_info=None)"))

  def test_stacklevel_of_error_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import error\n"
                                  "error(stacklevel=None)"))

  def test_extra_of_exception_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import exception\n"
                                  "exception(extra=None)"))

  def test_stack_info_of_exception_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import exception\n"
                                  "exception(stack_info=None)"))

  def test_stacklevel_of_exception_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import exception\n"
                                  "exception(stacklevel=None)"))

  def test_extra_of_info_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import info\n"
                                  "info(extra=None)"))

  def test_stack_info_of_info_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import info\n"
                                  "info(stack_info=None)"))

  def test_stacklevel_of_info_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import info\n"
                                  "info(stacklevel=None)"))

  def test_extra_of_log_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import log\n"
                                  "log(extra=None)"))

  def test_stack_info_of_log_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import log\n"
                                  "log(stack_info=None)"))

  def test_stacklevel_of_log_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import log\n"
                                  "log(stacklevel=None)"))

  def test_stack_info_of_warn_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import warn\n"
                                  "warn(stack_info=None)"))

  def test_stacklevel_of_warn_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import warn\n"
                                  "warn(stacklevel=None)"))

  def test_extra_of_warning_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import warning\n"
                                  "warning(extra=None)"))

  def test_stack_info_of_warning_from_logging(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import warning\n"
                                  "warning(stack_info=None)"))

  def test_stacklevel_of_warning_from_logging(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import warning\n"
                                  "warning(stacklevel=None)"))

  def test_version_of_dump_from_marshal(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from marshal import dump\n"
                                  "dump(version=None)"))

  def test_version_of_dumps_from_marshal(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from marshal import dumps\n"
                                  "dumps(version=None)"))

  def test_domain_of_cat_from_nis(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from nis import cat\n"
                                  "cat(domain=None)"))

  def test_domain_of_maps_from_nis(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from nis import maps\n"
                                  "maps(domain=None)"))

  def test_domain_of_match_from_nis(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from nis import match\n"
                                  "match(domain=None)"))

  def test_usenetrc_of_NNTP_from_nntplib(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP(usenetrc=None)"))

  def test_dir_fd_of_lstat_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import lstat\n"
                                  "lstat(dir_fd=None)"))

  def test_exist_ok_of_makedirs_from_os(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from os import makedirs\n"
                                  "makedirs(exist_ok=None)"))

  def test_dir_fd_of_mkdir_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import mkdir\n"
                                  "mkdir(dir_fd=None)"))

  def test_dir_fd_of_mkfifo_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import mkfifo\n"
                                  "mkfifo(dir_fd=None)"))

  def test_dir_fd_of_mknod_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import mknod\n"
                                  "mknod(dir_fd=None)"))

  def test_dir_fd_of_readlink_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import readlink\n"
                                  "readlink(dir_fd=None)"))

  def test_dir_fd_of_remove_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import remove\n"
                                  "remove(dir_fd=None)"))

  def test_dst_dir_fd_of_rename_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import rename\n"
                                  "rename(dst_dir_fd=None)"))

  def test_src_dir_fd_of_rename_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import rename\n"
                                  "rename(src_dir_fd=None)"))

  def test_dir_fd_of_rmdir_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import rmdir\n"
                                  "rmdir(dir_fd=None)"))

  def test_operation_of_startfile_from_os(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from os import startfile\n"
                                  "startfile(operation=None)"))

  def test_arguments_of_startfile_from_os(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from os import startfile\n"
                                  "startfile(arguments=None)"))

  def test_cwd_of_startfile_from_os(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from os import startfile\n"
                                  "startfile(cwd=None)"))

  def test_show_cmd_of_startfile_from_os(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from os import startfile\n"
                                  "startfile(show_cmd=None)"))

  def test_dir_fd_of_stat_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import stat\n"
                                  "stat(dir_fd=None)"))

  def test_follow_symlinks_of_stat_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import stat\n"
                                  "stat(follow_symlinks=None)"))

  def test_dir_fd_of_symlink_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import symlink\n"
                                  "symlink(dir_fd=None)"))

  def test_dir_fd_of_unlink_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import unlink\n"
                                  "unlink(dir_fd=None)"))

  def test_dir_fd_of_utime_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import utime\n"
                                  "utime(dir_fd=None)"))

  def test_follow_symlinks_of_utime_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import utime\n"
                                  "utime(follow_symlinks=None)"))

  def test_ns_of_utime_from_os(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import utime\n"
                                  "utime(ns=None)"))

  def test_followlinks_of_walk_from_os(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from os import walk\n"
                                  "walk(followlinks=None)"))

  def test_strict_of_realpath_from_os_path(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from os.path import realpath\n"
                                  "realpath(strict=None)"))

  def test_nosigint_of_Pdb_from_pdb(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from pdb import Pdb\n"
                                  "Pdb(nosigint=None)"))

  def test_readrc_of_Pdb_from_pdb(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from pdb import Pdb\n"
                                  "Pdb(readrc=None)"))

  def test_skip_of_Pdb_from_pdb(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from pdb import Pdb\n"
                                  "Pdb(skip=None)"))

  def test_header_of_set_trace_from_pdb(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from pdb import set_trace\n"
                                  "set_trace(header=None)"))

  def test_buffer_callback_of_Pickler_from_pickle(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import Pickler\n"
                                  "Pickler(buffer_callback=None)"))

  def test_protocol_of_Pickler_from_pickle(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from pickle import Pickler\n"
                                  "Pickler(protocol=None)"))

  def test_buffers_of_Unpickler_from_pickle(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import Unpickler\n"
                                  "Unpickler(buffers=None)"))

  def test_buffer_callback_of_dump_from_pickle(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import dump\n"
                                  "dump(buffer_callback=None)"))

  def test_protocol_of_dump_from_pickle(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from pickle import dump\n"
                                  "dump(protocol=None)"))

  def test_buffer_callback_of_dumps_from_pickle(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import dumps\n"
                                  "dumps(buffer_callback=None)"))

  def test_protocol_of_dumps_from_pickle(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from pickle import dumps\n"
                                  "dumps(protocol=None)"))

  def test_buffers_of_load_from_pickle(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import load\n"
                                  "load(buffers=None)"))

  def test_buffers_of_loads_from_pickle(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pickle import loads\n"
                                  "loads(buffers=None)"))

  def test_timeout_of_POP3_from_poplib(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from poplib import POP3\n"
                                  "POP3(timeout=None)"))

  def test_context_of_POP3_SSL_from_poplib(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from poplib import POP3_SSL\n"
                                  "POP3_SSL(context=None)"))

  def test_sort_dicts_of_PrettyPrinter_from_pprint(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pprint import PrettyPrinter\n"
                                  "PrettyPrinter(sort_dicts=None)"))

  def test_underscore_numbers_of_PrettyPrinter_from_pprint(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from pprint import PrettyPrinter\n"
                                  "PrettyPrinter(underscore_numbers=None)"))

  def test_depth_of_pformat_from_pprint(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from pprint import pformat\n"
                                  "pformat(depth=None)"))

  def test_indent_of_pformat_from_pprint(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from pprint import pformat\n"
                                  "pformat(indent=None)"))

  def test_sort_dicts_of_pformat_from_pprint(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pprint import pformat\n"
                                  "pformat(sort_dicts=None)"))

  def test_width_of_pformat_from_pprint(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from pprint import pformat\n"
                                  "pformat(width=None)"))

  def test_underscore_numbers_of_pformat_from_pprint(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from pprint import pformat\n"
                                  "pformat(underscore_numbers=None)"))

  def test_depth_of_pprint_from_pprint(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from pprint import pprint\n"
                                  "pprint(depth=None)"))

  def test_indent_of_pprint_from_pprint(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from pprint import pprint\n"
                                  "pprint(indent=None)"))

  def test_sort_dicts_of_pprint_from_pprint(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pprint import pprint\n"
                                  "pprint(sort_dicts=None)"))

  def test_width_of_pprint_from_pprint(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from pprint import pprint\n"
                                  "pprint(width=None)"))

  def test_underscore_numbers_of_pprint_from_pprint(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from pprint import pprint\n"
                                  "pprint(underscore_numbers=None)"))

  def test_invalidation_mode_of_compile_from_py_compile(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from py_compile import compile\n"
                                  "compile(invalidation_mode=None)"))

  def test_optimize_of_compile_from_py_compile(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from py_compile import compile\n"
                                  "compile(optimize=None)"))

  def test_quiet_of_compile_from_py_compile(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from py_compile import compile\n"
                                  "compile(quiet=None)"))

  def test_flags_of_findall_from_re(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from re import findall\n"
                                  "findall(flags=None)"))

  def test_flags_of_finditer_from_re(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from re import finditer\n"
                                  "finditer(flags=None)"))

  def test_flags_of_split_from_re(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from re import split\n"
                                  "split(flags=None)"))

  def test_flags_of_sub_from_re(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from re import sub\n"
                                  "sub(flags=None)"))

  def test_flags_of_subn_from_re(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from re import subn\n"
                                  "subn(flags=None)"))

  def test_flags_of_epoll_from_select(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from select import epoll\n"
                                  "epoll(flags=None)"))

  def test_keyencoding_of_Shelf_from_shelve(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from shelve import Shelf\n"
                                  "Shelf(keyencoding=None)"))

  def test_protocol_of_Shelf_from_shelve(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from shelve import Shelf\n"
                                  "Shelf(protocol=None)"))

  def test_protocol_of_open_from_shelve(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from shelve import open\n"
                                  "open(protocol=None)"))

  def test_follow_symlinks_of_copy_from_shutil(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from shutil import copy\n"
                                  "copy(follow_symlinks=None)"))

  def test_follow_symlinks_of_copy2_from_shutil(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from shutil import copy2\n"
                                  "copy2(follow_symlinks=None)"))

  def test_follow_symlinks_of_copyfile_from_shutil(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from shutil import copyfile\n"
                                  "copyfile(follow_symlinks=None)"))

  def test_follow_symlinks_of_copymode_from_shutil(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from shutil import copymode\n"
                                  "copymode(follow_symlinks=None)"))

  def test_follow_symlinks_of_copystat_from_shutil(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from shutil import copystat\n"
                                  "copystat(follow_symlinks=None)"))

  def test_copy_function_of_copytree_from_shutil(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from shutil import copytree\n"
                                  "copytree(copy_function=None)"))

  def test_dirs_exist_ok_of_copytree_from_shutil(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from shutil import copytree\n"
                                  "copytree(dirs_exist_ok=None)"))

  def test_ignore_of_copytree_from_shutil(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from shutil import copytree\n"
                                  "copytree(ignore=None)"))

  def test_ignore_dangling_symlinks_of_copytree_from_shutil(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from shutil import copytree\n"
                                  "copytree(ignore_dangling_symlinks=None)"))

  def test_copy_function_of_move_from_shutil(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from shutil import move\n"
                                  "move(copy_function=None)"))

  def test_warn_on_full_buffer_of_set_wakeup_fd_from_signal(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from signal import set_wakeup_fd\n"
                                  "set_wakeup_fd(warn_on_full_buffer=None)"))

  def test_decode_data_of_SMTPChannel_from_smtpd(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from smtpd import SMTPChannel\n"
                                  "SMTPChannel(decode_data=None)"))

  def test_enable_SMTPUTF8_of_SMTPChannel_from_smtpd(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from smtpd import SMTPChannel\n"
                                  "SMTPChannel(enable_SMTPUTF8=None)"))

  def test_decode_data_of_SMTPServer_from_smtpd(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from smtpd import SMTPServer\n"
                                  "SMTPServer(decode_data=None)"))

  def test_enable_SMTPUTF8_of_SMTPServer_from_smtpd(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from smtpd import SMTPServer\n"
                                  "SMTPServer(enable_SMTPUTF8=None)"))

  def test_map_of_SMTPServer_from_smtpd(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from smtpd import SMTPServer\n"
                                  "SMTPServer(map=None)"))

  def test_source_address_of_create_connection_from_socket(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from socket import create_connection\n"
                                  "create_connection(source_address=None)"))

  def test_optlen_of_setsockopt_from_socket(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from socket import setsockopt\n"
                                  "setsockopt(optlen=None)"))

  def test_uri_of_connect_from_sqlite3(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from sqlite3 import connect\n"
                                  "connect(uri=None)"))

  def test_chars_of_lstrip_from_string(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from string import lstrip\n"
                                  "lstrip(chars=None)"))

  def test_chars_of_rstrip_from_string(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from string import rstrip\n"
                                  "rstrip(chars=None)"))

  def test_chars_of_strip_from_string(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from string import strip\n"
                                  "strip(chars=None)"))

  def test_encoding_of_TarFile_from_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarFile\n"
                                  "TarFile(encoding=None)"))

  def test_errors_of_TarFile_from_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarFile\n"
                                  "TarFile(errors=None)"))

  def test_format_of_TarFile_from_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarFile\n"
                                  "TarFile(format=None)"))

  def test_pax_headers_of_TarFile_from_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarFile\n"
                                  "TarFile(pax_headers=None)"))

  def test_tarinfo_of_TarFile_from_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tarfile import TarFile\n"
                                  "TarFile(tarinfo=None)"))

  def test_timeout_of_Telnet_from_telnetlib(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from telnetlib import Telnet\n"
                                  "Telnet(timeout=None)"))

  def test_delete_of_NamedTemporaryFile_from_tempfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from tempfile import NamedTemporaryFile\n"
                                  "NamedTemporaryFile(delete=None)"))

  def test_errors_of_NamedTemporaryFile_from_tempfile(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from tempfile import NamedTemporaryFile\n"
                                  "NamedTemporaryFile(errors=None)"))

  def test_errors_of_SpooledTemporaryFile_from_tempfile(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from tempfile import SpooledTemporaryFile\n"
                                  "SpooledTemporaryFile(errors=None)"))

  def test_errors_of_TemporaryFile_from_tempfile(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from tempfile import TemporaryFile\n"
                                  "TemporaryFile(errors=None)"))

  def test_ignore_cleanup_errors_of_TemporaryDirectory_from_tempfile(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from tempfile import TemporaryDirectory\n"
                                  "TemporaryDirectory(ignore_cleanup_errors=None)"))

  def test_daemon_of_Thread_from_threading(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from threading import Thread\n"
                                  "Thread(daemon=None)"))

  def test_globals_of_Timer_from_timeit(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from timeit import Timer\n"
                                  "Timer(globals=None)"))

  def test_globals_of_repeat_from_timeit(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from timeit import repeat\n"
                                  "repeat(globals=None)"))

  def test_globals_of_timeit_from_timeit(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from timeit import timeit\n"
                                  "timeit(globals=None)"))

  def test_tb_locals_of_TextTestRunner_from_unittest(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from unittest import TextTestRunner\n"
                                  "TextTestRunner(tb_locals=None)"))

  def test_warnings_of_TextTestRunner_from_unittest(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from unittest import TextTestRunner\n"
                                  "TextTestRunner(warnings=None)"))

  def test_buffer_of_main_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import main\n"
                                  "main(buffer=None)"))

  def test_catchbreak_of_main_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import main\n"
                                  "main(catchbreak=None)"))

  def test_exit_of_main_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import main\n"
                                  "main(exit=None)"))

  def test_failfast_of_main_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import main\n"
                                  "main(failfast=None)"))

  def test_verbosity_of_main_from_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import main\n"
                                  "main(verbosity=None)"))

  def test_warnings_of_main_from_unittest(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from unittest import main\n"
                                  "main(warnings=None)"))

  def test_context_of_URLopener_from_urllib(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib import URLopener\n"
                                  "URLopener(context=None)"))

  def test_context_of_urlopen_from_urllib(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib import urlopen\n"
                                  "urlopen(context=None)"))

  def test_proxies_of_urlopen_from_urllib(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from urllib import urlopen\n"
                                  "urlopen(proxies=None)"))

  def test_context_of_urlretrieve_from_urllib(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib import urlretrieve\n"
                                  "urlretrieve(context=None)"))

  def test_context_of_HTTPSHandler_from_urllib2(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib2 import HTTPSHandler\n"
                                  "HTTPSHandler(context=None)"))

  def test_cadefault_of_urlopen_from_urllib2(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib2 import urlopen\n"
                                  "urlopen(cadefault=None)"))

  def test_cafile_of_urlopen_from_urllib2(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib2 import urlopen\n"
                                  "urlopen(cafile=None)"))

  def test_capth_of_urlopen_from_urllib2(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib2 import urlopen\n"
                                  "urlopen(capth=None)"))

  def test_context_of_urlopen_from_urllib2(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urllib2 import urlopen\n"
                                  "urlopen(context=None)"))

  def test_timeout_of_urlopen_from_urllib2(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from urllib2 import urlopen\n"
                                  "urlopen(timeout=None)"))

  def test_max_num_fields_of_parse_qs_from_urlparse(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urlparse import parse_qs\n"
                                  "parse_qs(max_num_fields=None)"))

  def test_max_num_fields_of_parse_qsl_from_urlparse(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from urlparse import parse_qsl\n"
                                  "parse_qsl(max_num_fields=None)"))

  def test_backtick_of_encode_from_uu(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from uu import encode\n"
                                  "encode(backtick=None)"))

  def test_prompt_of_create_from_venv(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from venv import create\n"
                                  "create(prompt=None)"))

  def test_line_of_showwarning_from_warnings(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from warnings import showwarning\n"
                                  "showwarning(line=None)"))

  def test_preferred_of_register_from_webbrowser(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from webbrowser import register\n"
                                  "register(preferred=None)"))

  def test_key_of_OpenKey_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKey\n"
                                  "OpenKey(key=None)"))

  def test_sub_key_of_OpenKey_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKey\n"
                                  "OpenKey(sub_key=None)"))

  def test_reserved_of_OpenKey_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKey\n"
                                  "OpenKey(reserved=None)"))

  def test_access_of_OpenKey_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKey\n"
                                  "OpenKey(access=None)"))

  def test_key_of_OpenKeyEx_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKeyEx\n"
                                  "OpenKeyEx(key=None)"))

  def test_sub_key_of_OpenKeyEx_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKeyEx\n"
                                  "OpenKeyEx(sub_key=None)"))

  def test_reserved_of_OpenKeyEx_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKeyEx\n"
                                  "OpenKeyEx(reserved=None)"))

  def test_access_of_OpenKeyEx_from_winreg(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from winreg import OpenKeyEx\n"
                                  "OpenKeyEx(access=None)"))

  def test_compresslevel_of_ZipFile_from_zipfile(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from zipfile import ZipFile\n"
                                  "ZipFile(compresslevel=None)"))

  def test_strict_timestamps_of_ZipFile_from_zipfile(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from zipfile import ZipFile\n"
                                  "ZipFile(strict_timestamps=None)"))

  def test_level_of_compress_from_zlib(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from zlib import compress\n"
                                  "compress(level=None)"))

  def test_zdict_of_compressobj_from_zlib(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from zlib import compressobj\n"
                                  "compressobj(zdict=None)"))

  def test_bufsize_of_decompress_from_zlib(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from zlib import decompress\n"
                                  "decompress(bufsize=None)"))

  def test_wbits_of_decompress_from_zlib(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from zlib import decompress\n"
                                  "decompress(wbits=None)"))

  def test_zdict_of_decompressobj_from_zlib(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from zlib import decompressobj\n"
                                  "decompressobj(zdict=None)"))

  def test_policy_of_Message_from_email_message(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.message import Message\n"
                                  "Message(policy=None)"))

  def test_policy_of_BytesParser_from_email_parser(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.parser import BytesParser\n"
                                  "BytesParser(policy=None)"))

  def test_policy_of_Parser_from_email_parser(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from email.parser import Parser\n"
                                  "Parser(policy=None)"))

  def test_mangle_from__of_Policy_from_email_policy(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from email.policy import Policy\n"
                                  "Policy(mangle_from_=None)"))

  def test_convert_charrefs_of_HTMLParser_from_html_parser(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from html.parser import HTMLParser\n"
                                  "HTMLParser(convert_charrefs=None)"))

  def test_blocksize_of_HTTPConnection_from_http_client(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from http.client import HTTPConnection\n"
                                  "HTTPConnection(blocksize=None)"))

  def test_source_address_of_HTTPConnection_from_http_client(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.client import HTTPConnection\n"
                                  "HTTPConnection(source_address=None)"))

  def test_check_hostname_of_HTTPSConnection_from_http_client(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.client import HTTPSConnection\n"
                                  "HTTPSConnection(check_hostname=None)"))

  def test_context_of_HTTPSConnection_from_http_client(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.client import HTTPSConnection\n"
                                  "HTTPSConnection(context=None)"))

  def test_source_address_of_HTTPSConnection_from_http_client(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from http.client import HTTPSConnection\n"
                                  "HTTPSConnection(source_address=None)"))

  def test_disable_existing_loggers_of_fileConfig_from_logging_config(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging.config import fileConfig\n"
                                  "fileConfig(disable_existing_loggers=None)"))

  def test_encoding_of_fileConfig_from_logging_config(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from logging.config import fileConfig\n"
                                  "fileConfig(encoding=None)"))

  def test_verify_of_listen_from_logging_config(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from logging.config import listen\n"
                                  "listen(verify=None)"))

  def test_context_of_HTTPHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from logging.handlers import HTTPHandler\n"
                                  "HTTPHandler(context=None)"))

  def test_flushOnClose_of_MemoryHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from logging.handlers import MemoryHandler\n"
                                  "MemoryHandler(flushOnClose=None)"))

  def test_respect_handler_level_of_QueueListener_from_logging_handlers(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from logging.handlers import QueueListener\n"
                                  "QueueListener(respect_handler_level=None)"))

  def test_delay_of_RotatingFileHandler_from_logging_handlers(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging.handlers import RotatingFileHandler\n"
                                  "RotatingFileHandler(delay=None)"))

  def test_credentials_of_SMTPHandler_from_logging_handlers(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging.handlers import SMTPHandler\n"
                                  "SMTPHandler(credentials=None)"))

  def test_secure_of_SMTPHandler_from_logging_handlers(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from logging.handlers import SMTPHandler\n"
                                  "SMTPHandler(secure=None)"))

  def test_timeout_of_SMTPHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging.handlers import SMTPHandler\n"
                                  "SMTPHandler(timeout=None)"))

  def test_socktype_of_SysLogHandler_from_logging_handlers(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from logging.handlers import SysLogHandler\n"
                                  "SysLogHandler(socktype=None)"))

  def test_atTime_of_TimedRotatingFileHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from logging.handlers import TimedRotatingFileHandler\n"
                                  "TimedRotatingFileHandler(atTime=None)"))

  def test_delay_of_TimedRotatingFileHandler_from_logging_handlers(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging.handlers import TimedRotatingFileHandler\n"
                                  "TimedRotatingFileHandler(delay=None)"))

  def test_utc_of_TimedRotatingFileHandler_from_logging_handlers(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging.handlers import TimedRotatingFileHandler\n"
                                  "TimedRotatingFileHandler(utc=None)"))

  def test_context_of_Pool_from_multiprocessing_pool(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from multiprocessing.pool import Pool\n"
                                  "Pool(context=None)"))

  def test_maxtasksperchild_of_Pool_from_multiprocessing_pool(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from multiprocessing.pool import Pool\n"
                                  "Pool(maxtasksperchild=None)"))

  def test_quiet_of_check_warnings_from_test_support(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from test.support import check_warnings\n"
                                  "check_warnings(quiet=None)"))

  def test_encoding_of_parse_qs_from_urllib_parse(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.parse import parse_qs\n"
                                  "parse_qs(encoding=None)"))

  def test_errors_of_parse_qs_from_urllib_parse(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.parse import parse_qs\n"
                                  "parse_qs(errors=None)"))

  def test_max_num_fields_of_parse_qs_from_urllib_parse(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from urllib.parse import parse_qs\n"
                                  "parse_qs(max_num_fields=None)"))

  def test_separator_of_parse_qs_from_urllib_parse(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from urllib.parse import parse_qs\n"
                                  "parse_qs(separator=None)"))

  def test_encoding_of_parse_qsl_from_urllib_parse(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.parse import parse_qsl\n"
                                  "parse_qsl(encoding=None)"))

  def test_errors_of_parse_qsl_from_urllib_parse(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.parse import parse_qsl\n"
                                  "parse_qsl(errors=None)"))

  def test_max_num_fields_of_parse_qsl_from_urllib_parse(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from urllib.parse import parse_qsl\n"
                                  "parse_qsl(max_num_fields=None)"))

  def test_separator_of_parse_qsl_from_urllib_parse(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from urllib.parse import parse_qsl\n"
                                  "parse_qsl(separator=None)"))

  def test_quote_via_of_urlencode_from_urllib_parse(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from urllib.parse import urlencode\n"
                                  "urlencode(quote_via=None)"))

  def test_check_hostname_of_HTTPSHandler_from_urllib_request(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.request import HTTPSHandler\n"
                                  "HTTPSHandler(check_hostname=None)"))

  def test_context_of_HTTPSHandler_from_urllib_request(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.request import HTTPSHandler\n"
                                  "HTTPSHandler(context=None)"))

  def test_method_of_Request_from_urllib_request(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from urllib.request import Request\n"
                                  "Request(method=None)"))

  def test_cadefault_of_urlopen_from_urllib_request(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from urllib.request import urlopen\n"
                                  "urlopen(cadefault=None)"))

  def test_cafile_of_urlopen_from_urllib_request(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.request import urlopen\n"
                                  "urlopen(cafile=None)"))

  def test_capath_of_urlopen_from_urllib_request(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from urllib.request import urlopen\n"
                                  "urlopen(capath=None)"))

  def test_context_of_urlopen_from_urllib_request(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from urllib.request import urlopen\n"
                                  "urlopen(context=None)"))

  def test_context_of_ServerProxy_from_xmlrpc_client(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from xmlrpc.client import ServerProxy\n"
                                  "ServerProxy(context=None)"))

  def test_headers_of_ServerProxy_from_xmlrpc_client(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from xmlrpc.client import ServerProxy\n"
                                  "ServerProxy(headers=None)"))

  def test_use_builtin_types_of_ServerProxy_from_xmlrpc_client(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from xmlrpc.client import ServerProxy\n"
                                  "ServerProxy(use_builtin_types=None)"))

  def test_use_builtin_types_of_loads_from_xmlrpc_client(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from xmlrpc.client import loads\n"
                                  "loads(use_builtin_types=None)"))

  def test_short_empty_elements_of_XMLGenerator_from_xml_sax_saxutils(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from xml.sax.saxutils import XMLGenerator\n"
                                  "XMLGenerator(short_empty_elements=None)"))

  def test_timestamp_of_date_time_string_from_BaseHTTPServer_BaseHTTPRequestHandler(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from BaseHTTPServer import BaseHTTPRequestHandler\n"
                                  "x = BaseHTTPRequestHandler()\n"
                                  "x.date_time_string(timestamp=None)"))

  def test_timeout_of_get_from_Queue_Queue(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from Queue import Queue\n"
                                  "x = Queue()\n"
                                  "x.get(timeout=None)"))

  def test_timeout_of_put_from_Queue_Queue(self):
    self.assertOnlyIn((2, 3),
                      self.detect("from Queue import Queue\n"
                                  "x = Queue()\n"
                                  "x.put(timeout=None)"))

  def test_timeout_of_acquire_from__thread_lock(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from _thread import lock\n"
                                  "x = lock()\n"
                                  "x.acquire(timeout=None)"))

  def test_required_of_add_subparsers_from_argparse_ArgumentParser(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from argparse import ArgumentParser\n"
                                  "x = ArgumentParser()\n"
                                  "x.add_subparsers(required=None)"))

  def test_context_of_add_done_callback_from_asyncio_Future(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import Future\n"
                                  "x = Future()\n"
                                  "x.add_done_callback(context=None)"))

  def test_context_of_call_at_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.call_at(context=None)"))

  def test_context_of_call_later_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.call_later(context=None)"))

  def test_context_of_call_soon_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.call_soon(context=None)"))

  def test_context_of_call_soon_threadsafe_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.call_soon_threadsafe(context=None)"))

  def test_ssl_handshake_timeout_of_connect_accepted_socket_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.connect_accepted_socket(ssl_handshake_timeout=None)"))

  def test_happy_eyeballs_delay_of_create_connection_from_asyncio_loop(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_connection(happy_eyeballs_delay=None)"))

  def test_interleave_of_create_connection_from_asyncio_loop(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_connection(interleave=None)"))

  def test_ssl_handshake_timeout_of_create_connection_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_connection(ssl_handshake_timeout=None)"))

  def test_allow_broadcast_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(allow_broadcast=None)"))

  def test_family_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(family=None)"))

  def test_flags_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(flags=None)"))

  def test_proto_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(proto=None)"))

  def test_reuse_address_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(reuse_address=None)"))

  def test_reuse_port_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(reuse_port=None)"))

  def test_sock_of_create_datagram_endpoint_from_asyncio_loop(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_datagram_endpoint(sock=None)"))

  def test_ssl_handshake_timeout_of_create_server_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_server(ssl_handshake_timeout=None)"))

  def test_start_serving_of_create_server_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_server(start_serving=None)"))

  def test_name_of_create_task_from_asyncio_loop(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_task(name=None)"))

  def test_ssl_handshake_timeout_of_create_unix_connection_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_unix_connection(ssl_handshake_timeout=None)"))

  def test_ssl_handshake_timeout_of_create_unix_server_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_unix_server(ssl_handshake_timeout=None)"))

  def test_start_serving_of_create_unix_server_from_asyncio_loop(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from asyncio import loop\n"
                                  "x = loop()\n"
                                  "x.create_unix_server(start_serving=None)"))

  def test_chars_of_read_from_codecs_StreamReader(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from codecs import StreamReader\n"
                                  "x = StreamReader()\n"
                                  "x.read(chars=None)"))

  def test_firstline_of_read_from_codecs_StreamReader(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from codecs import StreamReader\n"
                                  "x = StreamReader()\n"
                                  "x.read(firstline=None)"))

  def test_keepends_of_readline_from_codecs_StreamReader(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from codecs import StreamReader\n"
                                  "x = StreamReader()\n"
                                  "x.readline(keepends=None)"))

  def test_encoding_of_read_from_configparser_ConfigParser(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ConfigParser\n"
                                  "x = ConfigParser()\n"
                                  "x.read(encoding=None)"))

  def test_source_address_of_connect_from_ftplib_FTP(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from ftplib import FTP\n"
                                  "x = FTP()\n"
                                  "x.connect(source_address=None)"))

  def test_timeout_of_connect_from_ftplib_FTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from ftplib import FTP\n"
                                  "x = FTP()\n"
                                  "x.connect(timeout=None)"))

  def test_callback_of_storbinary_from_ftplib_FTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from ftplib import FTP\n"
                                  "x = FTP()\n"
                                  "x.storbinary(callback=None)"))

  def test_rest_of_storbinary_from_ftplib_FTP(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from ftplib import FTP\n"
                                  "x = FTP()\n"
                                  "x.storbinary(rest=None)"))

  def test_callback_of_storlines_from_ftplib_FTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from ftplib import FTP\n"
                                  "x = FTP()\n"
                                  "x.storlines(callback=None)"))

  def test_names_of_install_from_gettext_NullTranslations(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from gettext import NullTranslations\n"
                                  "x = NullTranslations()\n"
                                  "x.install(names=None)"))

  def test_message_body_of_endheaders_from_httplib_HTTPConnection(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from httplib import HTTPConnection\n"
                                  "x = HTTPConnection()\n"
                                  "x.endheaders(message_body=None)"))

  def test_skip_accept_encoding_of_putrequest_from_httplib_HTTPConnection(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from httplib import HTTPConnection\n"
                                  "x = HTTPConnection()\n"
                                  "x.putrequest(skip_accept_encoding=None)"))

  def test_stack_info_of_critical_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.critical(stack_info=None)"))

  def test_stacklevel_of_critical_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.critical(stacklevel=None)"))

  def test_stack_info_of_debug_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.debug(stack_info=None)"))

  def test_stacklevel_of_debug_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.debug(stacklevel=None)"))

  def test_stack_info_of_error_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.error(stack_info=None)"))

  def test_stacklevel_of_error_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.error(stacklevel=None)"))

  def test_stack_info_of_exception_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.exception(stack_info=None)"))

  def test_stacklevel_of_exception_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.exception(stacklevel=None)"))

  def test_stack_info_of_info_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.info(stack_info=None)"))

  def test_stacklevel_of_info_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.info(stacklevel=None)"))

  def test_stack_info_of_log_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.log(stack_info=None)"))

  def test_stacklevel_of_log_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.log(stacklevel=None)"))

  def test_stack_info_of_warn_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.warn(stack_info=None)"))

  def test_stacklevel_of_warn_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.warn(stacklevel=None)"))

  def test_stack_info_of_warning_from_logging_Logger(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.warning(stack_info=None)"))

  def test_stacklevel_of_warning_from_logging_Logger(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from logging import Logger\n"
                                  "x = Logger()\n"
                                  "x.warning(stacklevel=None)"))

  def test_max_length_of_decompress_from_lzma_LZMADecompressor(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from lzma import LZMADecompressor\n"
                                  "x = LZMADecompressor()\n"
                                  "x.decompress(max_length=None)"))

  def test_group_pattern_of_list_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "x = NNTP()\n"
                                  "x.list(group_pattern=None)"))

  def test_missing_ok_of_unlink_from_pathlib_Path(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from pathlib import Path\n"
                                  "x = Path()\n"
                                  "x.unlink(missing_ok=None)"))

  def test_kwargs_of_enter_from_sched_scheduler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from sched import scheduler\n"
                                  "x = scheduler()\n"
                                  "x.enter(kwargs=None)"))

  def test_kwargs_of_enterabs_from_sched_scheduler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from sched import scheduler\n"
                                  "x = scheduler()\n"
                                  "x.enterabs(kwargs=None)"))

  def test_blocking_of_run_from_sched_scheduler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from sched import scheduler\n"
                                  "x = scheduler()\n"
                                  "x.run(blocking=None)"))

  def test_initial_response_ok_of_login_from_smtplib_SMTP(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from smtplib import SMTP\n"
                                  "x = SMTP()\n"
                                  "x.login(initial_response_ok=None)"))

  def test_deterministic_of_create_function_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from sqlite3 import Connection\n"
                                  "x = Connection()\n"
                                  "x.create_function(deterministic=None)"))

  def test_session_of_wrap_bio_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from ssl import SSLContext\n"
                                  "x = SSLContext()\n"
                                  "x.wrap_bio(session=None)"))

  def test_session_of_wrap_socket_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from ssl import SSLContext\n"
                                  "x = SSLContext()\n"
                                  "x.wrap_socket(session=None)"))

  def test_timeout_of_get_server_certificate_from_ssl(self):
    self.assertOnlyIn((3, 10), self.detect("""
from ssl import get_server_certificate
get_server_certificate(timeout=None)
"""))

  def test_timeout_of_open_from_telnetlib_Telnet(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from telnetlib import Telnet\n"
                                  "x = Telnet()\n"
                                  "x.open(timeout=None)"))

  def test_size_of_truncate_from_tempfile_SpooledTemporaryFile(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from tempfile import SpooledTemporaryFile\n"
                                  "x = SpooledTemporaryFile()\n"
                                  "x.truncate(size=None)"))

  def test_timeout_of_acquire_from_threading_Lock(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from threading import Lock\n"
                                  "x = Lock()\n"
                                  "x.acquire(timeout=None)"))

  def test_timeout_of_acquire_from_threading_RLock(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from threading import RLock\n"
                                  "x = RLock()\n"
                                  "x.acquire(timeout=None)"))

  def test_timeout_of_acquire_from_threading_Semaphore(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from threading import Semaphore\n"
                                  "x = Semaphore()\n"
                                  "x.acquire(timeout=None)"))

  def test_msg_of_assertRaises_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from unittest import TestCase\n"
                                  "x = TestCase()\n"
                                  "x.assertRaises(msg=None)"))

  def test_msg_of_assertRaisesRegex_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from unittest import TestCase\n"
                                  "x = TestCase()\n"
                                  "x.assertRaisesRegex(msg=None)"))

  def test_msg_of_assertWarns_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from unittest import TestCase\n"
                                  "x = TestCase()\n"
                                  "x.assertWarns(msg=None)"))

  def test_msg_of_assertWarnsRegex_from_unittest_TestCase(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from unittest import TestCase\n"
                                  "x = TestCase()\n"
                                  "x.assertWarnsRegex(msg=None)"))

  def test_pattern_of_loadTestsFromModule_from_unittest_TestLoader(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from unittest import TestLoader\n"
                                  "x = TestLoader()\n"
                                  "x.loadTestsFromModule(pattern=None)"))

  def test_timeout_of_open_from_urllib2_OpenerDirector(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from urllib2 import OpenerDirector\n"
                                  "x = OpenerDirector()\n"
                                  "x.open(timeout=None)"))

  def test_strict_timestamps_of_from_file_from_zipfile_ZipInfo(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from zipfile import ZipInfo\n"
                                  "x = ZipInfo()\n"
                                  "x.from_file(strict_timestamps=None)"))

  def test_max_length_of_decompress_from_zlib_Decompress(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from zlib import Decompress\n"
                                  "x = Decompress()\n"
                                  "x.decompress(max_length=None)"))

  def test_replace_of_set_param_from_email_message_EmailMessage(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from email.message import EmailMessage\n"
                                  "x = EmailMessage()\n"
                                  "x.set_param(replace=None)"))

  def test_policy_of_as_string_from_email_message_Message(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from email.message import Message\n"
                                  "x = Message()\n"
                                  "x.as_string(policy=None)"))

  def test_unquote_of_get_param_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "x = Message()\n"
                                  "x.get_param(unquote=None)"))

  def test_unquote_of_get_params_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "x = Message()\n"
                                  "x.get_params(unquote=None)"))

  def test_replace_of_set_param_from_email_message_Message(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from email.message import Message\n"
                                  "x = Message()\n"
                                  "x.set_param(replace=None)"))

  def test_charset_of_set_payload_from_email_message_Message(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "x = Message()\n"
                                  "x.set_payload(charset=None)"))

  def test_encode_chunked_of_endheaders_from_http_client_HTTPConnection(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from http.client import HTTPConnection\n"
                                  "x = HTTPConnection()\n"
                                  "x.endheaders(encode_chunked=None)"))

  def test_encode_chunked_of_request_from_http_client_HTTPConnection(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from http.client import HTTPConnection\n"
                                  "x = HTTPConnection()\n"
                                  "x.request(encode_chunked=None)"))

  def test_explain_of_send_error_from_http_server_BaseHTTPRequestHandler(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from http.server import BaseHTTPRequestHandler\n"
                                  "x = BaseHTTPRequestHandler()\n"
                                  "x.send_error(explain=None)"))

  def test_return_value_of_reset_mock_from_unittest_mock_Mock(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from unittest.mock import Mock\n"
                                  "x = Mock()\n"
                                  "x.reset_mock(return_value=None)"))

  def test_side_effect_of_reset_mock_from_unittest_mock_Mock(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from unittest.mock import Mock\n"
                                  "x = Mock()\n"
                                  "x.reset_mock(side_effect=None)"))

  def test_encoding_of_writexml_from_xml_dom_minidom_Document(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.dom.minidom import Document\n"
                                  "x = Document()\n"
                                  "x.writexml(encoding=None)"))

  def test_encoding_of_toprettyxml_from_xml_dom_minidom_Node(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.dom.minidom import Node\n"
                                  "x = Node()\n"
                                  "x.toprettyxml(encoding=None)"))

  def test_encoding_of_toxml_from_xml_dom_minidom_Node(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.dom.minidom import Node\n"
                                  "x = Node()\n"
                                  "x.toxml(encoding=None)"))

  def test_addindent_of_writexml_from_xml_dom_minidom_Node(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.dom.minidom import Node\n"
                                  "x = Node()\n"
                                  "x.writexml(addindent=None)"))

  def test_indent_of_writexml_from_xml_dom_minidom_Node(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.dom.minidom import Node\n"
                                  "x = Node()\n"
                                  "x.writexml(indent=None)"))

  def test_newl_of_writexml_from_xml_dom_minidom_Node(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.dom.minidom import Node\n"
                                  "x = Node()\n"
                                  "x.writexml(newl=None)"))

  def test_short_empty_elements_of_write_from_xml_etree_ElementTree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from xml.etree.ElementTree import ElementTree\n"
                                  "x = ElementTree()\n"
                                  "x.write(short_empty_elements=None)"))

  def test_indent_of_dump_from_ast(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from ast import dump\n"
                                  "dump(indent=None)"))

  def test_include_extras_of_get_type_hints_from_typing(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from typing import get_type_hints\n"
                                  "get_type_hints(include_extras=None)"))

  def test_base_url_of_include_from_xml_etree_ElementInclude(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from xml.etree import ElementInclude\n"
                                  "x = ElementInclude()\n"
                                  "x.include(base_url=None)"))

  def test_max_depth_of_include_from_xml_etree_ElementInclude(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from xml.etree import ElementInclude\n"
                                  "x = ElementInclude()\n"
                                  "x.include(max_depth=None)"))

  def test_msg_of_cancel_from_asyncio_Task(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from asyncio import Task\n"
                                  "x = Task()\n"
                                  "x.cancel(msg=None)"))

  def test_usedforsecurity_of_new_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import new\n"
                                  "new(usedforsecurity=None)"))

  def test_usedforsecurity_of_blake2b_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import blake2b\n"
                                  "blake2b(usedforsecurity=None)"))

  def test_usedforsecurity_of_blake2s_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import blake2s\n"
                                  "blake2s(usedforsecurity=None)"))

  def test_usedforsecurity_of_md5_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import md5\n"
                                  "md5(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha1_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha1\n"
                                  "sha1(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha224_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha224\n"
                                  "sha224(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha256_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha256\n"
                                  "sha256(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha384_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha384\n"
                                  "sha384(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha512_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha512\n"
                                  "sha512(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha3_224_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha3_224\n"
                                  "sha3_224(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha3_256_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha3_256\n"
                                  "sha3_256(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha3_384_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha3_384\n"
                                  "sha3_384(usedforsecurity=None)"))

  def test_usedforsecurity_of_sha3_512_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import sha3_512\n"
                                  "sha3_512(usedforsecurity=None)"))

  def test_usedforsecurity_of_shake_128_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import shake_128\n"
                                  "shake_128(usedforsecurity=None)"))

  def test_usedforsecurity_of_shake_256_from_hashlib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from hashlib import shake_256\n"
                                  "shake_256(usedforsecurity=None)"))

  def test_counts_of_sample_from_random(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from random import sample\n"
                                  "sample(counts=None)"))

  def test_encoding_of_FTP_from_ftplib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from ftplib import FTP\n"
                                  "FTP(encoding=None)"))

  def test_encoding_of_FTP_TLS_from_ftplib(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from ftplib import FTP_TLS\n"
                                  "FTP_TLS(encoding=None)"))

  def test_recursive_of_iglob_from_glob(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from glob import iglob\n"
                                  "iglob(recursive=None)"))

  def test_encoding_of_basicConfig_from_logging(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(encoding=None)"))

  def test_errors_of_basicConfig_from_logging(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from logging import basicConfig\n"
                                  "basicConfig(errors=None)"))

  def test_errors_of_RotatingFileHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from logging.handlers import RotatingFileHandler\n"
                                  "RotatingFileHandler(errors=None)"))

  def test_errors_of_TimedRotatingFileHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from logging.handlers import TimedRotatingFileHandler\n"
                                  "TimedRotatingFileHandler(errors=None)"))

  def test_errors_of_WatchedFileHandler_from_logging_handlers(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from logging.handlers import WatchedFileHandler\n"
                                  "WatchedFileHandler(errors=None)"))

  def test_in_fd_of_sendfile_from_os(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from os import sendfile\n"
                                  "sendfile(in_fd=None)"))

  def test_out_fd_of_sendfile_from_os(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from os import sendfile\n"
                                  "sendfile(out_fd=None)"))

  def test_extra_groups_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(extra_groups=None)"))

  def test_group_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(group=None)"))

  def test_umask_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(umask=None)"))

  def test_user_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(user=None)"))

  def test_pipesize_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from subprocess import Popen\n"
                                  "Popen(pipesize=None)"))

  def test_encoding_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from subprocess import call\n"
                                  "call(encoding=None)"))

  def test_errors_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from subprocess import call\n"
                                  "call(errors=None)"))

  def test_extra_groups_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import call\n"
                                  "call(extra_groups=None)"))

  def test_group_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import call\n"
                                  "call(group=None)"))

  def test_pass_fds_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import call\n"
                                  "call(pass_fds=None)"))

  def test_restore_signals_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import call\n"
                                  "call(restore_signals=None)"))

  def test_start_new_session_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import call\n"
                                  "call(start_new_session=None)"))

  def test_text_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from subprocess import call\n"
                                  "call(text=None)"))

  def test_umask_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import call\n"
                                  "call(umask=None)"))

  def test_user_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import call\n"
                                  "call(user=None)"))

  def test_pipesize_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from subprocess import call\n"
                                  "call(pipesize=None)"))

  def test_encoding_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(encoding=None)"))

  def test_errors_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(errors=None)"))

  def test_extra_groups_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(extra_groups=None)"))

  def test_group_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(group=None)"))

  def test_pass_fds_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(pass_fds=None)"))

  def test_restore_signals_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(restore_signals=None)"))

  def test_start_new_session_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(start_new_session=None)"))

  def test_text_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(text=None)"))

  def test_umask_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(umask=None)"))

  def test_user_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(user=None)"))

  def test_pipesize_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from subprocess import check_call\n"
                                  "check_call(pipesize=None)"))

  def test_extra_groups_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(extra_groups=None)"))

  def test_group_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(group=None)"))

  def test_pass_fds_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(pass_fds=None)"))

  def test_restore_signals_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(restore_signals=None)"))

  def test_start_new_session_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(start_new_session=None)"))

  def test_umask_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(umask=None)"))

  def test_user_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(user=None)"))

  def test_pipesize_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from subprocess import check_output\n"
                                  "check_output(pipesize=None)"))

  def test_extra_groups_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import run\n"
                                  "run(extra_groups=None)"))

  def test_group_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import run\n"
                                  "run(group=None)"))

  def test_umask_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import run\n"
                                  "run(umask=None)"))

  def test_user_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from subprocess import run\n"
                                  "run(user=None)"))

  def test_pipesize_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from subprocess import run\n"
                                  "run(pipesize=None)"))

  def test_msg_of_cancel_from_asyncio_Future(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from asyncio import Future\n"
                                  "x = Future()\n"
                                  "x.cancel(msg=None)"))

  def test_n_of_release_from_threading_Semaphore(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from threading import Semaphore\n"
                                  "x = Semaphore()\n"
                                  "x.release(n=None)"))

  def test_base_of_pow(self):
    self.assertOnlyIn((3, 8), self.detect("pow(base=None)"))

  def test_exp_of_pow(self):
    self.assertOnlyIn((3, 8), self.detect("pow(exp=None)"))

  def test_mod_of_pow(self):
    self.assertOnlyIn((3, 8), self.detect("pow(mod=None)"))

  def test_strict_of_zip(self):
    self.assertOnlyIn((3, 10), self.detect("zip(strict=True)"))

  def test_key_of_bisect_bisect(self):
    self.assertOnlyIn((3, 10), self.detect("""
import bisect
bisect.bisect(key='x')
"""))

  def test_key_of_bisect_bisect_left(self):
    self.assertOnlyIn((3, 10), self.detect("""
import bisect
bisect.bisect_left(key='x')
"""))

  def test_key_of_bisect_insort(self):
    self.assertOnlyIn((3, 10), self.detect("""
import bisect
bisect.insort(key='x')
"""))

  def test_key_of_bisect_insort_left(self):
    self.assertOnlyIn((3, 10), self.detect("""
import bisect
bisect.insort_left(key='x')
"""))

  def test_kw_only_of_dataclasses_dataclass(self):
    self.assertOnlyIn((3, 10), self.detect("""
from dataclasses import dataclass
@dataclass(kw_only=True)
class Foo: pass
"""))

  def test_match_args_of_dataclasses_dataclass(self):
    self.assertOnlyIn((3, 10), self.detect("""
from dataclasses import dataclass
@dataclass(match_args=True)
class Foo: pass
"""))

  def test_slots_of_dataclasses_dataclass(self):
    self.assertOnlyIn((3, 10), self.detect("""
from dataclasses import dataclass
@dataclass(slots=True)
class Foo: pass
"""))

  def test_kw_only_of_dataclasses_field(self):
    self.assertOnlyIn((3, 10), self.detect("""
from dataclasses import dataclass, field
@dataclass
class Foo:
  bar = field(kw_only=False)
"""))

    # variable annotations requires !2, 3.6
    if current_version() >= (3, 6):
      self.assertOnlyIn((3, 10), self.detect("""
from dataclasses import dataclass, field
@dataclass
class Foo:
  bar: int = field(kw_only=False)
"""))
