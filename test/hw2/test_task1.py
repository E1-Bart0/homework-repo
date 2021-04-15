import os
import unittest

from All_home_works.hw2.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

TEXT = """
Lorem Ipsum is simply dummy text of the printing and typesettingLalaBlabla
 industryDrvgtr. 1 Rarest non ascii is \u00dc and Most common \u00e4
Lorem Ipsum has been the industry's \u00e4 2 standard dummy text ever since the 1500s, 3
when an \u00e4 unknown printer took a galley of type and scrambled it to make a type specimen book. 4
It has survived not only five centuries, 5 but also the leap into electronic typesetting, 6
remaining essentially unchanged. 7 It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, 8 and more recently with desktop publishing software like
Aldus PageMaker \u00e4 including versions of Lorem Ipsum. 9

It will be the rarest unique punctuationQWERqwertyuiYUipodsajksd symbol!!!!? 14
Interesting that it rarest is z but not xxxxxx. 15

Large Words = typesetting 16
"""


class TestTask1(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = "Test_hw1.txt"
        with open(self.file_path, mode="w", encoding="raw_unicode_escape") as file:
            file.write(TEXT)

    def test_get_longest_diverse_words(self):
        result_start_with = [
            "punctuationQWERqwertyuiYUipodsajksd",
            "typesettingLalaBlabla",
            "industryDrvgtr",
        ]
        checking = get_longest_diverse_words(self.file_path)
        assert 10 == len(checking)
        assert result_start_with == checking[: len(result_start_with)]

    def test_get_rarest_char(self):
        rarest_char = "z"
        assert rarest_char == get_rarest_char(self.file_path)

    def test_count_punctuation_chars(self):
        result = 16
        assert result == count_punctuation_chars(self.file_path)

    def test_count_non_ascii_chars(self):
        result = 5
        assert result == count_non_ascii_chars(self.file_path)

    def test_get_most_common_non_ascii_char(self):
        result = "ä"
        assert result == get_most_common_non_ascii_char(self.file_path)

    def tearDown(self) -> None:
        os.remove(self.file_path)
