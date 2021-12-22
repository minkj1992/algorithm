# 테케 2개 틀림
from itertools import permutations
def solution(numbers, k):
    N = len(numbers)
    if N == 1: return 0
    for i in range(N-1):
        if abs(numbers[i] - numbers[i+1]) > k: break
    else: return 0

    answer = float('inf')
    for perm in permutations(numbers):
        swap = 0
        for i in range(N - 1):
            if numbers[i] != perm[i]: swap += 1
            if abs(perm[i] - perm[i + 1]) > k: break
        else:
            if swap % 2: continue
            if swap // 2 >= answer: continue
            answer = swap // 2
    return answer if answer != float('inf') else -1

