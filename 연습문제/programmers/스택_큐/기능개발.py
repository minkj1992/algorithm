import collections
def solution(progresses, speeds):
    tmp = collections.deque([(100-j)//speeds[i] for i,j in enumerate(progresses)])
    if len(tmp)==1: return [1,]
    top = tmp.popleft()
    answer =[];cnt=1
    while tmp:
        tmp_value = tmp.popleft()
        if top<tmp_value:
            top = tmp_value
            answer.append(cnt)
            cnt =1
        else:cnt+=1
    #마지막값
    answer.append(cnt)
    return answer