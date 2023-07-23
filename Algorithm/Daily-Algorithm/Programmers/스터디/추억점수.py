'''
https://school.programmers.co.kr/learn/courses/30/lessons/176963
사람마다 그리움 점수가 있음
그리움 점수 반환
'''
def solution(name, yearning, photo):
    answer = []

    missing_hash = {}
    for i in range(len(name)):
        missing_hash[name[i]] = yearning[i]

    for p in photo:
        res = 0
        for people in p:
            try:
                res += missing_hash[people]
            except:
                pass
        answer.append(res)

    return answer
