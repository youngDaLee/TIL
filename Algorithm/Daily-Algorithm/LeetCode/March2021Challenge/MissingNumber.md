# LeetCode
[Missing Number](https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/)

### 문제 이해하기
- [0, n] 범위의 nums 배열이 주어짐.
- 이 범위의 배열 내에서 생략된 한 숫자를 찾아라.
- 공간복잡도 O(1), 시간복잡도O(n)으로 풀어봐라

### 문제 접근 방법
- 방문하면 li를 1로 바꾸고, 다시 그 li 탐색하면서 0인거 찾아냄.


### 접근 방법을 적용한 코드
136ms 15.5MB
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        li = [0]*(len(nums)+1)

        for i in range(len(nums)): # O(n)
            li[nums[i]] = 1
        
        for i in range(len(li)):
            if li[i] ==0:
                return i
        return len(nums)+1
```
- 시간 54.89%
- 공간 54.29%
