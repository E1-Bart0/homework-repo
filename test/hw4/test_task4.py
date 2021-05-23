from tempfile import NamedTemporaryFile
from unittest.mock import patch

import pytest

from All_home_works.hw4.task1 import get_first_line, read_magic_number


@pytest.fixture(scope="module")
def file():
    data = "1"
    file = NamedTemporaryFile(mode="w")
    file.write(data)
    file.seek(0)
    yield file
    file.close()


def test_get_first_line(file):
    expect = "1"
    line = get_first_line(path=file.name)
    assert expect == line


def test_get_first_line_file_not_exist(file):
    with pytest.raises(ValueError, match="No such file: "):
        get_first_line(path="NOT/EXIST")


@patch("All_home_works.hw4.task1.get_first_line", return_value="1")
def test_read_magic_number__valid_number_in_interval(file):
    assert read_magic_number("")


@patch("All_home_works.hw4.task1.get_first_line", return_value="0")
def test_read_magic_number__valid_number_beneath_interval(file):
    assert not read_magic_number("")


@patch("All_home_works.hw4.task1.get_first_line", return_value="3")
def test_read_magic_number__valid_number_upper_interval(file):
    assert not read_magic_number("")


@patch("All_home_works.hw4.task1.get_first_line", return_value="str_instance")
def test_read_magic_number__not_valid_data__str_instead_of_num(file):
    with pytest.raises(ValueError, match="Expected a digit, got: "):
        read_magic_number("")
