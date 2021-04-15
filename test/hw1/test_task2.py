import os
import unittest

from All_home_works.hw1.task2 import find_maximum_and_minimum


class Task3Test(unittest.TestCase):
    def setUp(self):
        data = [
            0,
            123,
            432,
            5,
            6,
            7,
            8,
            23,
            5,
            65,
            -321,
        ]
        self.min_value = min(data)
        self.max_value = max(data)

        self.file_name = "test_task3.txt"
        self._fill_txt(self.file_name, data)

    @staticmethod
    def _fill_txt(file_name, data):
        with open(file_name, mode="w") as file:
            [file.write(str(num) + "\n") for num in data]

    def test_find_maximum_and_minimum(self):
        result = find_maximum_and_minimum(self.file_name)
        self.assertEqual((self.min_value, self.max_value), result)

    def tearDown(self):
        os.remove(self.file_name)
