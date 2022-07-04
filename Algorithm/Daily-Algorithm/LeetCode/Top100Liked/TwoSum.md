# LeetCode
[Two Sum](https://leetcode.com/problems/two-sum/)

### 문제 이해하기
- int list nums가 주어지고, 타겟넘버 target이 주어짐.
- list nums 중 두 수를 더해서 target을 만들어 낼 때, 인덱스 출력
- 각 숫자는 한 번 씩만 쓸 수 있고, 정답이 나오는 case는 오직 하나임.

### 문제 접근 방법
- 이중포문 돌림

### 접근 방법을 적용한 코드
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    self.result = [i,j]
                    return self.result
```
