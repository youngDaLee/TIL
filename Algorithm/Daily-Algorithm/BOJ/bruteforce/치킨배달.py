from itertools import combinations

n, m = map(int, input().split())
home = []
chiken = []
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 2:
            chiken.append([i+1,j+1])
        elif city[j] == 1:
            home.append([i+1,j+1])

chiken_list = list(combinations(chiken, m))
min_list = []
for chic in chiken_list:
    total = 0
    for h in home:
        road = 100
        for c in chic:
            road = min(road, abs(c[0]-h[0])+abs(c[1]-h[1]))
        total += road
    min_list.append(total)

result = min(min_list)
print(result)