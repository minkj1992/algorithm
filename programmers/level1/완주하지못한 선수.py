first try
def solution(participant, completion):
    answer = ''
    
    dic={name:0 for name in participant}
    for name in participant:dic[name]+=1
    for name in completion:dic[name]-=1
    for k,v in dic.items():
        if v != 0: answer+=k

    return answer