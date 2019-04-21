# 각 타입의 3가지 조각에 대해서 CHECK
def boardCheck(board,piv,type,delta=1):
    '''
    1) board를 delta로 check를 한다.
    1`) 끝까지 돌리기 위해서 flag를 사용하여 flow control
    2) n^2을 돌면서 조각 하나를 넣을 수 있다면 flag true
    3) outOfBound or (board[i][j]+=delta)>1 이면 flag false

    OUTPUT = 조각 1개를 넣을 수 있고 BOARD에 CHECK를 해줌. OR 조각 1개를 넣을 수 없고, BOARD CHECK를 해줌. 
    IF DELTA=-1이면 WIPE 또한 해준다.
    '''
    flag=True
    print(board)
    for move in coverType[type]:
        y=piv[0]+move[0]
        x=piv[1]+move[1]
        if not(0<=y<len(board) and 0<=x<len(board[0])):flag=False
        else:
            board[y][x]+=delta
            if board[y][x]>1: flag=False
    print(board)
    return flag

# MOVE TYPE별로 BOARDCHECK CALL
def boardCover(board):
    
    '''
    Recursive call
    1) board를 돌면서 가장 왼쪽/위에 있는 piv를 찾는다.
    2-1) main에서 ERRORHANDLING해준다.
    2-2) BASECONDITION:
        모든 칸을 다 채웠으면(if cannot find piv) return 1
    2-3) piv를 찾았다면 
        2-3-1) 4가지 type을 돌면서, if check: boardCover -> after that wipe with delta
    '''
    # (y,x)
    BASEPIV=(-1,-1)
    piv=BASEPIV
    ret=0
    # 1)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0:
                piv=(i,j)
                break
        if piv!=BASEPIV:break
    # 2-2)
    if piv==BASEPIV:return 1
    # 2-3) 
    for type in range(len(coverType)):
        if boardCheck(board,piv,type):
            ret+=boardCover(board)
        boardCheck(board,piv,type,-1)
    return ret


if __name__=='__main__':
    '''
        2-1) ERRORHANDLING:
            2-1-1) WHITE % 3!=0 OR len(WHITE)<3
            2-1-2) 2>W,H
    '''
    coverType=[((0,0),(1,0),(0,1)),
               ((0,0),(0,1),(1,1)),
               ((1,0),(0,1),(1,1)),
               ((0,0),(1,0),(0,1))]
    for _ in range(int(input())):
        H,W=map(int,input().split())
        board = []   
        cnt = 0
        # ERRORHANDLING
        if H<2 or W<2: print(0);continue
        for i in range(H):
            tmp=[]
            for j,val in enumerate(input()):
                if val=='.':
                    tmp.append(0)
                    cnt+=1
                else:
                    tmp.append(1)
            board.append(tmp)    
        # ERRORHANDLING
        if cnt%3!=0 or cnt<3:print(0);continue
        print(boardCover(board))

# 파이썬에서 board=[[1]*M]*H 
# 이런식으로 하니까 첫 row init되면 그 다음부터는 다 첫 row를 따라가게 된다. 왜이러지..



