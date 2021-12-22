def solution(p,s):

    answer = 0
    for a,b in zip(p,s):
        v = abs(int(a)-int(b)) 
        answer += min(10-v,v)
    return answer