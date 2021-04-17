from All_home_works.hw1.task1 import check_fibonacci


def test_check_valid_data():
    data = (
        0,
        1,
        1,
        2,
    )
    assert check_fibonacci(data)


def test_check_valid_data__not_from_begin():
    data = (
        8,
        13,
        21,
    )
    assert check_fibonacci(data)


def test_check_no_data():
    data = ()
    assert not check_fibonacci(data)


def test_check_invalid_data_first():
    data = (
        5,
        0,
        1,
    )
    assert not check_fibonacci(data)


def test_check_invalid_data_last():
    data = (
        0,
        1,
        1,
        2,
        3,
        1,
    )
    assert not check_fibonacci(data)


def test_check_invalid_data_middle():
    data = (
        0,
        1,
        100000,
        144,
    )
    assert not check_fibonacci(data)


def test_check_invalid_data_not_from_begin():
    data = (13, 22, 34)

    assert not check_fibonacci(data)
