import unittest

from All_home_works.hw1.task4 import find_maximal_subarray_sum


class TestTask4(unittest.TestCase):
    def test_find_maximal_subarray_sum__init_data(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]

        k = 3
        result = 16
        self.assertEqual(result, find_maximal_subarray_sum(nums, k))

    def test_find_maximal_subarray_sum__one_max(self):
        nums = [1, 3, -1, -3, -100, 1000, -100, 7]

        k = 5
        result = 1000
        self.assertEqual(result, find_maximal_subarray_sum(nums, k))

    def test_find_maximal_subarray_sum__(self):
        nums = [1, 100, -1, 0, 24, 432, 564, 76, 8, 8]

        k = 4
        result = 1096
        self.assertEqual(result, find_maximal_subarray_sum(nums, k))

    def test_find_maximal_subarray_sum__len100(self):
        nums = [
            9,
            -8,
            1,
            -8,
            -8,
            -6,
            -7,
            7,
            6,
            -8,
            5,
            -7,
            -1,
            -8,
            -7,
            -5,
            0,
            -4,
            -5,
            -8,
            0,
            6,
            10,
            6,
            -5,
            9,
            -3,
            1,
            8,
            4,
            0,
            -6,
            -7,
            2,
            -3,
            10,
            -9,
            -9,
            3,
            -9,
            3,
            3,
            3,
            -1,
            2,
            9,
            -6,
            1,
            0,
            -5,
            1,
            6,
            -9,
            1,
            6,
            -5,
            -7,
            -6,
            -1,
            10,
            -8,
            -3,
            -3,
            -5,
            -10,
            -6,
            -9,
            2,
            -1,
            7,
            -3,
            9,
            -3,
            -2,
            10,
            -3,
            7,
            -2,
            -6,
            9,
            9,
            9,
            1,
            4,
            1,
            10,
            0,
            0,
            8,
            -2,
        ]

        k = 3
        result = 27
        self.assertEqual(result, find_maximal_subarray_sum(nums, k))

    def test_find_maximal_subarray_sum__k_eq_len(self):
        nums = [
            -3,
            -3,
            -5,
            -10,
            -6,
            -100,
            2,
            -1,
            7,
            -3,
            9,
            -3,
            -2,
            10,
            -3,
            7,
            100,
            -6,
            9,
            9,
            9,
            1,
            4,
            1,
            10,
            0,
            0,
            8,
        ]

        k = len(nums)
        result = sum(
            [2, -1, 7, -3, 9, -3, -2, 10, -3, 7, 100, -6, 9, 9, 9, 1, 4, 1, 10, 0, 0, 8]
        )
        self.assertEqual(result, find_maximal_subarray_sum(nums, k))

    def test_find_maximal_subarray_sum__k_more_len(self):
        nums = [
            -3,
            -3,
            -5,
            -10,
            -6,
            -100,
            2,
            -1,
            7,
            -3,
            9,
            -3,
            -2,
            10,
            -3,
            7,
            100,
            -6,
            9,
            9,
            9,
            1,
            4,
            1,
            10,
            0,
            0,
            8,
        ]

        k = len(nums) * 2
        result = sum(
            [2, -1, 7, -3, 9, -3, -2, 10, -3, 7, 100, -6, 9, 9, 9, 1, 4, 1, 10, 0, 0, 8]
        )
        self.assertEqual(result, find_maximal_subarray_sum(nums, k))
