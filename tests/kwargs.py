from .testutils import VerminTest, detect, current_major_version

class VerminKwargsTests(VerminTest):
  def test_inheritable_of_dup2_from_os(self):
    self.assertOnlyIn((3, 4), detect("import os\nv = os.dup2(inheritable=True)"))
    self.assertOnlyIn((3, 4), detect("from os import dup2\nv = dup2(inheritable=True)"))

  def test_dir_fd_of_open_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.open(dir_fd=None)"))

  def test_dir_fd_of_access_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.access(dir_fd=None)"))

  def test_effective_ids_of_access_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.access(effective_ids=None)"))

  def test_follow_symlinks_of_access_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.access(follow_symlinks=None)"))

  def test_follow_symlinks_of_chflags_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.chflags(follow_symlinks=None)"))

  def test_dir_fd_of_chmod_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.chmod(dir_fd=None)"))

  def test_follow_symlinks_of_chmod_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.chmod(follow_symlinks=None)"))

  def test_dir_fd_of_chown_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.chown(dir_fd=None)"))

  def test_follow_symlinks_of_chown_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.chown(follow_symlinks=None)"))

  def test_src_dir_fd_of_link_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.link(src_dir_fd=None)"))

  def test_dst_dir_fd_of_link_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.link(dst_dir_fd=None)"))

  def test_follow_symlinks_of_link_from_os(self):
    self.assertOnlyIn((3, 3), detect("import os\nv = os.link(follow_symlinks=None)"))

  def test_maxtasksperchild_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn((3, 2),
                      detect("import multiprocessing\nmultiprocessing.Pool(maxtasksperchild=3)"))

  def test_context_of_Pool_from_multiprocessing(self):
    self.assertOnlyIn((3, 4), detect("import multiprocessing\nmultiprocessing.Pool(context=None)"))

  def test_daemon_of_Process_from_multiprocessing(self):
    self.assertOnlyIn((3, 3),
                      detect("import multiprocessing\nmultiprocessing.Process(daemon=None)"))

  def test_compact_of_PrettyPrinter_from_pprint(self):
    self.assertOnlyIn((3, 4), detect("import pprint\npprint.PrettyPrinter(compact=True)"))

  def test_compact_of_pformat_from_pprint(self):
    self.assertOnlyIn((3, 4), detect("import pprint\npprint.pformat(compact=True)"))

  def test_compact_of_pprint_from_pprint(self):
    self.assertOnlyIn((3, 4), detect("import pprint\npprint.pprint(compact=True)"))

  def test_delta_of_assertAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      detect("from unittest import TestCase\nTestCase.assertAlmostEqual(delta=1)"))

  def test_delta_of_assertNotAlmostEqual_from_unitest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      detect("from unittest import TestCase\n"
                             "TestCase.assertNotAlmostEqual(delta=1)"))

  def test_fold_of_datetime_from_datetime(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\ndatetime(fold=1)"))

  def test_tzinfo_of_combine_from_datetime(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\ndatetime.combine(tzinfo=1)"))

  def test_fold_of_replace_from_datetime(self):
    self.assertOnlyIn((3, 6), detect("from datetime import datetime\ndatetime.replace(fold=1)"))

  def test_timespec_of_isoformat_from_datetime(self):
    self.assertOnlyIn((3, 6),
                      detect("from datetime import datetime\ndatetime.isoformat(timespec=1)"))

  def test_fold_of_replace_from_datetime_time(self):
    self.assertOnlyIn((3, 6), detect("from datetime import time\ntime.replace(fold=1)"))

  def test_timespec_of_isoformat_from_datetime_time(self):
    self.assertOnlyIn((3, 6), detect("from datetime import time\ntime.isoformat(timespec=1)"))

  def test_domain_of_Filter_from_tracemalloc(self):
    self.assertOnlyIn((3, 6), detect("import tracemalloc\ntracemalloc.Filter(domain=1)"))

  def test_max_length_of_decompress_from_bz2_BZ2Decompressor(self):
    self.assertOnlyIn((3, 5),
                      detect("from bz2 import BZ2Decompressor\n"
                             "d = BZ2Decompressor()\n"
                             "d.decompress(max_length=1)"))

  def test_max_length_of_decompress_from_lzma(self):
    self.assertOnlyIn((3, 5),
                      detect("from lzma import decompress\n"
                             "decompress(max_length=1)"))

  def test_maxlen_of_deque_from_collections(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import collections\ncollections.deque(maxlen=1)"))

  def test_rename_of_namedtuple_from_collections(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      detect("import collections\ncollections.namedtuple(rename=True)"))

  def test_module_of_namedtuple_from_collections(self):
    self.assertOnlyIn((3, 6), detect("import collections\ncollections.namedtuple(module=None)"))

  def test_defaults_of_namedtuple_from_collections(self):
    self.assertOnlyIn((3, 7), detect("import collections\ncollections.namedtuple(defaults=None)"))

  def test_m_of_ChainMap_new_child_from_collections(self):
    self.assertOnlyIn((3, 4), detect("import collections\ncollections.ChainMap.new_child(m=None)"))

  def test_use_last_error_of_CDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.CDLL(use_last_error=True)"))

  def test_use_errno_of_CDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.CDLL(use_errno=True)"))

  def test_use_last_error_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.OleDLL(use_last_error=True)"))

  def test_use_errno_of_OleDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.OleDLL(use_errno=True)"))

  def test_use_last_error_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.WinDLL(use_last_error=True)"))

  def test_use_errno_of_WinDLL_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.WinDLL(use_errno=True)"))

  def test_use_last_error_of_CFUNCTYPE_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("import ctypes\nctypes.CFUNCTYPE(use_last_error=True)"))

  def test_use_errno_of_CFUNCTYPE_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.CFUNCTYPE(use_errno=True)"))

  def test_offset_of_byref_from_ctypes(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import ctypes\nctypes.byref(offset=3)"))

  def test_autojunk_of_SequenceMatcher_from_difflib(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      detect("import difflib\ndifflib.SequenceMatcher(autojunk=True)"))

  def test_charset_of_make_file_from_difflib(self):
    self.assertOnlyIn((3, 5), detect("from difflib import HtmlDiff\n"
                                     "HtmlDiff.make_file(charset=True)"))

  def test_use_builtin_types_of_SimpleXMLRPCServer_from_xmlrpc_server(self):
    self.assertOnlyIn((3, 3), detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                                     "SimpleXMLRPCServer(use_builtin_types=True)"))

  def test_use_builtin_types_of_CGIXMLRPCRequestHandler_from_xmlrpc_server(self):
    self.assertOnlyIn((3, 3), detect("from xmlrpc.server import CGIXMLRPCRequestHandler\n"
                                     "CGIXMLRPCRequestHandler(use_builtin_types=True)"))

  def test_use_builtin_types_of_DocXMLRPCServer_from_xmlrpc_server(self):
    self.assertOnlyIn((3, 3), detect("from xmlrpc.server import DocXMLRPCServer\n"
                                     "DocXMLRPCServer(use_builtin_types=True)"))

  def test_typed_of_lru_cache_from_functools(self):
    self.assertOnlyIn((3, 3), detect("import functools\nfunctools.lru_cache(typed=3)"))

  def test_key_of_nlargest_from_heapq(self):
    self.assertOnlyIn(((2, 4), (3, 0)), detect("import heapq\nheapq.nlargest(key=3)"))

  def test_key_of_nsmallest_from_heapq(self):
    self.assertOnlyIn(((2, 4), (3, 0)), detect("import heapq\nheapq.nsmallest(key=3)"))

  def test_key_of_merge_from_heapq(self):
    self.assertOnlyIn((3, 5), detect("import heapq\nheapq.merge(key=3)"))

  def test_reverse_of_merge_from_heapq(self):
    self.assertOnlyIn((3, 5), detect("import heapq\nheapq.merge(reverse=True)"))

  def test_follow_wrapped_of_signature_from_inspect(self):
    self.assertOnlyIn((3, 5), detect("import inspect\ninspect.signature(follow_wrapped=True)"))

  def test_write_through_of_TextIOWrapper_from_io(self):
    self.assertOnlyIn((3, 3), detect("import io\nio.TextIOWrapper(write_through=True)"))

  def test_func_of_accumulate_from_itertools(self):
    self.assertOnlyIn((3, 3), detect("import itertools\nitertools.accumulate(func=None)"))

  def test_step_of_count_from_itertools(self):
    self.assertOnlyIn((3, 1), detect("import itertools\nitertools.count(step=None)"))

  def test_object_pairs_hook_of_load_from_json(self):
    self.assertOnlyIn(((2, 7), (3, 1)), detect("import json\njson.load(object_pairs_hook=None)"))

  def test_object_pairs_hook_of_JSONDecoder_from_json(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      detect("import json\njson.JSONDecoder(object_pairs_hook=None)"))

  def test_func_of_makeRecord_from_logging_Logger(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      detect("from logging import Logger\nLogger.makeRecord(func=None)"))

  def test_extra_of_makeRecord_from_logging_Logger(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      detect("from logging import Logger\nLogger.makeRecord(extra=None)"))

  def test_func_of_LogRecord_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      detect("from logging import LogRecord\nLogRecord(func=None)"))

  def test_extra_of_debug_from_logging(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("import logging\nlogging.debug(extra=None)"))

  def test_stack_info_of_debug_from_logging(self):
    self.assertOnlyIn((3, 2), detect("import logging\nlogging.debug(stack_info=None)"))

  def test_style_of_Formatter_from_logging(self):
    self.assertOnlyIn((3, 2), detect("import logging\nlogging.Formatter(style=None)"))

  def test_annotate_of_dis_from_pickletools(self):
    self.assertOnlyIn((3, 2), detect("import pickletools\npickletools.dis(annotate=None)"))

  def test_posix_of_split_from_shlex(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import shlex\nshlex.split(posix=None)"))

  def test_punctuation_chars_of_shlex_from_shlex(self):
    self.assertOnlyIn((3, 6), detect("import shlex\nshlex.shlex(punctuation_chars=None)"))

  def test_allow_none_of_SimpleXMLRPCServer_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                             "SimpleXMLRPCServer(allow_none=True)"))

  def test_encoding_of_SimpleXMLRPCServer_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                             "SimpleXMLRPCServer(encoding=True)"))

  def test_bind_and_active_of_SimpleXMLRPCServer_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 6),
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                             "SimpleXMLRPCServer(bind_and_active=True)"))

  def test_allow_none_of_CGIXMLRPCRequestHandler_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      detect("from SimpleXMLRPCServer import CGIXMLRPCRequestHandler\n"
                             "CGIXMLRPCRequestHandler(allow_none=True)"))

  def test_encoding_of_CGIXMLRPCRequestHandler_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 5),
                      detect("from SimpleXMLRPCServer import CGIXMLRPCRequestHandler\n"
                             "CGIXMLRPCRequestHandler(encoding=True)"))

  def test_allow_dotted_names_of_register_instance_from_SimpleXMLRPCServer(self):
    self.assertOnlyIn((2, 3),
                      detect("from SimpleXMLRPCServer import SimpleXMLRPCServer\n"
                             "srv = SimpleXMLRPCServer()\n"
                             "srv.register_instance(allow_dotted_names=True)"))
    self.assertOnlyIn((3, 0),
                      detect("from xmlrpc.server import SimpleXMLRPCServer\n"
                             "srv = SimpleXMLRPCServer()\n"
                             "srv.register_instance(allow_dotted_names=True)"))

  def test_ciphers_of_wrap_socket_from_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), detect("import ssl\nssl.wrap_socket(ciphers=None)"))

  def test_password_of_load_cert_chain_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 3),
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.load_cert_chain(password=None)"))

  def test_cadata_of_load_verify_locations_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 4),
                      detect("from ssl import SSLContext\n"
                             "ctx = SSLContext()\n"
                             "ctx.load_verify_locations(cadata=None)"))

  def test_encoding_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 6), detect("import subprocess\nsubprocess.run(encoding=None)"))

  def test_errors_of_run_from_subprocess(self):
    self.assertOnlyIn((3, 6), detect("import subprocess\nsubprocess.run(errors=None)"))

  def test_encoding_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 6), detect("import subprocess\nsubprocess.check_output(encoding=None)"))

  def test_errors_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 6), detect("import subprocess\nsubprocess.check_output(errors=None)"))

  def test_text_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 7), detect("import subprocess\nsubprocess.check_output(text=None)"))

  def test_pass_fds_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      detect("from subprocess import Popen\n"
                             "Popen(pass_fds=True)"))

  def test_restore_signals_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      detect("from subprocess import Popen\n"
                             "Popen(restore_signals=True)"))

  def test_start_new_session_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 2),
                      detect("from subprocess import Popen\n"
                             "Popen(start_new_session=True)"))

  def test_encoding_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 6), detect("import subprocess\nsubprocess.Popen(encoding=None)"))

  def test_errors_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 6), detect("import subprocess\nsubprocess.Popen(errors=None)"))

  def test_text_of_Popen_from_subprocess(self):
    self.assertOnlyIn((3, 7), detect("import subprocess\nsubprocess.Popen(text=None)"))

  def test_timeout_of_wait_from_subprocess_Popen(self):
    self.assertOnlyIn((3, 3), detect("from subprocess import Popen\nPopen.wait(timeout=None)"))

  def test_timeout_of_communicate_from_subprocess_Popen(self):
    self.assertOnlyIn((3, 3),
                      detect("from subprocess import Popen\nPopen.communicate(timeout=None)"))

  def test_timeout_of_call_from_subprocess(self):
    self.assertOnlyIn((3, 3), detect("import subprocess\nsubprocess.call(timeout=None)"))

  def test_timeout_of_check_call_from_subprocess(self):
    self.assertOnlyIn((3, 3), detect("import subprocess\nsubprocess.check_call(timeout=None)"))

  def test_timeout_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 3), detect("import subprocess\nsubprocess.check_output(timeout=None)"))

  def test_input_of_check_output_from_subprocess(self):
    self.assertOnlyIn((3, 4), detect("import subprocess\nsubprocess.check_output(input=None)"))

  def test_exclude_of_add_from_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("from tarfile import TarFile\ntf = TarFile()\ntf.add(exclude=None)"))

  def test_filter_of_add_from_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      detect("from tarfile import TarFile\ntf = TarFile()\ntf.add(filter=None)"))

  def test_format_of_tobuf_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("from tarfile import TarInfo\ntf = TarInfo()\ntf.tobuf(format=None)"))

  def test_encoding_of_tobuf_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("from tarfile import TarInfo\n"
                             "tf = TarInfo()\n"
                             "tf.tobuf(encoding=None)"))

  def test_errors_of_tobuf_from_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("from tarfile import TarInfo\ntf = TarInfo()\ntf.tobuf(errors=None)"))

  def test_members_of_list_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 5),
                      detect("from tarfile import TarFile\ntf = TarFile()\ntf.list(members=None)"))

  def test_numeric_owner_of_extractall_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 5),
                      detect("from tarfile import TarFile\n"
                             "tf = TarFile()\n"
                             "tf.extractall(numeric_owner=None)"))

  def test_set_attrs_of_extract_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 2),
                      detect("from tarfile import TarFile\n"
                             "tf = TarFile()\n"
                             "tf.extract(set_attrs=None)"))

  def test_numeric_owner_of_extract_from_tarfile_TarFile(self):
    self.assertOnlyIn((3, 5),
                      detect("from tarfile import TarFile\n"
                             "tf = TarFile()\n"
                             "tf.extract(numeric_owner=None)"))

  def test_module_globals_of_warn_explicit_from_warnings(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      detect("import warnings\nwarnings.warn_explicit(module_globals=None)"))

  def test_line_of_formatwarning_from_warnings(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("import warnings\nwarnings.formatwarning(line=None)"))

  def test_source_of_warn_explicit_from_warnings(self):
    self.assertOnlyIn((3, 6),
                      detect("import warnings\nwarnings.warn_explicit(source=None)"))

  def test_source_of_warn_from_warnings(self):
    self.assertOnlyIn((3, 6),
                      detect("import warnings\nwarnings.warn(source=None)"))

  def test_parser_of_iterparse_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.iterparse(parser=None)"))

  def test_short_empty_elements_of_tostring_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.tostring(short_empty_elements=None)"))

  def test_xml_declaration_of_tostring_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.tostring(xml_declaration=None)"))

  def test_default_namespace_of_tostring_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.tostring(default_namespace=None)"))

  def test_short_empty_elements_of_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.tostringlist(short_empty_elements=None)"))

  def test_xml_declaration_of_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.tostringlist(xml_declaration=None)"))

  def test_default_namespace_of_tostringlist_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 8),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.tostringlist(default_namespace=None)"))

  def test_short_empty_elements_of_write_from_xml_etree_ElementTree(self):
    self.assertOnlyIn((3, 4),
                      detect("from xml.etree import ElementTree\n"
                             "ElementTree.write(short_empty_elements=None)"))

  def test_use_datetime_of_ServerProxy_from_xmlrpclib_ServerProxy(self):
    self.assertOnlyIn((2, 5),
                      detect("from xmlrpclib import ServerProxy\n"
                             "ServerProxy(use_datetime=None)"))

  def test_context_of_ServerProxy_from_xmlrpclib_ServerProxy(self):
    self.assertOnlyIn((2, 7),
                      detect("from xmlrpclib import ServerProxy\n"
                             "ServerProxy(context=None)"))

  def test_use_datetime_of_loads_from_xmlrpclib(self):
    self.assertOnlyIn((2, 5),
                      detect("import xmlrpclib\n"
                             "xmlrpclib.loads(use_datetime=None)"))

  def test_pwd_of_read_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      detect("from zipfile import ZipFile\n"
                             "zf = ZipFile()\n"
                             "zf.read(pwd=None)"))

  def test_compress_type_of_writestr_from_zipfile_ZipFile(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      detect("from zipfile import ZipFile\n"
                             "zf = ZipFile()\n"
                             "zf.writestr(compress_type=None)"))

  def test_filterfunc_of_writepy_from_zipfile_PyZipFile(self):
    self.assertOnlyIn((3, 4),
                      detect("from zipfile import PyZipFile\n"
                             "zf = PyZipFile()\n"
                             "zf.writepy(filterfunc=None)"))

  def test_optimize_of_PyZipFile_from_zipfile(self):
    self.assertOnlyIn((3, 2),
                      detect("from zipfile import PyZipFile\n"
                             "PyZipFile(optimize=None)"))

  def test_unsafe_of_Mock_from_unittest_mock(self):
    self.assertOnlyIn((3, 5),
                      detect("from unittest.mock import Mock\n"
                             "Mock(unsafe=False)"))

  def test_with_pip_of_EnvBuilder_from_venv(self):
    self.assertOnlyIn((3, 4),
                      detect("from venv import EnvBuilder\n"
                             "EnvBuilder(with_pip=False)"))

  def test_with_pip_of_create_from_venv(self):
    self.assertOnlyIn((3, 4),
                      detect("from venv import create\n"
                             "create(with_pip=False)"))

  def test_prompt_of_EnvBuilder_from_venv(self):
    self.assertOnlyIn((3, 6),
                      detect("from venv import EnvBuilder\n"
                             "EnvBuilder(prompt=False)"))

  def test_flags_of_compile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("compile(flags=None)"))

  def test_dont_inherit_of_compile(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("compile(dont_inherit=None)"))

  def test_optimize_of_compile(self):
    self.assertOnlyIn((3, 2), detect("compile(optimize=None)"))

  def test_start_of_enumerate(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("enumerate(start=None)"))

  def test_key_of_max(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("max(key=None)"))

  def test_default_of_max(self):
    self.assertOnlyIn((3, 4), detect("max(default=None)"))

  def test_key_of_min(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("min(key=None)"))

  def test_default_of_min(self):
    self.assertOnlyIn((3, 4), detect("min(default=None)"))

  def test_level_of___import__(self):
    self.assertOnlyIn(((2, 5), (3, 0)), detect("__import__(level=None)"))

  def test_opener_of_open(self):
    self.assertOnlyIn((3, 3), detect("open(opener=None)"))

  def test_flush_of_print(self):
    # `print()` is not a function in v2.
    if current_major_version() >= 3:
      self.assertOnlyIn((3, 3), detect("print(flush=None)"))

  def test_policy_of_email_mime_base_MIMEBase(self):
    self.assertOnlyIn((3, 6), detect("from email.mime.base import MIMEBase\nMIMEBase(policy=None)"))

  def test_policy_of_email_mime_multipart_MIMEMultipart(self):
    self.assertOnlyIn((3, 6),
                      detect("from email.mime.multipart import MIMEMultipart\n"
                             "MIMEMultipart(policy=None)"))

  def test_policy_of_email_mime_application_MIMEApplication(self):
    self.assertOnlyIn((3, 6),
                      detect("from email.mime.application import MIMEApplication\n"
                             "MIMEApplication(policy=None)"))

  def test_policy_of_email_mime_audio_MIMEAudio(self):
    self.assertOnlyIn((3, 6),
                      detect("from email.mime.audio import MIMEAudio\nMIMEAudio(policy=None)"))

  def test_policy_of_email_mime_image_MIMEImage(self):
    self.assertOnlyIn((3, 6),
                      detect("from email.mime.image import MIMEImage\nMIMEImage(policy=None)"))

  def test_policy_of_email_mime_message_MIMEMessage(self):
    self.assertOnlyIn((3, 6),
                      detect("from email.mime.message import MIMEMessage\n"
                             "MIMEMessage(policy=None)"))

  def test_policy_of_email_mime_text_MIMEText(self):
    self.assertOnlyIn((3, 6), detect("from email.mime.text import MIMEText\nMIMEText(policy=None)"))

  def test_domain_of_email_utils_make_msgid(self):
    self.assertOnlyIn((3, 2), detect("import email.utils\nemail.utils.make_msgid(domain=None)"))

  def test_charset_of_email_utils_formatdate(self):
    self.assertOnlyIn((3, 3), detect("import email.utils\nemail.utils.formatdate(charset=None)"))

  def test_strict_of_email_message_from_string(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      detect("import email\nemail.message_from_string(strict=None)"))

  def test_strict_of_email_message_from_file(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      detect("import email\nemail.message_from_file(strict=None)"))

  def test_policy_of_email_parser_BytesFeedParser(self):
    self.assertOnlyIn((3, 3),
                      detect("from email.parser import BytesFeedParser\n"
                             "BytesFeedParser(policy=None)"))

  def test_policy_of_email_parser_FeedParser(self):
    self.assertOnlyIn((3, 3),
                      detect("from email.parser import FeedParser\n"
                             "FeedParser(policy=None)"))

  def test_policy_of_email_generator_BytesGenerator(self):
    self.assertOnlyIn((3, 3),
                      detect("from email.generator import BytesGenerator\n"
                             "BytesGenerator(policy=None)"))

  def test_policy_of_email_generator_Generator(self):
    self.assertOnlyIn((3, 3),
                      detect("from email.generator import Generator\n"
                             "Generator(policy=None)"))

  def test_linesep_of_email_generator_Generator_flatten(self):
    self.assertOnlyIn((3, 2),
                      detect("from email.generator import Generator\n"
                             "g=Generator()\ng.flatten(linesep=None)"))

  def test_linesep_of_email_header_Header_encode(self):
    self.assertOnlyIn((3, 2),
                      detect("from email.header import Header\n"
                             "g=Header()\ng.encode(linesep=None)"))

  def test_base_of_math_log(self):
    self.assertOnlyIn(((2, 3), (3, 0)), detect("import math\nmath.log(base=None)"))

  def test_exit_ok_of_path_mkdir(self):
    self.assertOnlyIn(
      (3, 5), detect("from pathlib import Path\np=Path('foo')\np.mkdir(exist_ok=True)"))

  def test_strict_of_path_resolve(self):
    self.assertOnlyIn(
      (3, 6), detect("from pathlib import Path\np=Path('foo')\np.resolve(strict=True)"))

  def test_optimization_of_importlib_util_cache_from_source(self):
    self.assertOnlyIn((3, 5),
                      detect("from importlib.util import cache_from_source\n"
                             "cache_from_source(optimization=None)"))

  def test_allow_abbrev_of_argparse_ArgumentParser(self):
    self.assertOnlyIn((3, 5), detect("import argparse\nargparse.ArgumentParser(allow_abbrev=True)"))

  def test_skip_of_bdb_Bdb(self):
    self.assertOnlyIn((3, 1), detect("import bdb\nbdb.Bdb(skip=True)"))

  def test_backtick_of_binascii_b2a_uu(self):
    self.assertOnlyIn((3, 7), detect("import binascii\nbinascii.b2a_uu(backtick=True)"))

  def test_newline_of_binascii_b2a_base64(self):
    self.assertOnlyIn((3, 6), detect("import binascii\nbinascii.b2a_base64(newline=True)"))

  def test_encoding_of_cgi_parse_multipart(self):
    self.assertOnlyIn((3, 7), detect("import cgi\ncgi.parse_multipart(encoding='utf-8')"))

  def test_errors_of_cgi_parse_multipart(self):
    self.assertOnlyIn((3, 7), detect("import cgi\ncgi.parse_multipart(errors='utf-8')"))

  def test_exitmsg_of_code_interact(self):
    self.assertOnlyIn((3, 6), detect("import code\ncode.interact(exitmsg='hello')"))

  def test_legacy_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 2), detect("import compileall\ncompileall.compile_dir(legacy='hello')"))

  def test_optimize_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 2), detect("import compileall\ncompileall.compile_dir(optimize='hello')"))

  def test_invalidation_mode_of_compileall_compile_dir(self):
    self.assertOnlyIn((3, 7),
                      detect("import compileall\n"
                             "compileall.compile_dir(invalidation_mode='hello')"))

  def test_legacy_of_compileall_compile_path(self):
    self.assertOnlyIn((3, 2), detect("import compileall\ncompileall.compile_path(legacy='hello')"))

  def test_optimize_of_compileall_compile_path(self):
    self.assertOnlyIn((3, 2),
                      detect("import compileall\ncompileall.compile_path(optimize='hello')"))

  def test_invalidation_mode_of_compileall_compile_path(self):
    self.assertOnlyIn((3, 7),
                      detect("import compileall\n"
                             "compileall.compile_path(invalidation_mode='hello')"))

  def test_invalidation_mode_of_compileall_compile_file(self):
    self.assertOnlyIn((3, 7),
                      detect("import compileall\n"
                             "compileall.compile_file(invalidation_mode='hello')"))

  def test_chunksize_of_concurrent_futures_Executor(self):
    self.assertOnlyIn((3, 5),
                      detect("from concurrent.futures import Executor\n"
                             "Executor(chunksize=123)"))

  def test_thread_name_prefix_of_concurrent_futures_ThreadPoolExecutor(self):
    self.assertOnlyIn((3, 6),
                      detect("from concurrent.futures import ThreadPoolExecutor\n"
                             "ThreadPoolExecutor(thread_name_prefix='123')"))

  def test_initializer_of_concurrent_futures_ThreadPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      detect("from concurrent.futures import ThreadPoolExecutor\n"
                             "ThreadPoolExecutor(initializer='123')"))

  def test_initargs_of_concurrent_futures_ThreadPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      detect("from concurrent.futures import ThreadPoolExecutor\n"
                             "ThreadPoolExecutor(initargs=0)"))

  def test_mp_context_of_concurrent_futures_ProcessPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      detect("from concurrent.futures import ProcessPoolExecutor\n"
                             "ProcessPoolExecutor(mp_context='123')"))

  def test_initializer_of_concurrent_futures_ProcessPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      detect("from concurrent.futures import ProcessPoolExecutor\n"
                             "ProcessPoolExecutor(initializer='123')"))

  def test_initargs_of_concurrent_futures_ProcessPoolExecutor(self):
    self.assertOnlyIn((3, 7),
                      detect("from concurrent.futures import ProcessPoolExecutor\n"
                             "ProcessPoolExecutor(initargs=0)"))

  def test_rounds_of_crypt_mksalt(self):
    self.assertOnlyIn((3, 7), detect("import crypt\ncrypt.mksalt(rounds=8)"))

  def test_file_of_dis_show_code(self):
    self.assertOnlyIn((3, 4), detect("import dis\ndis.show_code(file=8)"))

  def test_file_of_dis_dis(self):
    self.assertOnlyIn((3, 4), detect("import dis\ndis.dis(file=8)"))

  def test_depth_of_dis_dis(self):
    self.assertOnlyIn((3, 7), detect("import dis\ndis.dis(depth=8)"))

  def test_file_of_dis_distb(self):
    self.assertOnlyIn((3, 4), detect("import dis\ndis.distb(file=8)"))

  def test_file_of_dis_disco(self):
    self.assertOnlyIn((3, 4), detect("import dis\ndis.disco(file=8)"))

  def test_file_of_dis_disassemble(self):
    self.assertOnlyIn((3, 4), detect("import dis\ndis.disassemble(file=8)"))

  def test_mtime_of_gzip_compress(self):
    self.assertOnlyIn((3, 8), detect("import gzip\ngzip.compress(mtime=8)"))

  def test_encoding_of_gzip_open(self):
    self.assertOnlyIn((3, 3), detect("import gzip\ngzip.open(encoding='utf-8')"))

  def test_errors_of_gzip_open(self):
    self.assertOnlyIn((3, 3), detect("import gzip\ngzip.open(errors=True)"))

  def test_newline_of_gzip_open(self):
    self.assertOnlyIn((3, 3), detect("import gzip\ngzip.open(newline=None)"))

  def test_encoding_of_str_decode(self):
    self.assertOnlyIn((2, 7), detect("'test'.decode(encoding=None)"))

  def test_errors_of_str_decode(self):
    self.assertOnlyIn((2, 7), detect("'test'.decode(errors=None)"))

  def test_encoding_of_str_encode(self):
    self.assertOnlyIn(((2, 7), (3, 1)), detect("'test'.encode(encoding=None)"))

  def test_errors_of_str_encode(self):
    self.assertOnlyIn(((2, 7), (3, 1)), detect("'test'.encode(errors=None)"))

  def test_filter_of_zipapp_create_archive(self):
    self.assertOnlyIn((3, 7), detect("import zipapp\nzipapp.create_archive(filter=None)"))

  def test_compressed_of_zipapp_create_archive(self):
    self.assertOnlyIn((3, 7), detect("import zipapp\nzipapp.create_archive(compressed=True)"))

  def test_timeout_of_smtplib_SMTP(self):
    self.assertOnlyIn(((2, 6), (3, 0)), detect("import smtplib\nsmtplib.SMTP(timeout=1)"))

  def test_source_address_of_smtplib_SMTP(self):
    self.assertOnlyIn((3, 3), detect("import smtplib\nsmtplib.SMTP(source_address=1)"))

  def test_source_address_of_smtplib_SMTP_SSL(self):
    self.assertOnlyIn((3, 3), detect("import smtplib\nsmtplib.SMTP_SSL(source_address=1)"))

  def test_context_of_smtplib_SMTP_SSL(self):
    self.assertOnlyIn((3, 3), detect("import smtplib\nsmtplib.SMTP_SSL(context=1)"))

  def test_context_of_smtplib_SMTP_starttls(self):
    self.assertOnlyIn((3, 3), detect("import smtplib\nsmtplib.SMTP.starttls(context=1)"))

  def test_capture_output_of_subprocess_run(self):
    self.assertOnlyIn((3, 7), detect("import subprocess\nsubprocess.run(capture_output=1)"))

  def test_lpAttributeList_of_subprocess_STARTUPINFO(self):
    self.assertOnlyIn((3, 7),
                      detect("import subprocess\nsubprocess.STARTUPINFO(lpAttributeList=1)"))
