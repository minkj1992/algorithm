# https://programmers.co.kr/learn/courses/30/lessons/42895
from typing import List, Set


def solution(N, number):
    def operate(set1: Set[int], set2: Set[int]) -> List[int]:
        result = []
        for a in set1:
            for b in set2:
                result.append(a + b)
                result.append(a - b)
                result.append(b - a)
                result.append(a * b)
                if b != 0:
                    result.append(a // b)
                if a != 0:
                    result.append(b // a)
        return result

    limit = 8
    dp = [None] + [set() for _ in range(limit)]
    for i in range(1, limit + 1):
        dp[i].add(int(str(N) * i))
        for piv in range(1, i // 2 + 1):
            dp[i].update(operate(dp[piv], dp[i - piv]))

        if number in dp[i]:
            return i
    return -1


N = 5
number = 31168
assert -1 == solution(N, number)
