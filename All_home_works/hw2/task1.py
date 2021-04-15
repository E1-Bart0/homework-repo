"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter, deque
from typing import List

TRANSLATE = str.maketrans({char: "" for char in string.punctuation})


def _get_lines(file_path: str) -> str:
    with open(file_path, encoding="raw_unicode_escape") as reading_file:
        for line in reading_file.readlines():
            line = line[:-1]
            if line:
                yield line


def get_longest_diverse_words(file_path: str) -> List[str]:
    queue = deque()
    for line in _get_lines(file_path):
        line = line.translate(TRANSLATE)
        words = [(word, len(set(word))) for word in line.split() if word]
        queue = _check_words(queue, words)

    return [word[0] for word in reversed(queue)]


def _check_words(queue, words):
    for word, len_word in words:
        if len(queue) < 10:
            queue.append((word, len_word))
            continue

        queue = sorted(queue, key=lambda x: x[1])
        if len_word > queue[0][1]:
            queue.append((word, len_word))
            queue.pop(0)
    return queue


def get_rarest_char(file_path: str) -> str:
    counter = Counter()
    for line in _get_lines(file_path):
        _check_char_in(line, counter)
    return list(reversed(counter.most_common()))[0][0]


def _check_char_in(line, counter):
    for char in line:
        if char not in string.punctuation and ord(char) < 126:
            counter[char] += 1


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    for line in _get_lines(file_path):
        for char in line:
            counter = _check_punctuation(char, counter)
    return counter


def _check_punctuation(char, counter):
    if char in string.punctuation:
        counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    for line in _get_lines(file_path):
        for char in line:
            counter = _check_non_ascii(char, counter)
    return counter


def _check_non_ascii(char, counter):
    if ord(char) > 126:
        if isinstance(counter, int):
            counter += 1
        else:
            counter[char] += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter = Counter()
    for line in _get_lines(file_path):
        for char in line:
            _check_non_ascii(char, counter)
    return counter.most_common()[0][0]
