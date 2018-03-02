from testutils import MinpyTest, detect

class MinpyClassMemberTests(MinpyTest):
  def test_ABC_of_abc(self):
    self.assertOnlyIn(3.4, detect("from abc import ABC"))

  def test_PathLike_of_os(self):
    self.assertOnlyIn(3.6, detect("from os import PathLike"))

  def test_terminal_size_of_os(self):
    self.assertOnlyIn(3.3, detect("from os import terminal_size"))

  def test_Barrier_of_multiprocessing(self):
    self.assertOnlyIn(3.3, detect("from multiprocessing import Barrier"))

  def test_TextTestResult_of_unittest(self):
    self.assertOnlyIn((2.7, 3.0), detect("from unittest import TextTestResult"))
