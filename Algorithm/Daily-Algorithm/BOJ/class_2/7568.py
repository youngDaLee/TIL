'''
https://www.acmicpc.net/problem/7568

나열된 덩치의 등수를 출력
1. 키순 정렬
2. 몸무게도 낮은 경우에 등수가 바뀜
'''
n = int(input())
li = []
for i in range(n):
    w, h = map(int, input().split())
    li.append((h, w))

for i in range(n):
    cnt = 1
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            cnt += 1
    print(cnt, end=' ')


def fail():
    '''
    예외케이스를 못찾겠음....
    '''
    li = []
    for i in range(n):
        w, h = map(int, input().split())
        li.append((h, w, i))
    li.sort(reverse=True)
    print(li)

    rank = 1
    res = ['1'] * n
    for i in range(1, len(li)):
        if li[i][0] < li[i-1][0] and li[i][1] < li[i-1][1]:
            rank = i+1
        res[li[i][2]] = str(rank)

    print(' '.join(res))
