def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue_truck = []  # 다리를 건너는 트럭
    queue_time = []  # 다리를 건너는 트럭 시간
    queue_weights = 0
    # 다리를 지난 트럭은 pop함.
    # 마지막 트럭이 들어오는데 걸린 시간 + 다리길이 = answer
    while truck_weights:
        truck_top = truck_weights[0]
        if queue_weights+truck_top <= weight:
            queue_time.append(0)
            queue_truck.append(truck_weights.pop(0))
            queue_weights = queue_weights+truck_top
        queue_time = list(map(lambda x: x+1, queue_time))

        if queue_time[0] >= bridge_length:
            queue_weights = queue_weights - queue_truck.pop(0)
            queue_time.pop(0)

        answer = answer+1

    answer = answer+bridge_length
    return answer


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
ans = solution(bridge_length, weight, truck_weights)

print(ans)
