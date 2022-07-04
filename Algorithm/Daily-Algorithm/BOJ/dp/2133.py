
def block(n):
    dp = [0]*31
    dp[0] = 1
    dp[2] = 3

    if n%2 != 0:
        return 0
    if n == 2:
        return dp[2]

    for i in range(4, n+1, 2):
        dp[i] += 3*dp[i-2]
        for j in range(4, i+1, 2):
            dp[i] += 2*dp[i-j]
    return dp[n]


n = int(input())
print(block(n))