import json
import os
from itertools import repeat
from multiprocessing import Pool
from operator import itemgetter

from All_home_works.hw10.task1_get_result import main as get_data_about_companies


def top_most_expensive_companies(data, limit):
    return sorted(data, key=itemgetter("price"), reverse=True)[:limit]


def top_fewest_pe_rating_companies(data, limit):
    return sorted(
        data, key=lambda x: x["P/E"] if x["P/E"] is not None else float("inf")
    )[:limit]


def top_most_growth_companies(data, limit):
    return sorted(
        data,
        key=lambda x: x["growth"] if x["growth"] is not None else float("-inf"),
        reverse=True,
    )[:limit]


def top_most_profit_companies(data, limit):
    return sorted(
        data,
        key=lambda x: x["potential profit"]
        if x["potential profit"] is not None
        else float("-inf"),
        reverse=True,
    )[:limit]


def save_to_file(func, data, limit):
    result = func(data, limit)
    path = func.__name__ + ".json"
    with open(path, mode="w") as file:
        json.dump(result, file, ensure_ascii=False)


def save():
    data_about_companies = get_data_about_companies()
    functions = (
        top_most_expensive_companies,
        top_fewest_pe_rating_companies,
        top_most_growth_companies,
        top_most_profit_companies,
    )
    limit = min(len(data_about_companies), 11)
    with Pool(os.cpu_count()) as pool:
        pool.starmap(
            save_to_file, zip(functions, repeat(data_about_companies), repeat(limit))
        )
