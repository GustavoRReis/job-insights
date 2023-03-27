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

    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        is_salary = int(salary)
    except (KeyError, TypeError, ValueError):
        raise ValueError("Valor invalido")

    if min_salary > max_salary:
        raise ValueError(
            "O valor do salario minimo é maior que o valor do salario maximo"
        )
    result = min_salary <= is_salary <= max_salary
    return result


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    result = []
    for index in jobs:
        try:
            if matches_salary_range(index, salary):
                result.append(index)
        except ValueError:
            pass

    return result


if __name__ == "__main__":
    print(get_max_salary("data/jobs.csv"))
    print(get_min_salary("data/jobs.csv"))
