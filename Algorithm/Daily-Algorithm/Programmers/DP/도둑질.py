def solution(money):
    # 첫 집 못 터는 경우
    dp1 = [0]*(len(money)+1)
    dp1[1] = 0
    dp1[2] = money[1]

    for i in range(3, len(dp1)):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i-1], dp1[i-3] + money[i-1])

    # 막집 못 터는 경우
    dp2 = [0]*(len(money)+1)
    dp2[1] = money[0]
    dp2[2] = money[1]
    money[len(money)-1] = 0

    for i in range(3, len(dp2)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i-1], dp2[i-3] + money[i-1])
    
    return max(dp1[len(money)], dp2[len(money)])
money = [10, 2, 2, 100, 2]
print(solution(money))