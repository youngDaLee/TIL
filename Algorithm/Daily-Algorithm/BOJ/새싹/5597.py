'''
https://www.acmicpc.net/problem/5597
'''

arr = [0] * 30
for _ in range(28):
    idx = int(input())
    arr[idx - 1] = 1

for i in range(30):
    if arr[i] == 0:
        print(i + 1)
