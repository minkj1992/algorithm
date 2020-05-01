# p: square sum
#in : n
#out : square sum

def sum_square(n):
    tmp = 0
    for i in range(1,n+1):
        tmp += i**2
    return tmp

def sum_square2(n):
    return sum([i**2 for i in range(1,n+1)])

# // for int type
#  implement by gaussian
def sum_square3(n):
    return n*(n+1)*(2*n+1)//6

    
print(sum_square(2))
print(sum_square2(2))
print(sum_square3(2))

