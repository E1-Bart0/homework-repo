from All_home_works.hw3.task2 import sum_of_slow_calculate


def test_sum_of_slow_calculate():
    expected = 1024259
    max_time = 60
    result, time = sum_of_slow_calculate()

    assert expected == result
    assert max_time > time


if __name__ == "__main__":
    test_sum_of_slow_calculate()
