from .testutils import VerminTest, detect

class VerminKwargsTests(VerminTest):
  def test_inheritable_of_dup2_from_os(self):
    self.assertOnlyIn(3.4, detect("import os\nv = os.dup2(inheritable=True)"))
    self.assertOnlyIn(3.4, detect("from os import dup2\nv = dup2(inheritable=True)"))

  def test_dir_fd_of_open_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.open(dir_fd=None)"))

  def test_dir_fd_of_access_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.access(dir_fd=None)"))

  def test_effective_ids_of_access_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.access(effective_ids=None)"))

  def test_follow_symlinks_of_access_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.access(follow_symlinks=None)"))

  def test_follow_symlinks_of_chflags_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chflags(follow_symlinks=None)"))

  def test_dir_fd_of_chmod_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chmod(dir_fd=None)"))

  def test_follow_symlinks_of_chmod_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chmod(follow_symlinks=None)"))

  def test_dir_fd_of_chown_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chown(dir_fd=None)"))

  def test_follow_symlinks_of_chown_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.chown(follow_symlinks=None)"))

  def test_src_dir_fd_of_link_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.link(src_dir_fd=None)"))

  def test_dst_dir_fd_of_link_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.link(dst_dir_fd=None)"))

  def test_follow_symlinks_of_link_from_os(self):
    self.assertOnlyIn(3.3, detect("import os\nv = os.link(follow_symlinks=None)"))

  def test_maxtasksperchild_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn(3.2, detect("import multiprocessing\nPool(maxtasksperchild=3)"))

  def test_context_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn(3.4, detect("import multiprocessing\nPool(context=None)"))

  def test_daemon_of_Process_from_multiprocessing(self):
    self.assertOnlyIn(3.3, detect("import multiprocessing\nProcess(daemon=None)"))

  def test_compact_of_PrettyPrinter_from_pprint(self):
    self.assertOnlyIn(3.4, detect("import pprint\npprint.PrettyPrinter(compact=True)"))

  def test_compact_of_pformat_from_pprint(self):
    self.assertOnlyIn(3.4, detect("import pprint\npprint.pformat(compact=True)"))

  def test_compact_of_pprint_from_pprint(self):
    self.assertOnlyIn(3.4, detect("import pprint\npprint.pprint(compact=True)"))

  def test_delta_of_assertAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestCase\nTestCase.assertAlmostEqual(delta=1)"))

  def test_delta_of_assertNotAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn((2.7, 3.0),
                      detect("from unittest import TestCase\n"
                             "TestCase.assertNotAlmostEqual(delta=1)"))

  def test_fold_of_datetime_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime(fold=1)"))

  def test_tzinfo_of_combine_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime.combine(tzinfo=1)"))

  def test_fold_of_replace_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime.replace(fold=1)"))

  def test_timespec_of_isoformat_from_datetime(self):
    self.assertOnlyIn(3.6, detect("from datetime import datetime\ndatetime.isoformat(timespec=1)"))

  def test_domain_of_Filter_from_tracemalloc(self):
    self.assertOnlyIn(3.6, detect("import tracemalloc\ntracemalloc.Filter(domain=1)"))

  def test_max_length_of_decompress_from_bz2_BZ2Decompressor(self):
    self.assertOnlyIn(3.5,
                      detect("from bz2 import BZ2Decompressor\n"
                             "d = BZ2Decompressor()\n"
                             "d.decompress(max_length=1)"))

  def test_maxlen_of_deque_from_collections(self):
    self.assertOnlyIn((2.6, 3.0), detect("import collections\ncollections.deque(maxlen=1)"))

  def test_rename_of_namedtuple_from_collections(self):
    self.assertOnlyIn((2.7, 3.1), detect("import collections\ncollections.namedtuple(rename=True)"))

  def test_module_of_namedtuple_from_collections(self):
    self.assertOnlyIn(3.6, detect("import collections\ncollections.namedtuple(module=None)"))

  def test_use_last_error_of_CDLL_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.CDLL(use_last_error=True)"))

  def test_use_errno_of_CDLL_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.CDLL(use_errno=True)"))

  def test_use_last_error_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.OleDLL(use_last_error=True)"))

  def test_use_errno_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.OleDLL(use_errno=True)"))

  def test_use_last_error_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.WinDLL(use_last_error=True)"))

  def test_use_errno_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.WinDLL(use_errno=True)"))

  def test_use_last_error_of_CFUNCTYPE_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.CFUNCTYPE(use_last_error=True)"))

  def test_use_errno_of_CFUNCTYPE_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.CFUNCTYPE(use_errno=True)"))

  def test_offset_of_byref_from_ctypes(self):
    self.assertOnlyIn((2.6, 3.0), detect("import ctypes\nctypes.byref(offset=3)"))

  def test_autojunk_of_SequenceMatcher_from_difflib(self):
    self.assertOnlyIn((2.7, 3.2), detect("import difflib\ndifflib.SequenceMatcher(autojunk=True)"))

  def test_charset_of_make_file_from_difflib(self):
    self.assertOnlyIn(3.5, detect("from difflib import HtmlDiff\n"
                                  "HtmlDiff.make_file(charset=True)"))

  def test_use_builtin_types_of_SimpleXMLRPCServer_from_xmlrpc_server(self):
    self.assertOnlyIn(3.3, detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                                  "SimpleXMLRPCServer(use_builtin_types=True)"))

  def test_use_builtin_types_of_CGIXMLRPCRequestHandler_from_xmlrpc_server(self):
    self.assertOnlyIn(3.3, detect("from xmlrpc.server import CGIXMLRPCRequestHandler\n"
                                  "CGIXMLRPCRequestHandler(use_builtin_types=True)"))

  def test_use_builtin_types_of_DocXMLRPCServer_from_xmlrpc_server(self):
    self.assertOnlyIn(3.3, detect("from xmlrpc.server import DocXMLRPCServer\n"
                                  "DocXMLRPCServer(use_builtin_types=True)"))

  def test_typed_of_lru_cache_from_functools(self):
    self.assertOnlyIn(3.3, detect("import functools\nfunctools.lru_cache(typed=3)"))

  def test_key_of_nlargest_from_heapq(self):
    self.assertOnlyIn((2.4, 3.0), detect("import heapq\nheapq.nlargest(key=3)"))

  def test_key_of_nsmallest_from_heapq(self):
    self.assertOnlyIn((2.4, 3.0), detect("import heapq\nheapq.nsmallest(key=3)"))

  def test_key_of_merge_from_heapq(self):
    self.assertOnlyIn(3.5, detect("import heapq\nheapq.merge(key=3)"))

  def test_reverse_of_merge_from_heapq(self):
    self.assertOnlyIn(3.5, detect("import heapq\nheapq.merge(reverse=True)"))

  def test_follow_wrapped_of_signature_from_inspect(self):
    self.assertOnlyIn(3.5, detect("import inspect\ninspect.signature(follow_wrapped=True)"))

  def test_write_through_of_TextIOWrapper_from_io(self):
    self.assertOnlyIn(3.3, detect("import io\nio.TextIOWrapper(write_through=True)"))

  def test_func_of_accumulate_from_itertools(self):
    self.assertOnlyIn(3.3, detect("import itertools\nitertools.accumulate(func=None)"))

  def test_step_of_count_from_itertools(self):
    self.assertOnlyIn(3.1, detect("import itertools\nitertools.count(step=None)"))

  def test_object_pairs_hook_of_load_from_json(self):
    self.assertOnlyIn((2.7, 3.1), detect("import json\njson.load(object_pairs_hook=None)"))

  def test_object_pairs_hook_of_JSONDecoder_from_json(self):
    self.assertOnlyIn((2.7, 3.1), detect("import json\njson.JSONDecoder(object_pairs_hook=None)"))

  def test_func_of_makeRecord_from_logging_Logger(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from logging import Logger\nLogger.makeRecord(func=None)"))

  def test_extra_of_makeRecord_from_logging_Logger(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from logging import Logger\nLogger.makeRecord(extra=None)"))

  def test_func_of_LogRecord_from_logging(self):
    self.assertOnlyIn((2.5, 3.0),
                      detect("from logging import LogRecord\nLogger.LogRecord(func=None)"))

  def test_extra_of_debug_from_logging(self):
    self.assertOnlyIn((2.5, 3.0), detect("import logging\nlogging.debug(extra=None)"))

  def test_stack_info_of_debug_from_logging(self):
    self.assertOnlyIn(3.2, detect("import logging\nlogging.debug(stack_info=None)"))

  def test_style_of_Formatter_from_logging(self):
    self.assertOnlyIn(3.2, detect("import logging\nlogging.Formatter(style=None)"))
