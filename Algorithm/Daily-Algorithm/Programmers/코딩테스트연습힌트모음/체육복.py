def solution(n, lost, reserve):
    cloth = {}
    for i in range(1,n+1):
        cloth[i] = 1
        if i in lost:
            cloth[i] -= 1
        if i in reserve:
            cloth[i] += 1

    cnt = 0
    for i, cloth_cnt in cloth.items():
        if cloth_cnt == 0:
            if i-1>0 and cloth[i-1] == 2:
                cloth[i-1] = 1
                cnt += 1
            elif i+1<=n and cloth[i+1] == 2:
                cloth[i+1] = 1
                cnt += 1
        else:
            cnt += 1
    return cnt


ans = solution(4, [2,3], [3,4])
print(ans)