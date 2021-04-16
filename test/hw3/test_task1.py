from All_home_works.hw3.task1 import cache

N = 4


@cache(times=N)
def f():
    return input("? ")


def test__cache():
    for _ in range(N):
        f()


if __name__ == "__main__":
    test__cache()
