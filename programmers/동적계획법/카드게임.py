# 같은 개수의 두 더미
def solution(left, right):
    N = len(left)
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if left[i]<=right[j]:
                dp[i][j] = max(dp[i+1][j],dp[i+1][j+1])
            else:
                dp[i][j] = dp[i][j+1]+right[j]
    return dp[0][0]