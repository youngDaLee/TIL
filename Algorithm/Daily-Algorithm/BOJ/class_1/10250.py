'''
https://www.acmicpc.net/problem/10250
1. ACM 호텔은 각 층에 W 개의 방이 있는 H 층 건물이다.
2. 엘리베이터는 가장 왼쪽에 있다.
3. 방 번호는 YXX 나 YYXX 형태 (Y는 층 수, X는 엘리베이터의 번호)
4. 손님은 엘레베이터를 타고 이동하는 거리는 신경쓰지 않고, 거리가 같을 때는 아래층의 방을 더 선호한다.
5. N번째 손님에게 배정될 방 번호를 계산하는 프로그램을 작성하시오.
'''


def hotel_room(h, w, n):
    floor = n % h
    if floor == 0:
        floor = h
        room = n // h
    else:
        room = n // h + 1

    return floor * 100 + room


def solution():
    t = int(input())
    for _ in range(t):
        h, w, n = map(int, input().split())
        print(hotel_room(h, w, n))


solution()
