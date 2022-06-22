# Real MySQL - ch04 트랜잭션과 잠금

## 4.1 트랜잭션
```SQL
Start TRANSACTION;

USE CRIMINAL_IP;
```
- 잠금 : 동시성 제어. UPDATE
- 트랜잭션 : 데이터 정합성 보장. 동일한 값에 대한 보장
- 트랜잭션 격리 수증 : 트랜잭션을 공유하고 차단하는 레벨

쿼리를 짜고 실행하는 데 테이블 락이 걸리면 서비스에 이슈가 생김

### 4.1.1 MySQL에서의 트랜잭션
- 논리적 작업 셋 자체가 100% 적용되거나(commit) 아무것도 적용되지 않거나(rollback 또는 트랜잭션 rollback시키는 오류 발생)

MyISAM
- 오류 발생해도 이전 실행했던 것이 db에 남아있음

InnoDB
- 오류 발생 시 해당 쿼리 전체 롤백됨

```SQL
CREATE TABLE myisam_tab(fdpk INT NOT NULL, PRIMARY KEY (fdp)) ENGINE=MyISAM;
CREATE TABLE innodb_tab(fdp INT NOT NULL, PRIMARY KEY (fdp)) ENGINE=INNODB;
INSERT INTO myisam_tab(fdpk) VALUES(3);
INSERT INTO innodb_tab(fdpk) VALUES(3);

INSERT INTO myisam_tab(fdpk) VALUES(1),(2),(3);
>>>
fdpk
1
2
3
INSERT INTO innodb_tab(fdpk) VALUES(1),(2),(3);
>>>
fdpk
3
```
### 4.1.2 주의사항
트랜잭션을 DB 커넥션과 같이 꼭 필요한 최소의 코드에만 적용하도록 함(트랜잭션 범위 최소화)

## 4.2 MySQL 엔진 잠금
엔진단 락/MySQL 락
- 스토리지 엔진 레벨
  - 모든 스토리지 엔진 영향
- MySQL 엔진 레벨: 스트로지 엔진 제외한 나머지 부분
  - 스토토리지 엔진 간 상호 영향 x

### 4.2.1 글로벌 락(GLOBAL LOCK)
글로벌락 걸리는 경우 거의 없음. 이렇게 잠기는 경우는 거의 없음.
- `FLUSH TABLES WITH READ LOCK` 명령으로만 획득 가능
- MYSQL에서 지원하는 락 중 가장 범위가 큼
- SELECT를 제외한 DDL, DML을 실행하는 경우, 글로벌락 해제될 때 까지 해당 문장 대기로 남음
- 영향 범위 : 서버 전체
- 작업 대상 테이블, DB 달라도 동일한 영향 받음
- mysqldump로 일관된 백업 받아야 할 때 글로벌락 사용함

### 4.2.2 테이블 락(TABLE LOCK)
- `LOCK TABLES table_name [READ|WRITE]` 명령으로 획득 가능
- 사용 가능 엔진 : MyISAM, InnoDB
  - InnoDB에서는대부분 DML에서는 무시되고, DDL에만 영향을 끼침
  - InnoDB : 레코드(로우 기반 락) -> 테이블 전체 락은 없음. DDL만 영향 -> 테이블에 뭐가 추가되면 전체적으로 락이 잡히게 되어 영향이 미치게 됨. 대용량 테이블 인덱스 생성하기 위해서는 무중단 서비스를 위해 새로 생성하고... 그런 경우
  - MyISAM : 전체
- 글로벌락과 마찬가지로 온라인 작업에 영향을 많이 미침.

### 4.3.3 유저 락(USER LOCK)
- 사용자가 지정한 문자열에 대해 획득, 반납하는 잠금
  - 5대 웹 서버가 어떤정보를 동기화하거나 여러 클라이언트가 상호 동기화 처리할 때 사용.
  - 배치프로그램 : 통신사가 일괄적으로 처리... 어떤 데몬이 12시가 될 때 일괄적으로 처리. 데이터를 쌓아놓고 특정 시간에 일괄적으로 처리. 데이터를 한 번에 많이 처리해서 데드락 걸리는경우가 있어 그럴 경우 유용하게 유저락이 사용됨
- 많은 레코드를 한 번에 변경하는 트랜잭션에서 유용하게 사용

### 4.3.4 네임 락
- DB 객체(테이블, 뷰, ..)이름 변경하는 경우에 잠금(RENAME)
- 테이블 


## 4.3 MyISAM, MEMORY 스토리지 엔진의 잠금
### 4.3.1 잠금 획득
- 읽기 잠금
  - 테이블에 쓰기잠금 걸려있지 않으면 바로 읽기잠금 획득하고 읽기 작업 가능
- 쓰기 잠금
  - 테이블에 아무런 잠금 걸려있지 않아야 쓰기잠금 획득 가능

### 4.3.2 잠금 튜닝

### 4.3.3 테이블 수준의 잠금 확인 및 해제


## 4.4 InnoDB 스토리지 엔진의 잠금
### 4.4.1 InnoDB 잠금 방식
- 비관적 잠금
  - 잠금을 획득하고 변경 작업을 처리
  - 일반적으로 **높은 동시성 처리에는** 비관적 잠금이 유리. INNODB는 비관적 잠금 방식 채택함
- 낙관적 잠금
  - 우선 변경작업 수행, 마지막에 문제가 있었으면 롤백

### 4.4.2 InnoDB 잠금 종류
- 레코드 락(RECORD LOCK, RECORD ONLY LOCK)
  - 레코드 자체만을 잠그는 락
  - 인덱스가 하나도 없는 테이블이어도, 내부적으로 자동생성된 클러스터 인덱스를 이용해 잠금 설정
  - PK, UK 변경 작업은 갭에 대해서는 잠그지 않고 레코드 자체에 대해서만 락을건다
  - InnoDB는 인덱스에 락을 건다.(레코드 자체가 아닌)

- 갭(GAP)락
  - 레코드와 바로 인접한 레코드 사이의 간격만 잠그는 락
  - 레코드 사이의 새로운 레코드 INSERT 제어

- 넥스트 키락(NEXT KEY LOCK)
  - 레코드락 + 갭락
  - Statsment 포맷 바이너리 로그 사용할때는 배업 위해 MySQL 서버에서 Repeatable 격리 수준 사용해야 함
  - 데드락 자주 발생하는 경우
  - 넥스트키락, 갭락 줄이는게 좋음.....
  - 바이너리 로그 포맷을 ROW형태로.. 우리는 Mixed 사용함

- 자동증가락(AUTO INCREMENT BOOK)
  - 자주 사용함.
  - AUTO_INCREMENT 락은 트랜잭션 과련 없이 AUTO_INCREMENT 값 가져오는 순간만 AUTO_INCREMENT락 걸렸다가 해제
  - AUTO_INCREMENT는 테이브렝서 하나만 존재.
  - 5.1이상은 파라미터 이용해 자동증가 락 작동 방싱 변경 가능.
    - INSERT 되는 건수를 예측할 ㅅ ㅜ있을땐 훨씬 빠른 래치(뮤텍스)이용해 처리함


### 4.4.3 인덱스와 잠금
- INNODB 잠금은 레코드가 아닌 인덱스를 잠그는 방식
- 변경해야 할 레코드를 찾기 위해 인덱스의 레코드를 모두 잠가야 함
- 만약 테이블의 인덱스가 하나도 없으면 테이블 풀스캔하며 작업. 테이블의 모든 레코드를 잠그게 되어 좋은 설계라 할 수 없음

## 4.5 MySQL 격리 수준 - 중요
### 4.5.1 READ UNCOMMITED
- 각 트랜잭션 변경 내용이 commit, rollback 여부 관련 없이 다른 트랜잭션에서도 보임
- Dirty Read : 어떤 트랜잭션 작업 완료되지 않았는데 다른 트랜잭션에서 볼 수 있음
  - 중간에 롤백 된 경우 select 쿼리 다시 때릴 때 없어질 수 있음

  - 한 트랜잭션 내에서도 정합성 문제가 발생함
- RDBMS 표준에서는 트랜잭션 표준으로 인정하지 않을만큼 정합성에 문제가 많은 격리수준.

**언두영역**
- InnoDB에서 업데이트 된 값, 업데이트 전 값을 언두영역에 저장함.
- 언두영역은 쿼리캐시랑은 무관하게 Update를 실행했을때만 임시로 사용하는 캐시이다.

### 4.5.2 READ COMMITED
- ORACLE DBMS에서 사용되는 격리수준
- DIRTY CACHE 발생 X(SELECT 쿼리 결과가 언두영역에 백업된 레코드에서 가져옴)
- 트랜잭션에서 변경한 내용이 커밋되기 전 까지는 다른 트랜잭션에서 해당 내용 조회 불가
- 하나의 트랜잭션 내 같은 SLEECT 쿼리 실행 시 항상 같은 결과를 가져와야 한다는 REPEATABLE READ 정합성 어긋남
- PHANTOM READ : 다른 트랜잭션에서 수행할 작업에 의해 레코드가 보였다 안보였다 하는 현상 발생
### 4.5.3 REPEATABLE READ
- 일반적으로 사용하고, 실제로 우리가 사용하는 격리 수준
- 바이너리 로그를 가진 데이터가 MySQL 장비에서는 REPEATABLE 격리 수준 이상 사용해야 함.
- 데이터가 CRUD되는 모든 로그 저장. 로그를 슬래이브로 보냄.
- MVCC를 위해 언두영역에 백업된 이전 데이터 이용해 **동일 트랜잭션 내 동일한 결과 보장함**

### 4.5.4 SERIALIZABLE
- 가장업격한 격리수준
- 읽기 작업도 공유 잠금을 획득해야만 함. 동시에 다른 트랜잭션 변경 부락
- InnoDB 스토리지 엔진에서는 REPEATABLE READ 격리수준에서도 PHANTOM READ 발생 X -> 굳이 SEREIALIZABLE 사용 필요 X



#### Q) 잠금 기능을 보고 MyISAM, InnoDB를 선택해야 하는 상황이 발생하는지

#### Q) MySQL 엔진 잠금은 DBA가 걸게 되는건지, MySQL 서버에서 걸게 되는건지.
- DDL, DML에 따라 락이 따라오는것. DBA가 락을 걸 수도 있지만, 대부분은 명령에 따라 서버에서 걸림

#### Q) 유저락의 범위. 클라이언트 접근을 락 하는건지?
- 클라이언트 접근을 락 하는 것

#### Q) 읽기/쓰기 잠금이 헷갈림

#### Q) 갭 vs 레코드

#### Q) 인덱스가 없을 땐 PK로 잠그는지. 무조건 인덱스로만 락이 걸리는지
- PK도 인덱스의 범주에 있는거라 인덱스가 없으면 PK사용하는게 맞음
- PK, 인덱스 없는 경우 : 클러스터 인덱스 -> 테이블에 PK, 인덱스 안만들어도 클러스터 인덱스를 생성함(INNODB의 특성)

#### Q) 마스터 -> 슬레이브가 흘러가는 구조
- 마스터 데이터를 슬레이브로 넘겨주는게 바이너리 로그.
- CRUD 로그가 다 로그에 저장되면 그걸 슬레이브에 보내지고, binary 로그 보고 똑같이 만들어줌