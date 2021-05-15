import pytest

from All_home_works.hw4.task3 import my_precious_logger


@pytest.mark.parametrize("input_data", ["error: 404", "error 404", "errorerrorText"])
def test_my_precious_logger__error_msg__test_msg_in_stderr(capsys, input_data):
    my_precious_logger(text=input_data)
    captured = capsys.readouterr()
    assert captured.err == input_data
    assert not captured.out


@pytest.mark.parametrize("input_data", ["Error: 404", "ERROR: 404"])
def test_my_precious_logger__error_msg_with_invalid_error_text__test_msg_not_in_stderr(
    capsys, input_data
):
    my_precious_logger(text=input_data)
    captured = capsys.readouterr()
    assert input_data == captured.out
    assert not captured.err


@pytest.mark.parametrize("input_data", [" error: 404", "An error: 404"])
def test_my_precious_logger__if_error_in_line_but_line_starts_with_no_error__msg_in_stdout(
    capsys, input_data
):
    my_precious_logger(text=input_data)
    captured = capsys.readouterr()
    assert input_data == captured.out
    assert not captured.err


def test_my_precious_logger__ordinary_msg__test_msg_in_stdout(capsys):
    text = "200"
    my_precious_logger(text=text)
    captured = capsys.readouterr()
    assert captured.out == text
    assert not captured.err
