import functools


def comparator(a, b):
    return (a + b > b + a) - (a + b < b + a)

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer