def solution(K, travel):
    N = len(travel)
    dp = [[0]*(K+1) for _ in range(N)]
    answer = 0
    try:
        dp[0][travel[0][0]] = travel[0][1] 
        dp[0][travel[0][2]] = travel[0][3]
    except:
        return max(dp[0][travel[0][0]],dp[0][travel[0][2]]) # 처음부터 못갈 경우 K = 1, travel[0][0] = 2

    for i in range(1,N):
        for j in range(K+1):
            if dp[i-1][j] == 0: continue
            if j+travel[i][0]<=K:
                dp[i][j+travel[i][0]] = max( dp[i][j+travel[i][0]],dp[i-1][j] + travel[i][1]) # 기존에 이미 와본적이 있을 경우
                answer = max(answer, dp[i][j+travel[i][0]])
            if j+travel[i][2]<=K:
                dp[i][j+travel[i][2]] = max(dp[i][j+travel[i][2]],dp[i-1][j] + travel[i][3]) 
                answer = max(answer, dp[i][j+travel[i][2]])
    return answer