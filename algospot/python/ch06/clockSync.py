import sys
'''
  # 4^10 중 스위치 한번 누르는 것이 one iteration in recursive 
    SWITCHES = [
        ['0', '1', '2'],
        ['3', '7', '9','11'],
        ['4', '10', '14', '15'],
        ['0', '4', '5', '6,', '7'],
        ['6', '7', '8', '10,', '12'],
        ['0', '2', '14', '15'],
        ['3', '14', '15'],
        ['4', '5', '7', '14', '15'],
        ['1', '2', '3', '4', '5'],
        ['3', '4', '5', '9', '13'],
        ] 
'''
def isAligned(clocks):
    for c in clocks:
        if c != 4: return False
    return True

# 스위치 한번 눌렀을 경우의 clocks 값 변경
def push(clocks,switch):
    global LINKED
    for i,j in enumerate(LINKED[switch]):
        if j==True:
            clocks[i]+=1
            if clocks[i]==5:clocks[i]=1
def solve(clocks,switch):
    global INF,SWITCH_LEN,CLOCK_SIZE
    if switch == SWITCH_LEN:
        return 0 if isAligned(clocks) else INF
    ret = INF
    for click in range(4):
        ret=min(ret,click+solve(clocks,switch+1))
        push(clocks,switch)
    return ret
    

if __name__=='__main__':
    # LINKED[switch][clock]
    LINKED = [
        [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, True, False, False, False, True, False, True, False, True, False, False, False, False],
        [False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, True],
        [True, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, True, True, True, False, True, False, True, False, False, False],
        [True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True],
        [False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, True],
        [False, False, False, False, True, True, False, True, False, False, False, False, False, False, True, True],
        [False, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False],
        [False, False, False, True, True, True, False, False, False, True, False, False, False, True, False, False],
        ]       
    SWITCH_LEN = 10
    CLOCK_SIZE =16
    INF = sys.maxsize
    for _ in range(int(input())):
        clocks=[int(i)//3 for i in input().split()]
        ret=solve(clocks,switch=0)
        print(-1) if ret==INF else print(ret)
