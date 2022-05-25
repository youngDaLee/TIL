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
SELECT * FROM domain_table WHERE source_domain REGEXP '(netmarble.net)$';
```


**LIKE 연산자**
- 상수 문자열이 있는지 없는지 정도를 판단함

- % : 0개 또는 1개 이상의 모든 문자에 일치
- _ : 정확히 1개의 문자에 일치
- ESCAPE : %, _ 자체를 비교
```SQL
SELECT * FROM domain_table WHERE source_domain LIKE '%netmarble.net';
SELECT * FROM domain_table WHERE source_domain LIKE '%netmarble.net' ESCAPE '%';
```

**BETWEEN 연산자**


**IN 연산자**


### 7.3.3 MySQL 내장 함수

