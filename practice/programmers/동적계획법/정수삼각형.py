# https://programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle) -> int:
    n = len(triangle)
    if n == 1:
        return triangle[0][0]

    dp = [[0] + t + [0] for t in triangle]
    for i in range(1, n):
        m = len(triangle[i])
        for j in range(1, m + 1):
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
    return max(dp[n - 1])


assert 30 == solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
