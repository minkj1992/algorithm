def solution(stones, k):
    if len(stones)==1:return stones[0]
    answer = 0
    N = len(stones)
    dp = [0]*N
    for n in range(N):
        if n<k:
            dp[n]=stones[n]
        else:
            dp[n] = min(max(dp[n-k:n]),stones[n])
    answer = max(dp[N-k:N])
    return answer

s = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(s,k))


# 2nd try

from functools import lru_cache
def solution(stones, k):
    @lru_cache()
    def cache(n):
        nonlocal k
        if n<k:
            return stones[n]
        else: 
            return min(max([cache(n) for n in range(n-k,n)]),stones[n])

    if len(stones)==1:return stones[0]
    N = len(stones)
    answer = max([cache(n) for n in range(N-k,N)])
    return answer

# 3rd try
def solution(stones, k):
    values = sorted(list(set(stones)),reverse=True)
    answer = 0
    
    while values:
        _min = values.pop()
        piv=_min-answer      # piv is adjustedMin
        zeros = 0
        answer = _min
        
        for i in range(len(stones)):
            if stones[i]==0:
                zeros+=1
                if zeros == k:
                    return answer
                continue
            else:
                stones[i]-=piv
                if stones[i]==0:
                    zeros+=1
                    if zeros == k:
                        return answer
                else:
                    zeros = 0

s = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k =3
print(solution(s,k))