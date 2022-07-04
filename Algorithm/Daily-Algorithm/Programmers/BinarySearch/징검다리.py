from itertools import combinations

def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    
    # 두 개 삭제한 다리 조합
    combi = combinations(rocks, len(rocks)-n)
    dis_li = []
    dis = distance

    for rock in combi:
        print(rock)
        for i in range(len(rock)):
            
            if i+1 == len(rock):
                dis = min(dis, distance-rock[i])
            else:
                print(rock[i+1]-rock[i])
                dis = min(dis, rock[i+1]-rock[i])
        dis_li.append(dis)
    print(dis_li)
    answer = max(dis_li)
    return answer

rocks = [2, 14, 11, 21, 17]
distance = 25
n =2

print(solution(distance,rocks,n))