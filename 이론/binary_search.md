# Binary Search
> 이분 탐색

- 정렬된 상태에서 진행되어야 함.
- 검색에 드는 비용은 `log(n)`이지만, 정렬되어 있지 않다면 다른 정렬 알고리즘을 사용해야 하니 퀵정렬 기준 `n*log(n)`
- 수도 코드를 보면 `while left < right`로 검색을 하지만 mid = (left+right)//2를 사용하기 때문에 mid 값이 left 값을 탐색하기 위해서는 `left<=right`로 탐색하는 것이 옳다고 생각한다.

- python 소스코드 (프로그래머스 예산 문제)
```python
def solution(budgets, M):
    budgets.sort()
    n = len(budgets)
    l, r = 0, budgets[n - 1]

    answer = 0
    while l <= r:
        mid = (l + r) // 2
        val = 0
        for i in range(n):
            if budgets[i] >= mid:
                val += mid * (n - i)
                break
            val += budgets[i]

        if val == M:
            return mid
        elif val > M:
            r = mid - 1
        else:
            # 작을경우에만 answer을 update한다.
            l = mid + 1
            answer = mid

    return answer
```
