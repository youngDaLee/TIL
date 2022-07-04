def solution(clothes):
    answer = 0
    clothes_dic = {}
    for cloth in clothes:
        key = cloth[1]
        if key in clothes_dic.keys():
            clothes_dic[key] += 1
        else:
            clothes_dic[key] = 1

    val = list(clothes_dic.values())

    answer = 1

    for i in val:
        answer *= (i+1)

    return answer-1


clothes = [["yellow_hat", "headgear"], [
    "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))
