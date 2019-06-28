### 아래는 테스트케이스 3번이 계속 틀린경우이다. 
### 솔직히 왜 이런 현상이 일어나는지 모르겠다.
def solution(begin, target, words):
    def dfs(here=0,cnt=0):
        if here == target[0]:
            answer[0] = min(cnt,answer[0])
        visited[here]=="GRAY"
        
        for i in adj[here]:
            if visited[i]!="BLACK":
                dfs(i,cnt+1)
        if here !=(len(words)-1):
            visited[here] = "BLACK"
         
    if target not in words:return 0  
    words.insert(0,begin)   
    # adj에는 words의 idx가 들어간다.
    adj = words2Adj(words)
    target = [words.index(target),]
    
    visited = ["WHITE" for i in range(len(words))]
    MAX_INTEGER = 9223372036854775807
    answer = [MAX_INTEGER,]
    dfs()
    return 0 if answer[0]==MAX_INTEGER else answer[0]

def words2Adj(words):
    n=len(words)
    adj = [[] for i in words]
    for i in range(n-1):
        for j in range(i+1,n):
            cnt = 0
            for a,b in zip(words[i],words[j]):
                if a != b: 
                    cnt+=1
                    if cnt>1:
                        break
            if cnt==1:
                adj[i].append(j)
    return adj


# print(solution("hit","cog",["hot","dot", "dog", "lot", "log", "cog"]))
# print(solution("hit","cog",["hot","dot", "dog", "lot", "log"]))


