# wc 3번 카카오문제랑 동일
```python
def solution(board, height):
    N = len(board)
    M = len(board[0])
    visited = [[0]*M for _ in range(N)]
    gid = 1

    def bfs(y,x,v,h):
        visited[y][x]=v
        stack = [(y,x)]
        while stack:
            y,x = stack.pop()
            for ny,nx in (y,x+1),(y,x-1),(y+1,x),(y-1,x):
                if (0<=ny<N and 0<=nx<M) and visited[ny][nx]<v:
                    if abs(board[y][x]-board[ny][nx])<=h:
                        visited[ny][nx]=v
                        stack.append((ny,nx))

    def find_height(i):
        for y in range(N):
            for x in range(M):
                for ny,nx in (y,x+1),(y,x-1),(y+1,x),(y-1,x):
                    if (0<=ny<N and 0<=nx<M) and visited[y][x]!=visited[ny][nx] and abs(board[y][x]-board[ny][nx])<adj_mtx[visited[y][x]-1][visited[ny][nx]-1]:
                        a = visited[y][x]-1
                        b = visited[ny][nx]-1
                        v = abs(board[y][x]-board[ny][nx])
                        adj_mtx[a][b] = v
                        adj_mtx[b][a] = v

    def kruskal(gi):
        def find_min():
            val = float('inf')
            pos = []
            for i in range(gi):
                for j in range(i+1,gi):
                    if adj_mtx[i][j]<val and group[i]!=group[j]:
                        val = adj_mtx[i][j]
                        pos = [i,j]
            return val,pos

        def union(a,b):
            v1 = group[a]
            v2 = group[b]
            for i in range(gi):
                if group[i]==v1: group[i]=v2

        ans = 0
        group = list(range(gi))
        for _ in range(gi-1):
            v,p = find_min()
            ans+=v
            union(*p)
        return ans


    for y in range(N):
        for x in range(M):
            if not visited[y][x]:
                bfs(y,x,gid,height)
                gid+=1
                
    adj_mtx = [[float('inf')]*(gid-1) for _ in range(gid-1)]
    find_height(gid-1)
    answer = kruskal(gid-1)
    return answer


l = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
h = 1
print(solution(l,h))
```