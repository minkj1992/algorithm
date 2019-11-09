import re
def solution(user_id, banned_id):
    queries = [bi.replace('*', '.') for bi in banned_id]
    regex = [(len(q),re.compile(q)) for q in queries]
    answer = []
    all_elem = []
    for rgx in regex:
        _len,r = rgx
        answer.append([])
        for i,uid in enumerate(user_id):
            if len(uid) == _len  and r.match(uid):
                answer[-1].append(uid)
                if uid not in all_elem:
                    all_elem.append(uid)
    visited = [0]*len(all_elem)
    e2idx = {v:k for k,v in enumerate(all_elem)}

    result = []
    depth = len(answer)

    def dfs(i,visited):
        nonlocal result,depth,answer
        if i == depth:
            if visited not in result:
                result.append(visited)
            return
        
        for v in answer[i]:
            if e2idx[v] not in visited:
                dfs(i+1,visited|set([e2idx[v]]))
    
    dfs(0,set())
    return len(result)