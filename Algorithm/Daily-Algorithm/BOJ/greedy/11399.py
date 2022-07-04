import sys
input = sys.stdin.readline()

n = int(input)
li = list(map(int, sys.stdin.readline().split()))

li.sort()
total = 0
for i in range(len(li)):
    s = sum(li[:i+1])
    total += s

print(total)