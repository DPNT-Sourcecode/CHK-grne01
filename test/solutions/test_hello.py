import unittest
import sys, os


sys.path.insert(0, os.path.abspath("../.."))

from lib.solutions.sum import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

    def test_sum_pos(self):
    	self.assertTrue(sum(1, 1) >= 0)

    def test_sum_neg(self):
    	self.assertTrue(sum(1, -11) < 0)

    def test_sum_type(self):
    	with self.assertRaises(TypeError):
   			sum("a", 0)


if __name__ == '__main__':
    unittest.main()
