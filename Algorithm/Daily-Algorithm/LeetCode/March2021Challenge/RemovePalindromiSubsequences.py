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



