from collections import deque


def dfs(conn_dict, visited, v, res=""):
    visited[v] = 1
    res += str(v) + " "
    for next_v in conn_dict[v]:
        if visited[next_v] == 0:
            res = dfs(conn_dict, visited, next_v, res)
    return res


def bfs(conn_dict, visited, v):
    res = ""
    queue = deque([v])
    visited[v] = 1
    while queue:
        now_v = queue.popleft()
        res += str(now_v) + " "
        for next_v in conn_dict[now_v]:
            if visited[next_v] == 0:
                queue.append(next_v)
                visited[next_v] = 1
    return res


n, m, v = map(int, input("N M V입력 : ").split())
conn_dict = {}
for i in range(1, n+1):
    conn_dict[i] = []

for i in range(m):
    a, b = map(int, input().split())
    conn_dict[a].append(b)
    conn_dict[b].append(a)

visited = [0] * (n+1)
res = dfs(conn_dict, visited, v)
print(res.strip())
visited = [0] * (n+1)
res = bfs(conn_dict, visited, v)
print(res.strip())
