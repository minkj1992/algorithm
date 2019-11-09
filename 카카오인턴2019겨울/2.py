def solution(strs):
    strs = strs[1:-1]
    strs = strs.split('},')
    if len(strs) == 1:return [int(strs[0][1:-1]),]
    strs = [s.replace('{','').replace('}','') for s in strs]
    strs = [list(map(int,s.split(','))) for s in strs]
    strs = sorted(strs,key=lambda s: len(s))
    
    answer = []
    for i in range(len(strs)):
        val = strs[i][0]
        answer.append(val)
        for j in range(i+1,len(strs)):
            try:
                idx = strs[j].index(val)
                strs[j] = strs[j][:idx] + strs[j][idx+1:]
            except:
                continue
    return answer