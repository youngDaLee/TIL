import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m, k = map(int, sys.stdin.readline().split())
gym = []
visit = []
for i in range(n):
    gym.append(sys.stdin.readline())
    visit.append([-1]*m)

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

def bfs(x1, y1):
    queue = deque()
    queue.append((x1, y1))
    visit[x1][y1] = 0

    while queue:
        x, y = queue.popleft()
        if (x==x2-1 and y==y2-1):
            return
        for i in range(4):
            for nk in range(1, k+1):
                nx = x + dx[i]*nk
                ny = y + dy[i]*nk

                if (nx<0 or nx>=n or ny<0 or ny>=m): break
                if (gym[nx][ny] == '#'): break

                if (visit[nx][ny] == -1):
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx,ny))
                elif (nx == x2-1 and ny == y2-1) : return
                elif (visit[nx][ny] > visit[x][y] + 1) : break


bfs(x1-1, y1-1)
print(visit[x2-1][y2-1])
 