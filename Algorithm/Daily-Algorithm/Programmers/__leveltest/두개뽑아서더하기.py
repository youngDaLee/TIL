def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer


numbers = [5, 0, 2, 7]
print(solution(numbers))
