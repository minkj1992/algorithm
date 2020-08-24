import json


def _parse_data(data_list, target):
    result = {}
    target_value = False
    for data in data_list:
        id = data['pk']
        value = data['value']
        is_active = data['is_active']
        parent = data['parent']
        if is_active or is_active == 'true':
            result[id] = (value, parent)
            if value == target:
                target_value = id
    return result, target_value


def get_summary(data, target_value):
    try:
        data, target_id = _parse_data(data, target_value)
    except Exception:
        return "INACTIVE"

    if not data:
        return "INACTIVE"
    if not target_id:
        return "INACTIVE"

    value_list = []
    while len(value_list) < 3:
        value, parent = data.get(target_id, (None,None))
        if not value:
            break
        value_list.append(value)
        target_id = parent
    if not value_list:
        return "INACTIVE"
    if len(value_list) == 1 and value_list[0]==target_value:
        return "INACTIVE"
    return value_list[0] if len(value_list) == 1 else '>'.join(reversed(value_list))


raw_data, target_value = input().split('/')
data = json.loads(raw_data)
result = get_summary(data, target_value)
print(result)
