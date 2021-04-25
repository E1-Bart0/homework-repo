"""
Here's a not very efficient calculation function that calculates something important:

import time
import struct
import random
import hashlib

def slow_calculate(value):

    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
 Calculation time should not take more than a minute.
 Use functional capabilities of multiprocessing module.
  You are not allowed to modify slow_calculate function.
"""
import hashlib
import random
import struct
import time
from multiprocessing import Pool

import matplotlib.pyplot as plt


def timer(func):
    def wrapper(num):
        start = time.time()
        res = func(num)
        finish = time.time() - start
        finish_per_number = finish / num
        return res, finish, finish_per_number

    return wrapper


def slow_calculate(value):
    time.sleep(random.randint(1, 3))  # noqa: S311
    data = hashlib.md5(str(value).encode()).digest()  # noqa: S303
    return sum(struct.unpack("<" + "B" * len(data), data))


@timer
def sum_of_slow_calculate(max_value=500):
    pool = Pool(processes=max_value)
    array = pool.map(slow_calculate, range(max_value))
    return sum(array)


def get_data(data):
    res = []
    [res.append(sum_of_slow_calculate(i)[1:]) for i in data]
    return res


def plot():
    x = list(range(1, 50)) + list(range(50, 500, 50))
    y = get_data(x)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(
        x,
        y,
    )
    plt.show()
