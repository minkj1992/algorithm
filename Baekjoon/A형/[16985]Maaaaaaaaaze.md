# [16985]Maaaaaaaaaze
> https://www.acmicpc.net/problem/16985
## 1st try
```python
# 200217
# [Maaaaaaaaaze](https://www.acmicpc.net/problem/16985)
# N =5, 5X5X5
# 1. 회전: 판을 시계방향, 반시계 방향으로 회전 가능
# 2. permutation
# 3. 3차원 이동

from collections import deque
# 내려가는 것만 생각해도 되지 않을까?
DIR = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(-1,0,0),(1,0,0))
def perms(arr,r):
    for i in range(len(arr)):
        if r == 1: yield [arr[i]]
        else:
            for nxt in perms(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]] + nxt

def rotate():
    for i in range(5):
        for _ in range(3):
            boards[i].append(raw[i])
            raw[i] = list(map(list,zip(*raw[i])))[::-1]
        boards[i].append(raw[i])

def is_range(z,y,x):
    return ((0<=z<5) and (0<=y<5) and (0<=x<5))

def bfs(p):
    global result
    if new_boards[p[0]][0][0]: return
    cnt = 1
    visited[p[0]][0][0] = 1
    queue = deque([(0,0,0)])
    while queue:
        if cnt >= result: return
        for _ in range(len(queue)):
            z,y,x = queue.popleft()
            for dz,dy,dx in DIR:
                nz,ny,nx = z+dz,y+dy,x+dx
                if not is_range(nz,ny,nx): continue
                if new_boards[p[nz]][ny][nx]: continue
                if visited[nz][ny][nx]: continue
                if (nz,ny,nx) == (4,4,4): result =cnt;return
                visited[nz][ny][nx] = 1
                queue.append((nz,ny,nx))
        cnt +=1

raw = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
boards = [[] for _ in range(5)]
rotate()
new_boards = []
result = float('inf')
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    new_boards = [boards[0][a],boards[1][b],boards[2][c],boards[3][d],boards[4][e]]
                    for perm in perms(list(range(5)),5):
                        visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
                        bfs(perm)
print(-1) if result == float('inf') else print(result)
```

- 왜 안될까 ? ㅋㅋ


## 2nd try ( 0 )

- 1360 ms
- **board가 1이면 통과 가능하다는 조건 또 빼먹음**
- 4^5 * 5!(120) = 1024 * 120 = 12880의 경우의 수에 대하여 bfs돌린다.
- 최단 경로 120 또는 cnt가 result를 넘어갈 경우 조기 종료 하도록 함.
- 콜백 지옥을 없애주고 싶은데 전역변수를 만들 방법이 없어서 그냥 해야 되는 듯하다. 
```python
from collections import deque
# 내려가는 것만 생각해도 되지 않을까?
DIR = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(-1,0,0),(1,0,0))
def perms(arr,r):
    for i in range(len(arr)):
        if r == 1: yield [arr[i]]
        else:
            for nxt in perms(arr[:i]+arr[i+1:],r-1):
                yield [arr[i]] + nxt

def rotate():
    for i in range(5):
        for _ in range(3):
            boards[i].append(raw[i])
            raw[i] = list(map(list,zip(*raw[i])))[::-1]
        boards[i].append(raw[i])

def is_range(z,y,x):
    return (0<=z<5) and (0<=y<5) and (0<=x<5)

def bfs(p,visited):
    global result
    cnt = 1
    visited[0][0][0] = 1
    queue = deque([(0,0,0)])
    while queue:
        if cnt >= result: return
        for _ in range(len(queue)):
            z,y,x = queue.popleft()
            for dz,dy,dx in DIR:
                nz,ny,nx = z+dz,y+dy,x+dx
                if not is_range(nz,ny,nx): continue
                if not new_boards[p[nz]][ny][nx]: continue
                if visited[nz][ny][nx]:continue
                if (nz,ny,nx) == (4,4,4):result = cnt;return
                visited[nz][ny][nx] = cnt
                queue.append((nz,ny,nx))
        cnt +=1

raw = [[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
boards = [[] for _ in range(5)]
rotate()
result = float('inf')
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    new_boards = [boards[0][a], boards[1][b], boards[2][c], boards[3][d], boards[4][e]]
                    for perm in perms(list(range(5)), 5):
                        if result == 12: break
                        if new_boards[perm[0]][0][0]==0 or new_boards[perm[4]][4][4]==0: continue  # 처음이 막혀있거나, 끝이 막혀있거나
                        visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
                        bfs(perm, visited)
                if result == 12: break
            if result == 12: break
        if result == 12: break
    if result == 12: break
print(-1) if result == float('inf') else print(result)
```


- `bfs()`매개변수로 visited, new_boards, permutation 넣어주니 메모리는 더 잡아먹지만 시간은 더 적게 소요되었고, callback 헬을 피할 수 있다.
    - `1344ms`
- `전역변수` 참조를 한다면 시간이 더 소요되는 듯하다. 지역변수를 제공하면 시간 소요는 줄이지만 메모리는 더 소모한다.
