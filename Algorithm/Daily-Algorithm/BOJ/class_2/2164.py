'''
https://www.acmicpc.net/problem/2164

1~n까지의 n장의 카드, 1번 카드가 제일 위, n번카드가 가장 아래. 가장 위 카드를 버리고, 그 다음 위 카드를 아래로 옮김... => 가장 마지막에 남는 카드 구하기

python에서의 deque vs list BigO 차이
* https://wellsw.tistory.com/122
append는 둘 다 O(1)
popleft
* queue : O(1)
* list : O(n)
'''
from collections import deque


def solution(n):
    queue = deque(map(lambda x: x+1, range(n)))
    while len(queue) != 1:
        queue.popleft()
        top = queue.popleft()
        queue.append(top)

    return (queue.pop())


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
