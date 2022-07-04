n = int(input())

li = list()
for i in range(n):
    num = int(input())
    li.append(num)
    li.sort()

    if len(li)%2 == 0:
        mid = len(li)//2 - 1
    else:
        mid = len(li)//2
    print(li[mid])