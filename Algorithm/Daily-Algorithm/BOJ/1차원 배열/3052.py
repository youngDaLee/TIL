numset = set()

for i in range(10):
    num = int(input())
    numset.add(num%42)

print(len(numset))