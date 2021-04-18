from All_home_works.hw3.task4 import is_armstrong


def test_is_armstrong__ok_153():
    assert is_armstrong(153)


def test_is_armstrong__not_ok_10():
    assert not is_armstrong(10)


def test_is_armstrong__ok_9():
    assert is_armstrong(9)
