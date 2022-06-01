# Real MySQL - ch07 쿼리 작성 및 최적화

## 7.4 SELECT

### 7.4.1 SELECT 각 절의 처리 순서
```
FROM > (ON > JOIN) > WHERE > GROUP BY > DISTINCT > HAVING > SELECT > ORDER BY > LIMIT
```

### 7.4.2 WHERE절과 GROUP BY 절, 그리고 ORDER BY 절의 인덱스 사용

### 7.4.3 WHERE절 조검 비교 사용시 주의사항
**NULL 비교**
- MySQL에서는NULL값 포함된 레코드도 인덱스로 관리됨 -> NULL을 하나의 값으로 인정
- SQL 표준에서는 NULL은 비교 불가한 값.
- 연산, 비교에서 한쪽이라도 NULL이면 `IS NULL` 연산자 이용해야 함

### 7.4.4 DISTINCT

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

