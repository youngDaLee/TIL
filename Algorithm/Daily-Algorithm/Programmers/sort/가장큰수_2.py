def solution(numbers):
    numbers = list(map(str, numbers))  # str변환
    # 세 번 붙이고, 역순으로 정렬 -> 세번 붙인 이유는 원소가 0 이상 100이하기 때문
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))  # big sort에서는 형변환 안 하는걸 추천

# 출처: https://dailyheumsi.tistory.com/102 [하나씩 점을 찍어 나가며]


numbers = [3, 30, 34, 5, 9]
str1 = solution(numbers)

print(str1)
