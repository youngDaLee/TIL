dp = []

def solution(n):
    for i in range(n+1):
        if i <= 1:
            dp.append(i)
            fibo = i
        else:
            fibo = dp[i-1] + dp[i-2]
            dp.append(fibo)
    fibo = fibo%1234567

    return fibo
