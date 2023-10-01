'''
https://www.acmicpc.net/problem/1436

연속된 666이 순차적으로 주어짐, 666 작은순....
1. 3자리수 -> 4자리수 ... 개수 빼나가기
2. 나머지에 따라 해당 수 검사
'''
END_NUM = '666'


'''
메모리 초과 난 코드
'''


def solution_oom(n):
    # 몇 자리수 인지 검사
    digit = 3
    if n == 1:
        # 3지리수(666)
        return '666'

    cnt = 1
    while cnt < n:
        digit_list = list(
            map(lambda x: str(x), range(10**digit, 10**(digit+1))))
        # 해당 자리수에 '666'이 포함된 수 찾기
        for num in digit_list:
            if END_NUM in num:
                cnt += 1

            if cnt == n:
                return num

        digit += 1


def solution(n):
    if n == 1:
        # 3지리수(666)
        return '666'

    n -= 1
    end_num_list = ['666']
    while n > 0:
        new_end_num_list = set()

        # make end_num_list(str)
        end_num_list_len = len(end_num_list)
        for num in end_num_list:
            for i in range(0, 10):
                new_end_num_list.add(num + str(i))
                new_end_num_list.add(str(i) + num)
        end_num_list = new_end_num_list

        new_end_num_list = sorted(new_end_num_list)
        if end_num_list_len + n - 1 < len(new_end_num_list):
            return new_end_num_list[end_num_list_len + n - 1]
        n -= len(new_end_num_list) - end_num_list_len


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
