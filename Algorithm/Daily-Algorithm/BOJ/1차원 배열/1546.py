n = int(input())
nums = list(map(int,input().split()))
m = max(nums)

total = 0
for num in nums:
    total += (num/m)*100

avg = total/n
print(avg)