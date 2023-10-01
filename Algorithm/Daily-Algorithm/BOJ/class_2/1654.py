'''
https://www.acmicpc.net/problem/1654

길이가 제각각인 K개의 랜선을 길이가 같은 N개 이상의 랜선을 만들때, 만들 수 있는 최대 랜선 길이
=> 알고리즘이 바로 떠오르지 않아 블로그를 찾아봄
참고
* https://growth-coder.tistory.com/127
* https://marades.tistory.com/7
* https://velog.io/@lake/%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89-%ED%8C%8C%EB%9D%BC%EB%A9%94%ED%8A%B8%EB%A6%AD-%EC%84%9C%EC%B9%98Parametric-Search

Parametric Search : BST와 다르게 주어진 값이 아니라 주어진 범위에서 원하는 조건에 일치하는 값을 찾아내는 알고리즘
* 범위 내에서 조건을 만족하는 가장 큰 값을 찾아라
* 중간값이 조건에 부합하는지 검사하고, 조건에 맞지 않다면 조건에 맞지 않는 부분(최대or최소)을 배제하고 나머지 부분 탐색
* 그렇게 중간값을 나눠서 탐색해나감

문제 수도코드
1. 최소 1, 최대 max(랜선들)의 중간값으로 랜선을 나눴을 때 n개가 나오는지 검사
2. n개 이상 나오면 -> 오른쪽 부분 검사
2. n개 이하 나오면 -> 왼쪽 부분 검사

처음에 틀린 이유
* min(랜선들)을 high값으로 잡음 => 혼자 엄청 작은 랜선이 있을 경우, 해당 랜선을 버리고, 나머지 길쭉한 랜선으로 n개 랜선 만들 수 있음
'''


def parametric_search(low, high, lan_list, n):
    max_lan = 0
    while (low <= high):
        mid = (high + low) // 2

        now_n = 0
        for lan in lan_list:
            now_n += (lan // mid)

        if now_n >= n:
            max_lan = mid
            low = mid + 1
        else:
            high = mid - 1
    return max_lan


if __name__ == '__main__':
    k, n = map(int, input().split())
    lan_list = []
    for _ in range(k):
        lan_list.append(int(input()))

    print(parametric_search(1, max(lan_list), lan_list, n))
