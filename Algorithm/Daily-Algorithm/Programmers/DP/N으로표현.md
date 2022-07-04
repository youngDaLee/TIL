# 프로그래머스
[N으로 표현](https://programmers.co.kr/learn/courses/30/lessons/42895)


### 문제 이해하기
- 숫자 N과 사칙연산만을 사용해서 number을 표현할 때, N 사용횟수의 최솟값을 리턴

### 문제 접근 방법
- 이중리스트 dp를 생성
- 최솟값이 8보다 크면 -1을 리턴한다 했으므로 최대 8까지 가질 수 있음
- 그러므로 dp[][0]에 n ~ nn,nnn,nnn 까지 숫자를 넣음
- 1만으로 연산해서 총 숫자 2개 쓴 연산을 i=2에 넣고, 1과 2로 연산한거를 3에 넣고... 하는 식으로 쭉 dp에 넣으면서 찾는 number가 나올 때 까지 반복

- 블로그 보고 list보다는 set으로 바꿔줌.
### 구현 배경 지식
dp

### 접근 방법을 적용한 코드
```python
def solution(N, number):
    answer = -1

    dp = []

    for i in range(1, 9):
        nums = {int(str(N)*i)}
        for j in range(0, i-1): 
            for x in dp[j]:
                for y in dp[i-j-2]: # i-1 - (j+1)
                    nums.add(x+y)
                    nums.add(x-y)
                    nums.add(x*y)
                    if y!=0:
                        nums.add(x//y)
        if number in nums:
            return i

        dp.append(nums)

    return answer # 실패시 -1 리턴
```
### 해결하지 못한 이유


### 문제를 해결한 코드
```

```

### 문제를 해결한 방법
