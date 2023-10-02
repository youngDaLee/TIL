'''
https://www.acmicpc.net/problem/1966

큐에 문서와 중요도가 주어졌을 때 어떤 문서가 몇 번째로 인쇄되는지 알아내는 것
첫째줄에 문서 개수 n, 몇번째로 출력되는지 궁굼한 문서가 현재 queue 몇번째인지 정수 m, 둘째줄에 문서
중요도는 1~9 자연수로, 중요도 중복될 수 있음
'''
from collections import deque


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    doc = list(map(int, input().split()))
    # doc 인덱스 순서대로 저장된 큐
    queue = deque(map(lambda x: x, range(n)))
    priority = sorted(doc)
    cnt = 0
    pcount = 0
    while queue:
        top = queue.popleft()
        pcount += 1
        if doc[top] == priority[-1]:
            cnt += 1
            priority.pop()
            if top == m:
                break
        else:
            queue.append(top)

    print(cnt)
