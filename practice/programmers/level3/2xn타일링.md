# 2xn 타일링

## 1st try (o)

```python
def solution(n):
    answer= 1 + sum([(n-2*k)*(k+1) for k in range(1,n//2+1)])
    return answer%(10**9+7)
```

## 2nd try (x)
```python
def solution(n):
    return 1+sum([n+1-(2*i) for i in range(1,n//2+1)])
```
