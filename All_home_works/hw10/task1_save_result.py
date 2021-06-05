import json
import os
from itertools import repeat
from multiprocessing import Pool
from operator import itemgetter

from All_home_works.hw10.task1_get_result import get_result


def get_length(data):
    return max(len(data), 11)


def top_most_expensive_companies(data):
    return sorted(data, key=itemgetter("price"), reverse=True)[: get_length(data)]


def top_fewest_pe_rating_companies(data):
    return sorted(
        data, key=lambda x: x["P/E"] if x["P/E"] is not None else float("inf")
    )[: get_length(data)]


def top_most_growth_companies(data):
    return sorted(
        data,
        key=lambda x: x["growth"] if x["growth"] is not None else float("-inf"),
        reverse=True,
    )[: get_length(data)]


def top_most_profit_companies(data):
    return sorted(
        data,
        key=lambda x: x["potential profit"]
        if x["potential profit"] is not None
        else float("-inf"),
        reverse=True,
    )[: get_length(data)]


def save_to_file(func, data):
    result = func(data)
    path = func.__name__ + ".json"
    with open(path, mode="w") as file:
        json.dump(result, file, ensure_ascii=False)


def save():
    data = get_result()
    func = (
        top_most_expensive_companies,
        top_fewest_pe_rating_companies,
        top_most_growth_companies,
        top_most_profit_companies,
    )
    with Pool(os.cpu_count()) as pool:
        pool.starmap(save_to_file, zip(func, repeat(data)))
