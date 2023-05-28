
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n,m = map(int, input().split())
graph = []
visit = []
for i in range(n):
    li = input()
    graph.append(li)

    visit_li = [0] * m
    visit.append(visit_li)


res = 101 * 101

def dfs(x, y, depth, visit):
    global res

    visit[x][y] = 1
    print(visit)
    if x == n-1 and y == m-1 :
        print(depth)
        res = min(res, depth)
    
    for i in range(4):
        new_x = dx[i] + x
        new_y = dy[i] + y

        if new_x < n and new_y < m:
            if graph[new_x][new_y] == '1' and visit[new_x][new_y] == 0:
                dfs(new_x, new_y, depth+1, visit)
                visit[x][y]=0


dfs(0,0,1, visit)
print(res)