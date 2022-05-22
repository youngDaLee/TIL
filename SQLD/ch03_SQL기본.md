# SQL �⺻ 
## ������ DB�� ����
### Table
column/row�� ������ ���� ������ �����.

Table ����
- �� (column)
- �ʵ� (field, value)
- �� (row)

Table ���� ����
- ����ȭ(Nomalization) : ���̺� �����ؼ� ������ ���ռ� Ȯ��, ���ʿ��� �ߺ� ���̴� ���μ���
- �⺻Ű(Primary Key)
- �ܺ�Ű(Foreign Key) 

### ERD
ERD �������
- ����Ƽ
- ����
- �Ӽ�

## DDL
### ������ ����
- NUMERIC : ����, �Ǽ�
- CHARACTER(s)/CHAR(s) : ��������
- VARCHAR2(s)/VARCHAR(s) : ��������
- DATETIME : ��¥/�ð�

### CHAR VS VARCHAR
���� ����
- VARCHAR : ��������. �ʿ��� ������ ���� ������ ũ��. ���̰� �پ��� �÷�/���ǵ� ���̿� ���� ������ ���� ���̰� �ִ� �÷��� ����
- CHAR : ��������

�񱳹��
- CHAR : ������ ä���� ���ϴ� ���
  - ª�� �ʿ� ���� �߰��ؼ� 2�� �����Ͱ� ���� ���̰� �ǵ��� �ϰ� �տ��� �� ���ھ� ��. ���� ���鸸 �ٸ� ���ڿ��� ���ٰ� �Ǵ�
- VARCHAR : ���鵵 �� ���ڷ� ���. ���� ������ �ٸ��� �ٸ� ���ڷ� �Ǵ�

```
CHAR
'AA' = 'AA  ' => TRUE

VARCHAR 
'AA' = 'AA  ' => FALSE
```

### CREATE TABLE
���ǻ���
- ���̺� �� : ��ü�� �ǹ��� �� �ִ� �ܼ��� �ǰ�. �ٸ� ���̺��� �ߺ�X
- �� ���̺� �� �÷��� �ߺ� �Ұ�, �÷����� ,�� ����
- �������� ����� ��� �Ұ�
- A-Z, a-z, 0-9, _, $, # ���ڸ� ���
- ��ҹ��� ���� X

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
#### ���̺� ���� Ȯ��
- ORACLE : `DESCRIBE ���̺��`
- SQL server : `exec sp_help 'dbo.���̺��'`

#### ��������
- �⺻Ű(PRIMARY KEY) : ���̺� �����ϴ� �� ���� �� ���� �ǹ̷� Ư���� �� �ִ� �� �� �̻� �÷�
- ����Ű(UNIQUE KEY) : �����ϰ� �ĺ� ���� ����Ű, NULL�� ���� �� ���� �� �־ OK
- �ܺ�Ű(FOREIGN KEY) : �ٸ� ���̺� �⺻Ű�� ���Ǵ� ���踦 �����ϴ� �÷�
- NULL : ���� ���ǵ��� ���� ������ ��
- DEFAULT : �⺻���� ������ ����. ������ �������� ���� ��� ������ ���ǵ� �⺻�� �ڵ� �Էµ�

#### SELECT�� ���̺� ����
ORACLE    
```SQL
CREATE TABLE ~ AS SELECT ~
```

SQL SERVER
```SQL
SELECT * INTO TABLE1 FROM TABLE2
```
- ���� ���̺� �������� �� NOT NULL�� ���մ� ���̺� ����.
- �⺻Ű, ����Ű, �ܷ�Ű, CHECK ���� �ٸ� �������� �����


### ALTER TABLE
���̺� ���� ����. �÷� �߰�/����, �������� �߰�/���� �۾�
```SQL
ALTER TABLE PLAYER              -- ���̺� ����
ADD (ADDRESS VARCHAR(80));      -- ���̺� �߰�

--�÷� ����
ALTER TABLE PLAYER DROP COLUMN ADDRESS;

-- ORACLE �÷� ����
ALTER TABLE PLAYER MODIFY (ADDRESS VARCHAR2(80));
-- SQL �÷� ����
ALTER TABLE PLAYER ALTER COLUMN ADDRESS VARCHAR2(80);

-- ORACLE �÷��� ����
ALTER TABLE PLAYER RENAME COLUMN ADDRESS TO ADD
-- SQL �÷��� ����
sp_rename 'dbo.TEAM_TEMP.TEAM_ID', 'TEAM_TEMT_ID', 'COLUMN'

-- �������� ����
ALTER TABLE PLAYER DROP CONSTRAINT PLAYER_FK;

-- �������� �߰�
ALTER TABLE PLAYER ADD CONSTRAINT PLAYER_FK FOREIGN KEY(TEAM_ID) REFERENCES TEAM(TEAM_ID);

-- ORACLE ���̺�� ����
RENAME TABLE_BEFORE TO TABLE_AFTER;
--SQL ���̺�� ����
sp_rename TABLE_BEFORE, TABLE_AFTER;

-- ���̺� ����(�����־��� ���� �������ǵ� ����)
DROP TABLE PLAYER [CASCADE CONSTRAINT];

-- ���̺� ���� ������ä �����͸� ���� ����
TRUNCATE TABLE PLAYER;
```
MODIFY COLUMN
- �÷� ũ�� �Ð��� �ִµ� �������� ����
- �÷��� NULL�� ������ �ְų� ������ �ƹ��͵� ������ ���� �� ����
- NULL�� ������ ������ ������ ���� ���� ����


`DELETE TABLE` VS `TRUNCATE TABLE`
- ���̺� ��ü ������ �����ϴ� ���, �ý��� Ȱ�� ���鿡�� �ý��� ���ϰ� ���� TRUNCATE TABLE �ǰ�
- ��, TRUNCATE TABLE�� �������� ���� �Ұ���

## DML
�ڷ�� ��ȸ, �Է�, ����, ����(SELECT, INSERT, UPDATE, DELETE)   
�ǽð����� ���̺� ������ ��ġ�� �ʰ� COMMIT�� �̿��� TRANSACTION �����ؾ߸� ���� ���̺� �ݿ���(DDL�� AUTO COMMIT��)

```SQL
SELECT PLAYER_ID [ALL/DISTINCT] FROM PLAYER;
```
- ALL�� ����Ʈ.
- DISTINCT : �ߺ��� ������ 1������ ó���ؼ� ���
- WILDCARD : �ش� ���̺� ��� �÷� ���� ��ȸ�ϰ� ���� �� `*`
- ALIAS : �÷��� �ڿ� ��ġ. AS, as Ű����� ��� ����.
```SQL
INSERT INTO PLAYER(PLAYER_ID, PLAYER_NAME) VALUES ('200207', '������');
UPDATE PLAYER SET POSITION = 'MF';
DELETE FROM PLAYER;
```

### ��������ڿ� �ռ�������
���������
- NUMBER, DATE �ڷ����� �����.
- `()`, `*`, `/`, `+`, `-` �켱����

�ռ�(CONCATENTANION)������
- ���ڿ� ���� ����
  - ORACLE : `||`
  - SQL SERVER : `+`
  - ���� : `CONCAT(str1, str2)`

## TCL
COMMIT, ROLLBACK, SAVEPOINT.   
DML�� ���� ���۵��� ����� �۾�����(Ʈ�����)���� �����ϴ� ���
#### Ʈ������� Ư��
- ���ڼ�(automicity) : Ʈ����� ���ǵ� ����� ��� ���������� ����Ǵ���, ���� ������� ����ä �����ִ���(all or nothing)
- �ϰ���(consistency) : Ʈ����� �� DB ���� �߸��Ǿ� ���� �ʴٸ� Ʈ����� ���� ���Ŀ��� DB ���� �߸��Ǿ� ������ �ȵ�
- ����(isolation) : Ʈ����� ���� ���� �ٸ� Ʈ����� ����޾� �߸��� ��� ����� �ȵ�
- ���Ӽ�(durabilty) : Ʈ����� ���������� ����Ǹ� ������ DB ���� ���� ����

#### COMMIT, ROLLBACK ȿ��
������ ���Ἲ ����, ������ ���� �� ������ ������� Ȯ�� ����. ���� ������ �۾� �׷����ؼ� ó�� ����
- COMMIT ����Ʈ
  - ORACLE : NOT AUTO COMMIT
  - SQL SERVER : AUTO COMMIT

### SQL SERVER Ʈ����� 3���� ���
- AUTO COMMIT : ��ɾ� ���������� ���� -> AUTO COMMIT, ���� �߻� -> ROLLBACK
- �Ͻ��� Ʈ����� : ORACLE�� ���� ���. Ʈ����� ���� ����ڰ� ��������� COMMIT, ROLLBACK ó��
- ����� Ʈ����� : Ʈ����� ����/���� ����ڰ� ����. BEGIN TARSACTION(BEGIN TRAN)���� Ʈ����� ����


### SAVE POINT
SAVE POINT �����ϸ� ROLLBACK �� SAVEPOINT���� Ʈ����� �Ϻθ� �ѹ鰡��
```SQL
SAVEPOINT SVPT1;
ROLLBACK TO SVPT1;

SAVE TRANSACTION SVTR1;
ROLLBACK TRANSATION SVTR1;
```
## WHERE ��
### ������
- �� ������ : `=`, `>`, `>=`, `<`, `<=`
- SQL ������
  - `BETWEEN A AND B` : A, B ��θ� �����ϴ� ����
  - `IN(LIST)` : ����Ʈ �� �� ��� �ϳ��� ��ġ�ϸ� ��
  - `LIKE '�񱳹��ڿ�'` : �� ���ڿ��� ������ ��ġ�ϸ� ��
    - `%` : 0�� �̻� � ����
    - `_` : 1���� ���� ����
    - `WHERE PLAYER_NAME LIKE '_A%'` : ���� ���� �̸� �ι�° ���ڰ� A�� ������ �̸�
  - `IS NULL`
- �� ������ : `AND`, `OR`, `NOT`
- ���� ������ : `!=`, `^=`, `<>`, `NOT BETWEEN a AND b`, `NOT IN (LIST)`, `IS NOT NULL`

#### ������ �켱����
`()` -> NOT ������ -> ��, SQL �� ������ -> `AND` -> `OR`


### �Լ�
### �����Լ�
- ������ : ������ �Լ�, ������ �Լ�, ��¥�� �Լ�, ��ȯ�� �Լ�, NULL �����Լ�
- ������ : �����Լ�, �׷��Լ�, �������Լ�

### ������ �Լ��� ����
#### ������ �Լ�
- `LOWER`, `UPPER`, `SUBSTR`
- `SUBSTRING`, `LENGTH`
- `LEN`, `LTRIM`, `RTRIM`, `TRIM`, `ASCII`, `CONCAT`

### ������ �Լ�
- `ABS`, `MOD`, `ROUND`, `SIGN`, `CHR`
- `CHAR`, `CEIL`
- `CEILING`, `FLOOR`, `EXP`, `LOG`, `LN`, `POWER`, `SIN`, `COS`, `TAN`

CEIL/CELING VS FLOOR
- `CEIL` / `CEILING` : ���ں��� ũ�ų� ���� �ּ� ���� ����
  - `CEIL(38.123)` `CEILING(38.123)` => 39 
  - `CEILING(-38.123)` => -38 
- `FLOOR` : ���ں��� �۰ų� ���� �ִ� ���� ����
  - `FLOOR(38.123)` => 38
  - `FLOOR(-38.123)` => -39

### ��ȯ�� �Լ�
�Ͻ��� ������ ���� ��ȯ(���ڰ� ���ڷ� ������)

### NULL ���� �Լ�
- `NVL(ǥ����1, ǥ����2)` `ISNULL(ǥ����1, ǥ����2)` : ǥ���� 1�� �ƴϸ� ǥ���� 2�� ��� 
- `NULLIF(ǥ����1, ǥ����2)` : ǥ���� 1���� ǥ���� 2�� ������ NULL, ���� ������ ǥ���� 1�� ���
- `COALESCE(ǥ����1, ǥ����2, ...)` : ������ ���� ǥ���Ŀ��� NULL�� �ƴ� ������ ǥ���� ��Ÿ��. ��� ǥ������ NULL�̸� NULL ����

`IS NULL` `IS NOT NULL` �� NULL ���� �Լ��� �ƴ� ��������


## Group By, Having��

## Order By��

## JOIN