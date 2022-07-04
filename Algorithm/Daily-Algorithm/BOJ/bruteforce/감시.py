# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def cctv_1(dot):
    cnt = 0
    





n, m = map(int, input().split())
room = list()
cctv = []
for i in range(n):
    r = list(map(int, input().split()))
    for j in range(m):
        if r[j]<=5 and r[j]>=1:
            cctv.append([i,j])
    room.append(r)


for c in cctv:
    dot = room[c[0]][c[1]]

