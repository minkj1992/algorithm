def solution(answers):
    N = len(answers)
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    
    tmp = one*(N//len(one))+one[:(N%len(one))]
    tmp2 = two*(N//len(two))+two[:(N%len(two))]
    tmp3 = thr*(N//len(thr))+thr[:(N%len(thr))]
    one = two = thr = 0
    for a,i,j,k in zip(answers,tmp,tmp2,tmp3):
        if a == i: one +=1
        if a == j: two +=1
        if a == k: thr +=1
    num = max(one,two,thr)
    return [i+1 for i,j in enumerate([one,two,three]) if j==num]
