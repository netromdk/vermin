from .testutils import VerminTest

class VerminDecoratorMemberTests(VerminTest):
  def test_abstractclassmethod_of_abc(self):
    self.assertOnlyIn((3, 2), self.detect("from abc import abstractclassmethod"))

  def test_abstractstaticmethod_of_abc(self):
    self.assertOnlyIn((3, 2), self.detect("from abc import abstractstaticmethod"))

  def test_asynccontextmanager_of_contextlib(self):
    self.assertOnlyIn((3, 7), self.detect("from contextlib import asynccontextmanager"))

  def test_cached_property_of_functools(self):
    self.assertOnlyIn((3, 8), self.detect("from functools import cached_property"))

  def test_lru_cache_of_functools(self):
    self.assertOnlyIn((3, 2), self.detect("from functools import lru_cache"))

  def test_partial_method_of_functools(self):
    self.assertOnlyIn((3, 4), self.detect("from functools import partial_method"))

  def test_singledispatch_of_functools(self):
    self.assertOnlyIn((3, 4), self.detect("from functools import singledispatch"))

  def test_singledispatchmethod_of_functools(self):
    self.assertOnlyIn((3, 8), self.detect("from functools import singledispatchmethod"))

  def test_total_ordering_of_functools(self):
    self.assertOnlyIn(((2, 7), (3, 2)), self.detect("from functools import total_ordering"))

  def test_cache_of_functools(self):
    self.assertOnlyIn((3, 9), self.detect("from functools import cache"))

  def test_recursive_repr_of_reprlib(self):
    self.assertOnlyIn((3, 2), self.detect("from reprlib import recursive_repr"))

  def test_final_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import final"))

  def test_runtime_checkable_of_typing(self):
    self.assertOnlyIn((3, 8), self.detect("from typing import runtime_checkable"))

  def test_expectedFailure_of_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from unittest import expectedFailure"))

  def test_skip_of_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from unittest import skip"))

  def test_skipIf_of_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from unittest import skipIf"))

  def test_skipUnless_of_unittest(self):
    self.assertOnlyIn(((2, 7), (3, 1)), self.detect("from unittest import skipUnless"))
