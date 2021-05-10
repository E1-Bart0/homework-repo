"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    num_generators = [_get_nums_from_file(file) for file in file_list]
    numbers = [
        (index, next(number, float("inf")))
        for index, number in enumerate(num_generators)
    ]
    stop = all(num[1] == float("inf") for num in numbers)
    while not stop:
        num, stop = _get_min_number(numbers, num_generators, stop)
        yield num


def _get_min_number(numbers, num_generators, stop):
    index, num = min(numbers, key=lambda x: x[1])
    next_number = next(num_generators[index], float("inf"))
    numbers[index] = (index, next_number)
    if next_number == float("inf"):
        stop = all(num[1] == float("inf") for num in numbers)
    return num, stop


def _get_nums_from_file(filename):
    with open(filename) as file:
        for line in file:
            line = line.rstrip("\n")
            yield int(line)
