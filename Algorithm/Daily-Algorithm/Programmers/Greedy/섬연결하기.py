def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x:x[2])
    island = set([costs[0][0]])

    while len(island) != n:
        for cost in costs:
            if cost[0] in island and cost[1] in island:
                continue
            if cost[0] in island or cost[1] in island:
                island.add(cost[0])
                island.add(cost[1])
                answer += cost[2]
                break

    return answer

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4

print(solution(n,costs))