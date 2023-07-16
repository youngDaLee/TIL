# ch06. 잠금과 트랜잭션

## 6.1 잠금
- ~ MongoDB 2.6(MMAP만 사용)
    - 서버 엔진과 스토리지 엔진 구분이 없음.
    - 스토리지 엔진 잠금이 없이 MongoDB 서버 잠금(글로벌, DB 수준 락)
    - 공유 잠금(shared lock. S-Lock. 현재 스레드가 참조하고 있는 데이터를 다른 스레드가 변경하지 못하도록 하는것. 다른 스레드 s-lock과 호환됨-> 같은 데이터를 읽기만 하는 경우에는 여러 스레드가 동시에 읽을 수 있음), 배타적 잠금(exclusive lock. X-Lock. 데이터 변경 목적. 현재 스레드가 변경하는 데이터를 다른 데이터가 변경하지 못하도록 막는것 -> 변경중인 데이터를 다른 스레드가 읽지 못하게 함.)
- MongoDB 3.2~(WiredTiger)
    - 오브젝트에 대한 인텐션 잠금 도입
### 6.1.1 MongoDB 엔진의 잠금
- 명시적 잠금(프로그램을 통해 의도적으로 잠금을 실행하는 것)
    - 글로벌 잠금
- 묵시적 잠금(프로그램 코드 상에 명시적으로 지정하지 않아도 잠금이 발생하는 것)
    - 글로벌 잠금 외 모든 잠금
    - 쿼리가 실행될 때 자동으로 획득했다가 나중에 자동으로 해제되는 잠금

#### 6.1.1.1 글로벌 잠금
- 유일하게 명시적으로 사용할 수 있는 잠금
    - MongoDB에 단 하나만 있는 잠금
    - 인스턴스 잠금이라고도 함
- 3.4 버전에서 다른 잠금은 모두 묵시적으로 사용됨
    - 쿼리나 DB 변경 명령이 실행 될 때 잠금 획득했다가 필요 없는 시점에 자동으로 해제

글로벌 잠금(인스턴스 잠금)획득 방법
```tsx
> db.fsyncLock({fsync:1, lock:true})
```

- fsync 1로 설정 시, 디스크에 기록되지 못하고 메모리에만 기록된 데이터를 디스크로 플러시(기록)
- lock 옵션 true로 설정 시 글로벌 잠금 획득
    - false면 디스크 플러시만 하고 잠금 걸지 않음
- 쓰기 잠금이 아닌 읽기 잠금에 해당함 → 서버 데이터가 변경되는 것을 막는 용도의 잠금
    - 다른 커넥션 데이터 읽기를 막지 않음
- `db.currentOp()` 로 글로벌 잠금 상태 확인 가능
- 모든 커넥션의 데이터 저장/변경을 막음 → `db.fsyncLock()` 실행되는 커넥션에서도 저장/변경 불가능
    - 다른 커넥션의 경우 데이터 변경 명령이 불가능. 다른 읽기 처리도 불가능

```tsx
> db.user.find() //가능
> db.user.update({_id:1}, {$set: {score:19}}) // 불가
> db.user.fnid() //불가
```

- `db.fsyncUnlock()` 으로 해제
    - fsynckLock 커넥션을 닫지 않고 유지했다가, 그대로 fsyncUnlock 명령을 수행해야 함
    - 문제 없다고는 하지만 가능성이 있으므로 권장

#### 6.1.1.2 오브젝트 잠금

MMAPv1 스토리지 엔진은 컬렉션 수준의 잠금을 사용함. DML 문장이 많이 실행될수록 쿼리가 컬렉션을 사용할 수 있는 시간이 줄어들어 동시처리 성능이 떨어짐
- S잠금(SharedLock)
- X(Exclusive)
- Intention Lock
    - IS(Intent Shared Lock)
    - IX(Intent Exclusive Lock)

| 상호호환 | IS | IX | S | X |
| --- | --- | --- | --- | --- |
| IS | O | O | O | X |
| IX | O | O | X | X |
| S | O | X | O | X |
| X | X | X | X | X |

### 6.1.2 WiredTiger 스토리지 엔진의 잠금
도큐먼트(레코드) 기반 잠금 사용.
- 글로벌(인스턴스 레벨)
- 인텐션(데이터베이스, 컬렉션 레벨)
    - DB, 컬렉션 레벨의 명령(컬렉션 생성 삭제, 인덱스 생성 삭제)와 도큐먼트 레벨 명령(도큐먼트 저장 및 변경)이 최적의 동시성을 유지하며 실행될 수 있게 함

MongoDB 계층 구조
- MongoDB 인스턴스(global) > DB > 컬렉션 > 도큐먼트

하위 오브젝트에 대해 잠금을 획득하려면 상위 계층 인텐션 잠금을 먼저 획득해야 함

특정 도큐먼트를 변경하는 과정(쓰기 잠금, Exclusive Lock을 획득해야 하는 상황)

1. 글로벌 인텍션 잠금(Gloval intention exclutive lock) 획득
2. 데이터베이스 인텐션 잠금(Database Intention Exclusive Lock) 획득
3. 컬렉션 인텐션 잠금(Collection Intention Exclusive Lock) 획득

컬렉션의 도큐먼트를 읽는 과정
- 마찬가지로 글로벌,데이터베이스,컬렉션 인텐션 잠금 획득
- 쓰기 시에는 쓰기 잠금 → 읽기 시에는 별도 잠금 획득하지 않음 : **MVCC(Multi Version Concurrency Control)**

### 6.1.3 잠금 Yield
- RDBMS : 쿼리 처리를 위해 한 번 잠금 획득하면 쿼리 처리 완료될 때 까지 잠금 해제하지 않음
- MongoDB : 트랜잭션보다 높은 동시성 처리가 우선순위. → 설정된 조건모다 오랜 시간 실행되거나 자원 많이 소모하면 쉬었다가 쿼리 재개
    - 쿼리 실행 도중 일정 규칙에 맞으면 쿼리를 처리하는 스레드는 가진 모든 잠금을 반납하고 일정 시간 sleep

yield 수행 조건
- 쿼리가 지정된 건수의 도큐먼트를 읽은 경우
- 쿼리가 지정된 시간 동안 수행된 경우

⇒ yield 기준 조회
```tsx
> db.runCommand({getParameter:'*'})
{
	...
	"internalQueryExecYieldIterations": 128,
	"internalQueryExecYieldPeriodMS": 10,
	...
}
```
- 3.2 부터 특정 시간동안 쉬는(yield) 형태가 아닌, 가지고 있던 잠금을 해제하고, 가지던 CPU 점유권을 놓고 다시 운영체제 스레드 스케줄을 기다리는 형태

### 6.1.4 잠금 진단

`db.currnetOp()`

| r | Intention Shared Lock |
| --- | --- |
| w | Intention Exclusive Lock |
| R | SharedLock |
| W | ExclusiveLock |

[MongoDB Lock (잠금) - RastaLion's IT Blog](https://rastalion.me/mongodb-lock-잠금/)

## 6.2 트랜잭션

~2.6 버전까지는 트랜잭션을 지원하지 않음(MMAPv1 은 트랜잭션과 관련된 부분이 거의 없음)

WiredTiger 엔진에서 제공하는 트랜잭션의 ACID(Atomicity, Consistency, Isolation, Durability) 특성

- 최고 레벨 격리 수준은 스냅샷
- 트랜잭션 커밋과 체크포인트 2가지 형태로 영속성(Durability) 보장
    - 트랜잭션 로그(리두로그, 저널로그) 뿐만 아니라 체크포인트로도 영속성이 보장됨
    - 하나의 트랜잭션이 변경할 수 있는 데이터 크기는 WT 스토리지 엔진이 가진 공유캐시 크기로 제한됨
- 커밋되지 않은 변경 데이터는 공유 캐시 크기보다 작아야 함

WT에서 READ-UNCOMMITTED, READ-COMMITTED, SNAPSHOT(REPETABLE-READ) 수준의 격리 수준을 제공하긴 하지만, 실제 WT엔진의 격리 수준을 선택해서 사용 할 수는 없음. → SNAPSHOT 레벨로 고정해서 초기화 하기 때문. 그렇다고 스냅샷 수준의 격리 수준을 100% 보장하지는 않음

### 6.2.1 쓰기 충돌(Write Conflict)

MongoDB는 데이터 변경 도중 Write Confilct가 발생할 수 있음

- 하나의 도큐먼트를 동시에 변경하려고 하는 상황

MongoDB 충돌 해결 방법

- 변경하고자 하는 도큐먼트가 다른 커넥션에 의해 잠금 걸려 있으면 즉시 업데이트 실행 취소
- Write Conflict Exception을 받은 세션이 같은 업데이트문을 재실행

동시에 여러 update가 발생하면 심각한 문제 → 쓰기 충돌과 재처리 과정의 반복 → CPU 부하

- `db.serverStatus()` 로 모니터링
- 컬렉션 모델 변경해서 write conflict를 최소화 하도록 노력하자~

### 6.2.2 단일 도큐먼트 트랜잭션

애초에 단일 도큐먼트의 트랜잭션만 지원함.

`db.user.insert({name:"dd", user_id:1})` 실행 시(named에 인덱스)

1. user collection INSERT
2. users({name:1}) index INSERT
3. OpLog Collection INSERT

위 세 과정을 하나의 트랜잭션으로 실행

- 리눅스 메모리 맵(MMAP)에서 제공하는 Shared Mapped, Private Mapped 메모리를 활용

### 6.2.3 문장의 트랜잭션 처리

- 여러 도큐먼트가 저장되는 배치 INSERT 등의 트랜잭션
    - 다 다른 트랜잭션으로 쪼개져서 실행함
    - 다중문장 트랜잭션을 기대하기 어려움