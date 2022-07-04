
def answer(s):
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    
    dp = [0]*(len(s)+1)
    dp[0] = 1
    if s[1] == '0' and int(s[:2]) > 26:
        return 0
    elif( s[1] == '0' and int(s[:2]) <= 26) or int(s[:2]) > 26:
        dp[1] = 1
    else:
        dp[1] = 2
    
    for i in range(2, len(s)):
        num = int(s[i-1]+s[i])
        last_num = int(s[i-2]+s[i-1])
        
        if (s[i] == '0' and num > 26)\
            or (s[i] =='0' and s[i-1] == '0'):
            return 0
        if s[i] == '0':
            if dp[i-1] == 0 or s[i-2] == '0' or last_num > 26 :
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2]
        else:
            if num > 26 or s[i-1] == '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
    
    return dp[len(s)-1]%1000000

s = input()
print(answer(s))