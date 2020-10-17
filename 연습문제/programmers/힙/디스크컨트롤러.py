import heapq


def solution(jobs=[[0, 3], [1, 9], [2, 6]]):
    # base condition
    if len(jobs) == 1:
        return jobs[1]

    jobs = sorted(jobs, key=lambda x: x[0])
    min_in_time = jobs[0][0]
    for job in jobs:
        job[0] -= min_in_time

    print(jobs)
    min_heap = []

    answer = 0
    return answer

# 다음 시작 시간 + 소모시간 - 들어온 시점
