# O(n^2)
# 울타리 문제,두번째 for문 indexing
def FenceBruteForce(rect):
    ret = 1
    for l in range(len(rect)):
        # 파이썬에서 [:outofBound]여도 error 안뜬다.
        for r in range(l+1,len(rect)+1):
            ret= max(ret,(r-l)*min(rect[l:r]))
    return ret
# 종만 행님코드,indexing이 훨씬 깔끔하다. [:]사용하지 않고 minheight 만 그때그때 구해준다.
def FenceBruteForce2(rect):
    ret = 1
    for l in range(len(rect)):
        minHeight = rect[l]
        # 파이썬에서 [:outofBound]여도 error 안뜬다.
        for r in range(l,len(rect)):
            minHeight = min(minHeight,rect[r])
            ret= max(ret,(r-l+1)*minHeight)
    return ret

for _ in range(int(input())):
    input()
    rect = [int(i) for i in input().split()]
    print(FenceBruteForce(rect))

 
