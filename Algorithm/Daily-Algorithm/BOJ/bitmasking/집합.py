import sys

m = int(input())
S = set()

for _ in range(m):
    data = list(map(str, sys.stdin.readline().split()))
    ch = data[0]

    if ch == 'add':
        S.add(int(data[1]))
    elif ch == 'remove':
        S.discard(int(data[1]))
    elif ch == 'check':
        if int(data[1]) in S:
            print(1)
        else:
            print(0)
    elif ch == 'toggle':
        S.discard(int(data[1]))
    elif ch == 'all':
        S = set(map(lambda x : x, range(1, 21)))
    elif ch == 'empty':
        S = set()

