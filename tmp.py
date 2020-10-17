import heapq
from collections import deque


def make_priority(job, before_time=0):
    in_time, cost_time = job
    return before_time + cost_time - in_time, job


def get_pop_idx(jobs, nxt_time=0):
    for i, job in enumerate(jobs):
        if job[0] > nxt_time:
            return i

    # 모두 nxt_time 일경우
    return len(jobs)


def solution(jobs):
    N = len(jobs)

    # base condition
    if N == 1:
        return jobs[0][1]

    jobs = deque(sorted(jobs, key=lambda x: x[0]))
    first_job = jobs.popleft()
    for job in jobs:
        job[0] -= first_job[0]

    min_heap = []
    first_job[0] = 0
    heapq.heappush(min_heap, make_priority(first_job))

    i = get_pop_idx(jobs)

    for _ in range(i):
        job = jobs.popleft()
        heapq.heappush(min_heap, make_priority(job))

    cur_time = -1
    nxt_time = 0
    answer = []
    while cur_time < 1001 and jobs:
        i = get_pop_idx(jobs, cur_time)
        for _ in range(i):
            job = jobs.popleft()
            heapq.heappush(min_heap, make_priority(job, cur_time))

        if nxt_time <= cur_time:
            if min_heap:
                _, nxt_job = heapq.heappop(min_heap)
                in_time, cost_time = nxt_job
                nxt_time = cost_time + max(in_time, cur_time)
                answer.append(cost_time + max(cur_time-in_time, 0))
        cur_time += 1

    while min_heap:
        _, nxt_job = heapq.heappop(min_heap)
        in_time, cost_time = nxt_job
        nxt_time = cost_time + max(in_time, cur_time)
        answer.append(cost_time + max(cur_time - in_time, 0))
        cur_time = nxt_time

    print(answer)
    return sum(answer) // N

result = solution([[0, 10], [2,10], [9,10], [15,2]])
print(result)
