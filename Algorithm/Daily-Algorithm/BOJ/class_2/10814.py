'''
https://www.acmicpc.net/problem/10814

'''

n = int(input())
di = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    try:
        di[age].append(name)
    except:
        di[age] = [name]

k_li = sorted(di)

for k in k_li:
    for v in di[k]:
        print(k, v, sep=' ')
