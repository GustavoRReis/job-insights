from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        result = []
        with open(path, "r") as file:
            result = list(csv.DictReader(file))
    except FileNotFoundError:
        print("File not found")
    return result


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    result = set()
    for index in data:
        result.add(index["job_type"])
    return result


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    data = jobs
    result = []
    for index in data:
        if index["job_type"] == job_type:
            result.append(index)
    return result


if __name__ == "__main__":
    data_read = read("data/jobs.csv")
    data_get_unique_job_types = get_unique_job_types("data/jobs.csv")
    print(filter_by_job_type(data_read, "OTHER"))
    print(data_get_unique_job_types)
