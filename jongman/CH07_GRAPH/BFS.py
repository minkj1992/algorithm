from collections import deque
def bfs(adj,start):
    visit = dict()
    queue = deque([start,])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit[node] = True
            queue.extend(adj[node])
    return visit
