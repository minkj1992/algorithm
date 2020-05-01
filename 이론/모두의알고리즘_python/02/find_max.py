#   P : find max problem
#   In: list of numbers
#   Out: max elements

def find_max(li):
    return max(li)

def find_max2(li):
    max = li[0]
    for i in li:
        if max < i:
            max = i
    return max


print(find_max([1,2,3,4,5,100]))
print(find_max2([1,2,3,4,5,100]))