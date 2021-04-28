from All_home_works.hw4.task3 import my_precious_logger

ERROR = "error: 404"
TEXT = "OK: 200"


def test_my_precious_logger__error_msg__test_msg_in_stderr(capsys):
    my_precious_logger(text=ERROR)
    captured = capsys.readouterr()
    assert captured.err == ERROR


def test_my_precious_logger__error_msg__test_none_in_stdout(capsys):
    my_precious_logger(text=ERROR)
    captured = capsys.readouterr()
    assert not captured.out


def test_my_precious_logger__ok__msg__test_msg_in_stdout(capsys):
    my_precious_logger(text=TEXT)
    captured = capsys.readouterr()
    assert captured.out == TEXT


def test_my_precious_logger__ok_msg__test_none_in_stderr(capsys):
    my_precious_logger(text=TEXT)
    captured = capsys.readouterr()
    assert not captured.err
