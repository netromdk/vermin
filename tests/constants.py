from .testutils import VerminTest

class VerminConstantMemberTests(VerminTest):
  def test_name_of_AttributeError(self):
    self.assertOnlyIn((3, 10), self.detect("AttributeError.name"))

  def test_obj_of_AttributeError(self):
    self.assertOnlyIn((3, 10), self.detect("AttributeError.obj"))

  def test___suppress_context___of_BaseException(self):
    self.assertOnlyIn((3, 3), self.detect("BaseException.__suppress_context__"))

  def test_name_of_ImportError(self):
    self.assertOnlyIn((3, 3), self.detect("ImportError.name"))

  def test_path_of_ImportError(self):
    self.assertOnlyIn((3, 3), self.detect("ImportError.path"))

  def test_name_of_NameError(self):
    self.assertOnlyIn((3, 10), self.detect("NameError.name"))

  def test_filename2_of_OSError(self):
    self.assertOnlyIn((3, 4), self.detect("OSError.filename2"))

  def test_value_of_StopIteration(self):
    self.assertOnlyIn((3, 3), self.detect("StopIteration.value"))

  def test_end_lineno_of_SyntaxError(self):
    self.assertOnlyIn((3, 10), self.detect("SyntaxError.end_lineno"))

  def test_end_offset_of_SyntaxError(self):
    self.assertOnlyIn((3, 10), self.detect("SyntaxError.end_offset"))

  def test___wrapped___of_classmethod(self):
    self.assertOnlyIn((3, 10), self.detect("classmethod.__wrapped__"))

  def test___wrapped___of_staticmethod(self):
    self.assertOnlyIn((3, 10), self.detect("staticmethod.__wrapped__"))

  def test___match_args___of_object(self):
    self.assertOnlyIn((3, 10), self.detect("object.__match_args__"))

  def test_encoding_of_file(self):
    self.assertOnlyIn((2, 3), self.detect("file.encoding"))

  def test_errors_of_file(self):
    self.assertOnlyIn((2, 6), self.detect("file.errors"))

  def test_start_of_range(self):
    self.assertOnlyIn((3, 3), self.detect("range.start"))

  def test_step_of_range(self):
    self.assertOnlyIn((3, 3), self.detect("range.step"))

  def test_stop_of_range(self):
    self.assertOnlyIn((3, 3), self.detect("range.stop"))

  def test_flags_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from sys import flags"))

  def test_supports_unicode_filenames_of_os_path(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect(
        "from os.path import supports_unicode_filenames"))

  def test_supports_bytes_environ_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import supports_bytes_environ"))

  def test_environb_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import environb"))

  def test_PRIO_PROCESS_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import PRIO_PROCESS"))

  def test_PRIO_PGRP_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import PRIO_PGRP"))

  def test_PRIO_USER_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import PRIO_USER"))

  def test_F_LOCK_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import F_LOCK"))

  def test_F_TLOCK_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import F_TLOCK"))

  def test_F_ULOCK_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import F_ULOCK"))

  def test_F_TEST_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import F_TEST"))

  def test_O_CLOEXEC_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import O_CLOEXEC"))

  def test_O_PATH_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import O_PATH"))

  def test_O_TMPFILE_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import O_TMPFILE"))

  def test_O_EVTONLY_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import O_EVTONLY"))

  def test_O_FSYNC_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import O_FSYNC"))

  def test_O_SYMLINK_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import O_SYMLINK"))

  def test_O_NOFOLLOW_ANY_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import O_NOFOLLOW_ANY"))

  def test_POSIX_FADV_NORMAL_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import POSIX_FADV_NORMAL"))

  def test_POSIX_FADV_SEQUENTIAL_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import POSIX_FADV_SEQUENTIAL"))

  def test_POSIX_FADV_RANDOM_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import POSIX_FADV_RANDOM"))

  def test_POSIX_FADV_NOREUSE_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import POSIX_FADV_NOREUSE"))

  def test_POSIX_FADV_WILLNEED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import POSIX_FADV_WILLNEED"))

  def test_POSIX_FADV_DONTNEED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import POSIX_FADV_DONTNEED"))

  def test_SF_NODISKIO_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SF_NODISKIO"))

  def test_SF_MNOWAIT_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SF_MNOWAIT"))

  def test_SF_SYNC_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SF_SYNC"))

  def test_float_info_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from sys import float_info"))

  def test_float_repr_style_of_sys(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from sys import float_repr_style"))

  def test_long_info_of_sys(self):
    self.assertOnlyIn((2, 7), self.detect("from sys import long_info"))

  def test_py3kwarning_of_sys(self):
    self.assertOnlyIn((2, 6), self.detect("from sys import py3kwarning"))

  def test_subversion_of_sys(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from sys import subversion"))

  def test_api_version_of_sys(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from sys import api_version"))

  def test_version_info_of_sys(self):
    self.assertOnlyIn(((2, 0), (3, 0)), self.detect("from sys import version_info"))

  def test_sentinel_of_multiprocessing_Process(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from multiprocessing import Process\np = Process()\np.sentinel"))

  def test_skipped_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestResult\np = TestResult()\np.skipped"))

  def test_buffer_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestResult\np = TestResult()\np.buffer"))

  def test_failfast_of_unittest_TestResult(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestResult\np = TestResult()\np.failfast"))

  def test_fold_of_datetime_datetime(self):
    self.assertOnlyIn((3, 6), self.detect("from datetime import datetime\np = datetime()\np.fold"))

  def test_fold_of_datetime_time(self):
    self.assertOnlyIn((3, 6), self.detect("from datetime import time\np = time()\np.fold"))

  def test_algorithms_of_hashlib(self):
    self.assertOnlyIn((2, 7), self.detect("from hashlib import algorithms"))

  def test_algorithms_available_of_hashlib(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from hashlib import algorithms_available"))

  def test_algorithms_guaranteed_of_hashlib(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from hashlib import algorithms_guaranteed"))

  def test_reverse_pointer_of_ipaddress_IPv4Address(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from ipaddress import IPv4Address\n"
                                  "addr = IPv4Address('127.0.0.1')\n"
                                  "addr.reverse_pointer"))
    self.assertTrue(self.config.add_backport("ipaddress"))
    self.assertOnlyIn(((2, 6), (3, 2)),
                      self.detect("from ipaddress import IPv4Address\n"
                                  "addr = IPv4Address('127.0.0.1')\n"
                                  "addr.reverse_pointer"))

  def test_is_global_of_ipaddress_IPv4Address(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from ipaddress import IPv4Address\n"
                                  "addr = IPv4Address('127.0.0.1')\n"
                                  "addr.is_global"))
    self.assertTrue(self.config.add_backport("ipaddress"))
    self.assertOnlyIn(((2, 6), (3, 2)),
                      self.detect("from ipaddress import IPv4Address\n"
                                  "addr = IPv4Address('127.0.0.1')\n"
                                  "addr.is_global"))

  def test_is_global_of_ipaddress_IPv6Address(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from ipaddress import IPv6Address\n"
                                  "addr = IPv6Address(':::1')\n"
                                  "addr.is_global"))
    self.assertTrue(self.config.add_backport("ipaddress"))
    self.assertOnlyIn(((2, 6), (3, 2)),
                      self.detect("from ipaddress import IPv6Address\n"
                                  "addr = IPv6Address(':::1')\n"
                                  "addr.is_global"))

  def test_nested_scopes_of___future__(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from __future__ import nested_scopes"))

  def test_generators_of___future__(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from __future__ import generators"))

  def test_division_of___future__(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from __future__ import division"))

  def test_absolute_import_of___future__(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from __future__ import absolute_import"))

  def test_with_statement_of___future__(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from __future__ import with_statement"))

  def test_print_function_of___future__(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from __future__ import print_function"))

  def test_unicode_literals_of___future__(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from __future__ import unicode_literals"))

  def test_generator_stop_of___future__(self):
    self.assertOnlyIn((3, 5), self.detect("from __future__ import generator_stop"))

  def test_PyCF_ALLOW_TOP_LEVEL_AWAIT_of_ast(self):
    self.assertOnlyIn((3, 8), self.detect("from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT"))

  def test_PyCF_TYPE_COMMENTS_of_ast(self):
    self.assertOnlyIn((3, 8), self.detect("from ast import PyCF_TYPE_COMMENTS"))

  def test_eof_of_bz2_BZ2Decompressor(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from bz2 import BZ2Decompressor\nd = BZ2Decompressor()\nd.eof"))

  def test_needs_input_of_bz2_BZ2Decompressor(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from bz2 import BZ2Decompressor\n"
                                  "d = BZ2Decompressor()\n"
                                  "d.needs_input"))

  def test_maxlen_of_collections_deque(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from collections import deque\nd = deque()\nd.maxlen"))

  def test_block_size_of_hmac_HMAC(self):
    self.assertOnlyIn((3, 4), self.detect("from hmac import HMAC\nd = HMAC()\nd.block_size"))

  def test_name_of_hmac_HMAC(self):
    self.assertOnlyIn((3, 4), self.detect("from hmac import HMAC\nd = HMAC()\nd.name"))

  def test_CO_COROUTINE_of_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.CO_COROUTINE"))

  def test_CO_ITERABLE_COROUTINE_of_inspect(self):
    self.assertOnlyIn((3, 5), self.detect("import inspect\ninspect.CO_ITERABLE_COROUTINE"))

  def test_CO_ASYNC_GENERATOR_of_inspect(self):
    self.assertOnlyIn((3, 6), self.detect("import inspect\ninspect.CO_ASYNC_GENERATOR"))

  def test_lastResort_of_logging(self):
    self.assertOnlyIn((3, 2), self.detect("import logging\nlogging.lastResort"))

  def test_rpc_paths_of_SimpleXMLRPCServer_SimpleXMLRPCRequestHandler(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler\n"
                                  "SimpleXMLRPCRequestHandler.rpc_paths"))
    self.assertOnlyIn((3, 0),
                      self.detect("from xmlrpc.server import SimpleXMLRPCRequestHandler\n"
                                  "SimpleXMLRPCRequestHandler.rpc_paths"))

  def test_encode_threshold_of_SimpleXMLRPCServer_SimpleXMLRPCRequestHandler(self):
    self.assertOnlyIn((2, 7),
                      self.detect("from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler\n"
                                  "SimpleXMLRPCRequestHandler.encode_threshold"))

  def test_library_of_ssl_SSLError(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import SSLError\nSSLError.library"))

  def test_reason_of_ssl_SSLError(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import SSLError\nSSLError.reason"))

  def test_VERIFY_DEFAULT_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import VERIFY_DEFAULT"))

  def test_VERIFY_CRL_CHECK_LEAF_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import VERIFY_CRL_CHECK_LEAF"))

  def test_VERIFY_CRL_CHECK_CHAIN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import VERIFY_CRL_CHECK_CHAIN"))

  def test_VERIFY_X509_STRICT_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import VERIFY_X509_STRICT"))

  def test_VERIFY_X509_TRUSTED_FIRST_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import VERIFY_X509_TRUSTED_FIRST"))

  def test_VERIFY_X509_PARTIAL_CHAIN_of_ssl(self):
    self.assertOnlyIn((3, 10), self.detect("from ssl import VERIFY_X509_PARTIAL_CHAIN"))

  def test_VERIFY_ALLOW_PROXY_CERTS_of_ssl(self):
    self.assertOnlyIn((3, 10), self.detect("from ssl import VERIFY_ALLOW_PROXY_CERTS"))

  def test_PROTOCOL_TLS_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 6)), self.detect("from ssl import PROTOCOL_TLS"))

  def test_PROTOCOL_TLSv1_1_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import PROTOCOL_TLSv1_1"))

  def test_PROTOCOL_TLSv1_2_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import PROTOCOL_TLSv1_2"))

  def test_OP_ALL_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OP_ALL"))

  def test_OP_NO_SSLv2_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OP_NO_SSLv2"))

  def test_OP_NO_SSLv3_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OP_NO_SSLv3"))

  def test_OP_NO_TLSv1_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OP_NO_TLSv1"))

  def test_OP_NO_TLSv1_1_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import OP_NO_TLSv1_1"))

  def test_OP_NO_TLSv1_2_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import OP_NO_TLSv1_2"))

  def test_OP_NO_TLSv1_3_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 6)), self.detect("from ssl import OP_NO_TLSv1_3"))

  def test_OP_CIPHER_SERVER_PREFERENCE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import OP_CIPHER_SERVER_PREFERENCE"))

  def test_OP_SINGLE_DH_USE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import OP_SINGLE_DH_USE"))

  def test_OP_SINGLE_ECDH_USE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import OP_SINGLE_ECDH_USE"))

  def test_OP_NO_COMPRESSION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import OP_NO_COMPRESSION"))

  def test_OP_NO_TICKET_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import OP_NO_TICKET"))

  def test_OP_IGNORE_UNEXPECTED_EOF_of_ssl(self):
    self.assertOnlyIn((3, 10), self.detect("from ssl import OP_IGNORE_UNEXPECTED_EOF"))

  def test_HAS_ALPN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 5)), self.detect("from ssl import HAS_ALPN"))

  def test_HAS_ECDH_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import HAS_ECDH"))

  def test_HAS_SNI_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import HAS_SNI"))

  def test_HAS_NPN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import HAS_NPN"))

  def test_HAS_TLSv1_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import HAS_TLSv1"))

  def test_HAS_TLSv1_1_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import HAS_TLSv1_1"))

  def test_HAS_TLSv1_2_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import HAS_TLSv1_2"))

  def test_HAS_TLSv1_3_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 7)), self.detect("from ssl import HAS_TLSv1_3"))

  def test_HAS_NEVER_CHECK_COMMON_NAME_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import HAS_NEVER_CHECK_COMMON_NAME"))

  def test_CHANNEL_BINDING_TYPES_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from ssl import CHANNEL_BINDING_TYPES"))

  def test_OPENSSL_VERSION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OPENSSL_VERSION"))

  def test_OPENSSL_VERSION_INFO_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OPENSSL_VERSION_INFO"))

  def test_OPENSSL_VERSION_NUMBER_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import OPENSSL_VERSION_NUMBER"))

  def test_context_of_ssl_SSLSocket(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from ssl import SSLSocket\nSSLSocket.context"))

  def test_server_side_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 2), self.detect("from ssl import SSLSocket\nSSLSocket.server_side"))

  def test_server_hostname_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 2), self.detect("from ssl import SSLSocket\nSSLSocket.server_hostname"))

  def test_session_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import SSLSocket\nSSLSocket.session"))

  def test_session_reused_of_ssl_SSLSocket(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import SSLSocket\nSSLSocket.session_reused"))

  def test_check_hostname_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 4), self.detect("from ssl import SSLContext\nSSLContext.check_hostname"))

  def test_security_level_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 10), self.detect("from ssl import SSLContext\nSSLContext.security_level"))

  def test_verify_flags_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 4), self.detect("from ssl import SSLContext\nSSLContext.verify_flags"))

  def test_post_handshake_auth_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 8), self.detect(
        "from ssl import SSLContext\nSSLContext.post_handshake_auth"))

  def test_hostname_checks_common_name_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7), self.detect(
      "from ssl import SSLContext\nSSLContext.hostname_checks_common_name"))

  def test_keylog_filename_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 8), self.detect("from ssl import SSLContext\nSSLContext.keylog_filename"))

  def test_num_tickets_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 8), self.detect("from ssl import SSLContext\nSSLContext.num_tickets"))

  def test_maximum_version_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import SSLContext\nSSLContext.maximum_version"))

  def test_minimum_version_of_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import SSLContext\nSSLContext.minimum_version"))

  def test_DEVNULL_of_subprocess(self):
    self.assertOnlyIn((3, 3), self.detect("from subprocess import DEVNULL"))

  def test_pax_headers_of_tarfile_TarFile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from tarfile import TarFile\nTarFile.pax_headers"))

  def test_pax_headers_of_tarfile_TarInfo(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect(
        "from tarfile import TarInfo\nTarInfo.pax_headers"))

  def test_args_of_subprocess_Popen(self):
    self.assertOnlyIn((3, 3), self.detect("from subprocess import Popen\nPopen.args"))

    # In this test "args" cannot be matched as "subprocess.Popen.args" constant (as above)!
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("import subprocess\nargs=[]\nsubprocess.Popen(args)"))

  def test_ZIP_BZIP2_of_zipfile(self):
    self.assertOnlyIn((3, 3), self.detect("import zipfile\nzipfile.ZIP_BZIP2"))

  def test_ZIP_LZMA_of_zipfile(self):
    self.assertOnlyIn((3, 3), self.detect("import zipfile\nzipfile.ZIP_LZMA"))

  def test_METHOD_SHA512_of_crypt(self):
    self.assertOnlyIn((3, 3), self.detect("import crypt\ncrypt.METHOD_SHA512"))

  def test_METHOD_SHA256_of_crypt(self):
    self.assertOnlyIn((3, 3), self.detect("import crypt\ncrypt.METHOD_SHA256"))

  def test_METHOD_MD5_of_crypt(self):
    self.assertOnlyIn((3, 3), self.detect("import crypt\ncrypt.METHOD_MD5"))

  def test_METHOD_CRYPT_of_crypt(self):
    self.assertOnlyIn((3, 3), self.detect("import crypt\ncrypt.METHOD_CRYPT"))

  def test_METHOD_BLOWFISH_of_crypt(self):
    self.assertOnlyIn((3, 7), self.detect("import crypt\ncrypt.METHOD_BLOWFISH"))

  def test_methods_of_crypt(self):
    self.assertOnlyIn((3, 3), self.detect("import crypt\ncrypt.methods"))

  def test_tau_of_math(self):
    self.assertOnlyIn((3, 6), self.detect("import math\nmath.tau"))

  def test_inf_of_math(self):
    self.assertOnlyIn((3, 5), self.detect("import math\nmath.inf"))

  def test_nan_of_math(self):
    self.assertOnlyIn((3, 5), self.detect("import math\nmath.nan"))

  def test_SOURCE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect(
        "from importlib import machinery\nmachinery.SOURCE_SUFFIXES"))

  def test_DEBUG_BYTECODE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3), self.detect(
      "from importlib import machinery\nmachinery.DEBUG_BYTECODE_SUFFIXES"))

  def test_OPTIMIZED_BYTECODE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from importlib import machinery\n"
                                  "machinery.OPTIMIZED_BYTECODE_SUFFIXES"))

  def test_BYTECODE_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from importlib import machinery\nmachinery.BYTECODE_SUFFIXES"))

  def test_EXTENSION_SUFFIXES_of_importlib_machinery(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from importlib import machinery\nmachinery.EXTENSION_SUFFIXES"))

  def test_json_from_importlib_metadata_metadata(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from importlib.metadata import metadata\n"
                                  "metadata().json"))

  def test_MAGIC_NUMBER_of_importlib_util(self):
    self.assertOnlyIn((3, 4), self.detect("from importlib import util\nutil.MAGIC_NUMBER"))

  def test_CLOCK_BOOTTIME_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import CLOCK_BOOTTIME"))

  def test_CLOCK_HIGHRES_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import CLOCK_HIGHRES"))

  def test_CLOCK_MONOTONIC_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import CLOCK_MONOTONIC"))

  def test_CLOCK_MONOTONIC_RAW_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import CLOCK_MONOTONIC_RAW"))

  def test_CLOCK_PROCESS_CPUTIME_ID_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import CLOCK_PROCESS_CPUTIME_ID"))

  def test_CLOCK_THREAD_CPUTIME_ID_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import CLOCK_THREAD_CPUTIME_ID"))

  def test_CLOCK_PROF_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import CLOCK_PROF"))

  def test_CLOCK_UPTIME_of_time(self):
    self.assertOnlyIn((3, 7), self.detect("from time import CLOCK_UPTIME"))

  def test_CLOCK_UPTIME_RAW_of_time(self):
    self.assertOnlyIn((3, 8), self.detect("from time import CLOCK_UPTIME_RAW"))

  def test_CLOCK_REALTIME_of_time(self):
    self.assertOnlyIn((3, 3), self.detect("from time import CLOCK_REALTIME"))

  def test_CLOCK_TAI_of_time(self):
    self.assertOnlyIn((3, 9), self.detect("from time import CLOCK_TAI"))

  def test_cssclass_noday_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from calendar import HTMLCalendar\n"
                                  "c=HTMLCalendar()\nc.cssclass_noday"))

  def test_cssclasses_weekday_head_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from calendar import HTMLCalendar\n"
                                  "c=HTMLCalendar()\nc.cssclasses_weekday_head"))

  def test_cssclass_month_head_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from calendar import HTMLCalendar\n"
                                  "c=HTMLCalendar()\nc.cssclass_month_head"))

  def test_cssclass_year_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from calendar import HTMLCalendar\n"
                                  "c=HTMLCalendar()\nc.cssclass_year"))

  def test_cssclass_year_head_of_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from calendar import HTMLCalendar\n"
                                  "c=HTMLCalendar()\nc.cssclass_year_head"))

  def test_tau_of_cmath(self):
    self.assertOnlyIn((3, 6), self.detect("from cmath import tau"))

  def test_inf_of_cmath(self):
    self.assertOnlyIn((3, 6), self.detect("from cmath import inf"))

  def test_infj_of_cmath(self):
    self.assertOnlyIn((3, 6), self.detect("from cmath import infj"))

  def test_nan_of_cmath(self):
    self.assertOnlyIn((3, 6), self.detect("from cmath import nan"))

  def test_nanj_of_cmath(self):
    self.assertOnlyIn((3, 6), self.detect("from cmath import nanj"))

  def test_FAIL_FAST_of_doctest(self):
    self.assertOnlyIn((3, 4), self.detect("import doctest\ndoctest.FAIL_FAST"))

  def test_ACCESS_DEFAULT_of_mmap(self):
    self.assertOnlyIn((3, 7), self.detect("import mmap\nmmap.ACCESS_DEFAULT"))

  def test_MADV_NORMAL_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_NORMAL"))

  def test_MADV_RANDOM_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_RANDOM"))

  def test_MADV_SEQUENTIAL_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_SEQUENTIAL"))

  def test_MADV_WILLNEED_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_WILLNEED"))

  def test_MADV_DONTNEED_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_DONTNEED"))

  def test_MADV_REMOVE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_REMOVE"))

  def test_MADV_DONTFORK_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_DONTFORK"))

  def test_MADV_DOFORK_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_DOFORK"))

  def test_MADV_HWPOISON_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_HWPOISON"))

  def test_MADV_MERGEABLE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_MERGEABLE"))

  def test_MADV_UNMERGEABLE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_UNMERGEABLE"))

  def test_MADV_SOFT_OFFLINE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_SOFT_OFFLINE"))

  def test_MADV_HUGEPAGE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_HUGEPAGE"))

  def test_MADV_NOHUGEPAGE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_NOHUGEPAGE"))

  def test_MADV_DONTDUMP_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_DONTDUMP"))

  def test_MADV_DODUMP_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_DODUMP"))

  def test_MADV_FREE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_FREE"))

  def test_MADV_NOSYNC_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_NOSYNC"))

  def test_MADV_AUTOSYNC_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_AUTOSYNC"))

  def test_MADV_NOCORE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_NOCORE"))

  def test_MADV_CORE_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_CORE"))

  def test_MADV_PROTECT_of_mmap(self):
    self.assertOnlyIn((3, 8), self.detect("import mmap\nmmap.MADV_PROTECT"))

  def test_MAP_POPULATE_of_mmap(self):
    self.assertOnlyIn((3, 10), self.detect("import mmap\nmmap.MAP_POPULATE"))

  def test_MFD_CLOEXEC_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_CLOEXEC"))

  def test_MFD_ALLOW_SEALING_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_ALLOW_SEALING"))

  def test_MFD_HUGETLB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGETLB"))

  def test_MFD_HUGE_SHIFT_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_SHIFT"))

  def test_MFD_HUGE_MASK_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_MASK"))

  def test_MFD_HUGE_64KB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_64KB"))

  def test_MFD_HUGE_512KB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_512KB"))

  def test_MFD_HUGE_1MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_1MB"))

  def test_MFD_HUGE_2MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_2MB"))

  def test_MFD_HUGE_8MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_8MB"))

  def test_MFD_HUGE_16MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_16MB"))

  def test_MFD_HUGE_32MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_32MB"))

  def test_MFD_HUGE_256MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_256MB"))

  def test_MFD_HUGE_512MB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_512MB"))

  def test_MFD_HUGE_1GB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_1GB"))

  def test_MFD_HUGE_2GB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_2GB"))

  def test_MFD_HUGE_16GB_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import MFD_HUGE_16GB"))

  def test_XATTR_SIZE_MAX_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import XATTR_SIZE_MAX"))

  def test_XATTR_CREATE_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import XATTR_CREATE"))

  def test_XATTR_REPLACE_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import XATTR_REPLACE"))

  def test_ncurses_version_of_curses(self):
    self.assertOnlyIn((3, 8), self.detect("from curses import ncurses_version"))

  def test_A_ITALIC_of_curses(self):
    self.assertOnlyIn((3, 7), self.detect("from curses import A_ITALIC"))

  def test_FMT_XML_of_plistlib(self):
    self.assertOnlyIn((3, 4), self.detect("from plistlib import FMT_XML"))

  def test_FMT_BINARY_of_plistlib(self):
    self.assertOnlyIn((3, 4), self.detect("from plistlib import FMT_BINARY"))

  def test_TIMEOUT_MAX_of_threading(self):
    self.assertOnlyIn((3, 2), self.detect("from threading import TIMEOUT_MAX"))

  def test_pycache_prefix_of_sys(self):
    self.assertOnlyIn((3, 8), self.detect("from sys import pycache_prefix"))

  def test_POSIX_SPAWN_OPEN_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import POSIX_SPAWN_OPEN"))

  def test_POSIX_SPAWN_CLOSE_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import POSIX_SPAWN_CLOSE"))

  def test_POSIX_SPAWN_DUP2_of_os(self):
    self.assertOnlyIn((3, 8), self.detect("from os import POSIX_SPAWN_DUP2"))

  def test_OP_ENABLE_MIDDLEBOX_COMPAT_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 8)), self.detect("from ssl import OP_ENABLE_MIDDLEBOX_COMPAT"))

  def test_S_IFDOOR_of_stat(self):
    self.assertOnlyIn((3, 4), self.detect("from stat import S_IFDOOR"))

  def test_S_IFPORT_of_stat(self):
    self.assertOnlyIn((3, 4), self.detect("from stat import S_IFPORT"))

  def test_S_IFWHT_of_stat(self):
    self.assertOnlyIn((3, 4), self.detect("from stat import S_IFWHT"))

  def test_FILE_ATTRIBUTE_ARCHIVE_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_ARCHIVE"))

  def test_FILE_ATTRIBUTE_COMPRESSED_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_COMPRESSED"))

  def test_FILE_ATTRIBUTE_DEVICE_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_DEVICE"))

  def test_FILE_ATTRIBUTE_DIRECTORY_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_DIRECTORY"))

  def test_FILE_ATTRIBUTE_ENCRYPTED_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_ENCRYPTED"))

  def test_FILE_ATTRIBUTE_HIDDEN_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_HIDDEN"))

  def test_FILE_ATTRIBUTE_INTEGRITY_STREAM_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_INTEGRITY_STREAM"))

  def test_FILE_ATTRIBUTE_NORMAL_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_NORMAL"))

  def test_FILE_ATTRIBUTE_NOT_CONTENT_INDEXED_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED"))

  def test_FILE_ATTRIBUTE_NO_SCRUB_DATA_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA"))

  def test_FILE_ATTRIBUTE_OFFLINE_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_OFFLINE"))

  def test_FILE_ATTRIBUTE_READONLY_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_READONLY"))

  def test_FILE_ATTRIBUTE_REPARSE_POINT_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_REPARSE_POINT"))

  def test_FILE_ATTRIBUTE_SPARSE_FILE_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_SPARSE_FILE"))

  def test_FILE_ATTRIBUTE_SYSTEM_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_SYSTEM"))

  def test_FILE_ATTRIBUTE_TEMPORARY_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_TEMPORARY"))

  def test_FILE_ATTRIBUTE_VIRTUAL_of_stat(self):
    self.assertOnlyIn((3, 5), self.detect("from stat import FILE_ATTRIBUTE_VIRTUAL"))

  def test_IO_REPARSE_TAG_SYMLINK_of_stat(self):
    self.assertOnlyIn((3, 8), self.detect("from stat import IO_REPARSE_TAG_SYMLINK"))

  def test_IO_REPARSE_TAG_MOUNT_POINT_of_stat(self):
    self.assertOnlyIn((3, 8), self.detect("from stat import IO_REPARSE_TAG_MOUNT_POINT"))

  def test_IO_REPARSE_TAG_APPEXECLINK_of_stat(self):
    self.assertOnlyIn((3, 8), self.detect("from stat import IO_REPARSE_TAG_APPEXECLINK"))

  def test_ABOVE_NORMAL_PRIORITY_CLASS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import ABOVE_NORMAL_PRIORITY_CLASS"))

  def test_BELOW_NORMAL_PRIORITY_CLASS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import BELOW_NORMAL_PRIORITY_CLASS"))

  def test_HIGH_PRIORITY_CLASS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import HIGH_PRIORITY_CLASS"))

  def test_IDLE_PRIORITY_CLASS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import IDLE_PRIORITY_CLASS"))

  def test_NORMAL_PRIORITY_CLASS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import NORMAL_PRIORITY_CLASS"))

  def test_REALTIME_PRIORITY_CLASS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import REALTIME_PRIORITY_CLASS"))

  def test_CREATE_NO_WINDOW_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import CREATE_NO_WINDOW"))

  def test_DETACHED_PROCESS_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import DETACHED_PROCESS"))

  def test_CREATE_DEFAULT_ERROR_MODE_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import CREATE_DEFAULT_ERROR_MODE"))

  def test_CREATE_BREAKAWAY_FROM_JOB_of_subprocess(self):
    self.assertOnlyIn((3, 7), self.detect("from subprocess import CREATE_BREAKAWAY_FROM_JOB"))

  def test_error_content_type_from_BaseHTTPServer_BaseHTTPRequestHandler(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from BaseHTTPServer import BaseHTTPRequestHandler\n"
                                  "BaseHTTPRequestHandler().error_content_type"))

  def test_httponly_from_Cookie_Morsel(self):
    self.assertOnlyIn((2, 6),
                      self.detect("from Cookie import Morsel\n"
                                  "Morsel().httponly"))

  def test_TIMEOUT_MAX_of__thread(self):
    self.assertOnlyIn((3, 2), self.detect("from _thread import TIMEOUT_MAX"))

  def test_cssclass_month_from_calendar_HTMLCalendar(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from calendar import HTMLCalendar\n"
                                  "HTMLCalendar().cssclass_month"))

  def test__field_defaults_from_collections_namedtuple(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from collections import namedtuple\n"
                                  "namedtuple()._field_defaults"))

  def test_lineno_from_configparser_DuplicateSectionError(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import DuplicateSectionError\n"
                                  "DuplicateSectionError().lineno"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import DuplicateSectionError\n"
                                  "DuplicateSectionError().lineno"))

  def test_source_from_configparser_DuplicateSectionError(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import DuplicateSectionError\n"
                                  "DuplicateSectionError().source"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import DuplicateSectionError\n"
                                  "DuplicateSectionError().source"))

  def test_source_from_configparser_ParsingError(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from configparser import ParsingError\n"
                                  "ParsingError().source"))
    self.assertTrue(self.config.add_backport("configparser"))
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from configparser import ParsingError\n"
                                  "ParsingError().source"))

  def test_rfc2109_from_cookielib_Cookie(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from cookielib import Cookie\n"
                                  "Cookie().rfc2109"))

  def test_rfc2109_as_netscape_from_cookielib_DefaultCookiePolicy(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from cookielib import DefaultCookiePolicy\n"
                                  "DefaultCookiePolicy().rfc2109_as_netscape"))

  def test_fieldnames_from_csv_csvreader(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from csv import csvreader\n"
                                  "csvreader().fieldnames"))

  def test_line_num_from_csv_csvreader(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from csv import csvreader\n"
                                  "csvreader().line_num"))

  def test_encoding_from_curses_window(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from curses import window\n"
                                  "window().encoding"))

  def test_bjunk_from_difflib_SequenceMatcher(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from difflib import SequenceMatcher\n"
                                  "SequenceMatcher().bjunk"))

  def test_bpopular_from_difflib_SequenceMatcher(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from difflib import SequenceMatcher\n"
                                  "SequenceMatcher().bpopular"))

  def test_COMPARISON_FLAGS_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import COMPARISON_FLAGS"))

  def test_DONT_ACCEPT_BLANKLINE_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import DONT_ACCEPT_BLANKLINE"))

  def test_ELLIPSIS_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import ELLIPSIS"))

  def test_IGNORE_EXCEPTION_DETAIL_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import IGNORE_EXCEPTION_DETAIL"))

  def test_NORMALIZE_WHITESPACE_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import NORMALIZE_WHITESPACE"))

  def test_REPORTING_FLAGS_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import REPORTING_FLAGS"))

  def test_REPORT_CDIFF_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import REPORT_CDIFF"))

  def test_REPORT_NDIFF_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import REPORT_NDIFF"))

  def test_REPORT_ONLY_FIRST_FAILURE_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect(
      "from doctest import REPORT_ONLY_FIRST_FAILURE"))

  def test_REPORT_UDIFF_of_doctest(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from doctest import REPORT_UDIFF"))

  def test_SKIP_of_doctest(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from doctest import SKIP"))

  def test_defects_from_email_message_Message(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from email.message import Message\n"
                                  "Message().defects"))

  def test_content_manager_from_email_policy_EmailPolicy(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from email.policy import EmailPolicy\n"
                                  "EmailPolicy().content_manager"))

  def test_message_factory_from_email_policy_Policy(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from email.policy import Policy\n"
                                  "Policy().message_factory"))

  def test_F_ADD_SEALS_of_fcntl(self):
    self.assertOnlyIn((3, 8), self.detect("from fcntl import F_ADD_SEALS"))

  def test_F_GET_SEALS_of_fcntl(self):
    self.assertOnlyIn((3, 8), self.detect("from fcntl import F_GET_SEALS"))

  def test_F_SEAL_GROW_of_fcntl(self):
    self.assertOnlyIn((3, 8), self.detect("from fcntl import F_SEAL_GROW"))

  def test_F_SEAL_SEAL_of_fcntl(self):
    self.assertOnlyIn((3, 8), self.detect("from fcntl import F_SEAL_SEAL"))

  def test_F_SEAL_SHRINK_of_fcntl(self):
    self.assertOnlyIn((3, 8), self.detect("from fcntl import F_SEAL_SHRINK"))

  def test_F_SEAL_WRITE_of_fcntl(self):
    self.assertOnlyIn((3, 8), self.detect("from fcntl import F_SEAL_WRITE"))

  def test_F_OFD_GETLK_of_fcntl(self):
    self.assertOnlyIn((3, 9), self.detect("from fcntl import F_OFD_GETLK"))

  def test_F_OFD_SETLK_of_fcntl(self):
    self.assertOnlyIn((3, 9), self.detect("from fcntl import F_OFD_SETLK"))

  def test_F_OFD_SETLKW_of_fcntl(self):
    self.assertOnlyIn((3, 9), self.detect("from fcntl import F_OFD_SETLKW"))

  def test_DEFAULT_IGNORES_of_filecmp(self):
    self.assertOnlyIn((3, 4), self.detect("from filecmp import DEFAULT_IGNORES"))

  def test_callbacks_of_gc(self):
    self.assertOnlyIn((3, 3), self.detect("from gc import callbacks"))

  def test_mtime_from_gzip_GzipFile(self):
    self.assertOnlyIn((3, 1),
                      self.detect("from gzip import GzipFile\n"
                                  "GzipFile().mtime"))

  def test_name_from_hashlib_hash(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from hashlib import hash\n"
                                  "hash().name"))

  def test_codepoint2name_of_htmlentitydefs(self):
    self.assertOnlyIn((2, 3), self.detect("from htmlentitydefs import codepoint2name"))

  def test_name2codepoint_of_htmlentitydefs(self):
    self.assertOnlyIn((2, 3), self.detect("from htmlentitydefs import name2codepoint"))

  def test_MISDIRECTED_REQUEST_from_http_HTTPStatus(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from http import HTTPStatus\n"
                                  "HTTPStatus().MISDIRECTED_REQUEST"))

  def test_UNAVAILABLE_FOR_LEGAL_REASONS_from_http_HTTPStatus(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from http import HTTPStatus\n"
                                  "HTTPStatus().UNAVAILABLE_FOR_LEGAL_REASONS"))

  def test_EARLY_HINTS_from_http_HTTPStatus(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from http import HTTPStatus\n"
                                  "HTTPStatus().EARLY_HINTS"))

  def test_IM_A_TEAPOT_from_http_HTTPStatus(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from http import HTTPStatus\n"
                                  "HTTPStatus().IM_A_TEAPOT"))

  def test_TOO_EARLY_from_http_HTTPStatus(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from http import HTTPStatus\n"
                                  "HTTPStatus().TOO_EARLY"))

  def test_blocksize_from_http_client_HTTPConnection(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from http.client import HTTPConnection\n"
                                  "HTTPConnection().blocksize"))

  def test_responses_of_httplib(self):
    self.assertOnlyIn((2, 5), self.detect("from httplib import responses"))

  def test_utf8_enabled_from_imaplib_IMAP4(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from imaplib import IMAP4\n"
                                  "IMAP4().utf8_enabled"))

  def test_description_from_inspect_Parameter_kind(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from inspect.Parameter import kind\n"
                                  "kind().description"))

  def test_SEEK_CUR_of_io(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from io import SEEK_CUR"))

  def test_SEEK_END_of_io(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from io import SEEK_END"))

  def test_SEEK_SET_of_io(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from io import SEEK_SET"))

  def test_write_through_from_io_TextIOWrapper(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from io import TextIOWrapper\n"
                                  "TextIOWrapper().write_through"))

  def test_default_msec_format_from_logging_Formatter(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging import Formatter\n"
                                  "Formatter().default_msec_format"))

  def test_default_time_format_from_logging_Formatter(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging import Formatter\n"
                                  "Formatter().default_time_format"))

  def test_funcName_from_logging_LogRecord(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from logging import LogRecord\n"
                                  "LogRecord().funcName"))

  def test_processName_from_logging_LogRecord(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from logging import LogRecord\n"
                                  "LogRecord().processName"))

  def test_manager_from_logging_LoggerAdapter(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from logging import LoggerAdapter\n"
                                  "LoggerAdapter().manager"))

  def test_terminator_from_logging_StreamHandler(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from logging import StreamHandler\n"
                                  "StreamHandler().terminator"))

  def test_name_from_logging_handlers_BaseRotatingHandler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging.handlers import BaseRotatingHandler\n"
                                  "BaseRotatingHandler().name"))

  def test_rotator_from_logging_handlers_BaseRotatingHandler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from logging.handlers import BaseRotatingHandler\n"
                                  "BaseRotatingHandler().rotator"))

  def test_needs_input_from_lzma_LZMADecompressor(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from lzma import LZMADecompressor\n"
                                  "LZMADecompressor().needs_input"))

  def test_version_of_marshal(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from marshal import version"))

  def test_closed_from_mmap_mmap(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from mmap import mmap\n"
                                  "mmap().closed"))

  def test_nntp_implementation_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().nntp_implementation"))

  def test_nntp_version_from_nntplib_NNTP(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from nntplib import NNTP\n"
                                  "NNTP().nntp_version"))

  def test_CLD_CONTINUED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import CLD_CONTINUED"))

  def test_CLD_DUMPED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import CLD_DUMPED"))

  def test_CLD_EXITED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import CLD_EXITED"))

  def test_CLD_TRAPPED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import CLD_TRAPPED"))

  def test_CLD_KILLED_of_os(self):
    self.assertOnlyIn((3, 9), self.detect("from os import CLD_KILLED"))

  def test_CLD_STOPPED_of_os(self):
    self.assertOnlyIn((3, 9), self.detect("from os import CLD_STOPPED"))

  def test_EX_CANTCREAT_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_CANTCREAT"))

  def test_EX_CONFIG_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_CONFIG"))

  def test_EX_DATAERR_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_DATAERR"))

  def test_EX_IOERR_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_IOERR"))

  def test_EX_NOHOST_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_NOHOST"))

  def test_EX_NOINPUT_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_NOINPUT"))

  def test_EX_NOPERM_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_NOPERM"))

  def test_EX_NOTFOUND_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_NOTFOUND"))

  def test_EX_NOUSER_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_NOUSER"))

  def test_EX_OK_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_OK"))

  def test_EX_OSERR_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_OSERR"))

  def test_EX_OSFILE_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_OSFILE"))

  def test_EX_PROTOCOL_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_PROTOCOL"))

  def test_EX_SOFTWARE_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_SOFTWARE"))

  def test_EX_TEMPFAIL_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_TEMPFAIL"))

  def test_EX_UNAVAILABLE_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_UNAVAILABLE"))

  def test_EX_USAGE_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import EX_USAGE"))

  def test_GRND_NONBLOCK_of_os(self):
    self.assertOnlyIn((3, 6), self.detect("from os import GRND_NONBLOCK"))

  def test_GRND_RANDOM_of_os(self):
    self.assertOnlyIn((3, 6), self.detect("from os import GRND_RANDOM"))

  def test_P_ALL_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import P_ALL"))

  def test_P_PGID_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import P_PGID"))

  def test_P_PID_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import P_PID"))

  def test_RTLD_DEEPBIND_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_DEEPBIND"))

  def test_RTLD_GLOBAL_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_GLOBAL"))

  def test_RTLD_LAZY_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_LAZY"))

  def test_RTLD_LOCAL_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_LOCAL"))

  def test_RTLD_NODELETE_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_NODELETE"))

  def test_RTLD_NOLOAD_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_NOLOAD"))

  def test_RTLD_NOW_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import RTLD_NOW"))

  def test_RWF_DSYNC_of_os(self):
    self.assertOnlyIn((3, 7), self.detect("from os import RWF_DSYNC"))

  def test_RWF_HIPRI_of_os(self):
    self.assertOnlyIn((3, 7), self.detect("from os import RWF_HIPRI"))

  def test_RWF_NOWAIT_of_os(self):
    self.assertOnlyIn((3, 7), self.detect("from os import RWF_NOWAIT"))

  def test_RWF_SYNC_of_os(self):
    self.assertOnlyIn((3, 7), self.detect("from os import RWF_SYNC"))

  def test_RWF_APPEND_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import RWF_APPEND"))

  def test_SCHED_BATCH_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_BATCH"))

  def test_SCHED_FIFO_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_FIFO"))

  def test_SCHED_IDLE_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_IDLE"))

  def test_SCHED_OTHER_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_OTHER"))

  def test_SCHED_RESET_ON_FORK_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_RESET_ON_FORK"))

  def test_SCHED_RR_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_RR"))

  def test_SCHED_SPORADIC_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SCHED_SPORADIC"))

  def test_SEEK_CUR_of_os(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from os import SEEK_CUR"))

  def test_SEEK_DATA_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SEEK_DATA"))

  def test_SEEK_END_of_os(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from os import SEEK_END"))

  def test_SEEK_HOLE_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import SEEK_HOLE"))

  def test_SEEK_SET_of_os(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from os import SEEK_SET"))

  def test_ST_APPEND_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_APPEND"))

  def test_ST_IMMUTABLE_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_IMMUTABLE"))

  def test_ST_MANDLOCK_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_MANDLOCK"))

  def test_ST_NOATIME_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_NOATIME"))

  def test_ST_NODEV_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_NODEV"))

  def test_ST_NODIRATIME_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_NODIRATIME"))

  def test_ST_NOEXEC_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_NOEXEC"))

  def test_ST_NOSUID_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import ST_NOSUID"))

  def test_ST_RDONLY_of_os(self):
    self.assertOnlyIn((3, 2), self.detect("from os import ST_RDONLY"))

  def test_ST_RELATIME_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_RELATIME"))

  def test_ST_SYNCHRONOUS_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_SYNCHRONOUS"))

  def test_ST_WRITE_of_os(self):
    self.assertOnlyIn((3, 4), self.detect("from os import ST_WRITE"))

  def test_WCONTINUED_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import WCONTINUED"))

  def test_WEXITED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import WEXITED"))

  def test_WNOWAIT_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import WNOWAIT"))

  def test_WSTOPPED_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import WSTOPPED"))

  def test_WUNTRACED_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import WUNTRACED"))

  def test_devnull_of_os(self):
    self.assertOnlyIn(((2, 4), (3, 0)), self.detect("from os import devnull"))

  def test_extsep_of_os(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from os import extsep"))

  def test_killpg_of_os(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from os import killpg"))

  def test_P_PIDFD_of_os(self):
    self.assertOnlyIn((3, 9), self.detect("from os import P_PIDFD"))

  def test_SPLICE_F_MOVE_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import SPLICE_F_MOVE"))

  def test_SPLICE_F_NONBLOCK_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import SPLICE_F_NONBLOCK"))

  def test_SPLICE_F_MORE_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import SPLICE_F_MORE"))

  def test_EFD_CLOEXEC_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import EFD_CLOEXEC"))

  def test_EFD_NONBLOCK_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import EFD_NONBLOCK"))

  def test_EFD_SEMAPHORE_of_os(self):
    self.assertOnlyIn((3, 10), self.detect("from os import EFD_SEMAPHORE"))

  def test_st_atime_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_atime"))

  def test_st_atime_ns_from_os_stat(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import stat\n"
                                  "stat().st_atime_ns"))

  def test_st_attrs_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_attrs"))

  def test_st_birthtime_from_os_stat(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_birthtime"))

  def test_st_blksize_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_blksize"))

  def test_st_blocks_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_blocks"))

  def test_st_ctime_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_ctime"))

  def test_st_ctime_ns_from_os_stat(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import stat\n"
                                  "stat().st_ctime_ns"))

  def test_st_dev_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_dev"))

  def test_st_file_attributes_from_os_stat(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from os import stat\n"
                                  "stat().st_file_attributes"))

  def test_st_flags_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_flags"))

  def test_st_ftype_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_ftype"))

  def test_st_gen_from_os_stat(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_gen"))

  def test_st_gid_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_gid"))

  def test_st_ino_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_ino"))

  def test_st_mode_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_mode"))

  def test_st_mtime_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_mtime"))

  def test_st_mtime_ns_from_os_stat(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from os import stat\n"
                                  "stat().st_mtime_ns"))

  def test_st_nlink_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_nlink"))

  def test_st_obtype_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_obtype"))

  def test_st_rdev_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_rdev"))

  def test_st_reparse_tag_from_os_stat(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from os import stat\n"
                                  "stat().st_reparse_tag"))

  def test_st_size_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_size"))

  def test_st_uid_from_os_stat(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import stat\n"
                                  "stat().st_uid"))

  def test_f_bavail_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_bavail"))

  def test_f_bfree_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_bfree"))

  def test_f_blocks_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_blocks"))

  def test_f_bsize_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_bsize"))

  def test_f_favail_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_favail"))

  def test_f_ffree_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_ffree"))

  def test_f_files_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_files"))

  def test_f_flag_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_flag"))

  def test_f_frsize_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_frsize"))

  def test_f_fsid_from_os_statvfs(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_fsid"))

  def test_f_namemax_from_os_statvfs(self):
    self.assertOnlyIn(((2, 2), (3, 0)),
                      self.detect("from os import statvfs\n"
                                  "statvfs().f_namemax"))

  def test_supports_dir_fd_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import supports_dir_fd"))

  def test_supports_effective_ids_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import supports_effective_ids"))

  def test_supports_fd_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import supports_fd"))

  def test_supports_follow_symlinks_of_os(self):
    self.assertOnlyIn((3, 3), self.detect("from os import supports_follow_symlinks"))

  def test_HIGHEST_PROTOCOL_of_pickle(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from pickle import HIGHEST_PROTOCOL"))

  def test_dispatch_table_from_pickle_Pickler(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from pickle import Pickler\n"
                                  "Pickler().dispatch_table"))

  def test_SortKey_of_pstats(self):
    self.assertOnlyIn((3, 7), self.detect("from pstats import SortKey"))

  def test_children_from_pyclbr_Class(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from pyclbr import Class\n"
                                  "Class().children"))

  def test_end_lineno_from_pyclbr_Class(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from pyclbr import Class\n"
                                  "Class().end_lineno"))

  def test_parent_from_pyclbr_Class(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from pyclbr import Class\n"
                                  "Class().parent"))

  def test_children_from_pyclbr_Function(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from pyclbr import Function\n"
                                  "Function().children"))

  def test_end_lineno_from_pyclbr_Function(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from pyclbr import Function\n"
                                  "Function().end_lineno"))

  def test_parent_from_pyclbr_Function(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from pyclbr import Function\n"
                                  "Function().parent"))

  def test_is_async_from_pyclbr_Function(self):
    self.assertOnlyIn((3, 10),
                      self.detect("from pyclbr import Function\n"
                                  "Function().is_async"))

  def test_colno_from_re_error(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from re import error\n"
                                  "error().colno"))

  def test_lineno_from_re_error(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from re import error\n"
                                  "error().lineno"))

  def test_msg_from_re_error(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from re import error\n"
                                  "error().msg"))

  def test_pattern_from_re_error(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from re import error\n"
                                  "error().pattern"))

  def test_pos_from_re_error(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from re import error\n"
                                  "error().pos"))

  def test_maxfrozenset_from_repr_Repr(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from repr import Repr\n"
                                  "Repr().maxfrozenset"))

  def test_maxset_from_repr_Repr(self):
    self.assertOnlyIn((2, 4),
                      self.detect("from repr import Repr\n"
                                  "Repr().maxset"))

  def test_RLIMIT_MSGQUEUE_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_MSGQUEUE"))

  def test_RLIMIT_NICE_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_NICE"))

  def test_RLIMIT_NPTS_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_NPTS"))

  def test_RLIMIT_KQUEUES_of_resource(self):
    self.assertOnlyIn((3, 10), self.detect("from resource import RLIMIT_KQUEUES"))

  def test_RLIMIT_RTPRIO_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_RTPRIO"))

  def test_RLIMIT_RTTIME_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_RTTIME"))

  def test_RLIMIT_SBSIZE_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_SBSIZE"))

  def test_RLIMIT_SIGPENDING_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_SIGPENDING"))

  def test_RLIMIT_SWAP_of_resource(self):
    self.assertOnlyIn((3, 4), self.detect("from resource import RLIMIT_SWAP"))

  def test_RUSAGE_THREAD_of_resource(self):
    self.assertOnlyIn((3, 2), self.detect("from resource import RUSAGE_THREAD"))

  def test_ru_idrss_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_idrss"))

  def test_ru_inblock_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_inblock"))

  def test_ru_isrss_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_isrss"))

  def test_ru_ixrss_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_ixrss"))

  def test_ru_majflt_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_majflt"))

  def test_ru_maxrss_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_maxrss"))

  def test_ru_minflt_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_minflt"))

  def test_ru_msgrcv_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_msgrcv"))

  def test_ru_msgsnd_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_msgsnd"))

  def test_ru_nivcsw_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_nivcsw"))

  def test_ru_nsignals_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_nsignals"))

  def test_ru_nswap_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_nswap"))

  def test_ru_nvcsw_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_nvcsw"))

  def test_ru_oublock_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_oublock"))

  def test_ru_stime_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_stime"))

  def test_ru_utime_from_resource_getrusage(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from resource import getrusage\n"
                                  "getrusage().ru_utime"))

  def test_queue_from_sched_scheduler(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from sched import scheduler\n"
                                  "scheduler().queue"))

  def test_EPOLLEXCLUSIVE_of_select(self):
    self.assertOnlyIn((3, 6), self.detect("from select import EPOLLEXCLUSIVE"))

  def test_PIPE_BUF_of_select(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from select import PIPE_BUF"))

  def test_closed_from_select_devpoll(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from select import devpoll\n"
                                  "devpoll().closed"))

  def test_eof_from_shlex_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from shlex import shlex\n"
                                  "shlex().eof"))

  def test_escape_from_shlex_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from shlex import shlex\n"
                                  "shlex().escape"))

  def test_escapedquotes_from_shlex_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from shlex import shlex\n"
                                  "shlex().escapedquotes"))

  def test_punctuation_chars_from_shlex_shlex(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from shlex import shlex\n"
                                  "shlex().punctuation_chars"))

  def test_whitespace_split_from_shlex_shlex(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from shlex import shlex\n"
                                  "shlex().whitespace_split"))

  def test_avoids_symlink_attacks_from_shutil_rmtree(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from shutil import rmtree\n"
                                  "rmtree().avoids_symlink_attacks"))

  def test_CTRL_BREAK_EVENT_of_signal(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from signal import CTRL_BREAK_EVENT"))

  def test_CTRL_C_EVENT_of_signal(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from signal import CTRL_C_EVENT"))

  def test_SIG_BLOCK_of_signal(self):
    self.assertOnlyIn((3, 3), self.detect("from signal import SIG_BLOCK"))

  def test_SIG_SETMASK_of_signal(self):
    self.assertOnlyIn((3, 3), self.detect("from signal import SIG_SETMASK"))

  def test_SIG_UNBLOCK_of_signal(self):
    self.assertOnlyIn((3, 3), self.detect("from signal import SIG_UNBLOCK"))

  def test_ENABLE_USER_SITE_of_site(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from site import ENABLE_USER_SITE"))

  def test_PREFIXES_of_site(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from site import PREFIXES"))

  def test_USER_BASE_of_site(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from site import USER_BASE"))

  def test_USER_SITE_of_site(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from site import USER_SITE"))

  def test_AF_ALG_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import AF_ALG"))

  def test_AF_CAN_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import AF_CAN"))

  def test_AF_LINK_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import AF_LINK"))

  def test_AF_QIPCRTR_of_socket(self):
    self.assertOnlyIn((3, 8), self.detect("from socket import AF_QIPCRTR"))

  def test_AF_RDS_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import AF_RDS"))

  def test_AF_TIPC_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import AF_TIPC"))

  def test_AF_VSOCK_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import AF_VSOCK"))

  def test_ALG_OP_DECRYPT_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_OP_DECRYPT"))

  def test_ALG_OP_ENCRYPT_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_OP_ENCRYPT"))

  def test_ALG_OP_SIGN_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_OP_SIGN"))

  def test_ALG_OP_VERIFY_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_OP_VERIFY"))

  def test_ALG_SET_AEAD_ASSOCLEN_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_SET_AEAD_ASSOCLEN"))

  def test_ALG_SET_AEAD_AUTHSIZE_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_SET_AEAD_AUTHSIZE"))

  def test_ALG_SET_IV_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_SET_IV"))

  def test_ALG_SET_KEY_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_SET_KEY"))

  def test_ALG_SET_OP_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_SET_OP"))

  def test_ALG_SET_PUBKEY_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import ALG_SET_PUBKEY"))

  def test_CAN_BCM_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM"))

  def test_CAN_BCM_CAN_FD_FRAME_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_CAN_FD_FRAME"))

  def test_CAN_BCM_RX_ANNOUNCE_RESUME_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_ANNOUNCE_RESUME"))

  def test_CAN_BCM_RX_CHANGED_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_CHANGED"))

  def test_CAN_BCM_RX_CHECK_DLC_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_CHECK_DLC"))

  def test_CAN_BCM_RX_DELETE_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_DELETE"))

  def test_CAN_BCM_RX_FILTER_ID_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_FILTER_ID"))

  def test_CAN_BCM_RX_NO_AUTOTIMER_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_NO_AUTOTIMER"))

  def test_CAN_BCM_RX_READ_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_READ"))

  def test_CAN_BCM_RX_RTR_FRAME_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_RTR_FRAME"))

  def test_CAN_BCM_RX_SETUP_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_SETUP"))

  def test_CAN_BCM_RX_STATUS_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_STATUS"))

  def test_CAN_BCM_RX_TIMEOUT_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_RX_TIMEOUT"))

  def test_CAN_BCM_SETTIMER_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_SETTIMER"))

  def test_CAN_BCM_STARTTIMER_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_STARTTIMER"))

  def test_CAN_BCM_TX_ANNOUNCE_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_ANNOUNCE"))

  def test_CAN_BCM_TX_COUNTEVT_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_COUNTEVT"))

  def test_CAN_BCM_TX_CP_CAN_ID_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_CP_CAN_ID"))

  def test_CAN_BCM_TX_DELETE_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_DELETE"))

  def test_CAN_BCM_TX_EXPIRED_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_EXPIRED"))

  def test_CAN_BCM_TX_READ_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_READ"))

  def test_CAN_BCM_TX_RESET_MULTI_IDX_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_RESET_MULTI_IDX"))

  def test_CAN_BCM_TX_SEND_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_SEND"))

  def test_CAN_BCM_TX_SETUP_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_SETUP"))

  def test_CAN_BCM_TX_STATUS_of_socket(self):
    self.assertOnlyIn((3, 4), self.detect("from socket import CAN_BCM_TX_STATUS"))

  def test_CAN_EFF_FLAG_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_EFF_FLAG"))

  def test_CAN_EFF_MASK_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_EFF_MASK"))

  def test_CAN_ERR_FLAG_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_ERR_FLAG"))

  def test_CAN_ERR_MASK_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_ERR_MASK"))

  def test_CAN_ISOTP_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import CAN_ISOTP"))

  def test_CAN_J1939_of_socket(self):
    self.assertOnlyIn((3, 9), self.detect("from socket import CAN_J1939"))

  def test_CAN_RAW_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_RAW"))

  def test_CAN_RAW_ERR_FILTER_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_RAW_ERR_FILTER"))

  def test_CAN_RAW_JOIN_FILTERS_of_socket(self):
    self.assertOnlyIn((3, 9), self.detect("from socket import CAN_RAW_JOIN_FILTERS"))

  def test_CAN_RAW_FD_FRAMES_of_socket(self):
    self.assertOnlyIn((3, 5), self.detect("from socket import CAN_RAW_FD_FRAMES"))

  def test_CAN_RAW_FILTER_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_RAW_FILTER"))

  def test_CAN_RAW_LOOPBACK_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_RAW_LOOPBACK"))

  def test_CAN_RAW_RECV_OWN_MSGS_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_RAW_RECV_OWN_MSGS"))

  def test_CAN_RTR_FLAG_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_RTR_FLAG"))

  def test_CAN_SFF_MASK_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import CAN_SFF_MASK"))

  def test_IOCTL_VM_SOCKETS_GET_LOCAL_CID_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import IOCTL_VM_SOCKETS_GET_LOCAL_CID"))

  def test_PF_CAN_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import PF_CAN"))

  def test_PF_RDS_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import PF_RDS"))

  def test_RCVALL_IPLEVEL_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import RCVALL_IPLEVEL"))

  def test_RCVALL_MAX_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import RCVALL_MAX"))

  def test_RCVALL_OFF_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import RCVALL_OFF"))

  def test_RCVALL_ON_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import RCVALL_ON"))

  def test_RCVALL_SOCKETLEVELONLY_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import RCVALL_SOCKETLEVELONLY"))

  def test_RDS_CANCEL_SENT_TO_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CANCEL_SENT_TO"))

  def test_RDS_CMSG_RDMA_ARGS_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CMSG_RDMA_ARGS"))

  def test_RDS_CMSG_RDMA_DEST_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CMSG_RDMA_DEST"))

  def test_RDS_CMSG_RDMA_MAP_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CMSG_RDMA_MAP"))

  def test_RDS_CMSG_RDMA_STATUS_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CMSG_RDMA_STATUS"))

  def test_RDS_CMSG_RDMA_UPDATE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CMSG_RDMA_UPDATE"))

  def test_RDS_CONG_MONITOR_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_CONG_MONITOR"))

  def test_RDS_FREE_MR_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_FREE_MR"))

  def test_RDS_GET_MR_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_GET_MR"))

  def test_RDS_GET_MR_FOR_DEST_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_GET_MR_FOR_DEST"))

  def test_RDS_RDMA_DONTWAIT_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_DONTWAIT"))

  def test_RDS_RDMA_FENCE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_FENCE"))

  def test_RDS_RDMA_INVALIDATE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_INVALIDATE"))

  def test_RDS_RDMA_NOTIFY_ME_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_NOTIFY_ME"))

  def test_RDS_RDMA_READWRITE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_READWRITE"))

  def test_RDS_RDMA_SILENT_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_SILENT"))

  def test_RDS_RDMA_USE_ONCE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RDMA_USE_ONCE"))

  def test_RDS_RECVERR_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import RDS_RECVERR"))

  def test_SIO_KEEPALIVE_VALS_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import SIO_KEEPALIVE_VALS"))

  def test_SIO_LOOPBACK_FAST_PATH_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import SIO_LOOPBACK_FAST_PATH"))

  def test_SIO_RCVALL_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import SIO_RCVALL"))

  def test_SOCK_CLOEXEC_of_socket(self):
    self.assertOnlyIn((3, 2), self.detect("from socket import SOCK_CLOEXEC"))

  def test_SOCK_NONBLOCK_of_socket(self):
    self.assertOnlyIn((3, 2), self.detect("from socket import SOCK_NONBLOCK"))

  def test_SOL_ALG_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import SOL_ALG"))

  def test_SOL_CAN_BASE_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import SOL_CAN_BASE"))

  def test_SOL_CAN_RAW_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import SOL_CAN_RAW"))

  def test_SOL_RDS_of_socket(self):
    self.assertOnlyIn((3, 3), self.detect("from socket import SOL_RDS"))

  def test_SOL_TIPC_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import SOL_TIPC"))

  def test_SO_DOMAIN_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import SO_DOMAIN"))

  def test_SO_PASSSEC_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import SO_PASSSEC"))

  def test_SO_PEERSEC_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import SO_PEERSEC"))

  def test_SO_PROTOCOL_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import SO_PROTOCOL"))

  def test_SO_VM_SOCKETS_BUFFER_MAX_SIZE_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import SO_VM_SOCKETS_BUFFER_MAX_SIZE"))

  def test_SO_VM_SOCKETS_BUFFER_MIN_SIZE_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import SO_VM_SOCKETS_BUFFER_MIN_SIZE"))

  def test_SO_VM_SOCKETS_BUFFER_SIZE_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import SO_VM_SOCKETS_BUFFER_SIZE"))

  def test_TCP_CONGESTION_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import TCP_CONGESTION"))

  def test_TCP_NOTSENT_LOWAT_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import TCP_NOTSENT_LOWAT"))

  def test_TCP_USER_TIMEOUT_of_socket(self):
    self.assertOnlyIn((3, 6), self.detect("from socket import TCP_USER_TIMEOUT"))

  def test_TCP_KEEPALIVE_of_socket(self):
    self.assertOnlyIn((3, 10), self.detect("from socket import TCP_KEEPALIVE"))

  def test_TIPC_ADDR_ID_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_ADDR_ID"))

  def test_TIPC_ADDR_NAME_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_ADDR_NAME"))

  def test_TIPC_ADDR_NAMESEQ_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_ADDR_NAMESEQ"))

  def test_TIPC_CFG_SRV_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_CFG_SRV"))

  def test_TIPC_CLUSTER_SCOPE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_CLUSTER_SCOPE"))

  def test_TIPC_CONN_TIMEOUT_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_CONN_TIMEOUT"))

  def test_TIPC_CRITICAL_IMPORTANCE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_CRITICAL_IMPORTANCE"))

  def test_TIPC_DEST_DROPPABLE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_DEST_DROPPABLE"))

  def test_TIPC_HIGH_IMPORTANCE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_HIGH_IMPORTANCE"))

  def test_TIPC_IMPORTANCE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_IMPORTANCE"))

  def test_TIPC_LOW_IMPORTANCE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_LOW_IMPORTANCE"))

  def test_TIPC_MEDIUM_IMPORTANCE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_MEDIUM_IMPORTANCE"))

  def test_TIPC_NODE_SCOPE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_NODE_SCOPE"))

  def test_TIPC_PUBLISHED_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_PUBLISHED"))

  def test_TIPC_SRC_DROPPABLE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_SRC_DROPPABLE"))

  def test_TIPC_SUBSCR_TIMEOUT_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_SUBSCR_TIMEOUT"))

  def test_TIPC_SUB_CANCEL_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_SUB_CANCEL"))

  def test_TIPC_SUB_PORTS_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_SUB_PORTS"))

  def test_TIPC_SUB_SERVICE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_SUB_SERVICE"))

  def test_TIPC_TOP_SRV_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_TOP_SRV"))

  def test_TIPC_WAIT_FOREVER_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_WAIT_FOREVER"))

  def test_TIPC_WITHDRAWN_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_WITHDRAWN"))

  def test_TIPC_ZONE_SCOPE_of_socket(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from socket import TIPC_ZONE_SCOPE"))

  def test_VMADDR_CID_ANY_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import VMADDR_CID_ANY"))

  def test_VMADDR_CID_HOST_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import VMADDR_CID_HOST"))

  def test_VMADDR_PORT_ANY_of_socket(self):
    self.assertOnlyIn((3, 7), self.detect("from socket import VMADDR_PORT_ANY"))

  def test_IPPROTO_UDPLITE_of_socket(self):
    self.assertOnlyIn((3, 9), self.detect("from socket import IPPROTO_UDPLITE"))

  def test_IPPROTO_MPTCP_of_socket(self):
    self.assertOnlyIn((3, 10), self.detect("from socket import IPPROTO_MPTCP"))

  def test_IP_RECVTOS_of_socket(self):
    self.assertOnlyIn((3, 10), self.detect("from socket import IP_RECVTOS"))

  def test_has_ipv6_of_socket(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from socket import has_ipv6"))

  def test_family_from_socket_socket(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().family"))

  def test_proto_from_socket_socket(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().proto"))

  def test_type_from_socket_socket(self):
    self.assertOnlyIn(((2, 5), (3, 0)),
                      self.detect("from socket import socket\n"
                                  "socket().type"))

  def test_block_on_close_from_socketserver_ForkingMixIn(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from socketserver import ForkingMixIn\n"
                                  "ForkingMixIn().block_on_close"))

  def test_block_on_close_from_socketserver_ThreadingMixIn(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from socketserver import ThreadingMixIn\n"
                                  "ThreadingMixIn().block_on_close"))

  def test_in_transaction_from_sqlite3_Connection(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from sqlite3 import Connection\n"
                                  "Connection().in_transaction"))

  def test_ALERT_DESCRIPTION_ACCESS_DENIED_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_ACCESS_DENIED"))

  def test_ALERT_DESCRIPTION_BAD_CERTIFICATE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE"))

  def test_ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE"))

  def test_ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE"))

  def test_ALERT_DESCRIPTION_BAD_RECORD_MAC_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_BAD_RECORD_MAC"))

  def test_ALERT_DESCRIPTION_CERTIFICATE_EXPIRED_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_CERTIFICATE_EXPIRED"))

  def test_ALERT_DESCRIPTION_CERTIFICATE_REVOKED_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_CERTIFICATE_REVOKED"))

  def test_ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN"))

  def test_ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE"))

  def test_ALERT_DESCRIPTION_CLOSE_NOTIFY_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_CLOSE_NOTIFY"))

  def test_ALERT_DESCRIPTION_DECODE_ERROR_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_DECODE_ERROR"))

  def test_ALERT_DESCRIPTION_DECOMPRESSION_FAILURE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_DECOMPRESSION_FAILURE"))

  def test_ALERT_DESCRIPTION_DECRYPT_ERROR_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_DECRYPT_ERROR"))

  def test_ALERT_DESCRIPTION_HANDSHAKE_FAILURE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE"))

  def test_ALERT_DESCRIPTION_ILLEGAL_PARAMETER_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER"))

  def test_ALERT_DESCRIPTION_INSUFFICIENT_SECURITY_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_INSUFFICIENT_SECURITY"))

  def test_ALERT_DESCRIPTION_INTERNAL_ERROR_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_INTERNAL_ERROR"))

  def test_ALERT_DESCRIPTION_NO_RENEGOTIATION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_NO_RENEGOTIATION"))

  def test_ALERT_DESCRIPTION_PROTOCOL_VERSION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_PROTOCOL_VERSION"))

  def test_ALERT_DESCRIPTION_RECORD_OVERFLOW_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_RECORD_OVERFLOW"))

  def test_ALERT_DESCRIPTION_UNEXPECTED_MESSAGE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE"))

  def test_ALERT_DESCRIPTION_UNKNOWN_CA_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect("from ssl import ALERT_DESCRIPTION_UNKNOWN_CA"))

  def test_ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY"))

  def test_ALERT_DESCRIPTION_UNRECOGNIZED_NAME_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME"))

  def test_ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE"))

  def test_ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
        "from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION"))

  def test_ALERT_DESCRIPTION_USER_CANCELLED_of_ssl(self):
    self.assertOnlyIn(((2, 7), (3, 4)), self.detect(
      "from ssl import ALERT_DESCRIPTION_USER_CANCELLED"))

  def test_HAS_SSLv2_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import HAS_SSLv2"))

  def test_HAS_SSLv3_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import HAS_SSLv3"))

  def test_OP_NO_RENEGOTIATION_of_ssl(self):
    self.assertOnlyIn((3, 7), self.detect("from ssl import OP_NO_RENEGOTIATION"))

  def test_PROTOCOL_TLS_CLIENT_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import PROTOCOL_TLS_CLIENT"))

  def test_PROTOCOL_TLS_SERVER_of_ssl(self):
    self.assertOnlyIn((3, 6), self.detect("from ssl import PROTOCOL_TLS_SERVER"))

  def test_CLIENT_AUTH_from_ssl_Purpose(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      self.detect("from ssl import Purpose\n"
                                  "Purpose().CLIENT_AUTH"))

  def test_SERVER_AUTH_from_ssl_Purpose(self):
    self.assertOnlyIn(((2, 7), (3, 4)),
                      self.detect("from ssl import Purpose\n"
                                  "Purpose().SERVER_AUTH"))

  def test_sni_callback_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from ssl import SSLContext\n"
                                  "SSLContext().sni_callback"))

  def test_sslobject_class_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from ssl import SSLContext\n"
                                  "SSLContext().sslobject_class"))

  def test_sslsocket_class_from_ssl_SSLContext(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from ssl import SSLContext\n"
                                  "SSLContext().sslsocket_class"))

  def test_braceidpattern_from_string_Template(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from string import Template\n"
                                  "Template().braceidpattern"))

  def test_flags_from_string_Template(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from string import Template\n"
                                  "Template().flags"))

  def test_letters_of_string(self):
    self.assertOnlyIn((2, 0), self.detect("from string import letters"))

  def test_lowercase_of_string(self):
    self.assertOnlyIn((2, 0), self.detect("from string import lowercase"))

  def test_uppercase_of_string(self):
    self.assertOnlyIn((2, 0), self.detect("from string import uppercase"))

  def test_stderr_from_subprocess_CalledProcessError(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from subprocess import CalledProcessError\n"
                                  "CalledProcessError().stderr"))

  def test_stdout_from_subprocess_CalledProcessError(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from subprocess import CalledProcessError\n"
                                  "CalledProcessError().stdout"))

  def test_lpAttributeList_from_subprocess_STARTUPINFO(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from subprocess import STARTUPINFO\n"
                                  "STARTUPINFO().lpAttributeList"))

  def test_stderr_from_subprocess_TimeoutExpired(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from subprocess import TimeoutExpired\n"
                                  "TimeoutExpired().stderr"))

  def test_stdout_from_subprocess_TimeoutExpired(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from subprocess import TimeoutExpired\n"
                                  "TimeoutExpired().stdout"))

  def test___breakpointhook___of_sys(self):
    self.assertOnlyIn((3, 7), self.detect("from sys import __breakpointhook__"))

  def test___interactivehook___of_sys(self):
    self.assertOnlyIn((3, 4), self.detect("from sys import __interactivehook__"))

  def test___unraisablehook___of_sys(self):
    self.assertOnlyIn((3, 8), self.detect("from sys import __unraisablehook__"))

  def test__xoptions_of_sys(self):
    self.assertOnlyIn((3, 2), self.detect("from sys import _xoptions"))

  def test_abiflags_of_sys(self):
    self.assertOnlyIn((3, 2), self.detect("from sys import abiflags"))

  def test_base_exec_prefix_of_sys(self):
    self.assertOnlyIn((3, 3), self.detect("from sys import base_exec_prefix"))

  def test_base_prefix_of_sys(self):
    self.assertOnlyIn((3, 3), self.detect("from sys import base_prefix"))

  def test_dont_write_bytecode_of_sys(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from sys import dont_write_bytecode"))

  def test_platlibdir_of_sys(self):
    self.assertOnlyIn((3, 9), self.detect("from sys import platlibdir"))

  def test_dev_mode_from_sys_flags(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from sys import flags\n"
                                  "flags().dev_mode"))

  def test_hash_randomization_from_sys_flags(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from sys import flags\n"
                                  "flags().hash_randomization"))

  def test_isolated_from_sys_flags(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from sys import flags\n"
                                  "flags().isolated"))

  def test_quiet_from_sys_flags(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from sys import flags\n"
                                  "flags().quiet"))

  def test_utf8_mode_from_sys_flags(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from sys import flags\n"
                                  "flags().utf8_mode"))

  def test_build_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().build"))

  def test_major_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().major"))

  def test_minor_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().minor"))

  def test_platform_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().platform"))

  def test_product_type_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().product_type"))

  def test_service_pack_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().service_pack"))

  def test_service_pack_major_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().service_pack_major"))

  def test_service_pack_minor_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().service_pack_minor"))

  def test_suite_mask_from_sys_getwindowsversion(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import getwindowsversion\n"
                                  "getwindowsversion().suite_mask"))

  def test_hash_info_of_sys(self):
    self.assertOnlyIn((3, 2), self.detect("from sys import hash_info"))

  def test_algorithm_from_sys_hash_info(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from sys import hash_info\n"
                                  "hash_info().algorithm"))

  def test_hash_bits_from_sys_hash_info(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from sys import hash_info\n"
                                  "hash_info().hash_bits"))

  def test_seed_bits_from_sys_hash_info(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from sys import hash_info\n"
                                  "hash_info().seed_bits"))

  def test_implementation_of_sys(self):
    self.assertOnlyIn((3, 3), self.detect("from sys import implementation"))

  def test_int_info_of_sys(self):
    self.assertOnlyIn((3, 1), self.detect("from sys import int_info"))

  def test_thread_info_of_sys(self):
    self.assertOnlyIn((3, 3), self.detect("from sys import thread_info"))

  def test_orig_argv_of_sys(self):
    self.assertOnlyIn((3, 10), self.detect("from sys import orig_argv"))

  def test_stdlib_module_names_of_sys(self):
    self.assertOnlyIn((3, 10), self.detect("from sys import stdlib_module_names"))

  def test_major_from_sys_version_info(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import version_info\n"
                                  "version_info().major"))

  def test_micro_from_sys_version_info(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import version_info\n"
                                  "version_info().micro"))

  def test_minor_from_sys_version_info(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import version_info\n"
                                  "version_info().minor"))

  def test_releaselevel_from_sys_version_info(self):
    self.assertOnlyIn(((2, 7), (3, 0)),
                      self.detect("from sys import version_info\n"
                                  "version_info().releaselevel"))

  def test_DEFAULT_FORMAT_of_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from tarfile import DEFAULT_FORMAT"))

  def test_GNU_FORMAT_of_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from tarfile import GNU_FORMAT"))

  def test_PAX_FORMAT_of_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from tarfile import PAX_FORMAT"))

  def test_USTAR_FORMAT_of_tarfile(self):
    self.assertOnlyIn(((2, 6), (3, 0)), self.detect("from tarfile import USTAR_FORMAT"))

  def test_break_on_hyphens_from_textwrap_TextWrapper(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from textwrap import TextWrapper\n"
                                  "TextWrapper().break_on_hyphens"))

  def test_drop_whitespace_from_textwrap_TextWrapper(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from textwrap import TextWrapper\n"
                                  "TextWrapper().drop_whitespace"))

  def test_max_lines_from_textwrap_TextWrapper(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from textwrap import TextWrapper\n"
                                  "TextWrapper().max_lines"))

  def test_placeholder_from_textwrap_TextWrapper(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from textwrap import TextWrapper\n"
                                  "TextWrapper().placeholder"))

  def test_tabsize_from_textwrap_TextWrapper(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from textwrap import TextWrapper\n"
                                  "TextWrapper().tabsize"))

  def test_daemon_from_threading_Thread(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from threading import Thread\n"
                                  "Thread().daemon"))

  def test_ident_from_threading_Thread(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from threading import Thread\n"
                                  "Thread().ident"))

  def test_name_from_threading_Thread(self):
    self.assertOnlyIn(((2, 6), (3, 0)),
                      self.detect("from threading import Thread\n"
                                  "Thread().name"))

  def test_native_id_from_threading_Thread(self):
    self.assertOnlyIn((3, 8),
                      self.detect("from threading import Thread\n"
                                  "Thread().native_id"))

  def test___excepthook___from_threading(self):
    self.assertOnlyIn((3, 10), self.detect("from threading import __excepthook__"))

  def test_tm_gmtoff_from_time_struct_time(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from time import struct_time\n"
                                  "struct_time().tm_gmtoff"))

  def test_tm_zone_from_time_struct_time(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from time import struct_time\n"
                                  "struct_time().tm_zone"))

  def test_ASYNC_of_token(self):
    self.assertOnlyIn((3, 5), self.detect("from token import ASYNC"))

  def test_AWAIT_of_token(self):
    self.assertOnlyIn((3, 5), self.detect("from token import AWAIT"))

  def test_COMMENT_of_token(self):
    self.assertOnlyIn((3, 7), self.detect("from token import COMMENT"))

  def test_ENCODING_of_token(self):
    self.assertOnlyIn((3, 7), self.detect("from token import ENCODING"))

  def test_NL_of_token(self):
    self.assertOnlyIn((3, 7), self.detect("from token import NL"))

  def test_TYPE_COMMENT_of_token(self):
    self.assertOnlyIn((3, 8), self.detect("from token import TYPE_COMMENT"))

  def test_domain_from_tracemalloc_Filter(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from tracemalloc import Filter\n"
                                  "Filter().domain"))

  def test_domain_from_tracemalloc_Trace(self):
    self.assertOnlyIn((3, 6),
                      self.detect("from tracemalloc import Trace\n"
                                  "Trace().domain"))

  def test_total_nframe_from_tracemalloc_Traceback(self):
    self.assertOnlyIn((3, 9),
                      self.detect("from tracemalloc import Traceback\n"
                                  "Traceback().total_nframe"))

  def test_AsyncGeneratorType_of_types(self):
    self.assertOnlyIn((3, 6), self.detect("from types import AsyncGeneratorType"))

  def test_BooleanType_of_types(self):
    self.assertOnlyIn((2, 3), self.detect("from types import BooleanType"))

  def test_CellType_of_types(self):
    self.assertOnlyIn((3, 8), self.detect("from types import CellType"))

  def test_ClassMethodDescriptorType_of_types(self):
    self.assertOnlyIn((3, 7), self.detect("from types import ClassMethodDescriptorType"))

  def test_CoroutineType_of_types(self):
    self.assertOnlyIn((3, 5), self.detect("from types import CoroutineType"))

  def test___spec___from_types_ModuleType(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from types import ModuleType\n"
                                  "ModuleType().__spec__"))

  def test_NoneType_of_types(self):
    self.assertOnlyIn(((2, 0), (3, 10)), self.detect("from types import NoneType"))

  def test_NotImplementedType_of_types(self):
    self.assertOnlyIn(((2, 0), (3, 10)), self.detect("from types import NotImplementedType"))

  def test_EllipsisType_of_types(self):
    self.assertOnlyIn(((2, 0), (3, 10)), self.detect("from types import EllipsisType"))

  def test_UnionType_of_types(self):
    self.assertOnlyIn((3, 10), self.detect("from types import UnionType"))

  def test_GeneratorType_of_types(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from types import GeneratorType"))

  def test_GetSetDescriptorType_of_types(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from types import GetSetDescriptorType"))

  def test_MemberDescriptorType_of_types(self):
    self.assertOnlyIn(((2, 5), (3, 0)), self.detect("from types import MemberDescriptorType"))

  def test_MethodDescriptorType_of_types(self):
    self.assertOnlyIn((3, 7), self.detect("from types import MethodDescriptorType"))

  def test_MethodWrapperType_of_types(self):
    self.assertOnlyIn((3, 7), self.detect("from types import MethodWrapperType"))

  def test_StringTypes_of_types(self):
    self.assertOnlyIn((2, 2), self.detect("from types import StringTypes"))

  def test_WrapperDescriptorType_of_types(self):
    self.assertOnlyIn((3, 7), self.detect("from types import WrapperDescriptorType"))

  def test_NoReturn_of_typing(self):
    self.assertOnlyIn((3, 5), self.detect("from typing import NoReturn"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 3)), self.detect("from typing import NoReturn"))

  def test_Final_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import Final"))
    self.assertOnlyIn((3, 5), self.detect("""import typing
something.Final
"""))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 8)), self.detect("from typing import Final"))

  def test_Literal_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import Literal"))
    self.assertTrue(self.config.add_backport("typing"))
    self.assertOnlyIn(((2, 7), (3, 8)), self.detect("from typing import Literal"))

  def test_Annotated_of_typing(self):
    self.assertOnlyIn((3, 9), self.detect("from typing import Annotated"))

  def test_Concatenate_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import Concatenate"))

  def test_ParamSpecArgs_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import ParamSpecArgs"))

  def test_ParamSpecKwargs_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import ParamSpecKwargs"))

  def test_TypeAlias_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import TypeAlias"))

  def test_TypeGuard_of_typing(self):
    self.assertOnlyIn((3, 10), self.detect("from typing import TypeGuard"))

  def test_ucd_3_2_0_of_unicodedata(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from unicodedata import ucd_3_2_0"))

  def test_unidata_version_of_unicodedata(self):
    self.assertOnlyIn(((2, 3), (3, 0)), self.detect("from unicodedata import unidata_version"))

  def test_longMessage_from_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 1)),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().longMessage"))

  def test_maxDiff_from_unittest_TestCase(self):
    self.assertOnlyIn(((2, 7), (3, 2)),
                      self.detect("from unittest import TestCase\n"
                                  "TestCase().maxDiff"))

  def test_errors_from_unittest_TestLoader(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from unittest import TestLoader\n"
                                  "TestLoader().errors"))

  def test_testNamePatterns_from_unittest_TestLoader(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from unittest import TestLoader\n"
                                  "TestLoader().testNamePatterns"))

  def test_tb_locals_from_unittest_TestResult(self):
    self.assertOnlyIn((3, 5),
                      self.detect("from unittest import TestResult\n"
                                  "TestResult().tb_locals"))

  def test_headers_from_urllib_error_HTTPError(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from urllib.error import HTTPError\n"
                                  "HTTPError().headers"))

  def test__UNSAFE_URL_BYTES_TO_REMOVE_of_urllib_parse(self):
    self.assertOnlyIn((3, 10), self.detect("from urllib.parse import _UNSAFE_URL_BYTES_TO_REMOVE"))

  def test_method_from_urllib_request_Request(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from urllib.request import Request\n"
                                  "Request().method"))

  def test_fragment_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().fragment"))

  def test_hostname_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().hostname"))

  def test_netloc_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().netloc"))

  def test_params_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().params"))

  def test_password_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().password"))

  def test_path_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().path"))

  def test_port_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().port"))

  def test_query_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().query"))

  def test_scheme_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().scheme"))

  def test_username_from_urlparse_urlparse(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlparse\n"
                                  "urlparse().username"))

  def test_fragment_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().fragment"))

  def test_hostname_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().hostname"))

  def test_netloc_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().netloc"))

  def test_password_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().password"))

  def test_path_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().path"))

  def test_port_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().port"))

  def test_query_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().query"))

  def test_scheme_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().scheme"))

  def test_username_from_urlparse_urlsplit(self):
    self.assertOnlyIn((2, 5),
                      self.detect("from urlparse import urlsplit\n"
                                  "urlsplit().username"))

  def test_is_safe_from_uuid_UUID(self):
    self.assertOnlyIn((3, 7),
                      self.detect("from uuid import UUID\n"
                                  "UUID().is_safe"))

  def test___callback___from_weakref_ref(self):
    self.assertOnlyIn((3, 4),
                      self.detect("from weakref import ref\n"
                                  "ref().__callback__"))

  def test_REG_QWORD_of_winreg(self):
    self.assertOnlyIn((3, 6), self.detect("from winreg import REG_QWORD"))

  def test_REG_QWORD_LITTLE_ENDIAN_of_winreg(self):
    self.assertOnlyIn((3, 6), self.detect("from winreg import REG_QWORD_LITTLE_ENDIAN"))

  def test_code_from_xml_parsers_expat_ExpatError(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import ExpatError\n"
                                  "ExpatError().code"))

  def test_lineno_from_xml_parsers_expat_ExpatError(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import ExpatError\n"
                                  "ExpatError().lineno"))

  def test_offset_from_xml_parsers_expat_ExpatError(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import ExpatError\n"
                                  "ExpatError().offset"))

  def test_CurrentByteIndex_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().CurrentByteIndex"))

  def test_CurrentColumnNumber_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().CurrentColumnNumber"))

  def test_CurrentLineNumber_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 4), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().CurrentLineNumber"))

  def test_buffer_size_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().buffer_size"))

  def test_buffer_text_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().buffer_text"))

  def test_buffer_used_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 3), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().buffer_used"))

  def test_ordered_attributes_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().ordered_attributes"))

  def test_returns_unicode_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn((2, 0),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().returns_unicode"))

  def test_specified_attributes_from_xml_parsers_expat_XMLParserType(self):
    self.assertOnlyIn(((2, 1), (3, 0)),
                      self.detect("from xml.parsers.expat import XMLParserType\n"
                                  "XMLParserType().specified_attributes"))

  def test_codes_from_xml_parsers_expat_errors(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from xml.parsers.expat import errors\n"
                                  "errors().codes"))

  def test_messages_from_xml_parsers_expat_errors(self):
    self.assertOnlyIn((3, 2),
                      self.detect("from xml.parsers.expat import errors\n"
                                  "errors().messages"))

  def test_eof_from_zlib_Decompress(self):
    self.assertOnlyIn((3, 3),
                      self.detect("from zlib import Decompress\n"
                                  "Decompress().eof"))

  def test_ZLIB_RUNTIME_VERSION_of_zlib(self):
    self.assertOnlyIn((3, 3), self.detect("from zlib import ZLIB_RUNTIME_VERSION"))

  def test_avoids_symlink_attacks_of_shutil_rmtree(self):
    self.assertOnlyIn((3, 3), self.detect("from shutil import rmtree\n"
                                          "rmtree.avoids_symlink_attacks"))

  def test_html5_of_html_entities(self):
    self.assertOnlyIn((3, 3), self.detect("from html.entities import html5"))

  def test_DOMSTRING_SIZE_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import DOMSTRING_SIZE_ERR"))

  def test_EMPTY_NAMESPACE_of_xml_dom(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from xml.dom import EMPTY_NAMESPACE"))

  def test_HIERARCHY_REQUEST_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import HIERARCHY_REQUEST_ERR"))

  def test_INDEX_SIZE_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import INDEX_SIZE_ERR"))

  def test_INUSE_ATTRIBUTE_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import INUSE_ATTRIBUTE_ERR"))

  def test_INVALID_ACCESS_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import INVALID_ACCESS_ERR"))

  def test_INVALID_CHARACTER_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import INVALID_CHARACTER_ERR"))

  def test_INVALID_MODIFICATION_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import INVALID_MODIFICATION_ERR"))

  def test_INVALID_STATE_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import INVALID_STATE_ERR"))

  def test_NAMESPACE_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NAMESPACE_ERR"))

  def test_NOT_FOUND_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NOT_FOUND_ERR"))

  def test_NOT_SUPPORTED_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NOT_SUPPORTED_ERR"))

  def test_NO_DATA_ALLOWED_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import NO_DATA_ALLOWED_ERR"))

  def test_NO_MODIFICATION_ALLOWED_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect(
        "from xml.dom import NO_MODIFICATION_ALLOWED_ERR"))

  def test_SYNTAX_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import SYNTAX_ERR"))

  def test_WRONG_DOCUMENT_ERR_of_xml_dom(self):
    self.assertOnlyIn(((2, 1), (3, 0)), self.detect("from xml.dom import WRONG_DOCUMENT_ERR"))

  def test_XHTML_NAMESPACE_of_xml_dom(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from xml.dom import XHTML_NAMESPACE"))

  def test_XMLNS_NAMESPACE_of_xml_dom(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from xml.dom import XMLNS_NAMESPACE"))

  def test_XML_NAMESPACE_of_xml_dom(self):
    self.assertOnlyIn(((2, 2), (3, 0)), self.detect("from xml.dom import XML_NAMESPACE"))

  def test_softkwlist_from_keyword(self):
    self.assertOnlyIn((3, 9), self.detect("from keyword import softkwlist"))

  def test_HAVE_CONTEXTVAR_from_decimal(self):
    self.assertOnlyIn((3, 7), self.detect("from decimal import HAVE_CONTEXTVAR"))

  def test_annotations_of___future__(self):
    self.assertOnlyIn((3, 7), self.detect("from __future__ import annotations"))

  def test_F_GETPATH_of_fcntl(self):
    self.assertOnlyIn((3, 9), self.detect("from fcntl import F_GETPATH"))

  def test_F_GETPIPE_SZ_of_fcntl(self):
    self.assertOnlyIn((3, 10), self.detect("from fcntl import F_GETPIPE_SZ"))

  def test_F_SETPIPE_SZ_of_fcntl(self):
    self.assertOnlyIn((3, 10), self.detect("from fcntl import F_SETPIPE_SZ"))

  def test_COLONEQUAL_of_token(self):
    self.assertOnlyIn((3, 8), self.detect("from token import COLONEQUAL"))

  def test_TYPE_IGNORE_of_token(self):
    self.assertOnlyIn((3, 8), self.detect("from token import TYPE_IGNORE"))

  def test_args_of_unittest_mock_Mock_call_args(self):
    self.assertOnlyIn((3, 8), self.detect("from unittest.mock.Mock.call_args import args"))
    self.assertTrue(self.config.add_backport("mock"))
    self.assertOnlyIn((3, 6), self.detect("from unittest.mock.Mock.call_args import args"))

  def test_kwargs_of_unittest_mock_Mock_call_args(self):
    self.assertOnlyIn((3, 8), self.detect("from unittest.mock.Mock.call_args import kwargs"))
    self.assertTrue(self.config.add_backport("mock"))
    self.assertOnlyIn((3, 6), self.detect("from unittest.mock.Mock.call_args import kwargs"))

  def test_status_of_urllib_response_addinfourl(self):
    self.assertOnlyIn((3, 9), self.detect("from urllib.response.addinfourl import status"))
