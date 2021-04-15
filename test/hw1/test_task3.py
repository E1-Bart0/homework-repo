from All_home_works.hw1.task3 import check_sum_of_four


def test_check_sum_of_four():
    data = [[7, -7, -5], [-7, 5, -2], [-7, 0, -10], [-3, 0, 2]]

    result = check_sum_of_four(*data)
    assert 4 == result


def test_check_sum_of_four_with_zeros():
    length_list = 10
    data = [[0] * length_list for _ in range(4)]

    result = check_sum_of_four(*data)
    assert length_list ** 4 == result
