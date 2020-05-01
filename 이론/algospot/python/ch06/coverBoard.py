# M이 필요할까?
def boardCover(bMtx):
    
    # BASE CONDITION
    if all(x == False for row in bMtx for x in row):print(1);return
    # if any(x == False for row in bMtx for x in row):

    # if sum(bMtx)==0:
    # transaction 3단계 다 맞아야 bMtx[i][j]=False
    for i,row in enumerate(bMtx[:-1]):
        for j,flag in enumerate(row[:-1]):
            # flag true 이면서
            for moves in coverType:
                cond=True
                for mov in moves:
                    if M[i+mov[0]][j+mov[1]]!='.' or not bMtx[i+mov[0]][j+mov[1]]:cond=False;break
                if cond:
                    for mov in moves:
                        bMtx[i+mov[0]][j+mov[1]]=False
                    boardCover(bMtx)
                    for mov in moves:
                        bMtx[i+mov[0]][j+mov[1]]=True


# Brute force
# Recursion
for _ in range(int(input())):
    
    H,W = map(int,input().split())
    # ERROR HANDLING (1)
    if H<=1: print(0);continue
    # INIT
    M=[[0]*W]*H
    cnt=0
    # 탐색해야 하는 범위(H-2*W-2 && white)
    # bMtx = [[True]*(W-1)]*(H-1)
    bMtx = [[True]*W]*H
    for i in range(H):
        for j,val in enumerate(input()):
            M[i][j]=val
            if val =='.':
                cnt+=1
                
    if cnt%3!=0: print(0);continue
    coverType=[((0,0),(1,0),(0,1)),
               ((0,0),(0,1),(1,1)),
               ((1,0),(0,1),(1,1)),
               ((0,0),(1,0),(0,1))]


    boardCover(bMtx)


