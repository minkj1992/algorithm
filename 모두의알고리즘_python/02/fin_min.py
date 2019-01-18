#   P: find min
#   In: list of numbers
#   Out: min element

def find_min(li):
    return min(li)

def find_min2(li):
    min = li[0]
    for i in li:
        if min>i:
            min = i
    return min


li = [100,2,1,19,27,26,-9]

print(find_min(li))
print(find_min2(li))