# https://www.acmicpc.net/problem/16930
# 시간초과... 반례때문에 visit_i 만들어서 끼워맞췄는데 이게 맞는지도 모르겠음
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))
    visit[x1][y1] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            for nk in range(1, k+1):
                nx = x + dx[i]*nk
                ny = y + dy[i]*nk
                if(nx < 0 or nx >= n or ny < 0 or ny >= m):
                    break
                if(gym[nx][ny] == '#'):
                    break

                if(visit[nx][ny] == 0):
                    visit[nx][ny] = visit[x][y] + 1
                    visit_i[nx][ny].append(i)
                    queue.append((nx, ny))
                if(i not in visit_i[nx][ny]):
                    visit[nx][ny] = min(visit[x][y] + 1, visit[nx][ny])
                    visit_i[nx][ny].append(i)
                    queue.append((nx, ny))

    return visit[x2][y2]


n, m, k = map(int, input().split())
gym = []
visit = []
visit_i = {}
for i in range(n):
    gym.append(input())
    visit.append([0]*m)

    visit_i[i] = {}
    for j in range(m):
        visit_i[i][j] = []


x1, y1, x2, y2 = map(int, input().split())
x1 = n-x1
x2 = n-x2
y1 = y1-1
y2 = y2-1

res = bfs(x1, y1, x2, y2)

print(res-1)
