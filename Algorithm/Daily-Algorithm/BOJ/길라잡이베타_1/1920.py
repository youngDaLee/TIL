n = int(input())
a = list(map(int, input().split()))
res = dict.fromkeys(a, 1)

m = int(input())
b = list(map(int, input().split()))
for num in b:
    try:
        print(res[num])
    except:
        print(0)
