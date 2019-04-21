# TSP
# BRUTE FORCE
# RECURSIVE CALL
import sys
def shortestPath(visited,dist,curLen):
    global N
    # BASE CONDITION
    if len(path)==N:
        # 현재까지의 거리 + 원점으로 돌아가는 거리
        # return curLen + dist[0][path[-1]]
        return curLen
    ret = sys.float_info.max
    for next in range(N):
        if visited[next]:continue
        # path의 here 부터 시작하는데 init에 next를 넣어주어야 start point가 0만 되지 않는다.
        # 책의 코드는 main에서 n 만큼 함수 호출을 해서, 이 구문이 필요없다. (https://jaimemin.tistory.com/304)
        if path:
            here=path[-1]
        else: here=next

        visited[next]=True
        path.append(next)
        tmp = shortestPath(visited,dist,curLen+dist[here][next])
        ret = min(ret,tmp)
        visited[next]=False
        path.pop()
    return ret

    
if __name__=='__main__':
    for _ in range(int(input())):
        N = int(input())
        dist=[]
        # path = 지금까지의 루트(idxes) 포함 list
        path = []
        # visited = [False,False,False,.....]
        visited = [False]*(N)
        curLen = 0
        
        for _ in range(N):
            tmp=list(map(float,input().split()))
            dist.append(tmp)

        ret = shortestPath(visited,dist,curLen)
        
        # OUTPUT
        print(ret)
