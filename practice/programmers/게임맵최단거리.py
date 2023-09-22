# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

_dir = ((0, 1), (0, -1), (-1, 0), (1, 0))

def solution(maps):
    n, m = len(maps[0]), len(maps)
    visited = [[0] * n for _ in range(m)]
    queue = deque([(0, 0, 1),]) # y, x, step
    visited[0][0] = 1
    
    def next_pos(y, x):
        nonlocal n, m

        pos = []
        for (dy, dx) in _dir:
            ny, nx = y+dy, x+dx
            
            if not (0<= ny < m) or not (0<= nx < n):
                continue
            if visited[ny][nx]:
                continue
            if maps[ny][nx] == 0:
                continue
            pos.append((ny, nx))
        return pos
    
    while queue:
        (y, x, step) = queue.popleft()
        next_step = step + 1

        for (ny, nx) in next_pos(y, x):
            if (ny, nx) == (m-1, n-1):
                return next_step
            visited[ny][nx] = 1
            queue.append((ny, nx, next_step))
    return -1