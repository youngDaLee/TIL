# LeetCode
[Remove Palindromic Subsequences](https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3665/)

### ���� �����ϱ�
- a,b�θ� �̷���� string s�� �־���.
- �� ���� �� ���� palidromic�� subsequence�� ���� �� ����.
- string�� �� �� ���� �ּ����� ���� �����.

### ���� ���� ���
- stack���� palindrom �Ǻ��ؼ� palindrom ��������� ������.
- palindrom �Ǻ���
  - �ִ��� ū ���� �Ǿ�� �ϴϱ�(baabb���� �ε��� ���� 0124�� palindrom�̶� ģ����. �� ���� �ʾƵ� ��.)
  - �� �� index l,�� �� index r�� �ϳ��� �ø��� �ٿ����� palindrom �Ǻ���.
### ���� ��� ����
stack, palindrom

### ���� ����� ������ �ڵ�
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
