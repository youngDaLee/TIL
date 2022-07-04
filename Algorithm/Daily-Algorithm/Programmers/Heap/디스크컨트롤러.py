import heapq

import heapq


def solution(jobs):
    answer = 0

    # 먼저 정렬
    jobs = sorted(jobs)

    print(jobs)
    time = 0
    heap = []
    while jobs:
        for i in range(0, len(jobs)):
            heapq.heappush(jobs[i][1])
            jobs.pop(i)

        if len(heap) < 1:
            time += 1
        else:
            now = heapq.heappop(heap)
            answer += now
    return answer


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
