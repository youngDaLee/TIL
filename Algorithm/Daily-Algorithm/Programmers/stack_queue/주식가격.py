def solution(prices):
    answer = []

    for i in range(0, len(prices)):
        cnt = 0
        for j in range(i, len(prices)):
            if prices[i] > prices[j] or j+1 == len(prices):
                answer.append(cnt)
                break
            cnt = cnt+1

    return answer


prices = [1, 2, 3, 2, 3]
ans = solution(prices)
print(ans)
