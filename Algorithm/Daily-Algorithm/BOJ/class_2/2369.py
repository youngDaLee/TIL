'''
https://www.acmicpc.net/problem/2869
달팽이가 높이 V 나무 올라감
낮에 A밑터 올라가고 반에 B미터 미끄러짐.
나무막대를 모두 올라가는데 며칠 걸리는지 구하기
'''

a, b, v = map(int, input().split())

one_day = a - b
res = (v-a)//one_day + 1
if (v-a) > 0 and (v-a) < one_day:
    res += 1
print(res)
