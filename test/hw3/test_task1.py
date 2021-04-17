from All_home_works.hw3.task1 import cache

N = 4


@cache(times=N)
def f(attr=None):
    return attr


def test__cache():
    input_data = 1
    assert 1 == f(input_data)
    for _ in range(N - 1):
        assert 1 == f()
    assert not f()


if __name__ == "__main__":
    test__cache()
