def solution(heights):
    answer = []
    N = len(heights)
    for i in range(N-1,-1,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
        else:
            answer.append(0)
    return answer[::-1]