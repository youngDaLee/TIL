from collections import deque


def bfs(n, k, visited):
    queue = deque()
    queue.append(n)
    visited[n] = 1

    cnt = 0
    return_bfs = False
    while queue:
        new_n = queue.popleft()

        if visited[new_n-1] == 0:
            visited[new_n-1] = visited[new_n] + 1
            if (new_n-1 == k):
                cnt += 1
                return_bfs = True
            queue.append(new_n-1)
        if visited[new_n+1] == 0:
            visited[new_n+1] = visited[new_n] + 1
            if (new_n+1 == k):
                cnt += 1
                return_bfs = True
            queue.append(new_n+1)
        if new_n*2 < len(visited) and visited[new_n*2] == 0:
            visited[new_n*2] = visited[new_n] + 1
            if (new_n*2 == k):
                cnt += 1
                return_bfs = True
            queue.append(new_n*2)
        
        if return_bfs:
            return visited[new_n] + 1, cnt

    return -1

n, k = map(int, input().split())
visited = [0] * (max(n, k)*2)
res = bfs(n, k, visited)
print(res)
print(visited)
