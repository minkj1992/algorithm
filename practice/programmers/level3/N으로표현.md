# N으로 표현

## 1st try (x)
```python
from itertools import product
_dict = dict()
def nums(i):
    if _dict.get(i,-1)!=-1: return _dict[i]
    _dict[i] = set()
    _dict[i].add((i,))
    if i != 1:
        for j in range(1,i):
            for a,b in product(nums(j),nums(i-j)):
                _dict[i].add(a+b)
    return _dict[i]

# 중복방지 permutation
def permute(arr):
    idx = list(range(len(arr)))
    r = [[]]
    for i in range(len(idx)):
        r = [[a]+b for a in idx for b in r if a not in b]
    return set([tuple(arr[i] for i in ele) for ele in r])

# {key: value}
cal_cache = dict()
# {i: values}
result_cahce = dict()
def calculate(N,i):
    if result_cahce.get(i,-1) !=-1:
        return result_cahce[i]
    if i == 1:
        cal_cache[i] = [i]
        result_cahce[i] = set(cal_cache[i])
    else:
        results = set()
        for idx in nums(i):
            for perm in permute(idx):
                tmp_row = [int(str(N)*count) for count in perm]
                a = tmp_row[0]
                for  tmp_row[1:]
    return result_cahce[i]

# 해당 set에 대한 모든 permutation
def solution(N, number):
    if N == number:return 1

    for i in range(2,9):
        if number in calculate(N,i):
            return i
    return -1

```

## 2nd try (o)
```python
def solution(N, number):
    if N == number: return 1
    cache = [{N}]    
    for i in range(2,9):
        arr = [int(str(N)*i)]
        for rep in range(i//2):
            for a in cache[rep]:
                for b in cache[i-2-rep]:
                    arr.append(a+b)
                    arr.append(a*b)
                    arr.append(a-b)
                    arr.append(b-a)
                    if a!=0: arr.append(b//a)
                    if b!=0: arr.append(a//b)
        arr = set(tuple(arr))
        if number in arr:
            return i
        cache.append(arr)
    return -1
```

```
i = N을 사용한 횟수
rep = 몇번 계산할지, N= 4라면 (1,3), (2,2) 즉 기준을 나누는 방법
```

- 다시 풀어본 버전 ( 더빠르다 )

```python 
def solution(N, number):
    if N == number: return 1
    cache = [{N}]
    for i in range(2,9):
        arr = {int(str(N)*i)}
        for piv in range(i//2):
            for a in cache[piv]:
                for b in cache[i-2-piv]:
                    arr.add(a+b)
                    arr.add(a-b)
                    arr.add(b-a)
                    arr.add(a*b)
                    if a!=0: arr.add(b//a)
                    if b!=0: arr.add(a//b)
        if number in arr:return  i
        cache.append(arr)
    return -1
```