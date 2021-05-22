import tempfile
import unittest

from All_home_works.hw1.task2 import find_maximum_and_minimum


class HomeWork1Task2Tests(unittest.TestCase):
    def setUp(self):
        data = [
            0,
            10,
            100,
        ]
        self.min_value = 0
        self.max_value = 100
        self.file = self._get_file(data)

    @staticmethod
    def _get_file(data):
        file = tempfile.NamedTemporaryFile(mode="w")
        [file.write(str(num) + "\n") for num in data]
        file.seek(0)
        return file

    def test_find_maximum_and_minimum(self):
        result = find_maximum_and_minimum(self.file.name)
        assert (self.min_value, self.max_value) == result

    def tearDown(self):
        self.file.close()
