# https://www.acmicpc.net/problem/1303
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,wb):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = 1

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = dx[i] + x
            new_y = dy[i] + y

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            if visited[new_y][new_x] == 0 and war[new_y][new_x] == wb:
                cnt += 1
                visited[new_y][new_x] = 1
                queue.append((new_x, new_y))

    return cnt


n, m = map(int, input().split())
war = []
visited = []
for i in range(m):
    w = input()
    war.append(w)
    visited.append([0]*n)

w_list = []
for x in range(n):
    for y in range(m):
        if war[y][x] == 'W' and visited[y][x] == 0:
            cnt = bfs(x,y,'W')
            w_list.append(cnt*cnt)

b_list = []
for x in range(n):
    for y in range(m):
        if war[y][x] == 'B' and visited[y][x] == 0:
            cnt = bfs(x,y,'B')
            b_list.append(cnt*cnt)

w_sum = sum(w_list)
b_sum = sum(b_list)
print(w_sum , end=" ")
print(b_sum)
