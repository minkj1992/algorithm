_dir = ((-1,0),(0,1),(1,0),(0,-1))
def solution(office, r, c, move):
    def rotate(d,m):
        d+= 1 if m=="right" else -1
        if d==-1: d=3
        elif d==4:d=0
        return d
    N = len(office)
    answer = office[r][c]
    office[r][c] = 0
    d = 0
    for m in move:
        if m =="go":
            nr = r+_dir[d][0]
            nc = c+_dir[d][1]
            if not ((0<=nr<N) and(0<=nc<N)):continue
            if office[nr][nc]==-1:continue
            # 이동
            r=nr;c=nc
            # 청소
            answer+=office[r][c]
            office[r][c]=0 
        else:
            d=rotate(d,m)
    return answer