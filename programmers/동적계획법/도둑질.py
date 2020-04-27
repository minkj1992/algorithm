# 1. 0..n-2에서 최적해를 찾을 경우 (n-1번은 선택하면 안된다.)
# 2. 1..n-1에서 최적해를 찾을 경우 (0번은 선택하면 안된다.)
def solution(money):
    if len(money)==3: return max(money)
    N = len(money)
    dp1 = money[:]
    dp2 = money[:]
    dp1[1] = max(money[:2])
    dp2[0] = 0
    # 2부터 시작해야 하는 이유는 i-2 때문에 index out of range 먹을 수 있기 때문이다.
    for i in range(2,N-1): dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])
    for i in range(2,N): dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
    return max(dp1[N-2],dp2[N-1])