def partialSum(li):
    ret = []
    ret.append(li[0])
    for i,j in enumerate(li[1:]):
        ret.append(ret[i]+j)
    return ret

def rangeSum(pSum,s,e):
    if s==0: return pSum[e]
    return pSum[e]- pSum[s-1]
