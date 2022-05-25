# Real MySQL - ch07 쿼리 작성 및 최적화
## 7.1 쿼리와 연관된 시스템 설정
### 7.1.1 SQL 모드
여러 값이 구분자(,)를 통해 동시에 설정 가능

**STRICT_ALL_TABLES**
- 컬럼 정해진 길이보다 큰 값 저장할 때 오류 발생, 쿼리 실행 중지
- MySQL에서는 원래 저장하려는 값이 정해진 길이보다 큰 값 저장하려 해도 경고만 발생함

**STRICT_TRANS_TABLES**
- 원하지 않는 데이터 타입 변환 필요 시 강제 변환하지 않고 에러 발생
- MySQL에서는 컬럼 타입과 호환되지 않는 값 최대한 바꿔서 저장하려 함

**TRADITIONAL**
- STRICT_TRANS_TABLES 과 비슷. 더 엄격하게 제어

**ANSI_QUOTES**
- 홑따옴표만 문자열 값 표기로 사용 가능하고, 쌍따옴표는 컬럼명이나 테이블같은 식별자를 표기하는데만 사용 가능(Like Oracle)

**ONLY_FULL_GROUP_BY**
- SQL 문법에 더 엄격한 규칙 줌
  - MySQL은 다른 DBMS랑은 다르게 GROUP BY 절에 포함되지 않은 컬럼도 집합 함수 사용 없이 SELECT, HAVING절 사용 가능함

**PIPE_AS_CONCAT**
- `||` 를 OR이 아닌 CONCAT으로 사용(Like Oracle)

**PAD_CHAR_TO_FULL_LENGTH**
- CHAR타입 컬럼값을 뒤쪽의 공백 제거 없이 반환

**NO_BACKSLASH_ESCAPES**
- 역슬래시 문자를 이스케이프 용도로 사용 못하게 함

**IGNORE_SPACE**
- SP, 함수 뒤에 공백이 있으면 "스토어드 프로시저나 함수가 없습니다" 에러 출력 가능..(MySQL은 SP, 함수명과 괄호 사이의 공백도 SP, 함수명으로 간주 가능)
- 프로시저, 함수명과 괄호사이의 공백 무시

**ANSI**
- MySQL 서버가 최대한 SQL 표준에 맞게 동작하게 함


### 7.1.2 영문 대소문자 구분
윈도우에 설치된 MySQL은 대소문자를 구분하지 않지만, 유닉스 계열 OS에서는 대소문자를 구분함.
- OS 완계 없이 대소문자 구분 영향 받지 않기 위해서는 `lower_case_table_name` 시스템 변수 설정
  - 0 : default. DB나 테이블명에 대해 대소문자 구분
  - 1 : 모두 소문자. 대소문자 구분x
  - 2 : 저장은 대소문자 구분, MySQL 쿼리에서 대소문자 구분 x

### 7.1.3 MySQL 예약어
예약어로 테이블, 컬럼 설정 위해서는 역따옴표(`) 나 쌍따옴표로 감싸야 함


## 7.2 매뉴얼의 SQL 문법 표기를 읽는 방법
- 대소문자 : 키워드
- 이탤릭체 : 테이블 명, 컬럼 명, 표현식
- 대괄호[] : 선택사항(없어도 문법 오류 x)
- 파이프 | : 앞, 뒤 키워드/표현식 중 하나만 선택해서 사용 가능
- 중괄호{} : 괄호 내 아이템 중 하나 반드시 사용해야 함
- ... : 키워드, 표현식 조합 반복 가능


## 7.3 MySQL 연산자와 내장 함수
### 7.3.1 리터럴 표기법
**문자열**
- 홀따옴표(`'`) 사용해서 표시   
```SQL
SELECT * FROM domain_table WHERE id='asdfghjjk';
SELECT * FROM domain_table WHERE id='test_''dylee';
SELECT * FROM domain_table WHERE id='test_"dylee';
SELECT * FROM domain_table WHERE id="test_'dylee";  -- MySQL만 가능
SELECT * FROM domain_table WHERE id="test_""dylee";  -- MySQL만 가능
```
식별자와의 충돌을 막기 위해서는 역따옴표로 감싸기
```SQL
CREATE TABLE table_test (`table` VARCHAR(20) NOT NULL, ...);

SELECT `column` FROM test_table;
```

**숫자**
- 다른 타입간 비교 시
  - 숫자컬럼 - '100' : '100'을 숫자로 변환
  - 스트링컬럼 - 100 : 문자열 컬럼을 숫자로 변환(인덱스 활용 x) -> 쿼리 자체가 실패할수도
```SQL
SELECT * FROM domain_table WHERE abuse_record_cnt=5;

SELECT * FROM domain_table WHERE abuse_record_cnt='5';  -- '5' -> 5
SELECT * FROM domain_table WHERE ip_address=5;  -- str(ip_address) -> int(ip_address)
```


**날짜**
- 스트링을 자동으로 DATE or DATETIME으로 변환해줌
```SQL
SELECT * FROM domain_table WHERE reg_dtime>'2022-05-24';
SELECT * FROM domain_table WHERE reg_dtime>STR_TO_DATE('2022-05-24', '%Y-%m-%d');
```

**불리언**
- == TINYINT
- TRUE/FALSE -> 실제로는 1, 0

```SQL
SELECT * FROM domain_table WHERE is_auto_ip=True;
SELECT * FROM domain_table WHERE is_auto_ip=1;
```


### 7.3.2 MySQL 연산자
**동등 비교(=, <=>)**
- `<=>` : `=` 연산자와 같음. 부가적으로 NULL 비교까지 수행. **NULL-Safe** 비교 연산자
```SQL
SELECT 1=1, NULL=NULL, 1=NULL;
>>> 1   NULL    NULL

SELECT 1<=>1, NULL<=>NULL, 1<=>NULL;
>>> 1   1   0
```

**부정 비교(<>, !=)**
- `<>`, `!=` 같음


**NOT 연산자(!)**
- `NOT` `!`


**AND(&&) OR(||) 연산**
- SQL 표준 : `AND` `OR`
  - MySQL은 `&&` `||` 도 허용함
  - PIPE_AS_COCAT 시스템변수 추가하면 || 사용 불가 (||이 SQL 표준에서 CONCAT으로 사용됨)


**나누기(/, DIV) 나머지(%, MOD) 연산**
```SQL
SELECT 29 / 9;
>>> 3.2222

SELECT 29 DIV 9;
>>> 3

SELECT MOD(29,9);
>>> 2

SELECT 29 MOD 9;
>>> 2

SELECT 29 % 9;
>>> 2
```

**REGEXP 연산자**
- RLIKE : 정규표현식을 비교하는 연산자
```SQL
SELECT 'abc' REGEXP '^[x-z]';
```

정규표현식 정리
- ^ : 문자열 시작
- $ : 문자열 끝
- [] : 문자 그룹([]중 하나)
- () : 문자 그룹(()전부 포함)
- | : 문자열 중 하나인지 확인
    - ex) abc|xyz : "abc" 거나 "xyz"인지 확인
- . : 1개의 문자
- * : 0 or 1
- + : 1회 이상 반복
- ? : 정규표현식이 0 or 1번만 올 수 있음

```SQL
SELECT * FROM domain_table WHERE source_domain REGEXP '(test.net)$';
```


**LIKE 연산자**
- 상수 문자열이 있는지 없는지 정도를 판단함

- % : 0개 또는 1개 이상의 모든 문자에 일치
- _ : 정확히 1개의 문자에 일치
- ESCAPE : %, _ 자체를 비교
```SQL
SELECT * FROM domain_table WHERE source_domain LIKE '%test.net';
SELECT * FROM domain_table WHERE source_domain LIKE '%test.net' ESCAPE '%';
```

**BETWEEN 연산자**
- 크거나 같다와 작거나 같다가 합쳐진 연산자.
- 선형으로 인덱스를 검색


**IN 연산자**
- 동등비교 연산자와 비슷함. 동등비교를 여러 번 수행
  - 여러 개 값이 비교되지만 전부 동등비교로 수행되어 일반적으로 빠름
  - MySQL에서는 비효율적인 경우 존재: IN 연산자에 상수값을 입력값으로 전달하는 경우
- 여러 컬럼 인덱스에서 Between 보다 효율적인 경우 존재함


### 7.3.3 MySQL 내장 함수

**NULL값 비교 및 대체(IFNULL, ISNULL)**
- IFNULL : 컬럼, 표현식 값이 NULL이면 다른 값으로 대체
- ISNULL : NULL이면 1, 아니면 0

```SQL
SELECT IFNULL(NULL, 'aaa');
>>> 'aaa'

SELECT ISNULL(NULL);
>>> 1

SELECT ISNULL('aaa');
>>> 0
```


**현재 시각 조회(NOW, SYSDATE)**
- NOW : 하나의 SQL에서 모든 NOW 함수는 같은 값을 가짐
- SYSDATE : 하나의 SQL 내에서도 호출되는 시점에 따라 결과 값이 다름

```SQL
SELECT NOW(), SLEEP(2), NOW();
>>> 2022-05-25 21:55:05     0       2022-05-25 21:55:05

SELECT sysdate(), SLEEP(2), sysdate();
>>> 2022-05-25 21:55:12     0       2022-05-25 21:56:14
```
- SYSDATE()의 잠재적인 문제점
  - SYSDATE()가 사용된 SQL문은 복제가 구축된 Mysql 슬레이브에서 안정적으로 복제되지 못함
  - SYSDATE()함수와 비교되는 컬럼은 인덱스를 효율적으로 사용하지 못함

```SQL
SELECT * FROM domain_table WHERE modify_dtime > NOW();
>>> Extra절에 Using index

SELECT * FROM domain_table WHERE modify_dtime > SYSDATE();
>>> Extra 절에 Using Index 없음
```
- 꼭 필요할 때가 아니면 SYSDATE() 사용하지 않는 것이 좋음
  - 이미 SYSDATE()함수 쓰고 있으면 설정파일에  `sysdate-is-now` 설정 추가하여 SYSDATE를 NOW처럼 사용


**날짜와 시간의 포맷(DATE_FORMAT, STR_TO_DATE)**
```SQL
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d') AS curr_dt;
>>> str('2022-05-25')

SELECT STR_TO_DATE('2022-05-25', '%Y-%m-%d')
>>> date('2022-05-25')
```


**날짜와 시간의 연산(DATE_ADD, DATE_SUB)**
```SQL
SELECT DATE_ADD(NOW(), INTERVAL 1 DAY) AS tomorrow;
>>> '2022-05-26 22:14:12'

SELECT DATE_ADD(NOW(), INTERVAL 1 DAY) AS yesterday;
>>> '2022-05-24 22:14:12'
```
- YEAR : 년도
- MONTH : 월
- DAY : 일
- HOUR : 시
- MINUTE : 분
- SECOND : 초
- QUARTER : 분기
- WEEK : 주


**타임 스탬프 연산(UNIX_TIMESTAMP, FROM_UNIXTIME)**   
- UNIX_TIMESTAMP : 경과된 초 반환(4byte 내 범위 표현 가능)
- FROM_TIMESTAMP : 인자로 받은 TIMESTAMP를 DATETIME으로 변환
```SQL
SELECT UNIX_TIMESTAMP('2022-01-01');

SELECT FROM_UNIXTIME(UNIX_TIMESTAMP('2022-01-01'));
>>> '2022-01-01'
```


**문자열 처리(RPAD, LPAD / RTRIM, LTRIM, TRIM)**
- RPAD, LPAD : 문자의 우측/좌측에 문자를 원하는 만큼 덧붙여서 저장
```SQL
SELECT RPAD('HAHA', 10, '_')
>>> 'HAHA__________'

SELECT LPAD('HOHO', 3, '0')
>>>
```

- RTRIM, LTRIM, TRIM : 우측/좌측/양측 공백문자 제거

```SQL
SELECT LTRIM('          GG'); 
>>> 'GG'
SELECT RTRIM(' GG                '); 
>>> ' GG'
SELECT TRIM(' GG                '); 
>>> 'GG'
```

**문자열 결합(CONCAT)**
```SQL
SELECT CONCAT('HAHA', 'HOHO', 'HEHE');
>>> 'HAHAHOHOHEHE'
SELECT CONCAT('HAHA', 'HOHO', 2);
>>> 'HAHAHOHO2'
SELECT CONCAT_WS(',', 'HAHA', 'HOHO');
>>> 'HAHA,HOHO'
```

**GROUP BY 문자열 결합(GROUP_CONCAT)**
```SQL
SELECT GROUP_CONCAT(cve_id) FROM ~~;
SELECT GROUP_CONCAT(cve_id SEPERATOR '|') FROM ~~;
SELECT GROUP_CONCAT(cve_id ORDER BY ip_addr DESC) FROM ~~;
SELECT GROUP_CONCAT(DISTINCT cve_id ORDER BY ip_addr DESC) FROM ~~;
```
- 지정한 컬럼 값들을 연결하기 위해 메모리 버퍼 사용 -> 시스템 변수에 지정된 크기를 초과하면 경고 메세지(warning) 발생

**값의 비교와 대체(CASE WHEN .. THEN .. END)**    
switch 구문과 같은 역할.
- CASE로 시작하고 END로 끝나야 하며, WHEN .. THEN .. 은 반복 가능
```SQL
SELECT point_name,
	CASE region WHEN '노원구도봉구' THEN '노원구'
				WHEN '광진구중랑구' THEN '광진구'
				ELSE '그외'
	END AS region
FROM walkingtrails;


SELECT point_name,
	CASE region WHEN region LIKE '노원구%' THEN '노원구'
				WHEN  region LIKE '광진구%' THEN '광진구'
				ELSE '그외'
	END AS region
FROM walkingtrails
ORDER BY region;
```

**타입의 변환(CAST, CONVERT)**
```SQL
SELECT CAST('1234' AS SIGNED INTEGER);
>>> 1234
```

```SQL
SELECT CONVERT('ABC' USING 'utf-8')
```

**이진값과 16진수 문자열 변환(HEX, UNHEX)**


**암호화 및 해시 함수(MD5, SHA)**
- 비대칭형 암호화 알고리즘
- 문자열을 각각 지정된 비트수에 맞춰 해시값으로 만들어내는 함수
- SHA : SHA-1 암호화 알고리즘 사용해 160비트(20byte) 해시값 반환
- MD5 : Message Digest 알고리즘 사용해 128비트(16byte) 해시값 반환
```SQL
SELECT MD5('abc');
>>> 900150983cd24fb0d6963f7d28e17f72

SELECT SHA('abc');
>>> a9993e364706816aba3e25717850c26c9cd0d89d
```
- 중복 가능성이 매우 낮아 인덱싱 용도로 사용됨


**처리 대기(SLEEP)**


**벤치마크(BENCHMARK)**
- 디버깅, 함수 성능 테스트용으로 유용
- BENCHMARK(반복해서 수행할 횟수, 반복해서 실행할 표현식)
- 성능 확인에 사용됨

```SQL
SELECT BENCHMARK(1000000, MD5('ABC'));
```

**IP 주소 변환(INET_ATON, INET_NTOA)**
- INET_ATON : 문자열로 구성도니 IP주소를 정수형으로 변환
- INET_NTOA : 정수형 IP 주소를 사람이 읽을 수 있는 형태 문자열('.'으로 구분된 IP)로 변환

```SQL
SELECT INET_ATON('127.0.0.1');
>>> 2130706433

SELECT INET_NTOA(2130706433);
>>> '127.0.0.1'
```

**MySQL 전용 암호화(PASSWORD, OLD_PASSWORD)**
- 일반 사용자가 사용해서는 안되는 함수
- 비밀번호 관리 위한 함수였지만, 암호화 하는 용도로 적합하지 않음 -> MD5, SHA 함수 사용 권장
- 이전 버전과 호환 안됨
- 4.0 버전에서 PASSWORD 사용했으면, 4.1 이상에서 PASSWORD 사용하는 부분을 OLD_PASSWORD로 변경해야 함. (혹은 시스템 설정 변수 파일 my.cnf에 old_password=1 설정)

**VALUES()**
- INSERT INTO ... ON DUPLICATE KEY UPDATE ... 형태의 SQL문장에서만 사용 가능
- PK, UK 중복되는 경우에는 UPDATE, 그 외의 경우 INSERT 수행
- 해당 컬럼에 INSERT 하려 했던 값을 참조하는 것이 가능함

```SQL
INSERT INTO tab_statistics (member_id, visit_count)
SELECT member_id, COUNT(*) as cnt
    FROM tab_accesslog
    GROUP BY member_id
ON DUPLICATE KEY
    UPDATE visit_count = visit_count + VALUES(visit_count);
```
- PK(member_id) 존재 시 cnt를 visit_count에 더함

**COUNT()**
- ORDER BY 구문이나 LEFT JOIN과 같은 레코드 건수를 가져오는 것과 무관 자겁을 포함함.
- 인덱스 제대로 튜닝하지 못하면느림
- 컬럼명, 표현식이 인자로 사용되면 컬럼이나 표현식 결과가 null이 아닌 레코드 건수만 반환

### 7.3.4 SQL 주석
```SQL
-- 한 라인 주석

# 한 라인 주석

/* 여러
라인
주석처리
하기*/
```

/*! : 문법에 일치하지 않는 내용 들어가면 MySQL에서 에러 발생(MySQL 외의 DBMS에서는 순수 주석)


## 7.4 SELECT

### 7.4.1 SELECT 각 절의 처리 순서
```
FROM > (ON > JOIN) > WHERE > GROUP BY > DISTINCT > HAVING > SELECT > ORDER BY > LIMIT
```

### 7.4.2 WHERE절과 GROUP BY 절, 그리고 ORDER BY 절의 인덱스 사용

**인덱스 사용 위한 기본규칙**
- 인덱스된 컬럼 값 자체를 변환하지 않고 그대로 사용
- B-Tree에 정렬된 인덱스 사용.

인덱스 사용 못하는 경우
```SQL
SELECT * FROM salaries WHERE salary*100 > 15000;
```
- salaries 컬럼을 가공하여 상수값과 비교하고 있음 -> 인덱스 활용 못함

- 컬럼의 **데이터 타입**과 비교되는 값의 타입이 달라도 인덱스 활용 못함(index 레인지 스캔 불가능 -> 인덱스 풀스캔 하게 됨)


**WHERE 절의 인덱스 사용** -> 이해 못함...
- 범위 제한 조건
  - 동등 비교 조건, IN으로 구성된 조건이 인덱스 컬럼과 얼마나 좌측부터 일치하는가에 따라 달라짐
- 체크 조건


**GROUP BY 절의 인덱스 사용**
- GROUP BY에 명시된 컬럼 순서가 인덱스를구성하는 컬럼의 순서와 다르면 인덱스 사용 불가능
- 인덱스에 명시된 컬럼 중 뒷쪽 컬럼은 GROUP BY에 없어도 되지만, 앞쪽이 없으면 인덱스 사용 불가능
- WHERE 와 달리 GROUP BY에 명시된 컬럼이 하나라도 인덱스에 없으면 사용 불가능
```SQL
INDEX ip_addr, domain_name, port_no;

SELECT *
FROM table_
GROUP BY port_no, ip_addr, domain_name;
>>> x : 순서

SELECT *
FROM table_
GROUP BY ip_addr, domain_name;
>>> o

SELECT *
FROM table_
GROUP BY port_no;
>>> x : 앞쪽 인덱스 없음

SELECT *
FROM table_
GROUP BY ip_addr, domain_name, port_no;
>>> o

SELECT *
FROM table_
GROUP BY ip_addr, domain_name, port_no, banner;
>>> x : 인덱스 아닌 컬럼(banner)
```

- WHERE 조건절에 앞선 컬럼이 동등비교조건으로 사용되면, GROUP BY 절에서 앞선 컬럼이 빠져도 인덱스 사용 가능 할 때도 있음

```SQL
SELECT *
FROM table_
WHERE ip_addr='1.1.1.1'
GROUP BY domain_name, port_no;
```

**ORDER BY 절의 인덱스 사용**
- GROUP BY와 거의 동일
- 정렬되는 각 컬럼의 오름차순(ASC) 및 내림차수(DESC) 옵션이 인덱스와 같거나 정반대여야 함
- MySQL 인덱스는 모든컬럼이 오름차순
  - ORDER BY가 모두 오름차순이거나 내림차순일때만 인덱스 사용 가능


```SQL
INDEX ip_addr, domain_name, port_no;

SELECT *
FROM table_
ORDER BY port_no, ip_addr, domain_name;
>>> x : 순서

SELECT *
FROM table_
ORDER BY ip_addr, domain_name;
>>> o

SELECT *
FROM table_
ORDER BY port_no;
>>> x : 앞쪽 인덱스 없음

SELECT *
FROM table_
ORDER BY ip_addr ASC, domain_name ASC, port_no ASC;
>>> o

SELECT *
FROM table_
ORDER BY ip_addr, domain_name, port_no, banner;
>>> x : 인덱스 아닌 컬럼(banner)

SELECT *
FROM table_
ORDER BY ip_addr DESC, domain_name ASC, port_no, ASC;
>>> x

SELECT *
FROM table_
ORDER BY ip_addr DESC, domain_name DESC, port_no, DESC;
>>> o
```

**WHERE 조건과 ORDER BY(또는 GROUP BY)절의 인덱스 사용**
