import unittest

from All_home_works.hw2.task2 import major_and_minor_elem


class TestHW2Task2(unittest.TestCase):
    def test_major_and_minor_elem(self):
        input1 = [3, 2, 3]
        output1 = 3, 2
        self.assertEqual(output1, major_and_minor_elem(input1))

        input2 = [2, 2, 1, 1, 1, 2, 2]
        output2 = 2, 1
        self.assertEqual(output2, major_and_minor_elem(input2))

    def test_major_and_minor_elem_non_most_common(self):
        data = [1, 1, 1, 2, 2, 2, 0, 0, 0, 3]
        output = (None, 3)
        self.assertEqual(output, major_and_minor_elem(data))

    def test_major_and_minor_elem_non_min_common(self):
        data = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
        output = (3, None)
        self.assertEqual(output, major_and_minor_elem(data))
