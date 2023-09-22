# h-index
> https://school.programmers.co.kr/learn/courses/30/lessons/42747

## 1st
> 23.09.22

```py
def solution(citations):
    citations = sorted(citations)
    n = len(citations)

    for i, c in enumerate(citations):
        h = n - i # n편 중 남아있는 논문 수, 모두 c 이상 인용
        if c >= h: # h번 이상 인용됨
            return h
    return 0
```