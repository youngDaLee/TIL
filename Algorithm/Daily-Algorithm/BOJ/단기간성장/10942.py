from collections import deque
import sys

def pallendrom(li):
    queue = deque(li)
    while len(queue) > 1:
        l = queue.popleft()
        r = queue.pop()
        if l != r:
            return 0
    return 1



n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(pallendrom(li[s-1:e]))