def solution(n):
    num = 0
    m = 0
    while num < n:
        m = num + sum(list(map(int,str(num))))
        if m == n:
            return num
        num += 1
    
    return 0

n = int(input())
print(solution(n))
