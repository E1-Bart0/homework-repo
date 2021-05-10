import json
import os
from itertools import repeat
from multiprocessing import Pool

from All_home_works.hw10.task1_get_result import get_result


def top_most_expensive_companies(data):
    length = max(len(data), 11)
    return sorted(data, key=lambda x: x["price"], reverse=True)[:length]


def top_fewest_pe_rating_companies(data):
    length = max(len(data), 11)
    return sorted(
        data, key=lambda x: x["P/E"] if x["P/E"] is not None else float("inf")
    )[:length]


def top_most_growth_companies(data):
    length = max(len(data), 11)
    return sorted(
        data,
        key=lambda x: x["growth"] if x["growth"] is not None else float("-inf"),
        reverse=True,
    )[:length]


def top_most_profit_companies(data):
    length = max(len(data), 11)
    return sorted(
        data,
        key=lambda x: x["potential profit"]
        if x["potential profit"] is not None
        else float("-inf"),
        reverse=True,
    )[:length]


def save_to_file(args):
    data, func = args
    result = func(data)
    path = func.__name__ + ".txt"
    with open(path, mode="w") as file:
        json.dump(result, file, ensure_ascii=False)


async def save():
    data = await get_result()
    func = (
        top_most_expensive_companies,
        top_fewest_pe_rating_companies,
        top_most_growth_companies,
        top_most_profit_companies,
    )
    with Pool(os.cpu_count()) as pool:
        pool.map(save_to_file, zip(repeat(data), func))
