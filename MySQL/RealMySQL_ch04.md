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

