import sys


'''
### 런타임 에러
python은 재귀가 1000번 이상 일어나면 recursion 에러가 발생
재귀 한도를 늘려줘야 함
djdh 근데 자꾸 메모리초과남

그냥... 다빼고 파이썬 기본 모듈 쓰니까 해결됨
허무
'''


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    res = []
    for i in range(n):
        num = int(sys.stdin.readline())
        res.append(num)

    res = sorted(res)

    for i in res:
        print(i)
