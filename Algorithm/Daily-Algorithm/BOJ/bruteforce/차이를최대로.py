from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

lists = permutations(a)
result = []
for li in lists:
    total = 0
    for i in range(len(li)-1):
        total += abs(li[i]-li[i+1])
    result.append(total)

print(max(result))