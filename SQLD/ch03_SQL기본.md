# SQL 기본 
## 관계형 DB의 개요
### Table
column/row의 이차원 구조 데이터 저장소.

Table 구조
- 열 (column)
- 필드 (field, value)
- 행 (row)

Table 관계 용어들
- 정규화(Nomalization) : 테이블 분할해서 데이터 정합성 확보, 불필요한 중복 줄이는 프로세스
- 기본키(Primary Key)
- 외부키(Foreign Key) 

### ERD
ERD 구성요소
- 엔터티
- 관계
- 속성

## DDL
### 데이터 유형
- NUMERIC : 정수, 실수
- CHARACTER(s)/CHAR(s) : 고정길이
- VARCHAR2(s)/VARCHAR(s) : 가변길이
- DATETIME : 날짜/시각

### CHAR VS VARCHAR
저장 영역
- VARCHAR : 가변길이. 필요한 영역은 실제 데이터 크기. 길이가 다양한 컬럼/정의된 길이와 실제 데이터 길이 차이가 있는 컬럼에 적합
- CHAR : 고정길이

비교방법
- CHAR : 공백을 채워서 비교하는 방식
  - 짧은 쪽에 공백 추가해서 2개 데이터가 같은 길이가 되도록 하고 앞에서 한 문자씩 비교. 끝의 공백만 다른 문자열은 같다고 판단
- VARCHAR : 공백도 한 문자로 취급. 끝의 공백이 다르면 다른 문자로 판단

```
CHAR
'AA' = 'AA  ' => TRUE

VARCHAR 
'AA' = 'AA  ' => FALSE
```

### CREATE TABLE
주의사항
- 테이블 명 : 객체를 의미할 수 있는 단수형 권고. 다른 테이블명과 중복X
- 한 테이블 내 컬럼면 중복 불가, 컬럼들은 ,로 구분
- 벤더에서 예약어 사용 불가
- A-Z, a-z, 0-9, _, $, # 문자만 허용
- 대소문자 구분 X

```SQL
CREATE TABLE PLAYER(
    PLAYER_ID       CHAR(7)         NOT NULL,
    PLAYER_NAME     VARCHAR(20)     NOT NULL,
    TEAM_ID         CHAR(3)         NOT NULL,
    E_PLAYER_NAME   VARCHAR(40),
    VATION          VARCHAR(20),
    HEIGHT          SMALLINT,
    CONSTRAINT PLAYER_PK    PRIMARY KEY(PLAYER_ID),
    CONSTRAINT PLAYER_FK    FOREIGN KEY(TEAM_ID) REFERENCES TEAM(TEAM_ID),
)
```
#### 테이블 구조 확인
- ORACLE : `DESCRIBE 테이블명`
- SQL server : `exec sp_help 'dbo.테이블명'`

#### 제약조건
- 기본키(PRIMARY KEY) : 테이블에 존재하는 각 행을 한 가지 의미로 특정할 수 있는 한 개 이상 컬럼
- 고유키(UNIQUE KEY) : 고유하게 식별 위한 고유키, NULL값 가진 행 여러 개 있어도 OK
- 외부키(FOREIGN KEY) : 다른 테이블 기본키로 사용되는 관계를 연결하는 컬럼
- NULL : 아직 정의되지 않은 미지의 값
- DEFAULT : 기본값을 사전에 설정. 데이터 지정하지 않은 경운 사전에 정의된 기본값 자동 입력됨

#### SELECT로 테이블 생성
ORACLE    
```SQL
CREATE TABLE ~ AS SELECT ~
```

SQL SERVER
```SQL
SELECT * INTO TABLE1 FROM TABLE2
```
- 기존 테이블 제약조건 중 NOT NULL만 새롱누 테이블에 적용.
- 기본키, 고유키, 외래키, CHECK 등의 다른 제약조검 사라짐


### ALTER TABLE
테이블 구조 변경. 컬럼 추가/삭제, 제약조건 추가/삭제 작업
```SQL
ALTER TABLE PLAYER              -- 테이블 변경
ADD (ADDRESS VARCHAR(80));      -- 테이블 추가

--컬럼 삭제
ALTER TABLE PLAYER DROP COLUMN ADDRESS;

-- ORACLE 컬럼 수정
ALTER TABLE PLAYER MODIFY (ADDRESS VARCHAR2(80));
-- SQL 컬럼 수정
ALTER TABLE PLAYER ALTER COLUMN ADDRESS VARCHAR2(80);

-- ORACLE 컬럼명 변경
ALTER TABLE PLAYER RENAME COLUMN ADDRESS TO ADD
-- SQL 컬럼명 변경
sp_rename 'dbo.TEAM_TEMP.TEAM_ID', 'TEAM_TEMT_ID', 'COLUMN'

-- 제약조건 삭제
ALTER TABLE PLAYER DROP CONSTRAINT PLAYER_FK;

-- 제약조건 추가
ALTER TABLE PLAYER ADD CONSTRAINT PLAYER_FK FOREIGN KEY(TEAM_ID) REFERENCES TEAM(TEAM_ID);

-- ORACLE 테이블명 변경
RENAME TABLE_BEFORE TO TABLE_AFTER;
--SQL 테이블명 변경
sp_rename TABLE_BEFORE, TABLE_AFTER;

-- 테이블 삭제(관계있었던 참조 제약조건도 삭제)
DROP TABLE PLAYER [CASCADE CONSTRAINT];

-- 테이블 구조 유지한채 데이터만 전부 삭제
TRUNCATE TABLE PLAYER;
```
MODIFY COLUMN
- 컬럼 크기 늘릸는 있는데 줄이지는 못함
- 컬럼이 NULL만 가지고 있거나 데이터 아무것도 없으면 줄일 수 있음
- NULL만 가지고 있으면 데이터 유형 변경 가능


`DELETE TABLE` VS `TRUNCATE TABLE`
- 테이블 전체 데이터 삭제하는 경우, 시스템 활용 측면에서 시스템 부하가 적은 TRUNCATE TABLE 권고
- 단, TRUNCATE TABLE은 정상적인 복구 불가함

## DML
자료들 조회, 입력, 수정, 삭제(SELECT, INSERT, UPDATE, DELETE)   
실시간으로 테이블에 영향을 미치지 않고 COMMIT을 이용해 TRANSACTION 종료해야만 실제 테이블에 반영됨(DDL은 AUTO COMMIT임)

```SQL
SELECT PLAYER_ID [ALL/DISTINCT] FROM PLAYER;
```
- ALL이 디폴트.
- DISTINCT : 중복된 데이터 1건으로 처리해서 출력
- WILDCARD : 해당 테이블 모든 컬럼 정보 조회하고 싶을 때 `*`
- ALIAS : 컬럼명 뒤에 위치. AS, as 키워드로 사용 가능.
```SQL
INSERT INTO PLAYER(PLAYER_ID, PLAYER_NAME) VALUES ('200207', '박지성');
UPDATE PLAYER SET POSITION = 'MF';
DELETE FROM PLAYER;
```

### 산술연산자와 합성연산자
산술연산자
- NUMBER, DATE 자료형에 적용됨.
- `()`, `*`, `/`, `+`, `-` 우선순위

합성(CONCATENTANION)연산자
- 문자와 문자 연결
  - ORACLE : `||`
  - SQL SERVER : `+`
  - 공통 : `CONCAT(str1, str2)`

## TCL
COMMIT, ROLLBACK, SAVEPOINT.   
DML에 의해 조작도니 결과를 작업단위(트랜잭션)별로 제어하는 명령
#### 트랜잭션의 특성
- 원자성(automicity) : 트랜잭션 정의된 연산들 모두 성공적으로 실행되던지, 전혀 실행되지 않은채 남아있던지(all or nothing)
- 일관성(consistency) : 트랜잭션 전 DB 내용 잘못되어 있지 않다면 트랜잭션 실행 이후에도 DB 내용 잘못되어 있으면 안됨
- 고립성(isolation) : 트랜잭션 실행 도중 다른 트랜잭션 영향받아 잘못된 결과 만들면 안됨
- 지속성(durabilty) : 트랜잭션 성공적으로 수행되면 갱신한 DB 내용 영구 저장

#### COMMIT, ROLLBACK 효과
데이터 무결성 보장, 영구적 변경 전 데이터 변경사항 확인 가능. 논리적 연관된 작업 그룹핑해서 처리 가능
- COMMIT 디폴트
  - ORACLE : NOT AUTO COMMIT
  - SQL SERVER : AUTO COMMIT

### SQL SERVER 트랜잭션 3가지 방식
- AUTO COMMIT : 명령어 성공적으로 수행 -> AUTO COMMIT, 오류 발생 -> ROLLBACK
- 암시적 트랜잭션 : ORACLE과 같은 방식. 트랜잭션 끝을 사용자가 명시적으로 COMMIT, ROLLBACK 처리
- 명시적 트랜잭션 : 트랜잭션 시작/끝을 사용자가 지정. BEGIN TARSACTION(BEGIN TRAN)으로 트랜잭션 시작


### SAVE POINT
SAVE POINT 정의하면 ROLLBACK 시 SAVEPOINT까지 트랜잭션 일부만 롤백가능
```SQL
SAVEPOINT SVPT1;
ROLLBACK TO SVPT1;

SAVE TRANSACTION SVTR1;
ROLLBACK TRANSATION SVTR1;
```
## WHERE 절
### 연산자
- 비교 연산자 : `=`, `>`, `>=`, `<`, `<=`
- SQL 연산자
  - `BETWEEN A AND B` : A, B 모두를 포함하는 범위
  - `IN(LIST)` : 리스트 값 중 어느 하나라도 일치하면 됨
  - `LIKE '비교문자열'` : 비교 문자열고 ㅏ형태 일치하면 됨
    - `%` : 0개 이상 어떤 문자
    - `_` : 1개인 단일 문자
    - `WHERE PLAYER_NAME LIKE '_A%'` : 선수 영문 이름 두번째 문자가 A인 선수들 이름
  - `IS NULL`
- 논리 연산자 : `AND`, `OR`, `NOT`
- 부정 연산자 : `!=`, `^=`, `<>`, `NOT BETWEEN a AND b`, `NOT IN (LIST)`, `IS NOT NULL`

#### 연산자 우선순위
`()` -> NOT 연산자 -> 비교, SQL 비교 연산자 -> `AND` -> `OR`


### 함수
### 내장함수
- 단일행 : 문자형 함수, 숫자형 함수, 날짜형 함수, 변환형 함수, NULL 관련함수
- 다중행 : 집계함수, 그룹함수, 윈도우함수

### 단일행 함수의 종류
#### 문자형 함수
- `LOWER`, `UPPER`, `SUBSTR`
- `SUBSTRING`, `LENGTH`
- `LEN`, `LTRIM`, `RTRIM`, `TRIM`, `ASCII`, `CONCAT`

### 숫자형 함수
- `ABS`, `MOD`, `ROUND`, `SIGN`, `CHR`
- `CHAR`, `CEIL`
- `CEILING`, `FLOOR`, `EXP`, `LOG`, `LN`, `POWER`, `SIN`, `COS`, `TAN`

CEIL/CELING VS FLOOR
- `CEIL` / `CEILING` : 숫자보다 크거나 같은 최소 정수 리턴
  - `CEIL(38.123)` `CEILING(38.123)` => 39 
  - `CEILING(-38.123)` => -38 
- `FLOOR` : 숫자보다 작거나 같은 최대 정수 리턴
  - `FLOOR(38.123)` => 38
  - `FLOOR(-38.123)` => -39

### 변환형 함수
- 명시적(Explicit) 데이터 유형 변환 : 데이터 변환형 함수로 데이터 유형 변환하도록 명시해주는 경우
- 암시적(implicit) 데이터 유형 변환 : DB가 자동으로 데이터 유형 변환하여 계산하는경우

### CASE 표현
```SQL
CASE
    EXPR WHEN COMPARSINO_EXPR THEN RETURN_EXPR
    ELSE 표현
END
```

### NULL 관련 함수
- `NVL(표현식1, 표현식2)` `ISNULL(표현식1, 표현식2)` : 표현식 1이 아니면 표현식 2값 출력 
- `NULLIF(표현식1, 표현식2)` : 표현식 1값이 표현식 2와 같으면 NULL, 같지 않으면 표현식 1값 출력
- `COALESCE(표현식1, 표현식2, ...)` : 임의의 개수 표현식에서 NULL이 아닌 최초의 표현식 나타냄. 모든 표현식이 NULL이면 NULL 리턴

`IS NULL` `IS NOT NULL` 은 NULL 관련 함수가 아닌 연산자임

### 다중행 함수의 종류
#### 집계함수
`SELECT`, `HAVING`, `ORDER BY`절에 사용가능
- `COUNT(*)` : NULL값 포함한 행의 수
- `SUM()` : NULL값 제외한 합계
- `AVG()` : NULL값 제외한 평균
- `MAX()` `MIN()` : 최대/최소값 출력

## Group By, Having절
- SELECT 절에 정의되지 않은 컬럼은 사용불가
- 집계함수 WHERE절에 올 수 없음. GROUPBY 통해 소그룹멸 기준 정한 후 SELECT절에서 집계함수 사용
### GROUP BY
- ALIAS명 사용 불가
- WHERE절은 전체 데이터를 GROUP으로 나누기 전 행들을 미리 제거

### HAVING
- 일반적으로 GROUP BY 뒤에 위치
- WHRER절에서는 집계함수 사용 불가능하지만 HAING절은 집계함수 사용 가능
- WHERE절로 행 거르고 -> GROUP BY에서 그룹으로 묶어진 결과를 -> HAVING절에서 판단해서 리턴

```SQL
SELECT POSTION 포지션, ROUND(AVG(HEIGHT), 2) 평균 키
FROM PLAYER
GROUP BY POSITION HAVING AVG(HEIGHT) >= 180;

-- 실행 결과
포지션  평균키
------ --------
GK      180.26
DF      180.21
```
- 평균 키 180 넘는 POSITON만 출력됨

## Order By절
- SLECT절에 정의되지 않은 컬럼 사용 가능
- 기본적인 정렬 순서는 오름차순(`ASC`) <-> 내림차순(`DESC`)
  - 숫자 오름차순 : 작은 숫자부터 출력
  - 날짜 오름차순 : 날짜 빠른 값 먼저 출력
- ORACLE : NULL값이 가장 큰 값으로 간주. 오름차순이면 NULL이 가장 마지막
- SQL SERVER : NULL값이 가장 작은값. 오름차순이면 NULL이 가장 먼저
- 컬럼명, ALIAS명, 컬럼 순서 혼용 사용 가능

### SELECT 문장 실행 순서
`FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`

### TOP N 쿼리
#### ROWNUM
- WHERE절 행의 개수 제한

```SQL
WHERE ROWNUM = 1;

WHERE ROWNUM <= N;
WHERE ROWNUM < N;
```
### TOP()
- SQL SERVER에서 행 개수 제한

```SQL
SELECT TOP(2) ~ FROM EMP ORDER BY SAL
```
- 1위 한명, 공동 2위 2명있을 때 with ties 조건 추가하면 3건 출력, with ties 없으면 2건 출력

## JOIN
두 개 이상의 테이블에서 컬럼 가져오는 방법. 

### EQUI JOIN(등가 조인)
두 개 테이블 간 컬럼 값들 정확히 힐치하는 경우 사용하는 방법. 대부분 PK<->FK 관계 기반으로 함

```SQL
WHERE PLAYER.TEAM_ID = TEAM.TEAM_ID AND PLAYER.POSITION = 'GK';

FROM PLAYER INNER JOIN TEAM ON PLAYER.TEAM_ID=TEAM.TEAM_ID
WHERE PLAYER.POSITION = 'GK';
```


### NON EQUI JOIN(비등가 조인)
두 테이블 간 값들 정확하게 일치하지 않는 경우. `=` 연산자가 아닌 다른 연산자(`BETWEEN`, `>`, `>=`, `<`, `<=`) 연산자 사용해서 JOIN 수행

```SQL
WHERE E.SAL BETWEEN S.LOSAL AND S.HISAL;
```

### 3개 이상 TABLE JOIN
```SQL
SELECT P.PLAYER_NAME 선수명, P.POSITION 포지션, T.REGION_NAME 연고지, T.TEAM_NAME 팀명, S.STADIUM_NAME 구장명
FROM PLAYER P, TEAM T, STADIUM S 
WHERE P.TEAM_ID = T.TEAM_ID AND T.STADIUM_ID = S.STADIUM_ID
ORDER BY 선수명;
```

```SQL
SELECT P.PLAYER_NAME 선수명, P.POSITION 포지션, T.REGION_NAME 연고지, T.TEAM_NAME 팀명, S.STADIUM_NAME 구장명
FROM PLAYER P
    INNER JOIN TEAM T ON P.TEAM_ID = T.TEAM_ID 
    INNER JOIN STADIUM S ON T.STADIUM_ID = S.STADIUM_ID 
ORDER BY 선수명;
```