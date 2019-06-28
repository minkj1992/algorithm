def hanoi(N,s="1",m="2",e="3"):
    if N==1:
        print(s+" "+e)
        answer[0]+=1
        return
    hanoi(N-1,s,e,m)
    hanoi(1,s,m,e)
    hanoi(N-1,m,s,e)
n = int(input())
answer = [0,]
hanoi(n)
print(answer[0])