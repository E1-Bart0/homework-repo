from All_home_works.hw4.task3 import my_precious_logger


def test_my_precious_logger__error_msg__test_msg_in_stderr(capsys):
    error = "error: 404"
    my_precious_logger(text=error)
    captured = capsys.readouterr()
    assert captured.err == error
    assert not captured.out


def test_my_precious_logger__ok__msg__test_msg_in_stdout(capsys):
    text = "OK: 200"
    my_precious_logger(text=text)
    captured = capsys.readouterr()
    assert captured.out == text
    assert not captured.err
