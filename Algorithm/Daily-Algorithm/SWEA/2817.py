# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1
# 2817. 부분수열의 합

def dfs(idx, sum, k, arr):
    global cnt
    if idx >= len(arr):
        if sum == k:
            cnt += 1
        return

    dfs(idx+1, sum + arr[idx],k,arr)
    dfs(idx+1, sum,k,arr)

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    dfs(0,0,k,arr)

    print("#{} {}".format(i+1, cnt))
