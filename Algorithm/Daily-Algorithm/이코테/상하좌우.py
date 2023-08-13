'''
공간 크기 N이 주어지고, N을 벗어나는 움직임은 무시됨
(1, 1) 에서 주어진 L, R, U, D로 움직였을 때 최종 위치
'''
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
lrud = {
    'L': 0,
    'R': 1,
    'U': 2,
    'D': 3,
}

def solution(n, moves):
    point = [1, 1]
    for move in moves:
        i = lrud[move]
        point[0] += dy[i]
        point[1] += dx[i]
        # 위치 보정
        if point[0] > n:
            point[0] = n
        if point[1] > n:
            point[1] = n
        if point[0] < 1:
            point[0] = 1
        if point[1] < 1:
            point[1] = 1

    return point


n = int(input())
moves = list(input().split())
print(solution(n, moves))
