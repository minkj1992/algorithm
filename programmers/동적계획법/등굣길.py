DENOM = 1000000007
def solution(m, n, puddles):
    if m == 1 or n == 1: return 0 if puddles else 1
        
    dp = [[0]*(m+1) for _ in range(n+1)]
    for (x,y) in puddles:dp[y][x]=-1
    
    for i in range(1,n+1):
        if dp[i][1] == -1:break
        dp[i][1] = 1
    for j in range(1,m+1):
        if dp[1][j] == -1:break
        dp[1][j] = 1
    
    for i in range(2,n+1):
        for j in range(2,m+1):
            if dp[i][j]==-1: continue
            dp[i][j] += (max(dp[i][j-1],0)+max(dp[i-1][j],0))
    return dp[n][m]%DENOM