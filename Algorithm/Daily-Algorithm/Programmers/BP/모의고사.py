def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5] * 10000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000

    p1Ans, p2Ans, p3Ans = 0, 0, 0

    for i in range(0, len(answers)):
        if p1[i] == answers[i]:
            p1Ans += 1
        if p2[i] == answers[i]:
            p2Ans += 1
        if p3[i] == answers[i]:
            p3Ans += 1
    li = [p1Ans, p2Ans, p3Ans]
    max_num = max(li)
    for i in range(0, 3):
        if max_num == li[i]:
            answer.append(i+1)
    return answer


answer = [1, 2, 3, 4, 5]
print(solution(answer))
