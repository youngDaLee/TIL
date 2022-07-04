# LeetCode
[Big Countries](https://leetcode.com/problems/big-countries/)

### 문제 이해하기
- world table에서 area>3000000, population>25000000 인 row 출력

### 접근 방법을 적용한 코드
```SQL
SELECT name, population, area
FROM World
WHERE area>3000000 or population>25000000;
```
