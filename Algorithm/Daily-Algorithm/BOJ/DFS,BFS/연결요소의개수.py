# https://www.acmicpc.net/problem/11724
from collections import deque

n, m = map(int, input().split())

graph = {}
visited = [0]*(n+1)
for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(num):
    queue = deque()
    queue.append(num)
    visited[num] = 1
    while queue:
        x = queue.popleft()
        for n in graph[x]:
            if visited[n] == 0:
                visited[n] = 1
                queue.append(n)


res = 0
while sum(visited) < n:
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i)
            res += 1
            break
print(res)
