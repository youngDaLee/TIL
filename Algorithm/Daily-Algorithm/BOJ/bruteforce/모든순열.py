from itertools import permutations

n = int(input())
li = list(map(lambda x : x+1, range(n)))
per = permutations(li,n)

for pe in per:
    for p in pe:
        print(p, end=' ')
    print()