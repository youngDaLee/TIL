def solution(s):
    if len(s) not in [4,6]:
        return False

    answer = True
    for c in s:
        try:
            int(c)
        except:
            return False
    return answer