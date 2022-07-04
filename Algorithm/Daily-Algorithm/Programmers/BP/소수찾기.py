from itertools import permutations
import math


def solution(numbers):
    answer = 0

    # 모든 숫자 경우의 수 리스트 생성
    num_list = []
    for i in range(1, len(numbers)+1):
        permutation = permutations(numbers, i)
        for p in permutation:
            s = ''.join(p)
            num_list.append(int(s))
    # 중복제거
    num_list = list(set(num_list))

    for n in num_list:
        if n < 2:
            continue
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                answer -= 1
                break
        answer += 1

    return answer
numbers = "011"
print(solution(numbers))
