from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n,m = map(int, input().split())
graph = []
for i in range(n):
    raw = input()
    li = []
    for j in raw:
        li.append(int(j))
    graph.append(li)


def bfs(y, x):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(3):
            new_x = dx[i] + x
            new_y = dy[i] + y
            if new_x < m and new_y < n:
                if graph[new_x][new_y] == 1:
                     queue.append((new_y, new_x))
                     graph[new_x][new_y] = graph[x][y] + 1
                     print(graph)


bfs(0,0)
print(graph[n-1][m-1])