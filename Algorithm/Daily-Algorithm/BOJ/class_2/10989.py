'''
https://www.acmicpc.net/problem/10989

n개의 수를 오름차순 정렬
1. 정렬되어 있는 상태에서 삽입이 될 때 최적의 알고리즘이 무엇인지?
    -> 삽입을 하면서 정렬을 하는 tree sort를 사용하자. 
2. 그게 아니면 최악의 상황에서 nlogn 인 알고리즘을 찾아 사용하기
'''
import sys


n = int(input())
di = {}
for i in range(n):
    k = int(sys.stdin.readline())
    try:
        di[k] = di[k] + 1
    except:
        di[k] = 1

li = sorted(di)

for k in li:
    v = di[k]
    for i in range(v):
        print(k)
