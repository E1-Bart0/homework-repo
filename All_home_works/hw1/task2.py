"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as data_file:
        max_value, min_value = get_first_value_in(data_file)
        for line in data_file.readlines():
            line = line[:-1]
            if line:
                num = int(line)
                max_value, min_value = check_max_min_value(max_value, min_value, num)
    return min_value, max_value


def get_first_value_in(data_file):
    line = data_file.readline()[:-1]
    min_value = max_value = int(line)
    return max_value, min_value


def check_max_min_value(max_value, min_value, num):
    if num > max_value:
        max_value = num
    elif num < min_value:
        min_value = num
    return max_value, min_value
