'''
https://www.acmicpc.net/problem/2475
1. 5개의 숫자를 입력받는다.
2. 각 숫자를 제곱한 후 모두 더한다.
3. 10으로 나눈 나머지를 출력한다.
'''


def solution(li):
    answer = 0
    for i in li:
        answer += i**2
    return answer % 10


li = list(map(int, input().split()))
print(solution(li))
