# LeetCode
[Big Countries](https://leetcode.com/problems/big-countries/)

### ���� �����ϱ�
- world table���� area>3000000, population>25000000 �� row ���

### ���� ����� ������ �ڵ�
```SQL
SELECT name, population, area
FROM World
WHERE area>3000000 or population>25000000;
```
