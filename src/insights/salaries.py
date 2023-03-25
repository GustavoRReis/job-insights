from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = 0
    for index in data:
        if index["max_salary"].isdigit():
            value = int(index["max_salary"])
            if value > int(max_salary):
                max_salary = value
    print(type(max_salary))
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    max_salary = 383416
    for index in data:
        if index["min_salary"].isdigit():
            value = int(index["min_salary"])
            if value < int(max_salary):
                max_salary = value
    print(type(max_salary))
    return max_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("valor ausente")
    if not isinstance(job["min_salary"], (int)) or not isinstance(
        job["max_salary"], (int)
    ):
        raise ValueError("valor informado nao e numerico")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Valor de min_salary é maior que max_salary")
    if not isinstance(salary, (int, str)):
        raise ValueError("nao tem valor numerico")

    is_salary = int(salary)
    return job["min_salary"] <= is_salary <= job["max_salary"]


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


if __name__ == "__main__":
    print(get_max_salary("data/jobs.csv"))
    print(get_min_salary("data/jobs.csv"))
