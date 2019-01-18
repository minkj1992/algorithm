from partialSum import rangeSum,partialSum
def variance(li,s,e):
    sum = rangeSum(partialSum(li),s,e)
    mean = sum
    ret = rangeSum(partialSum([i*i for i in li]),s,e)-2*mean*sum+(e-s+1)*mean*mean
    return ret/(e-s+1)

li = [-14.82381293, -0.29423447, -13.56067979, -1.6288903, -0.31632439,0.53459687, -1.34069996, -1.61042692, -4.03220519, -0.24332097]
print(variance(li,0,len(li)-1))