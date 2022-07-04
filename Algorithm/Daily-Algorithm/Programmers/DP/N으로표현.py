def solution(N, number):
    answer = -1

    dp = []

    for i in range(1, 9):
        nums = {int(str(N)*i)}
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[i-j-2]:
                    nums.add(x+y)
                    nums.add(x-y)
                    nums.add(x*y)
                    if y!=0:
                        nums.add(x//y)
        if number in nums:
            return i

        dp.append(nums)


    return answer # 실패시 -1 리턴


N = 5
number = 12
print(solution(N, number))
