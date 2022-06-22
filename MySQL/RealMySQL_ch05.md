# Real MySQL - ch05 인덱스
- MySQL에서 사용 가능한 인덱스 종류 및 특성

## 5.1 디스크 읽기 방식
DB 성능 튜닝 중, 어떻게 디스크 I/O를 줄이느냐가 관건인 것들이 상당히 많음
### 5.1.1 저장매체
데이터를 저장할수 있는 메체(Disk)
- 내장 디스크(Internal Disk)
  - PC 본체 내에 장착된 디스크
  - DB 서버용 장비는 일반적으로 4~6개 내장 디스크를 장착함. -> 컴퓨터 본체 내부 물리적 공간이 제한적이라 장착할 수 있는 디스크개수도 적고, 용량도 부족
- DAS(Direct Attached Storage)
  - 내장디스크 용량 문제 해결
  - 디스크만 존재. 독자적으로 사용 불가. 컴퓨터 본체에 연결해서 사용
  - 사용 방식, 성능은 내장디스크와 거의 동일.
  - 대용량 디스크에 적합.
  - 반드시 하나의 컴퓨터 본체에만 연결해야 하기 때문에 해당 디스크 정보 여러 컴퓨터가 동시에 공유 불가
- NAS(Network Attached Storage)
  - 네트워크(TCP/IP)를 통해 연결
    - 빈던한 데이터 읽고 쓰기가 필요한 DB 서버용으로는 사용되지 않음
  - 여러 컴퓨터에서 공유해서 사용 가능
  - SATA, SAS 보다는 느림
- SAN(Storage Area Network)
  - DAS로 구축불가한 아주 대용량 스토리지 공간 제공
  - 여러 컴퓨터에서 동시에 읽는 것 가능, 컴퓨터 본체와 광케이블로 연결되어 빠르고 안정적인 데이터처리 -> 비쌈

#### 사양
(저사양) 내장디스크 < DAS < SAN (고사양)

전부 플래터(Platter, 디스크 드라이브 내부의 데이터 저장용 원판) 사용함

## 5.1.2 디스크 드라이브와 솔리드 스테이트 드라이브(SSD, Solid State Drive)
기계식 장치가 플래터를 회전시켜 데이터를 저장 -> 디스크 장치가 병목지점이 됨
- 기계식 드라이브 대체 => SSD(Solid State Drive)
  - 인터페이스(SATA, SAS)를 지원함 -> 내장디스크, DAS, SAM에 그대로 사용 가능

플래터 대신 **플래시 메모리** 장착함.
- 원판 기계식 회전 필요 x
- 매우 빠름
- 전원 공급되지 않아도 데이터 삭제되지 않음.
- D-RAM(컴퓨터 메모리)보다는 느리지만 기계식 디스크 드라이브보다 훨씬 빠름
- 초당 트랜잭션 처리 수
  - SSD : 436
  - HDD : 60

일반적인 웹서비스(OLTP)에서는 SSD가 HDD보다 훨씬 빠르다.

## 5.1.3 랜덤 I/O와 순차 I/O
랜덤, 순차 모두 디스크 드라이브의 플래터(원판)를 돌려서 읽어야 할 데이터가 저장된 위치로 디스크 헤더를 이동시킨 뒤 데이터를 읽는 방식.

- 순차 I/O
  - 3개 페이지 디스크 기록 위해 1번의 시스템 콜 요청
- 랜덤 I/O
  - 3개 페이지 디스크 기록 위해 3번 시스템 콜 요청

순차I/O가 랜덤보다 훨씬 빠르고, 부하가 적음.

DB 대부분이 작은 데이터를 빈번히 읽고 씀 -> MySLQ 서버에 그룹 커밋, 바이너리 로그 버퍼, InnoDB 로그 버퍼 기능 내장(부하 막기 위해)

쿼리 튜닝으로 랜덤 I/O를 순차 I/O로 바꿔 실행 할 방법이 많지 않음..
- 일반적으로 쿼리 튜닝 하는게 랜덤 I/O 자체를 줄여주는 것이 목적
- 랜덤 I/O를 줄이는 것 : 쿼리를 처리하는데 꼭 필요한 데이터만 읽도록 쿼리 개선하는 것
  - 레인지 스캔은 데이터 읽기 위해 랜덤 I/O 사용
  - 풀테이블 스캔은 순차 I/O 사용
  - => 큰 테이블 레코드 대부분을 읽는 작업에서는 인덱스 사용 않고 풀테이블 스캔 유도...(순차가 랜덤보다 훨씬 많이 읽어올 수 있기 때문) -> OLTP 성격의 웹서비스 보다는 DW, 통계 작업에서 자주 사용됨


## 5.2 인덱스란?
- 컬럼 값을 주어진 순서로 미리 보관하는 것(Key-Value Pair로 인덱스 미리 생성)

인덱스를 자료구조로 표현
- Sorted List
  - 정렬되어있기 때문에 아주 빠르게 원하는 값을 찾을 수 있음
  - 저장할 때 마다 정렬해야 하기 때문에 저장 과정이 복잡하고 느림
- Array List
  - 저장하는 그대로 값을 저장.

인덱스 결론
- 데이터 저장(INSERT, UPDATE, DELETE) 성능 희생하고 데이터 읽기 속도 향상

인덱스 역할별 분류
- PK
  - 레코드 대표하는 컬럼 값
  - 식별자
  - NULL, 중복 허용 X
- 보조키(Second Key)
  - PK 제외한 나머지 인덱스는 모두 보조 인덱스(Secondary Index)로 분류.
  - 유니크 인덱스 : PK와 성격비슷, PK 대체 가능 -> 대체키라고도 불림(별도로 분리하기도 하고 보조키와 묶이기도 하고..)

데이터 저장방식(알고리즘)별 분류
- B-Tree 인덱스
  - 일반적으로 사용하는 인덱스 알고리즘
  - 컬럼 값 변형 x, 원래의 값을 이용해 인덱싱
- Hash 인덱스
  - 컬럼 값으로 해시 값 계산
  - 매우 빠른 검색 지원
  - 값을 변형해서 인덱싱 -> 전방(Prefix) 일치와 같이 값의 일부만 검색하고자 할 때 해시 인덱스 불가
  - 메모리 기반 DB에서 사용
- Fractal_Tree
  - B-Tree 단점 보완
  - 값을 변형하지 않고 인덱싱, 범용적인 목적으로 사용 가능(B-Tree와 유사)
  - 데이터가 저장, 삭제 될때 B-Tree에 비해 처리 비용 줄일 수 있도록 설계됨
  - 아직 B-Tree만큼 안정적이진 않음

데이터 중복 여부 분류
- Unique 인덱스
- Non-Unique 인덱스


## 5.3 B-Tree 인덱스
인덱싱 알고리즘 중 가장 일반적으로 사용되고, 가장 먼저 도입된 알고리즘