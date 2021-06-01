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
    numbers_generators = _get_numbers_and_generators(file_list)

    while numbers_generators:
        num__gen = min(numbers_generators, key=lambda x: x[0])
        yield num__gen[0]

        next_number = next(num__gen[1], None)
        if next_number is None:
            numbers_generators.remove(num__gen)
            continue
        num__gen[0] = next_number


def _get_numbers_and_generators(file_list):
    numbers_generators = []
    for file in file_list:
        generator = _get_nums_from_file(file)
        first_num = next(generator, None)
        if first_num is not None:
            numbers_generators.append([first_num, generator])
    return numbers_generators


def _get_nums_from_file(filename):
    with open(filename) as file:
        for line in file:
            line = line.rstrip("\n")
            yield int(line)
