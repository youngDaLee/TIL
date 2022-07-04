# LeetCode
[Distribute Candies](https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3657/)

### 문제 이해하기
- 앨리스가 n개의 캔디를 갖고있고, i번째 캔디 타입은 candyType[i]이다.
- 의사는 앨리스에게 n/2개의 캔디만 먹으라고 했다.
- 앨리스는 의사의 조언을 따르면서 최대한으로 먹을 수 있는 다른 타입의 캔디를 구해라.
- n == candyType.length
- 캔디 타입은 번호로 주어짐... 

### 문제 접근 방법
- 제일 처음 n을 구하고
- set->list 해 줘서 중복삭제함.
- 그 리스트 길이 구해서

### 접근 방법을 적용한 코드
```python
class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType)
        candyType = list(set(candyType))
        candy_num = len(candyType)

        if candy_num <= int(n/2):
            self.result = candy_num
        else:
            self.result = int(n/2)
        
        return self.result

```