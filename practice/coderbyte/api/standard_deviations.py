import requests
import numpy as np
from typing import List


def get_sorted_numbers() -> List[int]:
    url = "https://coderbyte.com/api/challenges/json/list-numbers"
    r = requests.get(url)
    raw_numbers = r.json()['data']
    return sorted(raw_numbers)


def get_standard_deviation(numbers: List[int]) -> int:
    return round(np.std(numbers))


numbers = get_sorted_numbers()
extracted_numbers = numbers[:-2]
print(get_standard_deviation(numbers),
      get_standard_deviation(extracted_numbers),
      sep=' ')
