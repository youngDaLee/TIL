from collections import deque


def bfs(n, k, visited):
    queue = deque()
    queue.append(n)
    visited[n] = 0

    cnt = 0
    while queue:
        new_n = queue.popleft()
        if new_n == k:
            cnt += 1
            continue

        for x in (new_n-1, new_n+1, new_n*2):
            if -1 < x < len(visited) and (visited[x]==-1 or visited[x] == visited[new_n]+1):
                visited[x] = visited[new_n]+1
                queue.append(x)

    return visited[k], cnt

n, k = map(int, input().split())
visited = [-1] * (max(n, k)*2)
res, cnt = bfs(n, k, visited)
print(res)
print(cnt)
