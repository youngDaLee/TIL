'''
https://www.acmicpc.net/problem/10816

상근이가 가진 숫자 카드 n, m개의 숫자카드 중 상근이가 가지고 있는 숫자카드 구하기
1. di에 숫자카드:개수 로 입력 받기
2. m개 입력받을 때, di 검사하기

실패 1) 시간초과
-> 순서만 좀 바꿨는데 통과함... 띠용
'''
import sys


n = int(sys.stdin.readline())
n_li = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_li = list(map(int, sys.stdin.readline().split()))

di = {}
for k in n_li:
    try:
        di[k] += 1
    except:
        di[k] = 1

print(' '.join(str(di[k]) if k in di else '0' for k in m_li))
