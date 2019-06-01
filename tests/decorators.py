from .testutils import VerminTest, detect

class VerminDecoratorMemberTests(VerminTest):
  def test_asynccontextmanager_of_contextlib(self):
    self.assertOnlyIn(3.7, detect("from contextlib import asynccontextmanager"))
