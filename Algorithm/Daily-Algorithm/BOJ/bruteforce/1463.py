'''
https://www.acmicpc.net/problem/1463
'''


def solution(n):
    dp = [0] * (n+1)
    dp[1] = 0
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + 1
        if (i%2 == 0):
            dp[i] = min(dp[i], dp[i//2]+1)
        if (i%3 == 0):
            dp[i] = min(dp[i], dp[i//3]+1)

    return dp[n]

n = int(input())
print(solution(n))

