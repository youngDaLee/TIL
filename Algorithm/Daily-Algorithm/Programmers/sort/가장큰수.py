def solution(numbers):
    answer = ''
    for i in range(len(numbers)-1,0,-1) :
        for j in range (0,i): # 제일 앞에 수가 큰 게 앞에 올 수록 크다.
            last_num1 = int(numbers[j] / (10**(len(str(numbers[j]))-1)))
            last_num2 = int(numbers[j+1] / (10**(len(str(numbers[j+1]))-1)))
            if (last_num1<last_num2):
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    
    for i in range(0, len(numbers)):
        answer = answer + str(numbers[i])
    return answer

numbers = [3, 30, 34, 5, 9]
str1= solution(numbers)

print(str1)
