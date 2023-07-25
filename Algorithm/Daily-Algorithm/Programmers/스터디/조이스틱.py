'''
https://school.programmers.co.kr/learn/courses/30/lessons/42860
'''
def get_min_find(num_list):
    a_list = [len(num_list)+1]
    for i in range(len(num_list)):
        if num_list[i] == 0:
            idx = i
            a_num = 0
            while(num_list[i] == 0):
                a_num += 1
                i += 1

            if(idx == 0): idx=1
            a_list.append(len(num_list)-1 - a_num + (idx-1))

    return min(a_list) +sum(num_list) 

def solution(name):
    answer = 0

    num_list = []
    for alpha in name:
        change_num = min(ord(alpha)-ord('A'), ord('Z')-ord(alpha)+1)
        num_list.append(change_num)

    if 0 in num_list:
        answer = get_min_find(num_list)
    else:
        answer = sum(num_list) + len(num_list) - 1
    return answer


print(solution("JAN"))


'''
왜 이렇게까지 했었을까
'''
def solution1(name):
    answer = 0

    answer_num = 0
    stack = 0
    is_A = 0
    g = 0
    li = []
    for i in range(len(name)):
        num = min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
        answer_num += num
        
        if i < len(name)-1 and name[i+1] == 'A':
            # 뒤로 가는경우의 수 추가
            b_stack = 0 # A를 만난 후 A를 만나기 전 까지 이동거리
            go = g*2 + 1 # 뒤에서부터 이동 거리
            b_is_A = 0 # A를 만났으면 1
            for j in range(len(name)-1,i):
                if name[j] == 'A':
                    b_is_A = 1
                    b_stack += 1
                elif b_is_A == 1:
                    go += b_stack+1
                    b_stack = 0
                else:
                    go += 1
            
            li.append(go)
        
        g += 1
    

    g -= 1 # 맨 마지막에 한 번 더 가서..
    li.append(g)

    answer = answer_num + min(li)


    return answer
