import string
import unittest

from All_home_works.hw2.task5 import custom_range


class TestTask5(unittest.TestCase):
    def test_custom_range_str(self):
        self.assertEqual(
            ["a", "b", "c", "d", "e", "f"], custom_range(string.ascii_lowercase, "g")
        )
        self.assertEqual(
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
            custom_range(string.ascii_lowercase, "g", "p"),
        )
        self.assertEqual(
            ["p", "n", "l", "j", "h"],
            custom_range(string.ascii_lowercase, "p", "g", -2),
        )
