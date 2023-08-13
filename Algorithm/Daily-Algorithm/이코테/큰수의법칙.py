'''
배열 크기 n, 숫자 더해지는 횟수 m, 특정 인덱스가 연속해서 더해질 수 있는 횟수 k
가장 큰 수 구하기
'''

n, m, k = map(int, input().split())
li = list(map(int, input().split()))

# 가장 큰 수 구하기
first_max = max(li)
# 두번째로 큰 수 구하기
li.remove(first_max)
sec_max = max(li)

# 연속수+그다음수 패턴 회차
r = m // (k+1)
if (m%(k+1) == 0):
    # 연속수+그다음수 패턴이 0으로 나누어 떨어진다면
    result = first_max * k * r + sec_max * r
else:
    # 나누어 떨어지지 않는다면
    result = first_max * k * r + sec_max * r + first_max * (m%(k+1))
