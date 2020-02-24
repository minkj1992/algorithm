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


## 공부할 소스코드
- 1000ms
```python
import collections as col
import sys
sys.setrecursionlimit(1000000)

def per_depth(nums):
    if len(nums) >= 5:
        perdep.append(nums)
        return
    for i in range(4):
        per_depth(nums + [i])


def permutation(nums):
    if len(nums) >= 5:
        if nums[::-1] not in perlist:
            perlist.append(nums)
        return
    for i in range(1, 6):
        if str(i) not in nums:
            permutation(nums + str(i))


def BFS(k, z):
    global answer
    if answer == 12:
        return
    num = perlist[k]
    turns = perdep[z]
    if not maze[num[4]][turns[4]][4][4]:
        return
    que = col.deque()
    visit = []
    if maze[num[0]][turns[0]][0][0]:
        que.append((0, 0, 0))
        visit.append((0, 0, 0))
    else:
        return
    cnt = 1
    while que:
        if cnt >= answer:
            return
        for _ in range(len(que)):
            depth, u, v = que.popleft()
            for i in range(6):
                if 0 <= depth + dirs[i][0] < 5 and 0 <= u + dirs[i][1] < 5 and 0 <= v + dirs[i][2] < 5:
                    if maze[num[depth + dirs[i][0]]][turns[depth + dirs[i][0]]][u + dirs[i][1]][v + dirs[i][2]]:
                        if (depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]) == (4, 4, 4):
                            answer = cnt
                            return
                        elif (depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]) not in visit:
                            que.append((depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]))
                            visit.append((depth + dirs[i][0], u + dirs[i][1], v + dirs[i][2]))
        cnt += 1


dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
perlist = []
perdep = []
maze = {'1': [], '2': [], '3': [], '4': [], '5': []}
answer = 60

for i in range(1, 6):
    maze[str(i)].append([list(map(int, input().split())) for _ in range(5)])

for num in range(1, 6):
    p1, p2, p3 = [[0]*5 for _ in range(5)], [[0]*5 for _ in range(5)], [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            p1[i][j] = maze[str(num)][0][j][4-i]
            p2[i][j] = maze[str(num)][0][4-i][4-j]
            p3[i][j] = maze[str(num)][0][4-j][i]
        maze[str(num)].append(p1)
        maze[str(num)].append(p2)
        maze[str(num)].append(p3)
permutation('')
per_depth([])

for i in range(60):
    for j in range(len(perdep)):
        BFS(i, j)

if answer == 60:
    answer = -1
print(answer)
```