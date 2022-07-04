max_num = -1
index = -1
for i in range(9):
    n = int(input())
    if n > max_num:
        max_num = n
        index = i+1

print(max_num)
print(index)

