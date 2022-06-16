# Real MySQL - ch04 트랜잭션과 잠금

## 4.1 트랜잭션

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
### 4.2.1 글로벌 락(GLOBAL LOCK)
- `FLUSH TABLES WITH READ LOCK` 명령으로만 획득 가능
- MYSQL에서 지원하는 락 중 가장 범위가 금
- SELECT를 제외한 DDL, DML을 실행하는 경우, 글로벌락 해제될 때 까지 해당 문장 대기로 남음
- 영향 범위 : 서버 전체
- 작업 대상 테이블, DB 달라도 동일한 영향 받음
- mysqldump로 일관된 백업 받아야 할 때 글로벌락 사용함

### 4.2.2 테이블 락(TABLE LOCK)
- `LOCK TABLES table_name [READ|WRITE]` 명령으로 획득 가능
- 사용 가능 엔진 : MyISAM, InnoDB
  - InnoDB에서는대부분 DML에서는 무시되고, DDL에만 영향을 끼침
- 글로벌락과 마찬가지로 온라인 작업에 영향을 많이 미침.

### 4.3.3 유저 락(USER LOCK)
- 사용자가 지정한 문자열에 대해 획득, 반납하는 잠금
- 많은 레코드를 한 번에 변경하는 트랜잭션에서 유용하게 사용

### 4.3.4 네임 락
