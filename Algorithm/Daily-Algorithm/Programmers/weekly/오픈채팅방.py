def solution(record):
    answer = []
    userid_log = dict()
    user_log = list()
    for r in record:
        try:
            c, userid, nickname = map(str, r.split(' '))
        except:
            c, userid = map(str, r.split(' '))
        if c == 'Enter':
            userid_log[userid] = nickname
            user_log.append([userid, '님이 들어왔습니다.'])
        elif c == 'Leave':
            user_log.append([userid, '님이 나갔습니다.'])
        else:
            userid_log[userid] = nickname
    
    for u in user_log:
        msg = userid_log[u[0]] + u[1]
        answer.append(msg)

    return answer

recode = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(recode))