# 1st try
def solution(n, lost, reserve):    
    num = len(reserve)

    for j in lost:
        for i in [0,-1,1]:
            if i+j in reserve:
                reserve.remove(i+j)
                break
    return n-len(lost)+min(len(lost),(num-len(reserve)))
    

# 2nd try
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort() len(lost)-len(reserve)
    for i in reserve:len(lost)-len(reserve)
        for j in [0,-1,1]:
            if i+j in lost:
                lost.remove(i+j)
                break
    return n-len(lost)

# 5 [4,5] [3,4] 4 case exception
# 만약 reserve로 for문을 돈다면
def solution(n, lost, reserve):
    lost.sort();reserve.sort() 
    for idx,i in enumerate(reserve):
        for j in [0,-1,1]:
            # lost에 있으면서
            if i+j in lost:
                # 현재 reserve 보다 뒤에 녀석들에 i+j가 없을 경우(즉 lost와 reserve가 같은 경우 체크)
                if i+j not in reserve[idx+1:]:
                    lost.remove(i+j)
                break
    return n-len(lost)


# # 만약 lost로 for 문을 돈다면

# def solution(n, lost, reserve):
#     lost.sort();reserve.sort()
#     num = len(reserve);
#     for i in range(len(lost)):
#         # 현재 lost + 1이 lost에 존재하면서, reserve에 존재한다면 우선순위가 현재가 아닌 뒤에 가 있게 된다.
#         for j in [0,-1,1]:
#             if lost[i]+j in reserve:
#                 if lost[i+1] not in reserve:
#                     # del lost[i]
#                     # reserve를 지워주어야 한다.
#                     reserve.remove(lost[i])
#                 break
#     return n-len(lost)+min(len(lost),(num-len(reserve)))

