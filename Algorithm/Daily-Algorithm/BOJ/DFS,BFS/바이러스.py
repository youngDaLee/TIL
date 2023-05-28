# https://www.acmicpc.net/problem/2606
# 1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 바이러스에 걸리는 컴퓨터 수 출력

n = int(input())
pair = int(input())

# dict 초기화
visit = [0] * (n+1)
comDict = {}
for i in range(1, n+1):
    comDict[i] = []

# 연결 정보 입력
for i in range(pair):
    n, m = map(int, input().split())
    comDict[n].append(m)
    comDict[m].append(n)


def dfs(com, comDict, visit):
    visit[com] = 1

    for new_com in comDict[com]:
        if visit[new_com] == 1:
            continue
        else:
            visit = dfs(new_com, comDict, visit)

    return visit

visit = dfs(1,comDict,visit)
result = sum(visit) - 1 # 1번 컴퓨터 제외
print(result)