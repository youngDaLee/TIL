# 인덱스 튜닝
## 3.1 테이블 액세스 최소화
인덱스의 ROWID = 물리적 주소보다 논리적 주소에 가까움. 포인터가 아님!!


인덱스 클러스터링 팩터(CF) = 군집성 = 특정 컬럼을 기준으로 같은 값을 갖는 데이터가 모여있는 정도
* CF가 안좋다 -> 인덱스 정렬 순서랑 테이블 레코드 정렬순서가 일치하지 않는것 -> 블록IO발생


## 3.2 부분범위 처리 활용

## 3.3 인덱스 스캔 효율화

## 3.4 인덱스 설계
