# LeetCode
[Design HashMap](https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3663/)

### 문제 이해하기
- Hash table 라이브러리를 사용하지 않고 HashMap을 만들어봐라.

### 문제 접근 방법
- dictionary 생성하고
- dictioanry에서 key 삽입, 검색, 삭제 함

### 구현 배경 지식
- [Hash](https://github.com/youngDaLee/TIL/blob/main/Algorithm/Hash.md)

### 접근 방법을 적용한 코드
- runtime 92.76%
- memory 80.28%
```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dict__ = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.__dict__[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.__dict__.keys():
            return self.__dict__[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.__dict__.keys():
            del self.__dict__[key]

```
