x = int(input())
stick = 64
sticks = []

while stick > 0:
    sticks.append(stick)
    stick = int(stick//2)


total = 0
result = 0
for s in sticks:
    if total + s > x:
        continue
    total += s
    result += 1

print(result)