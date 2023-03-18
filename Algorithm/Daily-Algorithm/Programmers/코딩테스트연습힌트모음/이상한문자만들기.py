def solution(s):
    answer = ''
    slist = s.split(' ')

    for j in range(len(slist)):
        word = slist[j]
        len_word = len(word)
        for i in range(len_word):
            if i%2 != 0:
                answer += word[i].lower()
            else:
                answer += word[i].upper()
        if j+1 < len(slist):
            answer += ' '

    return answer


print(solution('    try hello world'))