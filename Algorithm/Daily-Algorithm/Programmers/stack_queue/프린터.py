def solution(priorities, location):
    answer = 0
    q = [(v,i) for i,v in enumerate(priorities)] #value, index 리스트 생성
    
    while q:
        i = q.pop(0)
        if max(q)[0] > i[0]:
            q.append(i)
        else :
            answer = answer+1
            if i[1] == location:
                break
    return answer

priorities=[1, 1, 9, 1, 1, 1]
location = 0

ans = solution(priorities, location)
print(ans)