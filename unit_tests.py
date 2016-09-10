import unittest
from flatten_array import *

class TestMethods(unittest.TestCase):

  def test_arrays(self):
      self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])
      self.assertEqual(flatten([1, [2, 3]]), [1, 2, 3])
      self.assertEqual(flatten([1, [2, [[3]]]]), [1, 2, 3])
      self.assertEqual(flatten([1, [2, [3, [4]]]]), [1, 2, 3, 4])
      self.assertEqual(flatten([[[1]], [2, [[3]]]]), [1, 2, 3])
      self.assertEqual(flatten([1, {"a": 2}, 3]), [1, {"a": 2}, 3])

if __name__ == '__main__':
    unittest.main()
