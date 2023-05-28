answer = []
def dfs(numbers, visit):
    if len(visit)== 2:
        num1 = numbers[visit[0]]
        num2 = numbers[visit[1]]
        return num1 + num2

    for j in range(len(numbers)):
        if j in visit:
            pass
        else:
            visit.append(j)
            res = dfs(numbers,visit)
            if res:
                answer.append(res)
            visit.pop()

def solution(numbers):
    global answer
    res = []
    dfs(numbers, res)
    answer = list(set(answer))
    answer.sort()
    return answer


a = solution([1,6,-3,5,8,-2,6,-9,9,-4,1])
print(a)