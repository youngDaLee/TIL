def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])

    print(routes)
    cam = -30001 # 최솟값
    
    for i in range(len(routes)):
        if cam < routes[i][0]:
            answer += 1
            cam = routes[i][1]

    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))