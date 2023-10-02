'''
https://www.acmicpc.net/problem/1676

N! 에서 뒤에서부터 0이아닌 숫자가 나올 때 까지 0의 개수
* 곱해서 10의 배수가 되는 값을 찾기
1. 5의 배수 개수
2. 5^2 배수 개수 더하기
3. 5^3 배수 개수 더하기
'''

n = int(input())
res = n//5
if n >= 5**2:
    res += n//(5**2)
if n >= 5**3:
    res += n//(5**3)
print(res)
