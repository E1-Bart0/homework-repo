import unittest

from All_home_works.hw2.task3 import combinations


class TestTask3(unittest.TestCase):
    def test_combinations(self):
        data = [[1, 2], [3, 4]]
        res = [
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
        ]
        self.assertEqual(res, combinations(*data))

        data = [[1, 2, 3], [4, 5, 6]]
        res = [
            [1, 4],
            [1, 5],
            [1, 6],
            [2, 4],
            [2, 5],
            [2, 6],
            [3, 4],
            [3, 5],
            [3, 6],
        ]
        self.assertEqual(res, combinations(*data))

        data = [[1, 2], [3, 4], [5, 6]]
        res = [
            [1, 3, 5],
            [1, 3, 6],
            [1, 4, 5],
            [1, 4, 6],
            [2, 3, 5],
            [2, 3, 6],
            [2, 4, 5],
            [2, 4, 6],
        ]
        self.assertEqual(res, combinations(*data))
