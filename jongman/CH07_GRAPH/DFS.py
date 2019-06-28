def dfsAll():
    def dfs(here):
        visited[here]=True
        for i in adj[here]:
            # 만약 i가 idx라면
            if not visited[i]:
                dfs(i)
    num = 10
    visited = [False]*num
    # adjMatrix or adjList
    adj = [[] for i in range(num)]
    for i in visited:
        if not i:
            dfs(i)
    