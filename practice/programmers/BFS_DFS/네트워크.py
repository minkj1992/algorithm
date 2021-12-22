
# https://programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    def dfs(here):
        visited[here]=True
        for there,state in enumerate(adjList[here]):
            if there == here or state==0: continue
            if not visited[there]:
                dfs(there)

    adjList = computers[:]
    # dfs에서는 visited가 Recursion의 base condition이 된다.
    visited = [False]*n
    # dfsAll()
    for i,j in enumerate(visited):
        if not j:
            dfs(i)
            cnt+=1
    return cnt

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
