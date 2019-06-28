import bisect
def solution(tickets):
    def dfs(here,parent=0):
        
        answer.append(here)
        flag = False
        # 인접한 vertex들 중에서
        for i,j in enumerate(adj[here]):
            
            # not visited되었다면
            if not visited[dict2idx[here]][i]:
                # end point 가 아니라면(end point는 오직 1개뿐이다.)
                if adj.get(j):
                    visited[dict2idx[here]][i] = True
                    
                    dfs(j,i)
                # 아무곳도 out이 없는 노드는 end가 되어야 한다.
                # 하지만 만약 모든 도시를 돌지 못했는데 break 부분이 있다면 다시 dfi가 실행되어야한다.(continue)
                elif len(answer)==len(tickets):
                    
                    answer.append(j)
                # 부모(answer[-1])가 잘못 길을 들었다면 false해주고 pop 해준다.
                else:
                    visited[dict2idx[answer[-1]]][parent]=False
                    answer.pop()
                    
                    
    answer = []
    adj,vertexLen,dict2idx = ticket2Adj(tickets)
    visited = [[False]*len(v) for k,v in adj.items()]
    dfs("ICN")
    # dfs(1)
    
    return answer
    
def ticket2Adj(tickets):
    tmp = dict()
    for i in tickets:
        fr,to = i
        if tmp.get(fr):
            # print(tmp[fr])
            bisect.insort(tmp[fr], to)
        else:
            tmp[fr]=[to,]
    # None타입 처리하는거

    # set화된 vertex들에게 idx를 부여하며 |V|를 센다.
    # 생성된 dict2Idx
    dict2Idx = dict()
    for i,j in enumerate(tmp.keys()):
        dict2Idx[j]=i
    
    vertexLen = i+1
    return tmp,vertexLen,dict2Idx

# print(solution([["ICN", "SFO"],["ICN", "SFO"],["ICN", "SFO"],["SFO","ICN"],["SFO","ICN"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# print(solution([[1,3],[1,2],[3,1]]))

print(solution([[1,2],[2,3],[2,4],[4,5],[5,2],[3,6]]))

# `bisect`: array에 sort하면서 append

# `bisect`: array에 sort하면서 append할 수 있다.
# `adjList`: Dict형식으로하면 참조하는데 O(1)로 adj 검색이 가능하다.
# |V|: print(len(tmp.keys()))

# ticket2Adj를 통하여 adj를 만든다. -> {'ICN': ['AFK', 'JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
# dfs를 사용하여 


# `adjList`: Dict형식으로하면 참조하는데 O(1)로 adj 검색이 가능하다.
# |V|: print(len(tmp.keys()))

# ticket2Adj를 통하여 adj를 만든다. -> {'ICN': ['AFK', 'JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
# dfs를 사용하여 

# 테스트케이스1 중복된 값도 들어온다
# if not visited[dict2idx[here]][adj[here].index(i)]: 이 파트에서 .index가 문제
# 정리하면 visited에서 중복 value 문제





# import bisect
# def solution(tickets):
#     def dfs(here):
#         answer.append(here)
#         for i in adj[here]:
#             if not visited[dict2idx[here]][adj[here].index(i)]:
#                 if adj.get(i):
#                     visited[dict2idx[here]][adj[here].index(i)] = True
#                     dfs(i)
#                 elif len(answer)==len(tickets):
#                     answer.append(i)         
#     answer = []
#     adj,vertexLen,dict2idx = ticket2Adj(tickets)
#     visited = [[False]*len(v) for k,v in adj.items()]
#     dfs("ICN")
#     return answer
    
# def ticket2Adj(tickets):
#     tmp = dict()
#     for i in tickets:
#         fr,to = i
#         if tmp.get(fr):
#             bisect.insort(tmp[fr], to)
#         else:
#             tmp[fr]=[to,]
#     dict2Idx = dict()
#     for i,j in enumerate(tmp.keys()):
#         dict2Idx[j]=i
    
#     vertexLen = i+1
#     return tmp,vertexLen,dict2Idx