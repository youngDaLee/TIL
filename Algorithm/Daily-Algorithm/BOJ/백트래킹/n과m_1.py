from itertools import permutations

n, m = map(int, input().split())
n_li = list(map(lambda x: x+1, range(n))) 

per = list(permutations(n_li, m))
for p in per:
    for num in p:
        print(num, end=" ")
    print()
