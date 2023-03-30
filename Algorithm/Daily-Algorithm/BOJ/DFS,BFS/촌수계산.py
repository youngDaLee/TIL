def dfs(now, target, depth):
    global res
    if visit[now] == 1:
        return
    visit[now] = 1
    li = graph[now]
    for l in li:
        if l == target:
            res = depth
            return
        dfs(l, target, depth+1)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = {}
visit = [0] * (n+1)
for i in range(n):
    graph[i+1] = []

for i in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)



res = -1
dfs(a, b, 1)
print(res)