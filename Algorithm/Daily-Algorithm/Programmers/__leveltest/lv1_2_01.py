def solution(n):
    answer = 0
    str_n = str(n)
    li = []
    for i in range(0, len(str_n)):
        li.append(str_n[i])
    li.sort(reverse=True)
    answer = int(''.join(li))
    return answer

n = 118372
print(solution(n))