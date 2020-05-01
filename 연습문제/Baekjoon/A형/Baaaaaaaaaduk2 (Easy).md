# Baaaaaaaaaduk2 (Easy)

> https://www.acmicpc.net/problem/16988

## 1st try

- z_pos를 구하고 2개의 조합을 구한다.
```python
def permute(arr,c):
    r = [[]]
    for i in range(c):
        r = [[a]+b for a in arr for b in r if a not in b]
    return r

def dbfs(_y,_x):
    visited[_y][_x] = 1
    stack = [(_y,_x)]
    segment = [(_y,_x)]
    while stack:
        y,x = stack.pop()
        for nxy in (y,x+1),(y,x-1),(y+1,x),(y-1,x):
            ny,nx =nxy
            if (0<=ny<N and 0<=nx<M) and not visited[ny][nx] and board[ny][nx]==2:
                visited[ny][nx]=1
                stack.append((ny,nx))
                segment.append((ny, nx))
    w_pos.append(segment)



# 1이나 outof bound이거나 perm속에 있어야한다. 없다면 false
def check(perm):
    global result
    count = 0
    for seg in w_pos:
        flag = False
        for w in seg:
            for nxy in (w[0],w[1]+1),(w[0],w[1]-1),(w[0]+1,w[1]),(w[0]-1,w[1]):
                ny,nx = nxy
                if (0<=ny<N and 0<=nx<M) and board[ny][nx]==0 and (ny,nx) not in perm:
                    flag = True
                    break
            if flag:break
        else:count+=len(seg)

    if count>result:
        result = count


# 시작 할 때 segment를 줄여야 한다.
N,M = map(int,input().split())
board = [list(map(int,input().split(' '))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
w_pos = []
z_pos = []
for y in range(N):
    for x in range(M):
        if board[y][x]==0:
            z_pos.append((y,x))
        elif board[y][x]==2:
            if not visited[y][x]:
                dbfs(y,x)    # segment


result = 0
for perm in permute(z_pos,2):
    check(perm)
print(result)
```


## 2nd try 
- 위의 `perm()`을 `combs()`로 변환
```python
def combs(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for nxt in combs(arr[i + 1:], k - 1):
                yield [arr[i]] + nxt


def dbfs(_y, _x):
    visited[_y][_x] = 1
    stack = [(_y, _x)]
    segment = [(_y, _x)]
    while stack:
        y, x = stack.pop()
        for nxy in (y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x):
            ny, nx = nxy
            if (0 <= ny < N and 0 <= nx < M) and not visited[ny][nx] and board[ny][nx] == 2:
                visited[ny][nx] = 1
                stack.append((ny, nx))
                segment.append((ny, nx))
    w_pos.append(segment)


# 1이나 outof bound이거나 perm속에 있어야한다. 없다면 false
def check(comb):
    global result
    count = 0
    for seg in w_pos:
        flag = False
        for w in seg:
            for nxy in (w[0], w[1] + 1), (w[0], w[1] - 1), (w[0] + 1, w[1]), (w[0] - 1, w[1]):
                ny, nx = nxy
                if (0 <= ny < N and 0 <= nx < M) and board[ny][nx] == 0 and (ny, nx) not in comb:
                    flag = True
                    break
            if flag: break
        else:
            count += len(seg)

    if count > result:
        result = count


# 시작 할 때 segment를 줄여야 한다.
N, M = map(int, input().split())
board = [list(map(int, input().split(' '))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
w_pos = []
z_pos = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            z_pos.append((y, x))
        elif board[y][x] == 2:
            if not visited[y][x]:
                dbfs(y, x)  # segment

result = 0
for comb in combs(z_pos, 2):
    check(comb)
print(result)
```

## 3rd try (20.02.02)

- 실패(x)
    - 2개 이하인 녀석만 검사
```python
MIS = lambda: map(int, input().split())
DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

N, M = MIS()
board = [list(MIS()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def is_range(y, x):
    global N, M
    return (0 <= y < N) and (0 <= x < M)



def bfs(sy, sx, gid):
    visited[sy][sx] = gid
    stack = [(sy, sx)]
    groups[gid] = []
    groups_meta[gid] = [1, 0]

    while stack:
        cy, cx = stack.pop()
        for d in DIR:
            ny, nx = cy + d[0], cx + d[1]
            if is_range(ny, nx):
                if board[ny][nx] == 2 and not visited[ny][nx]:
                    visited[ny][nx] = gid
                    groups_meta[gid][0] += 1
                    stack.append((ny, nx))

                if board[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = gid
                    groups_meta[gid][1] += 1
                    groups[gid].append((ny, nx))
    # clear()
    for p in groups[gid]: visited[p[0]][p[1]] = 0


# group check
gid = 0
groups = {}
groups_meta = {}  # 2_num, 0_num
for y in range(N):
    for x in range(M):
        if board[y][x] == 2 and not visited[y][x]:
            gid += 1
            bfs(y, x, gid)

# find group which contains 0_cnt<=2
candidate_gids = []
all_pos_set = set()
for k, v in groups_meta.items():
    _, z_num = v
    if z_num <= 2:
        candidate_gids.append(k)
        all_pos_set |= set(groups[k])
all_pos_arr = list(all_pos_set)


def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in combination(arr[i + 1:], r - 1):
                yield [arr[i]] + nxt


# combination
ans = 0
for comb in combination(all_pos_arr, 2):
    tmp = 0
    for i in candidate_gids:
        for p in groups[i]:
            if p not in comb: break
        else:
            tmp += groups_meta[i][0]

    if tmp > ans: ans = tmp
print(ans)
```
- 왜 안될까?
    - `group_meta`가 잘못 등록된 경우
    - 3이상인 녀석도 검사해야 되는 경우

- 모두 검사하도록 하니 성공 (0)
```python
MIS = lambda: map(int, input().split())
DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

N, M = MIS()
board = [list(MIS()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


def is_range(y, x):
    global N, M
    return (0 <= y < N) and (0 <= x < M)


def bfs(sy, sx, gid):
    visited[sy][sx] = gid
    stack = [(sy, sx)]
    groups[gid] = []
    groups_meta[gid] = [1, 0]

    while stack:
        cy, cx = stack.pop()
        for d in DIR:
            ny, nx = cy + d[0], cx + d[1]
            if is_range(ny, nx):
                if board[ny][nx] == 2 and not visited[ny][nx]:
                    visited[ny][nx] = gid
                    groups_meta[gid][0] += 1
                    stack.append((ny, nx))

                if board[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = gid
                    groups_meta[gid][1] += 1
                    groups[gid].append((ny, nx))
    # clear()
    for p in groups[gid]: visited[p[0]][p[1]] = 0


# group check
gid = 0
groups = {}
groups_meta = {}  # 2_num, 0_num
for y in range(N):
    for x in range(M):
        if board[y][x] == 2 and not visited[y][x]:
            gid += 1
            bfs(y, x, gid)
            
all_pos_set = set()
for k in groups_meta.keys():
    all_pos_set |= set(groups[k])
all_pos_arr = list(all_pos_set)

def combination(arr,r):
    for i in range(len(arr)):
        if r == 1: yield [arr[i]]
        else:
            for nxt in combination(arr[i+1:],r-1):
                yield [arr[i]] + nxt

# combination
ans = 0
for comb in combination(all_pos_arr,2):
    tmp = 0
    for k,pos in groups.items():
        for p in pos:
            if p not in comb: break
        else:
            tmp+=groups_meta[k][0]

    if tmp>ans: ans = tmp
print(ans)
```

## 공부할 소스코드

- 나만의 방법으로 다시 typing (`76ms`)
```python
from collections import defaultdict
input = __import__('sys').stdin.readline
MIS = lambda : map(int,input().split())

def dfs(y,x):
    stack = [(y,x)]
    board[y][x] = 3
    zero = set()
    sz = 0
    while stack:
        y,x = stack.pop()
        sz+=1
        for ny,nx in (y,x+1),(y,x-1),(y+1,x),(y-1,x):
            if not ((0<=ny<N)and(0<=nx<M)): continue
            if board[ny][nx] == 0: zero.add((ny,nx)); continue
            if board[ny][nx] != 2: continue

            board[ny][nx] = 3
            stack.append((ny,nx))
    return list(zero), sz


N,M = MIS()
board = [list(MIS()) for _ in range(N)]
one = defaultdict(int)
two = defaultdict(int)
for y in range(N):
    for x in range(M):
        if board[y][x] != 2: continue
        zero,sz = dfs(y,x)
        if len(zero) > 2: continue
        if len(zero)==1: one[zero[0]]+=sz
        else: two[tuple(zero)]+=sz

ans = sum(sorted(one.values())[-2:]) # one만 2개 선택하는 경우, ONE이 비어있더라도 0 return
for (p1,p2),sz in two.items():
    tmp = sz + one[p1] + one[p2]
    if tmp>ans: ans = tmp
print(ans)

```