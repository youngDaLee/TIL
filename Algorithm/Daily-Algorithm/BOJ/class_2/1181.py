'''
https://www.acmicpc.net/problem/1181
1. 길이가 짧은 것 부터
2. 짧으면 사전순 정렬
'''
n = int(input())

di = {}
for _ in range(n):
    w = input()
    try:
        di[len(w)].append(w)
    except:
        di[len(w)] = [w]

key_li = sorted(di)
for k in key_li:
    dict_li = sorted(set(di[k]))
    for w in dict_li:
        print(w)
