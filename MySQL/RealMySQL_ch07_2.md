# Real MySQL - ch07 쿼리 작성 및 최적화

## 7.4 SELECT

### 7.4.1 SELECT 각 절의 처리 순서
```
FROM > (ON > JOIN) > WHERE > GROUP BY > DISTINCT > HAVING > SELECT > ORDER BY > LIMIT
```

### 7.4.2 WHERE절과 GROUP BY 절, 그리고 ORDER BY 절의 인덱스 사용

### 7.4.3 WHERE절 조검 비교 사용시 주의사항
#### NULL 비교
- MySQL에서는NULL값 포함된 레코드도 인덱스로 관리됨 -> NULL을 하나의 값으로 인정
- SQL 표준에서는 NULL은 비교 불가한 값.
- 연산, 비교에서 한쪽이라도 NULL이면 `IS NULL` 연산자 이용해야 함
    - `ISNULL()` 을 WHERE 조건에서 활용할 때 인덱스 활용 못하는 경우
    ```SQL
    -- 활용 가능
    SELECT * FROM titles WHERE ISNULL(to_date);
    SELECT * FROM titles WHERE to_date ISNULL;

    -- 활용 불가
    SELECT * FROM titles WHERE ISNULL(to_date)==1;
    SELECT * FROM titles WHERE ISNULL(to_date)==true;
    ```

#### 날짜 비교
- DATE, DATETIME - 문자열 : 문자열 값을 자동으로 DATETIME으로 변환해서 비교 수행. 성능 이슈 X
  - DATETIME 컬럼을 hire_date를 사용해 강제로 str형변환 시키는 경우 성능 이슈 발생
- DATE - DATETIME
  - 디폴트 : DATE의 시간을 MySQL에서 자동으로 00:00:00 으로 설정하여 비교
  - DATE() 함수 사용해 DATETIME에서 TIME을 삭제 할 수도 있음(`DATE(NOW())`)
- DATETIME - TIMESTAMP : TIMESTAMP 결과값이 상수이기 때문에 반드시 상수값을 비교 대상 컬럼에 맞게 변환하여 보여줘야 함.
  - 컬럼이 DATETIME이면 `FROM_UNIXTIME()` 함수 사용하여 TIMESTAMP -> DATETIME 변환 필요
  - 컬럼이 TIMESTAMPㅁ녀 `UNIX_TIMESTAMP()` 사용해 DATETIME -> TIMESTAMP 변환 필요

### 7.4.4 DISTINCT
집합함수와 DISTINCT 함수가 함께 사용되는 경우 인덱스 활용 못함. 이 경우 임시테이블 있어야 하는데, "Using temporary" 메세지가 출력되지 않음

#### SELECT DISTINCT
- SELECT 되는 레코드 중 유니크한 레코드 가져올 때 사용
- GROUP BY와 같은 방식으로 처리함
  - SELECT DISTINCT는 정렬 보장 못한다는 차이점

```SQL
SELECT DISTINCT first_name, last_name FROM employees;
SELECT DISTINCT(first_name), last_name FROM employees;
```
- 첫번째, 두번째 구문 다 (first_name + last_name)이 유니크한 레코드 가져옴
- distinct가 컬럼 일부만 유니크하게 적용되지 않음

#### 집합 함수와 함께 사용된 DISTINCT
- 집함 함수의 인자로 전달된 컬럼 값 중 중복을 제거하고 남은 값만 가져옴

### 7.4.5 LIMIT n

### 7.4.6 JOIN

### 7.4.7 GROUP BY

### 7.4.8 ORDER BY

### 7.4.9 서브 쿼리

### 7.4.10 집합 연산

### 7.4.11 LOCK IN SHARE MODE 와 FOR UPDATE

### 7.4.12 SELECT INTO OUTFILE


## 7.5 INSERT
### 7.5.1 INSERT AUTO_INCREMENT

### 7.5.2 INSERT IGNORE

### 7.5.3 REPLACE

### 7.5.4 INSERT INTO ... ON DUPLICATE KEY UPDATE

### 7.5.5 INSERT ... SELECT ...

### 7.5.6 LOAD DATA(LOCAL) INFILE ...


## 7.6 UPDATE
### 7.6.1 UPDATE ... ORDER BY ... LIMIT n

### 7.6.2 JOIN UPDATE


### 7.7 DELETE
### 7.7.1 DELETE ... ORDER BY ... LIMIT n

### 7.7.2 JOIN DELETE


## 7.8 스키마 조작(DDL)
### 7.8.1 데이터베이스

### 7.8.2 테이블

### 7.8.3 컬럼 변경

### 7.8.4 인덱스 변경

### 7.8.5 프로세스 조회

### 7.8.6 프로세스 강제 종료

### 7.8.7 시스템 변수 조회 및 변경

### 7.8.8 경고나 에러 조회

### 7.8.9 권한 조회


## 7.9 SQL 힌트
### 7.9.1 힌트의 사용법

### 7.9.2 STRAIGHT_JOIN

### 7.9.3 USE INDEX / FORCE INDEX / IGNORE INDEX

### 7.9.4 SQL_CACHE / SQL_NO_CACHE

### 7.9.5 SQL_CALC_FOUND_ROWS

### 7.9.6 기타 힌트


## 7.10 쿼리 성능 테스트
### 7.10.1 쿼리의 성능에 영향을 미치는 요소

### 7.10.2 쿼리의 성능 테스트

### 7.10.3 쿼리 프로파일링

