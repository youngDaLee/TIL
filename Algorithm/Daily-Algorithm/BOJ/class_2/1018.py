'''
https://www.acmicpc.net/problem/1018
1. 지민이가 다시 칠해야 하는 정사각형 최소 개수
'''

n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

# 정상적으로 칠해진 chess판과 비교
white_cnt = 0
black_cnt = 0
for i in range(n):
    if (i % 2) == 0:
        white_line = 'WB' * (m//2)
        black_line = 'BW' * (m//2)
        if m % 2 == 1:
            white_line += 'W'
            black_line += 'B'
    else:
        white_line = 'BW' * (m//2)
        black_line = 'WB' * (m//2)
        if m % 2 == 1:
            white_line += 'B'
            black_line += 'W'

    print(white_line, black_line)
    chess_line = chess[i]
    for j in range(m):
        if white_line[j] != chess_line[j]:
            white_cnt += 1
        if black_line[j] != chess_line[j]:
            black_cnt += 1

print(white_cnt, black_cnt)
print(min(white_cnt, black_cnt))
