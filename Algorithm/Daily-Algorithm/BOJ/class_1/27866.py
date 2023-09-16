'''
https://www.acmicpc.net/problem/27866
1. 단어 S, 정수 i가 주어졌을 때 S의 i번째 글자를 출력하는 프로그램을 작성하시오.
'''


def solution(s, i):
    return s[i-1]


s = input()
i = int(input())
print(solution(s, i))
