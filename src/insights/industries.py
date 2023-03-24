from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    conjunto = set()
    for index in data:
        if index["industry"] != "":
            result = index["industry"]
            conjunto.add(result)
    return conjunto


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    data = jobs
    result = []
    for index in data:
        if index["industry"] == industry:
            result.append(index)
    return result
    raise NotImplementedError
