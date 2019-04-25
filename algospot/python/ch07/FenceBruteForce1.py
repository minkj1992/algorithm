# 울타리 문제,두번째 for문 indexing
def FenceBruteForce(rect):
    ret = 1
    for l in range(len(rect)):
        # 파이썬에서 [:outofBound]여도 error 안뜬다.
        for r in range(l+1,len(rect)+1):
            ret= max(ret,(r-l)*min(rect[l:r]))
    return ret
for _ in range(int(input())):
    input()
    rect = [int(i) for i in input().split()]
    print(FenceBruteForce(rect))
