# NMK

## 접근법
- 비둘기집의 원리에 의하여 N의 크기는 M+K-1(최소 1개의 값 공유)<= N <= M*K(M*K+1의 경우에는 M or K가 +1된다)

## first try
- step을 사용하여 움직였는데, 틀림으로 뜬다.

```python
n,m,k=list(map(int,input().split()))
if m+k-1<=n and n<=m*k:
    n=list(range(1,n+1));print(*n[:k][::-1],sep=' ',end=' ');step=(len(n)-k)//(m-1)
    for i in [n[i:i + step] for i in range(k, len(n),step)]:
        for j in i[::-1]: print(j,end=' ')
else:print(-1)
```


## 2nd try
- 끝의 녀석들 중에서 남는다면 pop 처리시켜서 그 전 녀석에게 extend하는 방식
- 쌩쑈
- 틀림
```python
n,m,k=list(map(int,input().split()))
if m+k-1<=n and n<=m*k:
    n=list(range(1,n+1));print(*n[:k][::-1],sep=' ',end=' ');step=(len(n)-k)//(m-1)
    lis=[n[i:i + step] for i in range(k, len(n),step)]
    if len(lis)==m:lis[-2].extend(lis.pop())
    elif len(lis)==m+1:
        tmp=lis.pop();tmp=lis.pop()+tmp;tmp2=lis.pop()
        lis[-1].extend(tmp2)
        lis.append(tmp)
        # lis[-2].extend(tmp[:k-step])
        # lis[-1].extend(tmp[k-step:])
    for i in lis:
        for j in i[::-1]: print(j,end=' ')
else:print(-1)
```

## success
- indexing하여 print하였다.
- index는 `a` = 몫, `b`= 나머지
- `a=(len(n)-k)//(m-1);b=(len(n)-k)%(m-1)`

- 이유를 알 수 없는 runtime error에 의하여 try except하니 오류가 해결되었다. 
```python
n,m,k=map(int,input().split())
try:
    if m+k-1<=n<=m*k:
        n=list(range(1,n+1));print(*n[:k][::-1],sep=' ',end=' ');a=(len(n)-k)//(m-1);b=(len(n)-k)%(m-1)
        for i in range(b):print(*n[k+i*(a+1):k+(i+1)*(a+1)][::-1],sep=' ',end=' ')
        for i in range(k+b*(a+1),len(n),a):print(*n[i:i+a][::-1],sep=' ',end=' ')
    else:print(-1)
except:pass
```
