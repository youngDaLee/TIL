def solution(n, lost, reserve):
    answer = 0

    li = []
    li.append(1)
    for i in range(1, n+1):
        if i in lost and i in reserve:
            li.append(1)
        elif i in lost:
            li.append(0)
        elif i in reserve:
            li.append(2)
        else:
            li.append(1)
    li.append(1)

    for i in range(1, n+1):
        if li[i] == 0:
            if li[i-1] == 2:
                li[i-1] = 1
                answer += 1
            elif li[i+1] == 2:
                li[i+1] = 1
                answer += 1
        else:
            answer += 1

    return answer


n = 5
lost = [1,2,4]
reserve = [1,2,5]
print(solution(n, lost, reserve))
