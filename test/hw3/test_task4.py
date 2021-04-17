from All_home_works.hw3.task4 import is_armstrong


def test_is_armstrong_case1():
    assert is_armstrong(153)


def test_is_armstrong_case2():
    assert not is_armstrong(10)


def test_is_armstrong_case3():
    assert is_armstrong(9)


if __name__ == "__main__":
    test_is_armstrong_case1()
    test_is_armstrong_case2()
    test_is_armstrong_case3()
