import unittest
import sys, os


sys.path.insert(0, os.path.abspath("../.."))

from lib.solutions.hello import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("John"), "Hello, John!")

    def test_hello_return_type(self):
        self.assertTrue(isinstance(hello("world"), str))

if __name__ == '__main__':
    unittest.main()
