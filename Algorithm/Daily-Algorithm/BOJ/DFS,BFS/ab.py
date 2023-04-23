def dfs(now, target, depth):
    global result

    num = int(now)
    if num == target:
        if result == -1:
            result = depth
        else:
            result = min(result, depth)
        return
    if num > target:
        result = max(result, -1)
        return

    new_depth = depth+1
    dfs(str(num*2), target, new_depth)
    dfs(str(num)+'1', target, new_depth)


a, b = map(int, input().split())
result = -1
dfs(a, b, 1)

print(result)
