# LeetCode
[Set Mismatch](https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/)

### 문제 이해하기
- 1부터 n까지의 정수 집합s.
- 어떤 오류로 인해 한 숫자가 사라지고 다른 숫자로 중복됨.
- 두 번 발생한 숫자를 찾고, 제대로 맞게 고쳐라.

### 문제 접근 방법
- 0*n 배열 만들어줌
- nums에서 숫자 하나씩 pop해주면서 배열 index 1로 바꿔줌
- 만약 1이면 이미 하나 있는거니까 그 숫자 저장함
- 반복문 다 돌고 한 번 더 검사.
- 0인 인덱스 찾아서 같이 리턴...

### 접근 방법을 적용한 코드
196ms
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        li = [0]*len(nums)

        n = 0

        while nums: #O(n)
            top = nums.pop() #O(1)
            if li[top-1] == 1:
                n = top
            else:
                li[top-1] = 1
        
        for i in range(0, len(li)):
            if li[i] == 0:
                return [n, i+1]
```

