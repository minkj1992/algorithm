# 최대 연속 부분 구간 합 문제
import sys
MIN = -sys.maxsize-1
# O(n^3)
def inefficientMaxSum(A):
    ret = MIN
    for i in range(len(A)):
        for j in range(i,len(A)):
            sum=0
            for k in A[i:j+1]:
                sum+=k
                ret=max(ret,sum)
    return ret

# O(n^2)
def betterMaxSum(A):
    ret = MIN
    for i in range(len(A)):
        sum=0
        for j in range(i,len(A)):
            sum+=A[j]
            ret=max(ret,sum)
    return ret

# O(nlogn)
def fastMaxSum(A,lo,hi):
    if lo==hi: return A[lo]
    mid = (lo+hi)//2
    left = right = MIN
    sum=0
    for i in reversed(A[lo:mid+1]):
        sum+=i
        left=max(sum,left)
    sum=0
    for i in A[mid+1:hi+1]:
        sum+=i
        right=max(sum,right)
    single = max(fastMaxSum(A,lo,mid),fastMaxSum(A,mid+1,hi))
    return max(left+right,single)

# O(n)
def fastestMaxSum(A):
    psum = 0
    ret = MIN
    for i in A:
        psum=max(psum,0)+i
        ret=max(psum,ret)
    return ret
    

if __name__=='__main__':
    A = [1,2,-3,4,5,-6,7,8,-100,10,10,10,10,10]
    print(inefficientMaxSum(A))
    print(betterMaxSum(A))
    print(fastMaxSum(A,0,len(A)-1))
    print(fastestMaxSum(A))
