import requests
import numpy as np
import pandas as pd
from typing import List


def parse_ages(data: str) -> List[int]:
    values = [v.split("=")[1] for v in data.split(", ")]
    # keys = values[:: 2]
    # {key: int(age) for age, key in zip(ages, keys)}
    return map(int, values[1::2])


r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
raw_data = r.json()['data']
ages = parse_ages(raw_data)

answer = sum([1 for age in ages if age >= 50])
print(answer)
