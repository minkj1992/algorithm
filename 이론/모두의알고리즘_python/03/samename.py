#   P: find duplicated element
#   In: List of names
#   Out: duplicated name


#  list - list is not available without class
#  so using list_comprehension
def same_name(li):
    [li.remove(i) for i in set(li)]
    return li

        
li_names = ["Tom","Tom","jane","minkj","minkj","kelly","kelly"]
print(same_name(li_names))
