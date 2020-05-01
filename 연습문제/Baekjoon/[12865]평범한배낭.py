N,K = map(int,input().split())
weights = []
values = []

for _ in range(N):
    w,v = map(int,input().split())
    weights.append(w)
    values.append(v)

def knapsack(N,W,wgt,val):
    dp = [[0]*(W+1) for n in range(N+1)]
    for n in range(1,N+1):
        for w in range(1,W+1):
            if weights[n-1]>w:
                dp[n][w] = dp[n-1][w]
            else:
                dp[n][w] = max(val[n-1]+dp[n-1][w-wgt[n-1]],dp[n-1][w])
    return dp[N][W]

result = knapsack(N,K,weights,values)
print(result)