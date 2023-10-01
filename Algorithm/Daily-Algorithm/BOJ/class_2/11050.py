'''
https://www.acmicpc.net/problem/11050

n, k가 주어졌을 때 이항계수
'''


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def solution(n, k):
    return factorial(n) // (factorial(n-k) * factorial(k))


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))
