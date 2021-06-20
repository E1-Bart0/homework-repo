from All_home_works.hw3.task2 import sum_of_slow_calculate


def test_sum_of_slow_calculate():
    expected = 1025932
    result = sum_of_slow_calculate()

    assert expected == result
