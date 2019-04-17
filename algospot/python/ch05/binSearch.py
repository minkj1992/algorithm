def binSearch(a, x):
    """
    a = non decreasing ordered list
    x = want to find value
    return error or index
    """  
    lo = 0
    hi = len(a)
    # a==[]
    if not hi: raise ValueError("NULL INDEX INSERTED")
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo-1 if a[lo-1]==x else "VALUE NOT FOUND"

def binSearch2(a, x):
    """
    a = non decreasing ordered list
    x = want to find value
    return error or index
    """  
    lo = -1
    hi = len(a)
    # a==[]
    if not hi: raise ValueError("NULL INDEX INSERTED")
    while lo+1 < hi:
        mid = (lo+hi)//2
        if x > a[mid]: lo = mid
        else: hi = mid
    return hi if a[hi]==x else "VALUE NOT FOUND"
 

 
if __name__=="__main__":
    li = [79]
    x = 78
    print(binSearch(li,x))
