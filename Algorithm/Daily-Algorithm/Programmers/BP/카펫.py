def solution(brown, yellow):
    answer = []

    yellow_list = []

    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_list.append([int(yellow/i), i])
    for y in yellow_list:
        if sum(y)*2+4 == brown:
            answer.append(y[0]+2)
            answer.append(y[1]+2)
            break
    return answer


brown = 8
yellow = 1
print(solution(brown, yellow))
