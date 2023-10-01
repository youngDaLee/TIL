'''
https://www.acmicpc.net/problem/9012

괄호가 제대로 되었는지 검사
'''


def vps(ps):
    stack = []
    while ps:
        top = ps.pop()
        if top == '(' and stack and stack[-1] == ')':
            stack.pop()
        else:
            stack.append(top)

    if stack:
        return False
    else:
        return True


def solution(n):
    for _ in range(n):
        ps = list(input())
        if (vps(ps)):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    n = int(input())
    solution(n)
