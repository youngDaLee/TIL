'''
https://www.acmicpc.net/problem/2609
최소공배수, 최대공약수 구하기
'''
import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
