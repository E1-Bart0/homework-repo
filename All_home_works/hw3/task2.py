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


def slow_calculate(value):
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        delta = time.time() - start
        return result, delta

    return wrapper


@timer
def sum_of_slow_calculate(max_value=500):
    pool = Pool(processes=max_value)
    array = pool.map(slow_calculate, range(max_value))
    return sum(array)
