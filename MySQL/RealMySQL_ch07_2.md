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

```SQL
UPDATE tp_test t1, employees e
SET t1.first_name=e.first_name
WHERE e.emp_no=t1.emp_no;
```
- 사원 번호로 조인하여 employees 테이블 first_name 컬럼을 tp_test의 first_name 컬럼으로 복사


옵티마이저에 실행 순서 명시하고 싶을 시 STRAIGHT_JOIN 키워드 사용
```SQL
UPDATE (SELECT de.depth_no, COUNT(*) AS emp_count FROM dept_emp de GROUP BY de.dept_no) dc
  STRAIGHT_JOIN departments d ON dc.dept_no=d.dept_no
SET d.emp_count=dc.emp_count;
```

### 7.7 DELETE
### 7.7.1 DELETE ... ORDER BY ... LIMIT n
ORDER BY, LIMIT 사용하는 방식은 UPDATE와 동일
```SQL
DELETE FROM employees ORDER BY first_name LIMIT 10;
```

### 7.7.2 JOIN DELETE
JOIN DELETE로 여러 테이블 조인해 레코드 삭제 가능.

3개 테이블 조인하여 하나의 테이블에서 레코드 삭제하는 쿼리
```SQL
DELETE e
FROM employees e, dept_emp de, departments d
WHERE e.emp_no=de.emp_no AND de.dept_no=d.dept_no
  AND d.dept_no='d001';
```

3개 테이블 조인하여 여러 테이블에서 레코드 삭제하는 쿼리
```SQL
DELETE e, de
FROM employees e, dept_emp de, departments d
WHERE e.emp_no=de.emp_no AND de.dept_no=d.dept_no
  AND d.dept_no='d001';

DELETE e, de, d
FROM employees e, dept_emp de, departments d
WHERE e.emp_no=de.emp_no AND de.dept_no=d.dept_no
  AND d.dept_no='d001';
```

옵티마이저가 조인 순서 결정하지 못하면 STRAIGHT_JOIN 키워드로 조인 순서를 옵티마이저에 지시
```SQL
DELETE e, de, d
FROM  departments d
  STRAIGHT_JOIN dept_emp de ON e.emp_no=de.emp_no
  STRAIGHT_JOIN employees e ON de.dept_no=d.dept_no
WHERE d.dept_no='d001';
```
## 7.8 스키마 조작(DDL)
### 7.8.1 데이터베이스
#### DB 생성
```SQL
CREATE DATABASE [IF NOT EXISTS] employees;
CREATE DATABASE [IF NOT EXISTS] employees CHARACTER SET utf8;
CREATE DATABASE [IF NOT EXISTS] employees CHARACTER SET utf8 COLLATE utf8_general_ci;
```

#### DB 목록
```SQL
SHOW DATABASES;
SHOW DATABASES LIKE '%emp%'
```

#### DB 선택
```SQL
USE employees;
```

#### DB 속성 변경
```SQL
ALTER DATABASE employees CHARSET SET=euckr;
ALTER DATABASE employees CHARSET SET=euckr COLLATE=euckr_korean_ci;
```

#### DB 삭제
```SQL
DROP DATABASE [IF EXIST] employees;
```

### 7.8.2 테이블
#### 테이블 생성
```SQL
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tb_test (
  member_id BIGINT [UNSIGNED] [AUTO_INCREMENT],
  nickname CHAR(20) [CHARACTER SET 'utf8'] [COLLATE 'utf8_general_ci'] [NOT NULL],
  home_url VARCHAR(200) [COLLATE 'latin_general_cs'],
  birth_year SMALLINT(4) [UNSIGNED] [ZEROFILL],
  member_point INT [NOT NULL] [DEFAULT 0],
  registered_dttm DATETIME [NOT NULL],
  modified_ts TIMESTAMP [NOT NULL] [DEFAULT CURRENT_TIMESTAMP],
  gender ENUM('Female', 'Male') [NOT NULL],
  hobby SET('Reading', 'Game', 'Sports'),
  profile TEXT [NOT NULL],
  session_data BLOB,
  PRIMARY KEY (memeber_id),
  UNIQUE INDEX ux_nickname (nickname),
  INDEX ix_registereddttm (registered_dttm)
) ENGINE=INNODB;
```

#### 테이블 구조 조회
- `SHOW CREATE TABLE`
  - 테이블 CREATE TABLE 문장 표시해줌
  - 최초 테이블 생성 시 사용자가 입력했던 값 그대로 보여주는 것 아님. MySQL 서버가 메타정보 읽어서 CREATE TABLE 명령으로 재작성해서 보여주는 것.
- `DESC`, `DESCRIBE`
  - 테이블 컬럼정보 표로 나타님


#### 테이블 구조 변경
```SQL
ALTER TABLE employees CHARACTER SET 'euckr';
ALTER TABLE employees ENGINE=myisam;
```
- 두번째 명령은 테이블 데이터 리빌드 하는 목적으로도 사용됨.
  - 리빌드 주 목적 : 레코드 삭제가 자주 발생하는 테이블에서 데이터 저장되지 않은 빈 공간(프래그맨테이션) 제거해 디스크 공간 확보

#### RENAME TABLE
```SQL
RENAME emp_stat TO backup_emp_stat;

-- 하나의 트랜잭션에서 여러 테이블 이름 변경 가능
RENAME emp_stat TO backup_emp_stat
      temp_emp_stat TO emp_stat;
```
- 주로 테이블 바꿔치기 할 때 사용
- Inno DB에서는 ㅁ낳은 데이터 변경된 뒤 메타 데이터 불일치하는 현상 발생 가능.

#### 테이블 DB 변경
```SQL
REMANE TABLE db1.employees TO db2.employees;
```

#### 테이블 상태 조회
```SQL
SHOW TABLE STATUS LIKE 'employees'\G -- \G : 레코드 컬럼을라인당 하나씩 표현하는 옵션(문장의 끝)
```

#### 테이블 구조 복사
```SQL
CREATE TABLE temp_employees LIKE employees;
```

```SQL
INSERT INTO temp_employees SELECT * FROM employees;
```
- 데이터까지 복사할 경우

#### 테이블 구조 및 데이터 복사

#### 테이블 삭제
레코드 많지 않은 테이블은 상관 없으나, 레코드 많은 테이블 삭제하는 작업은 부하가 큰 작업에 속함.
테이블이 크면 서비스 도중 삭제 작업 수행 x

```SQL
DROP TABLE
```
- LOCK_open 이라는 잠금 획득해야 함.
- A 테이블에 LOCK_open 걸면 A와 무관한 B,C테이블도 LOCK 걸림. 
- A 테이블 DROP TABLE 명령 완료 시 까지 다른 커넥션 쿼리 처리 못함

### 7.8.3 컬럼 변경
#### 컬럼 추가
```SQL
ALTER TABLE employees ADD COLUMN emp_telno VARCHAR(20);
ALTER TABLE employees ADD COLUMN emp_telno VARCHAR(20) ALTER emp_no; -- emp_no 뒤에 컬럼 추가
```

#### 컬럼 삭제
```sql
ALTER TABLE employees DROP COLUMN emp_telno;
```

#### 컬럼 명, 타입 변경
`CHANGE COLUMN 지금컬럼명 바꿀컬럼명`
```SQL
ALTER TABLE employees CHANGE COLUMN first_name name VARCHAR(14) NOT NULL;
```

컬럼명 이외의 값이나 NULL 여부 변경
```SQL
ALTER TABLE tb_enum MODIFY COLUMN member_hobby ENUM('Tennis', 'Game', 'Climbing');
```

#### ALTER TABLE 진행 상황
```SQL
SHOW GLOBAL STATUS LIKE 'Handler%';
```
- Handler_read_rnd_next : 풀 테이블 스캔 방식으로 모든 레코드 읽을 때 읽은 레코드 건수
- Handler_write : 테이블에 INSERT 되는 레코드 건수

### 7.8.4 인덱스 변경
#### 인덱스 추가
```SQL
ALTER TABLE employees ADD PRIMARY KEY [USING {BTREE|HASH}] (emp_no);
ALTER TABLE employees ADD UNIQUE INDEX [USING {BTREE|HASH}] ux_emptelno (emp_telno);
ALTER TABLE employees ADD INDEX [USING {BTREE|HASH}] ux_emptelno (emp_telno);
ALTER TABLE employees ADD FULLTEXT INDEX ux_emptelno (emp_telno);
ALTER TABLE employees ADD SPATIAL INDEX ux_emptelno (emp_telno);
```
- PRIMARY KEY : PK 생성 키워드. 어떤 스토리지 엔진에서나 사용 가능
- UNIQUE INDEX : 키값 중복 허용 X 인덱스. 스토리지 관계 없이 사용 가능
- FULLTEXT INDEX : 전문검색 인덱스. MyISAM에서만 사용 가능
- SPATIAL INDEX : 공간 검색 인덱스. MyISAM에서만 사용 가능
- INDEX : 중복 허용. 일반 보조 인덱스

- 인덱스 알고리즘 선택 가능. 일반적으로 B-TREE 기본 선택됨. -> MEMORY 테이블이나 NDB에 대해서는 HASH 생성

#### 인덱스 조회
```SQL
SHOW INDEX FROM employees;
```

#### 인덱스 삭제
```SQL
ALTER TABLE employees DROP PRIMARY KEY;
ALTER TABLE employees DROP INDEX ix_emptelno;
```

#### 컬럼 및 인덱스 변경을 모아서 실행
```SQL
ALTER TABLE employees 
  DROP INDEX ix_firstname
  ADD INDEX ix_new_firstname (first_name)
  ADD COLUMN emp_telno VARCHAR(15);
```

#### 인덱스 생성 위한 ALTER 테이블 진행 상황
InnoDB 사용하는 MySQL 5.1 & MySQL 5.5 이상의 InnoDB 테이블
- 인덱스 추가 삭제 작업 임시테이블 사용 x
- 삭제는 바로 수행
- 그나마 시간 걸리는 작업 -> 인덱스 신규 생성.
  - 임시테이블 사용 x ("Handler_write" 값 변화 x)
  - "Handler_read_rnd_nex" 컬럼 변화

MySQL 5.0 InnoDB 테이블, 모든 버전의 MyISAM 테이블
- ALTER TABLE 명령이 테이블 레코드를 임시테이블로 복사하며 처리됨

### 7.8.5 프로세스 조회
```SQL
SHOW PROCESSLIST;
```
- 서버 접속한 사용자 목록
- 각 클라이언트 사용자가 어떤 쿼리 실행중인지

각 컬럼의 의미
- id : 스레드 아이디. 쿼리,커넥션 강제종료 시 사용
- User : 클라이언트가 MySQL 서버 접속 시 사용한 계정
- Host : 클라이언트 호스트 명, IP 주소
- db : 클라이언트가 기본으로 사용하는 DB
- command : 해당스레드가 현재 어떤 작업 하는지
- Time : command 컬럼에 표시되는 작업이 얼마나 실행되고 있는지
- State : 소분류. 상당히 많음
- Info : 실행중인 쿼리 문장 -> 쿼리 전체 확인 시 SHOW FULL PROCESSLIST 명령 사용

### 7.8.6 프로세스 강제 종료
```sql
KILL QUERY 4228;
KILL 4228;
```

### 7.8.7 시스템 변수 조회 및 변경
```SQL
SHOW GLOBAL VARIABLES;
SHOW GLOBAL VARIABLES LIKE '%connections%';
SHOW SESSION VARIABLES LIKE '%timeout%';
SHOW VARIABLES LIKE '%timeout%';
```

### 7.8.8 경고나 에러 조회
```SQL
SHOW WARNINGS;
```
- 쿼리 실행 도중 에러 발생 시 에러가 아닌 경고, 정보성 메세지 발생했는지 보여줌.
- 그런 경고메세지 조회 위해 SHOW WARNINGS 명령 사용
  - 에러는 SHOW ERRORS;

### 7.8.9 권한 조회
```SQL
SHOW PRIVILEGES;

SHOW GRANTS FOR 'root'@'localhost';  -- 특정 사용자 권한 조회 시 GRANT 사용
```

## 7.9 SQL 힌트
MySQL 옵티마이저가 최적의 방법으로 데이터 읽지 못할 때 많음. SQL 문장에 **특별한 키워드를** 지정해 MySQL 옵티마이저에게 최적의 방법 제안. 이런 키워드를 **SQL 힌트** 라 함
### 7.9.1 힌트의 사용법
MySQL에서는 힌트 위치 지정되어 있음. 오라클은 힌트가 주석 일부로 해성되지만, MySQL은 SQL일부로 해석됨. 

```SQL
SELECT * FROM employees USE INDEX (PRIMARY) WHERE emp_no=10001;
SELECT * FROM employees /*! USE INDEX (PRIMARY) */ WHERE emp_no=10001;
```
- 두 번째의 힌트 기술 방식은 다른 DBMS에서는 힌트를 주석처리 하지만 MySLQ에서는 SQL 일부로 해석.

### 7.9.2 STRAIGHT_JOIN
옵티마이저 힌트이면서 조인키워드이기도 함. **조인 순서 고정 역할**. FROM절에 명시된 순서대로 조인 수행
```SQL
SELECT *
FROM employees e, depth_emp de, departments d
WHERE e.emp_no=de.emp_no AND d.depth_no=de.depth_no

-- STRAGIGHT_JOIN 힌트
-- employees -> depth_emp -> departments 순으로 조인 수행
SELECT STRAIGHT_JOIN e.first_name, e.last_name, d.dept_name
FROM employees e, depth_emp de, departments d
WHERE e.emp_no=de.emp_no AND d.depth_no=de.depth_no

-- 위와 같은 쿼리
SELECT /*!STRAIGHT_JOIN*/  e.first_name , e.last_name, d.dept_name
FROM employees e, depth_emp de, departments d
WHERE e.emp_no=de.emp_no AND d.depth_no=de.depth_no


-- employees -> depth_emp -> departments 순으로 조인 수행
SELECT /*!STRAIGHT_JOIN*/  e.first_name , e.last_name, d.dept_name
FROM employees e
  INNER JOIN depth_emp de ON e.emp_no=de.emp_no
  INNER JOIN departments d ON d.depth_no=de.depth_no

```

MySQL 힌트는 다른 DBMS에 비해 옵티마이저에 미치는 영향이 큰 편. 힌트를 잘못 사용하면 훨씬 느려지게 만들 수도 있음.  
```SQL
SELECT STRAIGHT_JOIN e.first_name, e.last_name, d.dept_name
FROM employees e, departments d, depth_emp de
WHERE e.emp_no=de.emp_no AND d.depth_no=de.depth_no
```
- 위 쿼리는, e 테이블과 d 테이블의 직접적인 조건이 없어도 무조건 힌트대로 (employees -> departments -> depth_emp) 조인 수행 => 비효율적

옵티마이저가 확실히 잘못한 경우 아니라면 STRAIGHT_JOIN은 사용 않는것이 좋다.

STARIGHT_JOIN 힌트 사용하는경우
- 임시테이블(인라인 뷰 혹은 파생된 테이블)과 일반테이블 조인
  - 임시테이블을 드라이빙으로 선정. 일반테이블 조인컬럼에 인덱스 없으면 레코드 건수 적은 테이블을 드라이빙으로.
- 임시테이블끼리 조인
  - 크기가 작은 테이블 드라이빙으로
- 일반테이블끼리 조인
  - 레코드 건수 적은 테이블. 한쪽에만 인덱스 있으면 인덱스 없는걸 드라이빙으로

=> 다만 레코드 건수가 전체 레코드 건수가 아닌, 선택되는 레코드 건수이기 때문에 유동적. 웬만하면 옵티마이저 실행계획 따르는 것이 좋음

### 7.9.3 USE INDEX / FORCE INDEX / IGNORE INDEX
4개 이상의 컬럼으로 된 인덱스(복잡한 인덱스)에서 MySQL 옵티마이저가 적합한 인덱스를 찾지 못할 경우, **USE INDEX** 혹은 **FORCE INDEX** 이용해서 인덱스 사용 유도 가능.

인덱스 힌트는 인덱스 포함한 테이블 뒤에 괄호로 명시.

#### USE INDEX
- MySQL 옵티마이저에게 특정 테이블 인덱스 권장

#### FORCE INDEX
- USE INDEX와 다른점 X. USE INDEX보다 옵티마이저에 미치는 영향이 더 강함.

#### IGNORE INDEX
- 인덱스를 사용하지 못하게 함.
- 풀테이블 스캔 유도할 때 사용

#### USE INDEX FOR JOIN
- JOIN 키워드는 조인뿐만 아니라 레코드 검색용도까지 포함.

#### USE INDEX FOR ORDER BY
- 명시된 인덱스를 ORDER BY 용으로만 사용

#### USE INDEX FOR JOIN
- 명시된 인덱스를 GROUP BY로만 사용

```SQL
SELECT * FROM employees WHERE emp_no=1001;
SELECT * FROM employees FORCE INDEX(primary) WHERE emp_no=1001;
SELECT * FROM employees USE INDEX(primary) WHERE emp_no=1001;
SELECT * FROM employees INGORE INDEX(primary) WHERE emp_no=1001;
SELECT * FROM employees FORCE INDEX(ix_test_idx) WHERE emp_no=1001;
```

### 7.9.4 SQL_CACHE / SQL_NO_CACHE
MySQL은 쿼리 결과를 재사용하기 위해 쿼리 캐시에 선택적으로 저장. 저장 여부를 결정하는 힌트.

query_cache_type(시스템 변수 설정)
- 쿼리 결과 저장 여부 결정

힌트 x
- query_cache_type 시스템 변수 설정 값
  - 0 or OFF : 캐싱 x
  - 1 or ON : 캐싱
  - 2 or DMAND : 캐싱 x

SQL_CACHE
- query_cache_type 시스템 변수 설정 값
  - 0 or OFF : 캐싱 x
  - 1 or ON : 캐싱
  - 2 or DMAND : 캐싱

SQL_NO_CACHE
- query_cache_type 시스템 변수 설정 값
  - 0 or OFF : 캐싱 x 
  - 1 or ON : 캐싱 x
  - 2 or DMAND : 캐싱 x

### 7.9.5 SQL_CALC_FOUND_ROWS
LIMIT을 걸어도 전체 레코드 건수 반환.
```SQL
SELECT SQL_CALC_FOUND_ROWS * FROM employees LIMIT 5;

SELECT FOUND_ROWS() AS total_record_count;
```
페이징 처리 시 활용? -> 효율적이지 않기 때무에 사용하지 않음.


## 7.10 쿼리 성능 테스트
쿼리의 성능을 판단하기 위해 고려해야 하는 점
### 7.10.1 쿼리의 성능에 영향을 미치는 요소
#### OS 캐시
대부분의 OS가 한 번 읽은 데이터는 OS가 관리하는 별도의 캐시영역에 보관했다가, 다시 해당 데이터 요청되었을 때 캐시 내용을 바로 MySQL 서버로 반환함. -> InnoDB는 OS 캐시가 큰 영향 x(파일시스템 캐시, 버퍼 거치지 않는 Direct I/O 사용하기 때문). MyISAM은 OS 캐시 의존도 높기 때문에 성능 차이 크다.

OS가 가지고 있는 캐시, 버퍼가 없는 상태에서 쿼리 성능 테스트하기 위해서는 MyhSQL 서버를 재시작하거나, 캐시 삭제 명령 필요
```
## 캐시, 버퍼 내용을 디스크와 동기화
>>> sycn

## OS에 포함된 캐시 내용 초기화
>>> echo 3 > /proc/sys/vm/drop_caches
```
#### MySQL 서버의 버퍼 풀(InnoDB 버퍼풀, MyISAM 키 캐시)
MySQL 서버도 데이터 파일 내용을 페이지 단위로 캐싱하는 기능 제공함.

#### MySQL 쿼리 캐시
이전에 실행했던 SQL 문장과, 그 결과를 임시로 저장해두는 메모리공간.

쿼리 캐시 비우기 위해 RESET QUERY CACHE 명령 수행.
=> 테스트 시 매번 지우기 번거로우므로 SQL_NO_CACHE 옵션 추가하여 쿼리 테스트.
#### 독립된 MySQL 서버
MySQL 서버 가동중인 장비에 다른 웹 서버나 배치용 프로그램 실행되면 쿼리 영향 줌.
### 7.10.2 쿼리의 성능 테스트
이해가 안감
```SQL
SELECT SQL_NO_CACHE STRAIGHT_JOIN
  e.first_name, d.depth_name
FROM employees e, depth_emp de, departments d
WHERE e.emp_no=de.emp_no AND d.dept_no=de.dept_no;


SELECT SQL_NO_CACHE STRAIGHT_JOIN
  e.first_name, d.depth_name
FROM departments d, employees e, depth_emp de
WHERE e.emp_no=de.emp_no AND d.dept_no=de.dept_no;
```
위 두 쿼리 실행시간을 단축시키기 때문에 임시테이블을 생성하는 방식으로 수정해서 쿼리 테스트를 한다 함.

```SQL
SELECT SQL_NO_CACHE COUNT(*) FROM(
  SELECT SQL_NO_CACHE STRAIGHT_JOIN
    e.first_name, d.depth_name
  FROM employees e, depth_emp de, departments d
  WHERE e.emp_no=de.emp_no AND d.dept_no=de.dept_no;
)


SELECT SQL_NO_CACHE COUNT(*) FROM(
  SELECT SQL_NO_CACHE STRAIGHT_JOIN
    e.first_name, d.depth_name
  FROM departments d, employees e, depth_emp de
  WHERE e.emp_no=de.emp_no AND d.dept_no=de.dept_no;
)
```
이렇게 했을 때 왜 실행시간이 단축되는지 이해가 힘들다.


+) 네트워크 통신 비용 부하 줄임(결과 데이터를 전부 가져오지는 않으므로)
```SQL
SELECT SQL_NO_CACHE STRAIGHT_JOIN
  e.first_name, d.depth_name
FROM employees e, depth_emp de, departments d
WHERE e.emp_no=de.emp_no AND d.dept_no=de.dept_no
LIMIT 0;

SELECT SQL_NO_CACHE STRAIGHT_JOIN
  e.first_name, d.depth_name
FROM departments d, employees e, depth_emp de
WHERE e.emp_no=de.emp_no AND d.dept_no=de.dept_no
LIMIT 0;
```



### 7.10.3 쿼리 프로파일링
쿼리의 각 단계별 작업 시간 확인

```SQL
>>> SET PROFILING=1; -- 프로파일링 설정 ON
>>> SHOW VARIABLES LIKE 'profiling'; -- 프로파일링 설정 확인
```

```SQL
... 쿼리 실행

>>> SHOW PROFILES;  -- 분석된 쿼리 목록
>>> SHOW PROFILE FOR QUERY 1;  -- Query_ID=1 인 쿼리의 상세 프로파일링 정보
>>> SHOW PROFILE;  -- 가장 최근 실행된 쿼리의 프로파일링 정보
>>> SHOW PROFILE CPU FOR QUERY 1;  -- Query_ID=1 쿼리의 CUP 관련된 내용만 구분해 확인.
```