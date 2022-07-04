# 모든 숫자를 돌면서 더하거나 빼는 모든 경우 조사함
def dfs(array, numbers, target, size):
    answer = 0 
    # 만약 조사 끝났는데
    if len(array) == size:
        # array에 들어있는 숫자들의 합이 타겟넘버와 같으면 
        if sum(array) == target:
            # 1 반환 
            return 1
        # 아니면
        else: 
            # 0 반환
            return 0
    # 조사 끝나지 않았으면
    else:
        # numbers에서 숫자 하나를 pop해서
        A = numbers.pop(0)
        # -나 +해줌
        for i in [1, -1]:
            array.append(A * i)
            # 그리고 순환
            answer += dfs(array, numbers, target, size)
            # A에 대해 조사가 끝나고 array에서 pop 해줌
            array.pop()
        # 다시 numbers끝에 A 넣어줌
        numbers.append(A)
        return answer 

def solution(numbers, target):
    answer = 0
    # 첫 번째 숫자가 양수인 경우 dfs 돌려주고
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    # 두 번째 숫자가 음수인 경우 dfs 돌려줌
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))