import pytest

from All_home_works.hw4.task3 import my_precious_logger


def test_my_precious_logger__error_msg__test_msg_in_stderr(capsys):
    error = "error: 404"
    my_precious_logger(text=error)
    captured = capsys.readouterr()
    assert captured.err == error
    assert not captured.out


@pytest.mark.parametrize("input_data", ["Error: 404", "error 404"])
def test_my_precious_logger__error_msg_with_invalid_error_text__test_msg_not_in_stderr(
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
