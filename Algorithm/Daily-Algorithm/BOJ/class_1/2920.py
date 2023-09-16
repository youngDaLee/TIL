'''
https://www.acmicpc.net/problem/2920
1. 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다.
2. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다.
    c는 1로, d는 2로, ..., C를 8로 바꾼다.
3. 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending,
'''


def solution(arr):
    if arr == sorted(arr):
        return 'ascending'
    elif arr == sorted(arr, reverse=True):
        return 'descending'
    else:
        return 'mixed'


print(solution(list(map(int, input().split()))))
