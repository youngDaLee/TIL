from collections import deque

def binary_sort(res, num):
    if len(res) < 2:
        lnum = res[0]
        if lnum <= num:
            res.append(num)
            return res
        else:
            res.appendleft(num)
            return res
    l = 0
    r = len(res) - 1
    while l <= r:
        mid = (l+r) // 2
        if res[mid] >= num and mid == 0:
            res.appendleft(num)
            return res
        if res[mid] <= num and mid == len(res)-1:
            res.append(num)
            return res

        if res[mid] >= num and res[mid-1] <= num:
            tmp = res[:mid-1]
            tmp.append(num)
            tmp += res[mid:]
            return tmp
        elif res[mid] <= num and res[mid+1] >= num:
            tmp = res[:mid]
            tmp.append(num)
            tmp += res[mid+1:]
            return tmp
        elif res[mid] >= num:
            r = mid - 1
        else:
            l = mid + 1

n = int(input())

res = deque()
for i in range(n):
    num = int(input())
    if not res:
        res.append(num)
        continue
    res = binary_sort(res, num)

for i in res:
    print(i)