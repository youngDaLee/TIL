# https://softeer.ai/practice/info.do?idx=1&eid=581
from itertools import permutations

n, m, k = map(int, input().split())
rail_input = list(map(int, input().split()))

rails = list(permutations(rail_input))

def findTotal(rail):
    total = 0
    idx = 0

    for _ in range(k):
        box = 0
        while box < m:
            if box + rail[idx] > m:
                break
            else:
                box += rail[idx]
                idx = (idx+1)%n
        total += box
    return total

total_list = []
for rail in rails:
    total_list.append(findTotal(rail))

print(min(total_list))