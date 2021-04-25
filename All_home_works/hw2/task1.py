"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List

PUNCTUATION = {char: "" for char in string.punctuation}
CROP_PUNCTUATION = str.maketrans(PUNCTUATION)


class Counter:
    def __init__(self):
        self.counter = {}

    def add(self, key):
        if key in self.counter:
            self.counter[key] += 1
        else:
            self.counter[key] = 0

    @property
    def sort_counter(self):
        sorted_counter = sorted(
            self.counter.items(), key=lambda item: item[1], reverse=True
        )
        return list(sorted_counter)


def _get_lines(file_path: str) -> str:
    with open(file_path, encoding="raw_unicode_escape") as reading_file:
        for line in reading_file:
            line = line.rstrip("\n")
            if line:
                yield line


def get_longest_diverse_words(file_path: str) -> List[str]:
    queue = []
    for line in _get_lines(file_path):
        line = line.translate(CROP_PUNCTUATION)
        words = [(word, len(set(word))) for word in line.split() if word]
        queue = _check_words(queue, words)

    return [word[0] for word in sorted(queue, key=lambda item: item[1], reverse=True)]


def _check_words(queue, words):
    for word, len_word in words:
        if len(queue) < 10:
            queue.append((word, len_word))
            continue

        index_word_len = min(enumerate(queue), key=lambda item: item[1][1])
        if len_word > index_word_len[1][1]:
            queue[index_word_len[0]] = (word, len_word)
    return queue


def get_rarest_char(file_path: str) -> str:
    counter = Counter()
    for line in _get_lines(file_path):
        [counter.add(char) for char in line if char.isalpha()]
    return list(reversed(counter.sort_counter))[0][0]


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    for line in _get_lines(file_path):
        counter += sum([1 for char in line if char in PUNCTUATION])
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    for line in _get_lines(file_path):
        counter += sum([1 for char in line if not char.isascii()])
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter = Counter()
    for line in _get_lines(file_path):
        [counter.add(char) for char in line if not char.isascii()]
    return counter.sort_counter[0][0]
