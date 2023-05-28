def findmax(n, li):
    for l in li:
        if l > n:
            return l
    return -1

def solution(numbers):
    answer = [-1] * (len(numbers))
    for i in range(len(numbers)-1, -1, -1):
        n = numbers[i]
        if (i+1<len(numbers)-1) and answer[i+1] != -1:
            if numbers[i+1] <= numbers[i]:
                answer[i] = answer[i+1]
            else:
                answer[i] = numbers[i+1]
        num = findmax(n, numbers[i:])
        answer[i] = num
    return answer


li = [2, 3, 3, 5]
print(solution(li))
