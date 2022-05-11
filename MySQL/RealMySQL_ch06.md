# Real MySQL - ch06 실행 계획
## 6.1 개요
- 옵티마이저 : DBMS의 쿼리 실행계획슬 수립. 가장 복잡한 부분으로 알려져있음.

옵티마이저의 실행 계획을 알아내야만 실행 계획의 불합리한 부분을 알아내고 최적화 할 수 있음.
### 6.1.1 쿼리 실행 절차
1. 사용자로부터 요청된 SQL문을 잘개 쪼개서 MySQL 서버가 이해할 수 있게 분리
   - 이 단계를 "SQL 파싱(parsing)" 이라 함
   - SQL 신텍스 에러가 여기에서 걸러짐
   - SQL 파스트리 생성됨(MySQL 서버는 SQL 자체가 아닌 SQL 파스트리로 쿼리 실행함)
2. SQL 파싱정보(파스트리)를 확인해 어떤 테이블부터 읽고 어떤 인덱스를 이용해 테이블을 읽을지 선택
   - 최적화 및 계획수립 단계
   - MySQL 서버 "옵티마이저"에서 처리
   - 실행계획 만든다.
   - SQL 파스트리로 아래 내용 처리
     - 불필요한 조건 제거, 복잡한 연산 단순화
     - 여러 테이블 조인 있는 경우 어떤 순서로 테이블 읽을지 결정
     - 각 테이블 조건과 인덱스 통계 정보 이용해 사용할 인덱스 결정
     - 가져온 레코드들을 임시 테이블에 넣고 다시 가공해야 하는지 결정
3. 결정된 테이블의 읽기 순서 or 선택된 인덱스를 이용해 스토리지 엔진으로부터 데이터 가져옴
    - 2단계에서 만든 실행계획대로 스토리지 엔진에 레코드를 읽어오도록 요청
    - MySQL 엔진에서 스토리지 엔진으로부터 받은 레코드 조인하거나 정렬하는 작업 수행

1, 2번 단계는 MySQL 엔진에서 처리, 3번단계는 MySQL 엔진과 스토리지 엔진이 동시에 참여해서 처리함

### 6.1.2 옵티마이저 종류
옵티마이저는 DB서버에서 두뇌 역할
- 비용 기반 최적화(Cost-based optimizer, CBO) : 현재 대부분의 DBMS가 선택
  - 쿼리 처리하기 위한 여러 가능한 방법 만들고,각 단위 작업 비용 정보와, 대상 테이블 통계정보로 각 실행계획 산출 -> 최소비용 처리방식 선택해 최종쿼리 실행
- 규칙 기반 최적화(Rule-based optimizer, RBO) : 예전 오라클에서 많이 사용
  - 옵티마이저 내장 우선순위에 따라 실행 계획 수립.
  - 통계 정보(테이블 레코드 건수, 컬럼값 분포도) 조사x -> 같은 쿼리에 대해 같은 실행방법 도출

### 6.1.3 통계 정보
- 통계정보가 명확해야 올바른 방향으로 쿼리 실행함
- MySQL에서의 통계정보는 대량의 레코드 건수와 인덱스의 유니크한 값의 개수 정도.
- 오라클과 같은 DBMS에서는 통계 정보 수집에 많은 시간 소요되어 통계 정보만 따로 백업함.
- MySQL 통계정보는 사용자가 알아채지 못하는 순간 변경되어 동적인 편. 
- 레코드 건수 많지 않으면 통계 정보 부정확한 경우 많아 `ANALYZE` 명령으로 통게 정보 갱신해야 함.



## 6.2 실행 계획 분석
`EXPLAIN` : 쿼리 실행 계획 확인 가능
- 확인하고 싶은 쿼리 문장 적으면 됨.

```SQL
EXPLAIN
SELECT point_name
FROM walkdb.walkingtrails
WHERE region='은평구'
LIMIT 10;
```
![explain](../.img/mysql/realmysql_ch06_1.PNG)
- 표 형태로 된 1줄 이상의 결과 표시됨
### 6.2.1 id 칼럼
**단위(SELECT) 쿼리** : SELECT 키워드 단위로 구분한 것
- !id 컬럼은 단위쿼리별로 값이 부과됨!

- 하나의 SELECT 문장 안에서 여러 테이블 조인하면, 조인하는 테이블 개수만큼 실행계획 레코드 출력되지만, 같은 id가 부여됨.
- SELECT 문장은 하나인데 여러 테이블 조인되는 경우는 id값증가하지 않고 같은 id 부여됨

![id](../.img/mysql/realmysql_ch06_2.PNG)

![id2](../.img/mysql/realmysql_ch06_3.PNG)

### 6.2.2 select_type 칼럼
각 SELECT 쿼리가 어떤 타입의 쿼리인지 표시.
- SIMPLE
  - UNION이나 서브쿼리 사용하지 않는 단순 SELECT인 경우
  - 실행계획에서 select_type이 SIMPLE인 경우는 반드시 하나만 존재함
- PRIMARY
  - UNION이나 서브쿼리 포함된 SELECT쿼리 실행계획에서 가장 바깥쪽(OUTER)에 있는 단위쿼리
  - 실행계획에서 select_type이 PRIMARY인 경우는 반드시 하나만 존재함
- UNION
  - 
- DEPENDENT UNION
- UNION RESULT
- SUBQUERY
- DEPENDENT SUBQUERY
- DERIVED
- UNCACHEABLE SUBQUERY
- UNCACHEABLE UNION
### 6.2.3 table 칼럼

### 6.2.4 type 칼럼



## 6.3 MySQL의 주요 처리 방식


## 6.4 실행 계획 분석 시 주의사항


## 읽기 좋은 블로그
- [데이터베이스 옵티마이저에 대하여](https://coding-factory.tistory.com/743)
- [Optimize Table & Analyze Table](https://myinfrabox.tistory.com/145)
- [InnoDB에 대하여(MyISAM과 차이점)](https://sarc.io/index.php/mariadb/346-innodb-myisam)

## QnA
### Q) select_type 컬럼에서 SIMPLE은 왜 하나만 존재함?

