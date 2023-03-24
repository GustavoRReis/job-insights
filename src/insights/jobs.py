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
    conjunto = set()
    for index in data:
        result = index["job_type"]
        conjunto.add(result)
    return conjunto


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


if __name__ == "__main__":
    data_read = read('data/jobs.csv')
    data_get_unique_job_types = get_unique_job_types('data/jobs.csv')
