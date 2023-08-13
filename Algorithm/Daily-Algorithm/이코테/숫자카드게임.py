'''
N(row) X M(col) 형태로 놓인 카드 중 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
1. 뽑고자 하는 행 선택
2. 선택된 행 중 가장 작은 카드 선택
'''

n, m = map(int, input().split())
min_row = []
for i in range(n):
    li = list(map, input().split())
    min_row.append(min(li))

print(max(min_row))
