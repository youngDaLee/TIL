# Real MongoDB - ch04. 샤딩
- Sharding : 데이터를 여러 서버에 분산하여 저장, 처리할 수 있도록 하는 기술

- Replication : 고가용성을 위한 솔루션
- Sharding : 분산 처리를 위한 솔루션

Sharding을 위해 필요한 서버

- MongoC (config서버)
- MongoS (Router서버)
- MongoD (DB 서버)

## 4.1 샤딩이란?

---

스케일 업을 통한 서버 처리 용량은 한계가 있음.

따라서 스케일 아웃을 통해 처리 용량을 선형적으로 늘려갈 필요가 있다.

### 4.1.1 샤딩의 필요성

접속하는 사용자가 늘어날수록, 서버쪽에서는 늘어난 요청 많큼을 처리할 수 있어야 한다.

웹 서버의 경우, 서버를 늘려준 뒤 로드밸런싱을 통해 비교적 손쉽게 서버를 확장하여 이러한 문제를 해결할 수 있다.

다만 DB 서버는 필요한 데이터를 영구적으로 가지고 있어야 하기 때문에, 단순 서버 투입으로 확장 불가능하다.

DB서버를 확장하기 위해서는 DB 데이터가 여러 서버로 분산될 수 있도록 미리 응용 프로그램을 개발해야 하는데, 이를 **샤딩**이라 한다

- 스케일 업을 통해 서버 사양을 늘리는 방법도 있기는 하지만, 어느 이상이 되면, 투자 대비 성능이 향상되지 않고, 비용도 크게 든다는 단점이 있다.
- RDBMS에서 저장된 데이터를 서비스 영향 없이 샤딩 규칙에 따라 데이터를 분산시키는 것은 어려운 작업니다. 따라서 처음부터 샤딩을 적용할지에 대한 고려사항은 피할 수 없는 설계 과정이다

### 4.1.2 샤딩의 종류

수직(Horizontal) 샤딩

- 컬렉션을 그룹핑하여, 그룹별로 샤드를 할당하는 방식
- 구현이 간단, 응용프로그램 변화 최소화 가능
- 간단한 샤딩이 필요한 경우 사용
- 컬렉션 별 쿼리 사용량이 같다는 보장이 없기 때문에 샤드간 불균형 자주 발생

수평(Vertical) 샤딩

- 하나의 컬렉션에 저장된 도큐먼트를 파티셔닝해서 각 샤드가 나눠갖는 방식
- 파티셔닝 기준 컬럼(샤드키) 선정이 매우 중요함.
- 샤트키에 따라 샤드간 부하가 균등할 수 도 있고, 그렇지 않을 수도 있음

MongoDB에서는 컬렉션에 대해 샤딩을 활성화 하지 않으면 자동으로 수직샤딩이 구현됨(primary shard)

샤딩을 활성화 하면, 해당 컬렉션은 수평샤딩이 적용됨

## 4.2 MongoDB 샤딩 아키텍쳐

---

- MongoS (Router)
    - 1개 이상 존재 가능(레플리카셋X)
- MongoC (config)
    - 1개 이상 레플리카셋 구현 가능
- MongoD (DB)
    - 1개 이상 레플리카셋 구현 가능

### 4.2.1 샤드 클러스터 컴포넌트

MongoS

- 데이터를 가지지 않음
- 사용자의 쿼리요청을 어느 샤드로 전달할지 정하고, 각 샤드로부터 받은 데이터를 사용자에게 리턴하는 역할

MongoC

- MongoD에 저장된 데이터가 어떻게 스플릿되어 분산되어 있는지에 대한 메타정보가 저장되어 있는 서버
- 손실될 경우 치명적인 문제가 발생할 수 있으므로 레플리카셋(PSS) 구조로 구성할 것을 권장함
    - PSS 구성하지 않을 시 Warning 발생

MongoD

- 실제 데이터가 저장된 DB 서버
- = 샤드 서버

### 4.2.2 샤드 클러스터의 쿼리 수행 절차(MongoS, MongoC 통신)

MongoC는 샤딩이 활성화된 DB, 컬렉션 정보를 관리함.

- DB, Collection 생성 시, 샤딩이 되어있지 않으면 MongoC가 아닌 각 MongoD 로컬에서 관리됨

MongoC는 각 컬렉션이 여러 샤드 서버로분산될 수 있도록 분산하기 위한 정보를 관리한다. 

샤딩이 활성화된 컬렉션은, 각 샤드로 분산될 수 있도록 데이터가 쪼개지는데, 이 데이터 조각을 MongoDB에서는 **청크(chunk)**라 한다.

MongoDB 서버에서 MonogS로 쿼리 요청 시 거치는 과정

1. 쿼리 컬렉션 정보를 MongoC에서 가져와 MongoS 메모리에 캐싱
2. 쿼리에서 샤딩 키 조건을 찾음
    1. 쿼리 조회 조건에 샤딩키가 있다면, 샤딩키 포함된 청크 정보를 1번의 캐시에서 검색해서 해당 샤드 서버로 쿼리를 직접 요청
    2. 쿼리 조회 조건에 샤딩키가 없으면 모든 샤드 서버로 쿼리 요청
3. 2번에서 전송한 결과에 대해 샤드로부터 응답이 오면 결과 병합해서 사용자에게 쿼리 반환

→ 1번 과정을 매번 거치는 것이아닌, MongoS에 해당 쿼리 컬렉션에 대한 청크 정보가 캐싱되어 있지 않거나, 너무 오래된 정보일 경우에만 1번 과정을 거침

### 4.2.3 컨피그 서버(MongoC)

샤딩된 클러스터를 운영하기 위한 모든 정보를 저장함.

MongoC 정보는 MongoC에 직접 접속해서 확인 할 수도 있지만, MonogS의 config DB에서도 해당 내용을 조회 가능함

config DB는 다음과 같은 컬렉션을 가지고 있음

- database
- collections
- chunks
- shards
- mongos
- settings
- version
- lockpings
- locks
- changelogs

#### 4.2.3.1 databases

샤드 클러스터가 가지고 있는 데이터베이스 목록

| field | description |
| --- | --- |
| _id | DB명 |
| partitioned | 샤딩 여부(bool) |
| primary | 프라이머리 샤드 |

#### 4.2.3.2 collections

샤드 클러스터가 가지고 있는 콜렉션 목록

**샤딩된 콜렉션만** 관리됨.

| field | description |
| --- | --- |
| _id | DB명.콜렉션명 (ex: TEST.testcoll) |
| lastmod | 컬렉션 구조가 마지막으로 변경된 시점 |
| dropped | 삭제된 컬렉션인지 ⇒ drop을 수행해도 메타정보 같이 삭제되는 것이 아닌, 삭제되었다 마크만 됨. 삭제 후 동일한 이름의 컬렉션 재생성 시, 해당 도큐먼트에 덮어써짐 |
| key | 컬렉션의 샤드키 |
| unique | 샤드키가 유니크한지 |
| lastmodEpoch | lastmod를 MongoDB ObjectId 포맷으로 저장한 것 |

#### 4.2.3.3 chunks

샤딩된 컬렉션의 모든 청크 정보

| field | description |
| --- | --- |
| _id | chunks id DB명.collection명과 청크 가지는 값 볌위 정보 중 시작값을 포함해서 할당됨 |
| lastmod | 청크 정보가 마지막으로 변경된 시점 |
| lastmodEpoch | lastmod를 MongoDB ObjectId 포맷으로 저장한 것 |
| ns | 청크 컬렉션 네임스페이스(DB명.collection명) |
| min | 청크 시작 값. |
| max | 청크 종료값 ⇒ [min,max) 범위로 청크 저장됨 |
| shard | 청크가 현재 저정된 샤드명 |

#### 4.2.3.4 shards

샤드 클러스터 내 모든 샤드 서버 정보

| field | description |
| --- | --- |
| _id | 샤드 서버 레플리카셋 명 |
| host | 샤드 연결 정보(레플리카셋명/레플리카셋멤버목록)
ex: replSet/replinstance01:27017,replinstance02:27017,,replinstance03:27017, |
| tags | tag 기반 샤딩일 때 각 샤드 태그 목록 |

#### 4.2.3.5 mongos

샤드 클러스터 내 실행중인 라우터(mongos) 목록

- 각 MongoS는 30초 단위로 핑을 주고받는다.

mongos컬렉션에는 단 한번이라도 핑을 주고받았던 모든 mongos 목록이 저장되며, 라우터 인스턴스가 종료되거나 없어져도 삭제되지 않는다.

#### 4.2.3.6 settings

청크 밸런싱과 관련된 작업 설정이 저장됨

해당 컬렉션 도큐먼트를 변경하여 관련 설정 변경 가능(공식 명령이 있으면 공식 명령 사용)

기본적으로 아래 도큐먼트를 가질 수 있으며, 이 외의 _id값은 허용하지 않고, 들어가더라도 아무런 의미를 갖지 못한다

```jsx
{ "_id": "chunksize", "value": 64 }
{ "_id": "balancer", "stopped": false }
{ "_id": "autosplit", "enabled": true }
```

- `chunksize`  : 샤드 클러스터 기본 청크 크기. 디폴트는 64MB로, 필요에 따라 청크 사이즈를 늘리거나 줄일 수 있음

```jsx
> db.settings.save({_id:"chunksize", value:128})
```

- `balancer` : 청크 밸런싱 활성화 여부. 활성화 여부 뿐만 아니라, 밸런싱 시간도 설정할 수 있다.

```jsx
mongos> sh.getBalancerState()  # 현재 밸런서가 작동중인지 확인
mongos> sh.isBalancerRunning() # 현재 밸런서가 청크이동 실행중인지 확인
mongos> sh.setBalancerState(true)  # 밸런서 활성화
mongos> sh.setBalancerState(false)  # 밸런서 비활성화

# 밸런싱 시간 설정
mongos> db.settings.update(
{ _id: "balancer"},
{ $set: { activeWindow : { start : "19:00", stop : "20:30"}}},
{ upsert: true}
)

mongos> sh.enableAutoSplit(true)  # 청크 크기 넘어갔을 때 자동 스플릿 활성화
mongos> sh.disableAutoSplit(false)  # 청크 크기 넘어갔을 때 자동 스플릿 비활성화
```

#### 4.2.3.7 version

컨피그 서버가 가지고 있느 샤드 클러스터 메타데이터 전체의 버전 정보

샤드 클러스터 청크, 컬렉션, DB 정보 등이 변경될 때 마다 메타정보도 함께 변경되는데, 메타 정보는 샤드 클러스터 모든 멤버가 동기화 되어야 함.

클러스터의 모든 멤버가 자신의 데이터가 최신인지 여부를 판단하기 위해 정보 변경 될 때 마다 버전 증가시킴. version 컬렉션은 메타 데이터의 최신 데이터를 저장함.

- 사용할 일 거의 없는 컬렉션

#### 4.2.3.8 lockpings

서버 연결 상태 확인

#### 4.2.3.9 locks

각 멤버들이 동일한 작업을 동시에 시작하며 충돌이 될 수 있다.

locks 컬렉션을 이용해서 이러한 충돌을 막아준다.

+) **3.6 버전 부터는 밸런서가 lock을 사용하지 않는다.**

- https://www.mongodb.com/docs/manual/reference/config-database/

책에서 설명한 예는 아래와 같다

```jsx
{
   "_id" : "balancer",  // 락을 획득한 작업
   "state" : 2,  // 현재 잠금 상태
   "ts" : ObjectId("5be0bc6cb20effa83b15baa8"),  // 잠금 획득/해제한 시각
   "who" : "ConfigServer:Balancer",  // 잠금획득한 클라이언트 프로세스 정보 + 포트 정보 + 스레드 정보
   "process" : "ConfigServer",  // 잠금 획득한 클라이언트 프로세스 정보
   "when" : ISODate("2018-11-05T21:56:13.096Z"),  // ~3.2 : 잠금 획득/해제된 시간 ~3.4 : 컨피그 프라이머리가 언제 선출되었는지
   "why" : "CSRS Balancer"  // 잠금 획득한 이유
}
```

- balancer 락은 더이상 이루어지지 않기 때문에 3.6 부터는_id:balancer에 대한 내용은 삭제됨

잘 이해가 가지 않는 부분… 일단 지금은 MongoS - MongoC 간 데이터 통신 동기화를 위한 분산락을 저장하는 개념으로 이해함.

컬렉션 분할/이관 등의 작업이 이루어질 때 특정 MongoS에서 분산락을 잡고 진행 → 이 때 분산락에 대한 정보를 locks컬렉션에 저장.

- http://mongodb.citsoft.net/?page_id=256

#### 4.2.3.10 changelog

MongoC 메타정보 변경 이벤트에 대한 이력을 관리.

대표적으로 DB/collection 생성 및 삭제, collection chunk 이동/스플릿 된 경우가 저장됨

기본 10M cap컬렉션으로, 오래된 로그는 자동 삭제됨

```jsx
{
 "_id" : "<hostname>-<timestamp>-<increment>",  // 어떤 멤버가 어떤 시간에 발생한 이벤트인지 식별
 "server" : "<hostname><:port>",  // 이벤트 대상 데이터 서버
 "clientAddr" : "127.0.0.1:63381",  // 이벤트 발생시킨 클라이언트 주소(config 변경을 라우터가 일으키므로, 라우터 서버정보가 저장됨)
 "time" : ISODate("2012-12-11T14:09:21.039Z"),  // 이벤트 발생 시간
 "what" : "split",  // 어떤 이벤트인지
 "ns" : "<database>.<collection>",  // 이벤트 대상 네임스페이스 정보
 "details" : {  // 이벤트 상세 내용
    "before" : {
       "min" : {
          "<database>" : { $minKey : 1 }
       },
       "max" : {
          "<database>" : { $maxKey : 1 }
       },
       "lastmod" : Timestamp(1000, 0),
       "lastmodEpoch" : ObjectId("000000000000000000000000")
    },
    "left" : {
       "min" : {
          "<database>" : { $minKey : 1 }
       },
       "max" : {
          "<database>" : "<value>"
       },
       "lastmod" : Timestamp(1000, 1),
       "lastmodEpoch" : ObjectId(<...>)
    },
    "right" : {
       "min" : {
          "<database>" : "<value>"
       },
       "max" : {
          "<database>" : { $maxKey : 1 }
       },
       "lastmod" : Timestamp(1000, 2),
       "lastmodEpoch" : ObjectId("<...>")
    },
    "owningShard" : "<value>"
 }
}
```

- `what`  이벤트 종류
    - dropCollection
    - dropCollection.start
    - dropDatabase
    - dropDatabase.start
    - moveChunk.start
    - moveChunk.commit
    - split
        - 수동 스플릿
    - multi-split
        - 자동 스플릿

### 4.2.4 컨피그 서버 복제 방식

MongoC 서버는 샤딩 활성화된 DB,Collection,Chunk에 대한 메타 정보를 가지고 있다.

이러한 메타정보는 매우 중요한 정보이기 때문에 MongoC 서버를 3대 이상의 레플리카셋(PSS) 구성을 권장한다

#### 4.2.4.1 SCCC(Sync Cluster Connection Config)

MongoDB 3.2 이전 버전까지 사용하던 미러링 방식의 컨피그 동기화 방법

→ 3.4 버전부터 사용 권장하지 않음. 이런게 있었구나~ 로 넘어가기

- 관계 없이 동작하는 3개의 Config 서버를 설치하고, Router에서 세 서버에 모두 접속하여 각 서버의 데이터를 동기화 하는 방식
- 라우터 서버가 청크 정보를 변경하고자 하면, 3개의 컨피그 서버에 접속해서 청크 정보를 업데이트 하는 문장을 각각 실행 → 작업 완료 시 커밋 수행하는 분산 트랜재셩(2-Phase Commit) 실행

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/031ad5d8-ffee-4cbe-902d-a9d19340a3ad/Untitled.png)

- 컨피그 서버 데이터 복잡해지고 변경 쿼리 복잡해질수록 구현이 어려워져 컨피그 서버간 동기화 문제를 자주 유발함

예시) 잠금 테이블 동기화 하지 못해 스플릿/밸런싱을 수행하지 못하는 상황

해결 방법 : 정상적으로 작동하는 컨피그 서버 데이터를 덤프하여 비정상 컨피그 서버로 적재(수동 동기화)

```jsx
conf> use config
conf> db.runCommand("dbhash")
```

- dbhasㅗ 값 비교해서 데이터 동일한지 확인

SCCC 에서 동기화 문제 일으키는 주원인 : locks, lockpings (라우터간 동기화 위한 잠금 컬렉션)

- 밸런서 멈췄다가 다시 실행 시 밸런서 정상 작동하는지 확인 필요

#### 4.2.4.2 CSRS(Config Server as Replica Sets)

3.4 부터 MongoC를 레플리카셋으로 구현할 수 있도록 개선됨

MongoC 레플리카셋은 아래 조건을 만족해야 함

- MongoC 서버는 반드시 WiredTiger 스토리지 엔진을 사용해야 한다
- 레플리카셋은 아비터를 가질 수 없다
- 레플리카셋은 지연된 멤버를 가질 수 없다
- 최소 3개 이상의 멤버로 구성해야 한다(권장사항. 필수는 아님)

+) ReadConcern, WriteConcern은 majority로 설정해서 진행한다. (레플리카셋 프라이머리 장애 발생 시 롤백 데이터 발생하지 않도록 하기 위함)

## 4.2.5 컨피그 서버 가용성과 쿼리 실행

MongoC 서버를 3대 이상 권장하는 이유

- ReadConcer, WriteConcer을 “majority”로 설정하는데, 이는 과반수 이상의 레플리카셋 멤버에 접근 할 수 있어야 쿼리를 수행할 수 있다는 것을 의미함. → 2대면 한 대에 장애 발생했을 때 메타정보 조회/삭제가 불가해짐

MongoC 서버가 중요한 서버이긴 하지만 항상 필요한 서버는 아님

모든 명령은 MongoS를 통해 처리되고, MongoS는 처음 기동 될 때 MongoC의 메타정보를 일괄 로드해서 캐시메모리에 적재하고, 샤드 클러스터에 새 멤버가 추가되거나 삭제될 때, 컬렉션 생성/삭제, 청크 분리/이동 시점에만 MongoC에서 변경 쿼리를 실행

MongoC 데이터 변경하는 경우

- 청크 마이그레이션
- 청크 스플릿

MongoC 데이터 조회

- MongoS 재시작
- MonogC 메타데이터 변경된 경우
- 사용자 인증 처리

### 4.2.6 라우터(MongoS)

- 사용자 쿼리를 전달해야 할 샤드 서버(MongoD) 결정하고, 해당 샤드로 쿼리 전송
    - 만약 쿼리가 특정 샤드로만 쿼리해도 되는경우(샤딩되지 않은 컬렉션에 대해 쿼리하는 경우) 나머지 샤드로는 쿼리 요청을 하지 않음 → 샤드 서버가 꼭 필요한 일만 처리하도록 함
- 샤드 서버(MongoD)로 부터 반환된 결과 조합해서 사용자에 전달
    - 각 샤드가 내려준 결과가, 실제 해당 MongoD가 가지지 말아야 할 데이터인지 판단하고, 가지지 말아야 할 데이터라면 해당 데이터를 제거하는 작업을 수행
        - shard2에 소속되어야 할 chunk가 shard1에서 리턴된 경우 (청크 마이그레이션 중 이거나, 마이그레이션 도중 실패했거나, 사용자가 MongoD에 직접 접속하여 강제로 샤드키에 맞지 않는 데이터 저장하거나)
        - 중복된 데이터나 삭제된 데이터가 리턴될 수도 있음
        - 따라서 라우터의 필터링 기능(데이터판단,삭제)은 매우 중요
    - Limit 옵션만 있을 때 : 각 샤드에 똑같이 limit 옵션을 전달, 샤드로부터 받은 결과에 대해 다시 limit 처리 해서 사용자에게 반환
    - skip 옵션만 있을 때 : skip 옵션 제거해서 샤드에 전달, 샤드 서버로부터 받은 결과 병합 후 skip 적용해서 필요한만큼 도큐먼트 버리고 반환
- 샤드간 청크 밸런싱/청크 스플릿 수행

### 4.2.7 라우터의 쿼리 분산

쿼리가 샤드키를 가지고 있는지에 따라 쿼리 요청 서버가 달라짐

- 타겟 쿼리 : 쿼리를 특정 샤드로만 전달
    - 효율적
- 브로드캐스트 쿼리 : 모든 샤드로 요청
    - 비효율적

#### 4.2.7.1 타겟 쿼리(Traget Query)

샤드키의 선행키가 조건으로 주어진 경우

- 범위 조건, IN 조건 제약 없음

#### 4.2.7.2 브로드캐스트 쿼리(Broadcast Query)

샤드키를 쿼리 조건으로 가지지 않는 경우 → 모든 샤드로 쿼리를 요청

특정 쿼리는 샤드 키 여부과 관계 없이 항상 브로드캐스트로 처리함

- 다중 업데이트(Multi-Update)
    - 샤드키 포함 여부과 관련 없이 항상 브로드캐스트 쿼리로 실행
- UpdateMany(), DeleteMany()
    - 업데이트 대상 검색조건이 샤드키를 모두 포함하는 경우에만 타겟쿼리로 실행
    - 샤드 키 구성하는 모든 필드가 조건으로 사용되어야만 타겟쿼리 실행 가능

### 4.2.8 라우터 배포

MongoD, MongoC는 전용 서버 할당해서 다른 프로세스 간섭 피하도록 함 

MongoS는 전용 서버에서 실행할만큼 중요성을 가지지않음

#### 4.2.8.1 응용프로그램 서버와 함께 배포

- App 서버에 MongoS를 함께 배포하는 방법(가장 일반적)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e2b77ab3-3af7-4d58-a386-2c0085057dbe/Untitled.png)

- 각 앱은 localhost:27017을 호출해서 샤드를 호출함
- 이런 형태 배포에서는 라우터에 대한 고가용성(HA)은 고민거리가 아니기 때문에 선택할 수 있는 방법
    - 특정 앱서버에 문제가 생기면, 해당 서버에서 실행중인 앱과 MongoDB 라우터만 멈추고, 나머지는 이슈 없이 요청 처리함

장점

- 라우터가 같은 서버에 위치하므로 네트워크 레이턴시(round-trip 시간) 최소화
- MongoDB 메뉴얼에서 권장하는 일반적인 방법

단점

- 앱 서버 늘어날수록 커넥션 늘어나게 됨
- 앱 서버에서 MongoS만 응답 불가 상태인 경우, 앱 서버는 문제가 없기 때문에 사용자 요청을 받지만 실제 DB 처리는 하나도 못 하는 상태가 됨.
    - 앱서버 MongoDB 라우터 응답불능 되면 앱서버 자체를 셧다운 시키거나 사용자 요청 처리 못하도록 막는 방법

#### 4.2.8.2 전용 라우터 서버 배포

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/47b98827-fa3a-4aed-afa9-afa05f610a54/Untitled.png)

앱서버와 무관하게 MongoS 전용 서버를 구성, 각 앱서버가 하나이상의 MongoS 서버와 통신하게 함

장점

- 커넥션 개수 줄어든다

단점

- MongoDB권장이 아님
- 라우터간 부하를 적절하게 분산해야 하고, 라우터 되살아났을 때 요청 다시 전달해야 함

#### 4.2.8.3 L4와 함께 라우터 배포

MongoDB 라우터 서버를 L4스위치로 묶어 사용

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7a73c4d5-b685-4811-acda-0f02caee18d0/Untitled.png)

장점

- 커넥션 시 모든 라우터 서버를 명시하지 않아도 됨

단점

- 네트워크 왕복시간(round-trip) 길게 만든다
- find 쿼리와, 후속 GetMore 명령이 서로 다른 라우터로 요청되는 경우 발생

#### 4.2.8.4 샤드 서버나 컨피그 서버와 함께 라우터 배포

### 4.2.9 커넥션 풀 관리

MongoS는 클라이언트(MongoDB 드라이버)와 MongoDB 샤드 서버(MongoD)를 중계하는 역할을 함 → 클라이언트와 서버쪽 커넥션을 모두 가지고 있어야 함.

클라이언트 커넥션이 서버 커넥션에 영향 미치지 않고 독립적으로 관리되기 때문에 커넥션 제어 쉽지 않음

#### 4.2.9.1 MongoDB 클라이언트

단일 서버 접속

```jsx
ServerAddress server = new ServerAddress("mongodb-0.com", 27017);
MongoClient mongoClient = new MongoClient(server);
```

- 주어진 서버로만 접속

레플리카셋 접속

```java
// 레플리카셋 시드리스트
List<ServerAddress> seedList = new ArrayList<ServerAddress>();
seedList.add(new ServerAddress("mongodb-0.com", 27017));
seedList.add(new ServerAddress("mongodb-1.com", 27017));

// 인증정보
List<MongoCredential> credentials = new ArrayList<MongoCredential>();
credentials.add(MongoCredential.createScramSha1Credential(username, DEFAULT_DB, passwd.toCharArray());

// 접속 옵션
MongoClientOptions options = MongoClientOptions.builder().requeiredReplicaSetName(ReplSetName).build();

MongoClient client = new MongoClient(seedList, credentials, options);
```

- `requeiredReplicaSetName` 이 반드시 포함되어야 함(레플리카셋 다른 멤버까지 찾아 접속을 맺어야 하기 때문)

라우터 접속

```java
// 레플리카셋 시드리스트
List<ServerAddress> seedList = new ArrayList<ServerAddress>();
seedList.add(new ServerAddress("mongodb-0.com", 27017));
seedList.add(new ServerAddress("mongodb-1.com", 27017));

// 인증정보
List<MongoCredential> credentials = new ArrayList<MongoCredential>();
credentials.add(MongoCredential.createScramSha1Credential(username, DEFAULT_DB, passwd.toCharArray());

MongoClient client = new MongoClient(seedList, credentials, options);
```

#### 4.2.9.2 MongoDB 라우터 - MongoDB 샤드 서버

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7ef52b4-6f7a-4d7f-b772-89295aef692d/Untitled.png)

- 초기 커넥션 수 100개로 설정해도, 샤드서버간의 연결은 100개까지 생성되지 않고 10개 정도만 생성됨
- MongoS는 클라이언트 요청 쿼리 처리를 위해, TaskExecutorPool을 CPU 코어 수 만큼 준비함(TaskExecutorPool = Thread Pool)
- TaskExecutorPool은 MongoD 서버와의 연결 정보를 가진 Connection Pool을 하나씩 가짐
- Connection Pool은 내부적으로 Sub-ConnectionPool을 가짐
    - SubConnectionPool은 샤드 서버(샤드 레플리카셋? 아니면 MongoD?) 하나 당 하나씩 생성됨
    - Sub-ConnectionPool = Specific Pool

TaskExecutionPool개수를 지정하고자 한다면, 컨피그 파일을 아래와 같이 수정

```java
setParameter:
	taskExecutorPoolSize: 5
```

- MongoDB 라우터가 전용 서버에서 사용되면 그대로 사용하는게 좋지만, 다른 응용프로그램과 같이 실행되어 응용프로그램에서 CPU 사용이 예상되면 조정 필요

SpecificPool

- minConnections, maxConnections, hostTimeout 옵션으로 커넥션 풀 결정
    - hostTimeout 시간동안 쿼리가 실행되지 않으면 자동으로 커넥션을 끊어버림

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/871d1fce-4679-4fb2-9d36-df8c8fd3d7e7/Untitled.png)

- 벤치마킹(스트레스 테스트)
- 히든 투입

- 아무 요청 없을시 100개 정도의 커넥션을 유지
- 쿼리 유입 되는 순간 스파이크 발생
    - A-B 사이의 스파이크 : 초기 커넥션이 적어 쿼리 요청 대기상태에서, 커넥션 새로 만들어져 소모되고, 이로 인해 커넥션이 급작스럽게 많이 만들어져 스파이크 되는것
- 이후 커넥션 안정상태 도입됨
- 이런 현상 막으려면, 라우터와 샤드 간 커넥션을 미리 생성해두어야 함 → 5분 지나면 끊어져버리니….

Mongo3.4 부터 라우터와 샤드 간 커넥션 조정 옵션이 추가됨

- 그래도 워밍업 이슈는 있기 때문에

### 4.2.10 백업 복구 시 주의사항

샤딩 적용된 클러스터 멤버에서 백업된 데이터 복구 시 주의사항

- LVM과 같은 스냅샷 도구로 데이터 파일 복구하는 경우(물리 복원) 복구된 mongodb 서버는 백업 전 MongoC로 접속해서 샤딩 구성 복구하려고 함
- 기존 멤버 대체하기 위해 복구하는 경우면 문제 없음
- 이미 없어진 클러스터거나 MongoC 변경되었으면, 물리복원된 MongoD 시작되지 못하고 기존 MongoC응답을 기다림

시작 시 `recoverShardingState` 옵션 사용해서 기존 컨피그 응답 무한으로 대기하는 현상 회피

- MongoDB 3.4 이상부터는 없어진 옵션 : 대신 시작 시 레플리케이션 옵션 명시하지 않으면, MongoC 서버 접속 및 클러스터 구성 복구 작업을 건너뜀



### 4.3.2 레인지 샤딩

샤드 키 값을 기준으로 범위를 나누고, 사용자 데이터가 어느 청크에 포함될지 결정한느 샤딩 알고리즘

```java
["D", "J")
```

- MongoDB 샤드키값은 MinKey보다 작을 수 없고, MaxKey보다 클 수 없다.
    - MinKey, MaxKey는 존재하는 값이 아닌 가상의 최소 최댓값이다.
- 샤드 키 값은 별도의 변형 과정을 거치지 않고 그 자체로 정렬되어서 청크에 범위가 결정되ㅁ.
- 레인지 샤딩은 청크가 어떤 범위의 값을 가지는지만 결정함
- 밸런서는 각 샤드 서버가 가진 청크 개수만으로 균등하게 분산되었는지 관리한다. 즉, MongoDB 밸런서는 쿼리 요청이 많거나 부하가 높은 청크를 고려해서 샤드별로 청크를 분산하는 것 까지는 고려하지 않는다.
- 따라서 하나의 샤드가 너무 커져 점보청크가 발생할 수 있고, 점보청크는 스플릿/청크 마이그레이션 등의 관리 작업을 포기하게 된다
- 샤드 키 값이 아주 균등하게 분산되지 않은 이상 언젠가는 청크/샤드 간 데이터 불균형이 발생한다.
- 따라서 해시 샤딩을 사용할 수 없는 경우 레인지 샤딩을 사용해야 한다

### 4.3.3 해시샤딩

- 샤드 키 값을 그대로 청크 할당하는 것이 아닌, 샤드키의 해시값을 이용해서 청크를 할당하는 방식이다
- 몽고DB에서는 MD5 해시함수를 사용한다

레인지 샤딩 단점을 제거

- 샤드 키 값이 특정 범위에 집중되었을 때의 데이터 불균형
- 연속된 샤드키 액세스로 인한 특정 샤드 서버 부하 편중

레인지 샤딩에 비해 갖는 제약사항

- 범위검색 쿼리는 브로드캐스트 쿼리로 실행됨
- 샤드 키 필드에 대해 해시 인덱스를 생성해야 함

해시인덱스의 제약사항

- 단일 필드에 대해서만 해시 인덱스 생성 가능(복합 인덱스에서 해시 인덱스 생성 불가)

```java
> db.user.insert({
	name:"matt",
	country: "korea",
	composite_field: {name:"matt",country:"korea"},
	email:"mat@mat.com"
})

// 불가
> db.user.createIndex({name:"hashed", country:"hashed"})

// 가능
> db.user.createIndex({composite_field:"hashed"})
```

- 멀티 키 필드에 대해서는 해시 인덱스 생성 불가
- 부동 소수점 필드는 소수점 이하를 버리고 해시 함수 수행
- 2^53보다 큰 부동 소수점에 대해서는 해시 인덱스 지원하지 않음

### 4.3.4 지역 기반 샤딩(Zone Sharding)

- MongoDB 3.2 까지는 태그 기반 샤딩(Tag-Awared Sharding) 이라 명명. 3.4 버전부터 지역기반 샤딩(Zone-Aware Sharding)으로 이름 변경 (목적은 동일. 이름만 변경)
- 레인지 샤딩이나 해시 샤딩처럼 독립적으로 사용할 수 있는 샤딩 방식이 아닌, 레인지 샤딩과 해시 샤딩과 함께 사용해야 하는 샤딩.
- 레인지, 해시 샤딩은 모든 데이터를 커버 가능해야 했지만, 지역 기반 샤딩은 선택적으로 적용할 수 있다.
    - 관심 대상 데이터에만 적용할 수 있기 때문에 단독 사용 불가능
- 가장 많이 사용되는 예시 : 글로벌 서비스 데이터 서버 분산
    - 지역 정보 필드를 추가하여, 지역 별로 각기 다른 샤드에 데이터 저장되도록 함
    - 특정 사용자 데이터를 지정된 샤드 서버로 구분해서 관리
    - 샤드 서버 클래스(샤드 서버의 처리 능력이나 저장공간)별로 저장할 데이터 구분)

샤드 별로 태그 할당

```tsx
> sh.addShardTag("shard-01", "KR")
> sh.addShardTag("shard-02", "KR")
> sh.addShardTag("shard-03", "US")
```

샤드 키 범위별로 태그 할당

```tsx
> sh.addTagRange("mysns.users", {user_id: MinKey}, {user_id: 300}, "KR")
> sh.addTagRange("mysns.users", {user_id:300}, {user_id: MaxKey}, "US")
```

- 샤드키 범위를 할당할 때, 반드시 연속되어야 하는 것은 아님.
- MinKey부터 MaxKey까지의 모든범위를 커버해야 하는 것도 아님
- 각 샤드 서버는 어떤 태그와도 연결되지 않을 수 있고, 1개 이상의 태그와 다중으로 맵팽 될 수도 있음

### 4.3.5 샤드키

MongoDB 샤딩에서 가장 중요한 것은 **샤드키, 샤딩 알고리즘**

- 샤드키가 중요한 이유 : 변경 불가
- 컬렉션 단위로 설정됨
- 샤드키의 특성
    - 샤드키가 설정된 컬렉션에 대해 샤드키를 재설정 하는 것은 불가능하다
    - 컬렉션의 샤드키가 되는 필드 값은 NULL이 올 수 없고, 변경 불가함
- 샤드키가 미치는 영향
    - 타겟쿼리와 브로드캐스트쿼리(쿼리 성능, 응답시간)
    - 각 샤드 서버 부하 분산
        - 청크간 도큐먼트 수가 불균형하게 분배될 수 있음.
        - MonogDB 클러스터는 청크 수로 데이터를 분산함. (각 청크의 도큐먼트 수나 특정 도큐먼트가 얼마나 빈번하게 읽히는지는 고려하지 않음)
    - 청크 밸런싱 작업
        - 청크 스프릿이 자주 일어나면 청크 밸런싱이 자주 일어남 → 청크 밸런싱은 부하가 큰 작업이기 때문에 최대한 지양해야 함
    

#### 4.3.5.1 타겟 쿼리와 브로드캐스트 쿼리 결정(쿼리 처리 성능과 응답시간)

- 무조건 타겟 쿼리가 좋고 브로드캐스트 쿼리가 나쁜건 아님
- 소량의 데이터를 빈번하게 읽는 경우는 가능하면 타겟쿼리를 유도하도록 샤드키를 설계해야 함.
    - 소량의 데이터를 읽는 과정에서 브로드캐스트 쿼리를 사용하게 된다면 서버가 받는 부담이 더 커짐
- 분석이나 통계용 MongoDB 서버에서 타겟쿼리로 작동한다면 각 샤드의 부하 불균형을 초래함. 5개 샤드 중 하나만 일하고 나머지 샤드는 노는 결과 발생… → 유입되는 쿼리가 모든 서버 사용하도록 설계해야함
    - (우리 기준) 오히려 이런경우 내부 쿼리용으로 서버 부하가 분산된다 하더라도 유저에게 영향을 끼치므로, 레플리카셋 중 하나의 서버를 히든으로 만들어놓고 라우터를 통하지 않고 해당 서버에 직접 쿼리해서 사용함(분산된 데이터는 서비스단에서 모아서 처리)

#### 4.3.5.2 각 샤드 서버의 부하 분산

- MongoDB는 샤드간의 균형을 **청크 개수로**만 판단함
- 실제 각 청크가 가진 도큐먼트 수나 도큐먼트가 얼마나 빈번하게 읽히고 변경되는지는 고려 대상이 아님
- 샤드 키 선정값에 따라 각 샤드간 부하 차이가 아주 커질 수 있음.

#### 4.3.5.3 청크 밸런스 작업

- 만약에 user_id를 샤드키로 잡고, 인서트 되는 데이터는 점점 증가하는 데이터 일 경우 → 데이터가 증가할 때 마다 항상 가장 마지막 샤드에 데이터가 저장됨 → 청크 크기보다 커졌을 시 스플릿 됨 → 해당 샤드에 청크가 몰려 **밸런싱 작업 발생 ⇒ 성능 악영향**
- find 뿐만 아니라 insert도 여러 샤드와 청크로 골고루 분산되어서 저장될 수 있게 해야 함. → 그래야 청크가 스플릿(논리작업) 되어도 청크 밸런싱 작업(물리작업)이 최소화됨


## 4.4 프라이머리 샤드

샤드 클러스터의 모든 DB는 프라이머리샤드(primary shard)를 가짐

프라이머리 샤드 : 샤딩되지 않은 컬렉션을 저장하는 샤드

```tsx
> use config
> db.database.find()
```

- 처음 DB가 생성될 때 각 샤드 중 가장 데이터를 적게 가진 샤드를 선택해서 프라이머리로 선택함
- 프라이머리 샤드는 다른 샤드로 옮겨질 수 있음

```tsx
> db.runCommand( { movePrimary: "mysns", to: "shard-01" } )
```

primary 샤드 이동 이후 라우터에게 프라이머리 샤드 변경되었다는 사실을 알려주는 방법

- router 재시작
- router에서 `flushRouterConfig` 명령 실행
    - 샤딩된 모든 컬렉션 메타정보를 갱신함
    - 컨피그 서버 부하가 높아질 수도 있음

프라이머리 샤드를 변경하는 작업은 서비스에 영향을 많이 미치는 작업임.
