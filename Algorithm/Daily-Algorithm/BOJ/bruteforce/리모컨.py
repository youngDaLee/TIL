n = int(input())
m = int(input())
if m == 0:
    broken_button = list()
else:
    broken_button = list(map(int, input().split()))
button = set()

for i in range(10):
    if i in broken_button:
        continue
    button.add(i)

number = str(n)
num1 = ''
num2 = ''
for i in range(len(number)):
    if int(number[i]) in button:
        num1 += number[i]
        num2 += number[i]
        continue

    left = int(number[i])-1
    rigth = int(number[i])+1
    for _ in range(10):
        if (left in button) and (rigth in button):
            if i == 0:
                num1 += str(left)
                num2 += str(rigth)
            else:
                num1 += str(rigth)
                num2 += str(left)
            break
        elif left in button:
            num1 += str(left)
            num2 += str(left)
            break
        elif rigth in button:
            num1 += str(rigth)
            num2 += str(rigth)
            break
        else:
            left -= 1
            rigth += 1
if num1 == '':
    num1 = '10000000'
if num2 == '':
    num2 = '10000000'
num1 = abs(n-int(num1)) + len(number)
num2 = abs(n-int(num2)) + len(number)
basic = abs(n-100)

result = min(num1, num2, basic)
start = n-result
end = n+result
if start<0:
    start = 0
num_lists = list(map(lambda x : list(map(int, str(x))), range(start, end)))
for num_list in num_lists:
    intersection = list(set(num_list) & set(broken_button))
    if len(intersection) > 0:
        continue
    num = int("".join(map(str,num_list)))
    result = min(result, abs(n-num)+len(str(num)))


print(result)