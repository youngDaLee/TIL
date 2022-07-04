def solution(genres, plays):
    answer = []
    music = list(zip(genres, plays))
    dic = {}
    play_num = {}
    for i in range(len(music)):
        dic[i] = music[i]
        if genres[i] in play_num.keys():
            play_num[genres[i]] += plays[i]
        else:
            play_num[genres[i]] = plays[i]

    import operator

    play_num = list(sorted(play_num.items(), reverse=True,
                           key=operator.itemgetter(1)))
    dic = sorted(dic.items(), reverse=True, key=operator.itemgetter(1))
    print(play_num)

    for genre in play_num:
        cnt = 0
        for dic_key, dic_val in dic:
            if dic_val[0] == genre[0]:
                cnt += 1
                answer.append(dic_key)
                if cnt == 2:
                    break

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
