'''
https://www.acmicpc.net/problem/1929

m이상 n이하 소수 구하기

에라토스테네스의 체
1. 배열 생성하여 초기화
2. 2부터 시작해서 특정 수 배수에 해당하는 수 지움(자기 자신은 지우지 않음)
'''

m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:
        continue

    # 2부터 i의 제곱근까지 검사
    flag = True
    for j in range(2, int(i ** 0.5)+1):
        if i != j and i % j == 0:
            flag = False
            break
    if flag:
        print(i)


def fail(m, n):
    '''시간초과 -> 미리 만드는게 아니라, m ~ n까지 하나씩 검사하는 로직으로 변경'''
    li = [1] * (n+1)
    for x in range(3, n+1, 2):
        if li[x] == 0:
            continue

        i = m
        while i <= n:
            if i % x == 0 and i != x:
                li[i] = 0

            if i % x == 0:
                i += x
            else:
                i += 1

    for i in range(m, n+1):
        if li[i] == 1 and i % 2 != 0:
            print(i)
