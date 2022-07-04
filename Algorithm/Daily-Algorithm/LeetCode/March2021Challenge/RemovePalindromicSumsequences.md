# LeetCode
[Remove Palindromic Subsequences](https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/)

### 문제 이해하기
- a,b로만 이루어진 string s가 주어짐.
- 한 번에 한 개의 palidromic한 subsequence를 지울 수 있음.
- string이 빌 때 까지 최소한의 수를 적어라.

### 문제 접근 방법
- stack으로 palindrom 판별해서 palindrom 만들어지면 지워줌.
- palindrom 판별법
  - 최대한 큰 수가 되어야 하니까(baabb에서 인덱스 기준 0124를 palindrom이라 친댔음. 꼭 붙지 않아도 됨.)
  - 맨 앞 index l,맨 뒤 index r로 하나씩 늘리고 줄여가며 palindrom 판별함.
### 구현 배경 지식
stack, palindrom

### 접근 방법을 적용한 코드
```python
from collections import deque
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        answer = 0
        stack = s
        li = deque(s)
        while stack:
            stack = []
            l = 0
            r = len(li)-1
            
            while l<=r:
                if l == r:
                    li.popleft()
                    break
                if li[l] == li[r]:
                    li.popleft()
                    li.pop()
                else:
                    stack.append(li.pop())
                r = len(li)-1
            answer += 1
            li = deque(stack)
        answer = min(2, answer)
        return answer 
```
