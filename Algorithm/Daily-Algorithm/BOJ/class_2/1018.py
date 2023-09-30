'''
https://www.acmicpc.net/problem/1018
1. 지민이가 다시 칠해야 하는 정사각형 최소 개수
'''

n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]

# 다시 칠야 하는 체스판을 1로 기록
white_cnt = [[0]*m for _ in range(n)]
black_cnt = [[0]*m for _ in range(n)]
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

    chess_line = chess[i]
    for j in range(m):
        if white_line[j] != chess_line[j]:
            white_cnt[i][j] = 1
        if black_line[j] != chess_line[j]:
            black_cnt[i][j] = 1

black_res = 50 * 50
white_res = 50 * 50
for i in range(0, n-7):
    for j in range(0, m-7):
        now_black_res = sum(black_cnt[i][j:j+8])
        now_black_res += sum(black_cnt[i+1][j:j+8])
        now_black_res += sum(black_cnt[i+2][j:j+8])
        now_black_res += sum(black_cnt[i+3][j:j+8])
        now_black_res += sum(black_cnt[i+4][j:j+8])
        now_black_res += sum(black_cnt[i+5][j:j+8])
        now_black_res += sum(black_cnt[i+6][j:j+8])
        now_black_res += sum(black_cnt[i+7][j:j+8])

        now_white_res = sum(white_cnt[i][j:j+8])
        now_white_res += sum(white_cnt[i+1][j:j+8])
        now_white_res += sum(white_cnt[i+2][j:j+8])
        now_white_res += sum(white_cnt[i+3][j:j+8])
        now_white_res += sum(white_cnt[i+4][j:j+8])
        now_white_res += sum(white_cnt[i+5][j:j+8])
        now_white_res += sum(white_cnt[i+6][j:j+8])
        now_white_res += sum(white_cnt[i+7][j:j+8])

        black_res = min(black_res, now_black_res)
        white_res = min(white_res, now_white_res)

print(min(black_res, white_res))
