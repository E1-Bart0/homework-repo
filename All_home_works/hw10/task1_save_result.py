import json
import os
from multiprocessing import Pool
from operator import itemgetter

from All_home_works.hw10.task1_get_result import CollectDataAboutCompany


class SaveDataAboutCompanies:
    def __init__(self):
        self.data = None
        self.limit = None

    @staticmethod
    def top_most_expensive_companies(data, limit):
        return sorted(data, key=itemgetter("price"), reverse=True)[:limit]

    @staticmethod
    def top_fewest_pe_rating_companies(data, limit):
        return sorted(
            data, key=lambda x: x["P/E"] if x["P/E"] is not None else float("inf")
        )[:limit]

    @staticmethod
    def top_most_growth_companies(data, limit):
        return sorted(
            data,
            key=lambda x: x["growth"] if x["growth"] is not None else float("-inf"),
            reverse=True,
        )[:limit]

    @staticmethod
    def top_most_profit_companies(data, limit):
        return sorted(
            data,
            key=lambda x: x["potential profit"]
            if x["potential profit"] is not None
            else float("-inf"),
            reverse=True,
        )[:limit]

    def save_to_file(self, func):
        result = func(self.data, self.limit)
        path = func.__name__ + ".json"
        with open(path, mode="w") as file:
            json.dump(result, file, ensure_ascii=False)

    def save(self):
        self.data = CollectDataAboutCompany().run()
        functions = (
            self.top_most_expensive_companies,
            self.top_fewest_pe_rating_companies,
            self.top_most_growth_companies,
            self.top_most_profit_companies,
        )
        self.limit = max(len(self.data), 11)
        with Pool(os.cpu_count()) as pool:
            pool.map(self.save_to_file, functions)
