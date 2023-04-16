# https://www.acmicpc.net/problem/2178
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,visited, mirro):
    n = len(mirro[0])
    m = len(mirro)

    queue = deque()
    queue.append((x,y))
    visited[y][x] = 1

    while queue:
        x, y = queue.popleft()
        now_visit = visited[y][x]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
                continue
            if visited[next_y][next_x]==0 and mirro[next_y][next_x]=="1":
                visited[next_y][next_x] = now_visit + 1
                queue.append((next_x,next_y))
    return visited[m-1][n-1]

n, m = map(int, input().split())
mirro = []
visited = []
for i in range(n):
    w = input()
    mirro.append(w)
    visited.append([0]*m)

res = bfs(0, 0, visited, mirro)
print(res)
