# Real MongoDB - ch01.MongoDB

### MongoDB 도입 배경
- MySQL과 같은 관계형데이터베이스(RDBMS)의 한계 -> 대용량 데이터를 전담하기에 비용 이슈
- HBase와 카산드라를 포함한 많은 NoSQL DBMS 솔루션이 도입됨. 대용량 데이터 분산처리에 취약한 RDBMS를 보완
- HBase, 카산드라는 단순 로그, 이력정보와 같은 단순한 대용량 데이터 저장용 DB
- MongoDB는 온라인 서비스를 위한 블록캐시, 보조인덱스, 동시성 처리를 위한 스킵리스트, 하자드 포인터오 ㅏ같은 특성을 가지고 있음

### MongoDB 특징
- 롤링 업그레이드(Rolling-Upgrade)
  - 서비스를 중지하지 않고 레플리카셋을 순차적으로 업그레이드
  - 하나의 레플리카셋에 최소 2개 이상의 버전 다른 멤버들이 공존 -> 더 낮은 버전으로 작동하도록 함(복제가 멈추지 않게 보호)
  - *높은 버전으로 동작할 수 있도록 하는 것 : setFeatureCompatibilityVersion
- NoSQL
- 스키마 프리(Schema-Free)
  - 사용할 컬럼을 미치 정의하지 않고 언제든지 필요한 시점에 데이터를 저장할 수 있음
- 비관계형 데이터베이스
- SQL을 사용하지 않고, 자바스크립트 기반 명령으러ㅗ 동작

### MongoDB vs RDBMS
| MongoDB | RDBMS |
|:-------:|:-----:|
|데이터베이스(Database)|데이터베이스(Database)|
|컬렉션(Collection)|테이블(Table)|
|도큐먼트(Document)|레코드(Record 또는 Row)|
|필드(Field)|컬럼(Column)|
|인덱스(Index)|인덱스(Index)|
|쿼리의 결과로 커서(Cursor)반환|쿼리의 결과로 레코드(Record)반환|

### MongoDB vs NoSQL(HBase)
- MongoDB는 컬럼스토어 개념이 없음. 데이터(Document)가 한 파일로 저장됨


### MongoDB 아키텍쳐

### MongoDB 배포 형태
- 클러스터 형태로도 서비스 가능
- 단일 서버로도 서비스 가능
- 복제도 샤딩된 구조로 활용 가능


- 단일 노드(Standalone)
  - 응용프로그램의 몽고DB드라이버가 몽고디비 서버로 직접 연결됨.
  - 개발서버구성
- 단일 레플리카 셋(Single Replica-set)
- 샤딩된 클러스터(Sharded Cluster)

## 모르는것
- 아직까지 배포 형태에서 단일노드, 단일레플리카셋, 샤딩된 클러스터 세 개의 차이를 명확하게 이해하지 못하겠다.  서버를 한 대 두고 운영, 레플리카를 하나 두고 운영, 레플리카 여러개에 여러 서버를 두고 운영 이 차인가??

