import unittest
import sys, os


sys.path.insert(0, os.path.abspath("../.."))

from lib.solutions.checkout import checkout


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        self.assertEqual(checkout("AABC"), 150)

    def test_checkout_a_deal(self):
        self.assertEqual(checkout("AAABC"), 180)

    def test_checkout_b_deal(self):
        self.assertEqual(checkout("ABBC"), 115)

    def test_checkout_illegal(self):
        self.assertEqual(checkout(15), -1)


if __name__ == '__main__':
    unittest.main()
