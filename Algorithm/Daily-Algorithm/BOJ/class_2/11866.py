'''
https://www.acmicpc.net/problem/11866

n명의 사람, k번째 사람 제거... 일 때 제거되는 순서
원형 큐 문제
'''
from collections import deque


n, k = map(int, input().split())
queue = deque(map(lambda x: x+1, range(n)))

res = '<'
while queue:
    for _ in range(k):
        queue.append(queue.popleft())
    res += str(queue.pop()) + ', '

print(res[:-2]+'>')
