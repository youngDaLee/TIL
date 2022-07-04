def solution(m, n, puddles):
    answer = 0
    # maps 만들기
    maps= []
    for i in range(n+1):
        maps.append([0]*(m+1))

    maps[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1 : 
                continue
            if [j, i] in puddles:
                continue
            else:
                maps[i][j] = maps[i-1][j] + maps[i][j-1]

    return maps[-1][-1]%1000000007


m = 4
n = 3
puddles = [[2, 2]]

print(solution(m,n,puddles))