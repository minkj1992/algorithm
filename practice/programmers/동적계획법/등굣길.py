"""
https://programmers.co.kr/learn/courses/30/lessons/42898
init 시점에 water가 나오면 break 해주어야 한다.
dp[i][j] = max(dp[i-1][j], 0) + max(dp[i][j-1], 0)
"""


def solution(m, n, puddles) -> int:
    water = -1
    dp = [[0] * m for _ in range(n)]
    for (x, y) in puddles:
        dp[y - 1][x - 1] = water

    for i in range(n):
        if dp[i][0] == water:
            break
        dp[i][0] = 1

    for j in range(m):
        if dp[0][j] == water:
            break
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == water:
                continue
            dp[i][j] = max(dp[i][j - 1], 0) + max(dp[i - 1][j], 0)

    return dp[n - 1][m - 1] % 1000000007


print(solution(1, 4, []))
print(solution(4, 1, []))
print(solution(1, 2, []))
print(solution(2, 1, []))
