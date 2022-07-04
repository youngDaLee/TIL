def solution(name):
    answer = 0

    answer_num = 0
    g = 0
    li = []
    for i in range(len(name)):
        num = min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        answer_num += num

        if i < len(name)-1 and name[i+1] == 'A':
            # 뒤로 가는경우의 수 추가
            stack = 0 # A를 만난 후 A를 만나기 전 까지 이동거리
            go = g*2 + 1 # 뒤에서부터 이동 거리
            is_A = 0 # A를 만났으면 1
            for j in range(len(name)-1,i):
                if name[j] == 'A':
                    is_A = 1
                    stack += 1
                elif is_A == 1:
                    go += stack+1
                    stack = 0
                else:
                    go += 1
            
            li.append(go)
        
        g += 1
    

    g -= 1 # 맨 마지막에 한 번 더 가서..
    li.append(g)

    answer = answer_num + min(li)


    return answer


name = "JAN"
print(solution(name))