# https://algospot.com/judge/problem/read/PICNIC
def countPairings(friends):
    global areFriends
    first = -1
    ret=0
    for i,j in enumerate(friends):
        if not j: first=i;break
    # BASE CONDITION
    if first is -1: return 1
    for pairIdx in range(first+1,len(friends)):
        if not friends[pairIdx] and areFriends[first][pairIdx]:
            friends[first]=friends[pairIdx]=True
            ret+=countPairings(friends)
            friends[first]=friends[pairIdx]=False
    return ret

if __name__=='__main__':
    for _ in range(int(input())):
        N,M = map(int,input().split())
        tmp=list(map(int,input().split()))
        # friends = list(zip(tmp[0::2],tmp[1::2]))
        # 파이썬에서 원소 한개를 바꾸었는데 리스트 전체가 바뀔 경우에 대하여 파이썬은 리스트 값을 복사하는 것이 아니라, 같은 객체를 가리키고 있는 것이다. 그러므로 같은 녀석일 경우에 list 재할당하면 한번에 모두 같은 값으로 변해버린다.
        # 이를 해결하기 위해서는 list comprehension을 사용하면 간단해진다.
        # mylist = [[1]*4 for n in range(3)]
        # N*N matrix
        areFriends=[[False,]*N for i in range(N)]
        for i in zip(tmp[0::2],tmp[1::2]):
            a,b=i
            areFriends[a][b]=True
            areFriends[b][a]=True
        friends=[False,]*N
        print(countPairings(friends))



# # mylist = [[1]*4 for n in range(3)]
# mylist = [[1]*4]*3
# mylist[0][0] = 7
# print(mylist)
# print(id(mylist[0][0]))
# print(id(mylist[0][1]))

# # [[7, 1, 1, 1], [7, 1, 1, 1], [7, 1, 1, 1]]
# # 94662471283776
# # 94662471283584
