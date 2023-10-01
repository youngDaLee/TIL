'''
https://www.acmicpc.net/problem/4153

직각삼각형이면 rigth, 아니면 wrong 출력
'''


def is_right_triangle(a, b, c):
    m = max(a, b, c) ** 2
    if a**2 == m:
        r = b ** 2 + c ** 2
    elif b**2 == m:
        r = a ** 2 + c ** 2
    else:
        r = b ** 2 + a ** 2

    if m == r:
        return True
    else:
        return False


def solution():
    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            return

        if (is_right_triangle(a, b, c)):
            print("right")
        else:
            print("wrong")


if __name__ == '__main__':
    solution()
