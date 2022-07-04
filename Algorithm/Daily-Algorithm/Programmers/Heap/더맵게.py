import heapq


def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        answer += 1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        s = s1 + s2*2

        heapq.heappush(scoville, s)

    if scoville[0] >= K:
        return answer

    answer = -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))
