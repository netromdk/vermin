from .testutils import VerminTest, detect

class VerminDecoratorMemberTests(VerminTest):
  def test_asynccontextmanager_of_contextlib(self):
    self.assertOnlyIn(3.7, detect("from contextlib import asynccontextmanager"))

  def test_final_of_typing(self):
    self.assertOnlyIn(3.8, detect("from typing import final"))

  def test_runtime_checkable_of_typing(self):
    self.assertOnlyIn(3.8, detect("from typing import runtime_checkable"))
