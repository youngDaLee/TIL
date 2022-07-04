def solution(progresses, speeds):
    answer = []
    stack = []
    li = list(map(lambda x,y: (100-x)//y if (100-x)%y==0 else ((100-x)//y)+1, progresses,speeds))
    
    answer.append(0)
    stack.append(li[0])
    for i in li:
        if stack[-1] >= i:
            answer[-1] = answer[-1]+1
        else :
            stack.append(i)
            answer.append(1)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

ans = solution(progresses, speeds)
print(ans)