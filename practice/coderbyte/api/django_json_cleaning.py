import copy
import requests
from typing import Union, List, Dict, Any, Optional

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, None]
REMOVAL_KEYS = tuple(['N/A', '', '-'])


def get_json() -> JSON:
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
    return r.json()  # type: ignore


def clean_str(data: str) -> Optional[str]:
    return None if data in REMOVAL_KEYS else data


def clean_list(data: List[Any]) -> List[Any]:
    copied_list = copy.deepcopy(data)
    for i, raw_value in enumerate(data):
        value = clean(raw_value)
        if value is None:
            copied_list.pop(i)
    return copied_list


def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    copied_dict = copy.deepcopy(data)
    for k, raw_value in data.items():
        value = clean(raw_value)
        if value is None:
            copied_dict.pop(k)
        else:
            copied_dict[k] = value
    return copied_dict


def clean(data: JSON) -> JSON:
    if isinstance(data, dict):
        return clean_dict(data)
    if isinstance(data, list):
        return clean_list(data)
    if isinstance(data, str):
        return clean_str(data)
    return data


raw_data = get_json()
print(clean(raw_data))
