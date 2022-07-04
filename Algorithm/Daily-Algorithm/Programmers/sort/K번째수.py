def solution(array, commands):
    answer = []

    for c in commands:  # comands 개수만큼 반복
        arr = []
        arr = list(array[c[0]-1:c[1]])
        arr.sort()

        answer.append(arr[c[2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

arr = solution(array, commands)
print(arr)
