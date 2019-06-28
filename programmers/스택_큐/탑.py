def solution(heights):
    # insertion sort 쓰면 어떨까?
    answer=[]
    for i,j in enumerate(heights):
        target = 0
        for piv in range(i-1,-1,-1):
            if j<heights[piv]:
                # index to number
                target=piv+1
                break
        answer.append(target)
    return answer
