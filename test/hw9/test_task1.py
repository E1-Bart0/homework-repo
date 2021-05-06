import tempfile
from unittest.mock import patch

import pytest

from All_home_works.hw9.task1 import _get_nums_from_file, merge_sorted_files


@pytest.fixture(name="filename")
def make_file():
    file = tempfile.NamedTemporaryFile(mode="w")
    data = ["1\n", "2\n", "3\n"]
    file.writelines(data)
    file.seek(0)
    yield file.name
    file.close()


def test__get_nums_from_file(filename):
    expected = [1, 2, 3]
    result = list(_get_nums_from_file(filename))
    assert result == expected


@patch("All_home_works.hw9.task1._get_nums_from_file", return_value=iter([1, 2, 3, 4]))
def test__merge_sorted_files__check_one_file(_get_nums_from_file):  # noqa: PT019
    file_list = ["test"]
    result = merge_sorted_files(file_list)
    assert [1, 2, 3, 4] == list(result)


@patch(
    "All_home_works.hw9.task1._get_nums_from_file",
    side_effect=[iter([1, 3, 5]), iter([2, 4, 6])],
)
def test__merge_sorted_files__check_two_files(_get_nums_from_file):  # noqa: PT019
    file_list = ["test", "test"]
    result = merge_sorted_files(file_list)
    assert [1, 2, 3, 4, 5, 6] == list(result)


@patch(
    "All_home_works.hw9.task1._get_nums_from_file",
    side_effect=[iter([]), iter([2, 4, 6])],
)
def test__merge_sorted_files__check_two_files_but_one_file_is_empty(  # noqa: PT019
    _get_nums_from_file,
):
    file_list = ["test", "test"]
    result = merge_sorted_files(file_list)
    assert [2, 4, 6] == list(result)


@patch(
    "All_home_works.hw9.task1._get_nums_from_file",
    side_effect=[iter([1, 10]), iter([2, 3, 4, 6])],
)
def test__merge_sorted_files__check_two_files_but_one_file_is_longer_then_another(  # noqa: PT019
    _get_nums_from_file,
):
    file_list = ["test", "test"]
    result = merge_sorted_files(file_list)
    assert [1, 2, 3, 4, 6, 10] == list(result)


@patch(
    "All_home_works.hw9.task1._get_nums_from_file",
    side_effect=[iter([1, 6]), iter([2, 4]), iter([3, 5])],
)
def test__merge_sorted_files__check_tree_files(_get_nums_from_file):  # noqa: PT019
    file_list = ["test", "test", "test"]
    result = merge_sorted_files(file_list)
    assert [1, 2, 3, 4, 5, 6] == list(result)
