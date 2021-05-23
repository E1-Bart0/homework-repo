"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    counter = 0
    for file_path in get_files_from_directory(dir_path, file_extension):
        with open(file_path) as file:
            if tokenizer is None:
                counter += count_lines(file)
            else:
                counter += count_tokens(file, tokenizer)
    return counter


def count_tokens(file, tokenizer):
    return len(tokenizer(file.read()))


def count_lines(file):
    counter = 0
    for line in file:  # noqa: B007
        counter += 1
    counter += 1 if counter and line.endswith("\n") else 0
    return counter


def get_files_from_directory(dir_path, file_extension):  # noqa: CCR001
    for dirpath, _, filenames in os.walk(dir_path):
        for file in filenames:
            if file.split(".")[-1] == file_extension:
                yield os.path.join(dirpath, file)
