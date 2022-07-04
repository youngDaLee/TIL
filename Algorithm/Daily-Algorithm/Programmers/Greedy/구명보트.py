def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    l=0
    r=len(people)-1
    while l<r:
        if people[l]+people[r]<=limit:
            l += 1
            r -= 1
        else:
            l += 1
        answer += 1
    
    # l과 r이 같을 땐 집계 안됨.
    # 그렇다고 while 조건 l<=r로 하면 index out of range
    if l==r :
        answer += 1
    
    return answer

people = [70, 80, 50]
limit = 100

print(solution(people,limit))