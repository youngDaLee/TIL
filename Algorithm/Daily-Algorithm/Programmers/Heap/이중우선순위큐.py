import heapq


def solution(operations):
    answer = []
    hq = []

    for o in operations:
        if o == "D 1":
            if len(hq) > 0:
                hq.remove(max(hq))
                heapq.heapify(hq)

        elif o == "D -1":
            if len(hq) > 0:
                heapq.heappop(hq)

        else:
            num = int(o[2:])
            heapq.heappush(hq, num)
    if len(hq) < 1:
        return [0, 0]

    answer.append(max(hq))
    answer.append(heapq.heappop(hq))

    return answer


operations = ["I 16", "D 1"]
print(solution(operations))
