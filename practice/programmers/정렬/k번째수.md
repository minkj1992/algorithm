# k번째 수
> https://school.programmers.co.kr/learn/courses/30/lessons/42748

## 1st

```py
def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer
```

## 2nd
> 23.09.22

```py
def solution(array, commands):
    answer = []
    for (i, j, k) in commands:
        i -= 1
        k -= 1
        answer.append(sorted(array[i:j])[k])
    return answer
```