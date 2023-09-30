'''
https://www.acmicpc.net/problem/1259
주어진 수가 팰린드롬이면 yes, 아니면 no 출력
'''


def palindrome(num):
    len_num = len(num)
    for i in range(len_num//2):
        if num[len_num-i-1] != num[i]:
            return "no"
    return "yes"


def solution():
    while True:
        num = input()
        if num == "0":
            break
        print(palindrome(num))


solution()
