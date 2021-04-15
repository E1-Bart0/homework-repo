import unittest

from All_home_works.hw2.task4 import cache


class TestTask4(unittest.TestCase):
    def test_cache(self):
        some = 100, 200

        cache_fun = cache(self.func)
        val1 = cache_fun(*some)
        val2 = cache_fun(*some)
        self.assertEqual(val1, val2)

    @staticmethod
    def func(a, b):
        return (a ** b) ** 2
