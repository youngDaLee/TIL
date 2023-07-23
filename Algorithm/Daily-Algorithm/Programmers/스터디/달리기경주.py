'''
https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3
현재 선수 등수가 담긴 배열 players
해설진이 이름을 부르면 추월 -> 해설진이 부른 이름 리스트 calling
최종 등수를 리턴
'''

"""
1) 무식하게 풀어본 방법
=> 역시 시간초과 이슈..
"""
def solution1(players, callings):
    for call in callings:
        idx = players.index(call)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players


"""
2) hash를 이용해 등수를 변경
=> 통과!
"""
def solution(players, callings):
    rank_hash = {}  # 1: "mumu", 2:"soe", ...
    name_hash = {}  # "mumu": 1, "soe":2, ...

    for i in range(len(players)):
        rank_hash[i+1] = players[i]
        name_hash[players[i]] = i+1

    for call in callings:
        rank = name_hash[call]
        faster_name = rank_hash[rank-1]

        # rank change
        name_hash[call], name_hash[faster_name] = rank-1, rank
        rank_hash[rank-1], rank_hash[rank]  = call, faster_name

    return list(rank_hash.values())

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))
