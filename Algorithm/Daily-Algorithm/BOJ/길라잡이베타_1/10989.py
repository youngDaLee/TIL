import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    res = []
    for i in range(n):
        num = int(sys.stdin.readline())
        res.append(num)

    res = sorted(res)

    for i in res:
        print(i)
    