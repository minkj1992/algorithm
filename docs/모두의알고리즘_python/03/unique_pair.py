from collections import Counter
#   P: list_a, list_b, make unique_pair
#   In: ls_a, ls_b
#   Out: unique_pair

def u_pair(ls_a,ls_b):
    tmp_list = [[i,j] for i in ls_a for j in ls_b]
    duplic = list()
    print(tmp_list)
    for i,j in enumerate(tmp_list):
        for k in tmp_list[i+1:]:
            if Counter(j)==Counter(k):
                duplic.append(j)
    for i in duplic:
       tmp_list.remove(i)
    return tmp_list 



ls_a = ['a','b','c']
ls_b = ['b','a','c']

print(u_pair(ls_a,ls_b))

