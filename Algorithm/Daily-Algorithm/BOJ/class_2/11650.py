'''
https://www.acmicpc.net/problem/11650
2차원 평면 n개를 x좌표 증가순 - y좌표 증가순으로 출력
'''
n = int(input())
li = []
for _ in range(n):
    k, v = map(int, input().split())
    li.append([k, v])
li.sort()

for l in li:
    print(l[0], l[1], sep=' ')
