def read(path: str) -> List[Dict]:
    result = []
    with open(path, 'r') as file:
        result = list(csv.DictReader(file))
    return result