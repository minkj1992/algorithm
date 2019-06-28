def makeGraph(words=["dictionary","english","is","ordered","ordinary","this"]):
    def idx(a):
        return ord(a)-ord('a')
    adj = [[False,]*26 for i in range(26)]
    for j in range(1,len(words)):
        i=j-1
        for a1,a2 in zip(words[i],words[j]):
            print(a1,a2)
            print(idx(a1),idx(a2))
            if not adj[idx(a1)][idx(a2)] and a1 != a2:
                # Q1 파이썬에서 list의 element ref 가지는법
                # 왜 adj[i][j], adj[j][i] true를 하지 않는가 -> directed graph 이니까
                adj[idx(a1)][idx(a2)] = True
    for i in adj:print(i)
    return adj

# visited
# order

# def topologicalSort():
#     def dfs(start):
#     visited = [False]


