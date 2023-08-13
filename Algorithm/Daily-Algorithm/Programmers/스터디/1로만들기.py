'''
1. N에서 1을 뺀다
2. N을 K로 나눈다
N이 될 때 까지 1 또는 2를 수행하는 최소 수를 구해라
'''
def solution(n, k):
    result = n
    answer = 0
    while result > 1:
        if (result%k == 0):
            # 나누어 떨어지면 나누기
            result = result//k
            answer += 1
        else:
            # 나누어 떨어지지 않으면 빼기
            result -= 1
            answer += 1
    return answer
n, k = map(int, input().split())
print(solution(n, k))

