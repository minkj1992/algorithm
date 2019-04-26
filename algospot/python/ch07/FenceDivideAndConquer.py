# Divide and Conquer
# 매번 n번 compare, 그렇게 lg(n)번 함수 호출이 일어난다.
# max(왼쪽 영역에서만 답이 존재할 경우 | 오른쪽 영역에서만 답이 존재할 경우 | 둘 영역 모두를 걸칠경우)
# 현재 상태에서 height가 높은쪽으로 확장 한뒤
# Height는 min 으로 계속 업데이트한다.
# 이후 넓이를 max를 통하여 구한다.
def FenceDivideAndConquqer(l,r):
    global rect
    # Base condition, 1개만 남았을 경우
    if l==r: return rect[l]
    mid = (l+r)//2
    ret = max(FenceDivideAndConquqer(l,mid),FenceDivideAndConquqer(mid+1,r))
    lo=mid;hi=mid+1
    height = min(rect[lo],rect[hi])
    ret = max(ret,height*2)
    # myerror "while(lo<left or right<hi)" -> while문이 작동하지 않았다.
    while (l<lo or hi<r):
        if (hi<r) and (lo==l or rect[lo-1]<rect[hi+1]):
            hi+=1; height = min(height,rect[hi])
        else: lo-=1;height = min(height,rect[lo])
        ret = max(ret,(hi+1-lo)*height)
    return ret

for _ in range(int(input())):
    input()
    rect = [int(i) for i in input().split()]
    print(FenceDivideAndConquqer(0,len(rect)-1))
