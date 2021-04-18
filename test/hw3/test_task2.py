from All_home_works.hw3.task2 import sum_of_slow_calculate


def test_sum_of_slow_calculate():
    expected = 1024259
    result = sum_of_slow_calculate()

    assert expected == result


if __name__ == "__main__":
    test_sum_of_slow_calculate()
