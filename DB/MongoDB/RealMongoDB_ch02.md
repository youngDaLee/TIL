# Real MongoDB - ch02. 스토리지 엔진
## 2.1 플러그인 스토리지 엔진
스토리지 엔진이란? : 사용자의 데이터를 디스크와 메모리에 저장하고 읽어오는 역할을 하는 것(MMAPv1, WiredTiger 등..)
- MySQL과 다르게 하나의 인스턴스에서 동시에 여러 스토리지 엔진을 쓸 수 없음
  - 내가 이해한 것 : MySQL은 한 스키마 내부에서도 어떤 테이블은 InnoDB, 어떤 테이블은 MyISAM을 쓸 수 있는데, MongoDB는 해당 DB가 WiredTiger을 쓰면 무조건 그 DB는 WiredTiger을 써야 함
  - 그렇다면 중간에 스토리지 엔진을 변경하는 것도 불가한가?

### MongoDB의 스토리지 엔진
- MMAPv1
- WiredTiger
- In-Memory
  - WiredTiger 변형. 데이터를 디스크에 기록하지 않고 메모리에만 보관하는 스토리지 엔진
- RocksDB
- TokuDB
|기능|MMAPv1|WiredTiger|RocksDB|TokuDB|
|:--:|:----:|:--------:|:-----:|:----:|
|잠금수준|컬렉션|도큐먼트|도큐먼트|도큐먼트|
|데이터 구조|B-Tree|B=Tree|LSM|Fractal-Tree|
|빌트인 캐시|X(운영체제캐시)|O|O|O|
|세컨드리 인덱스|O|O|O|O|
|데이터 압축|X|O|O|O|
|인덱스 압축|X|O|O|O|
|암호화|X|O|X|X|
|In-Memory지원|X|O|X|X|
|컬렉션 파티션|X|X|X|O|

### 스토리지 엔진 혼합 사용
MongoDB 인스턴스(서버)에서 동시에 여러 스토리지 엔진 사용 불가능
- 인스턴스만 다르면 스토리지 엔진 동시 사용 가능
- 1번 샤드에서 Wired Tiger 사용, 2번 샤드에서 RocksDB 사용...
- 하나의 레플리카셋에서 프라이머리 멤버는 WiredTiger 스토리지 엔진 사용, 세컨드리 멤버는 RocksDB 사용

#### 궁금한 점
- 하나의 레플리카셋에서 버전이 다른 것은 허용이 안 되는 것으로 이해했는데(충돌로 인해 별 다른 설정 없이는 롤링업그레이드 중 더 낮은 버전으로 통일하여 사용됨), 스토리지 엔진은 달라도 되는것인지??
- 중간에 스토리지 엔진 변경 가능?

## 2.2 MMAPv1 스토리지 엔진
- MongoDB 3.0까지 주로 사용되던 스토리지 엔진
- 2.6까지는 DB단위 잠금을 해서 DML 동시처리 성능이 좋지 않음. 3.0이후는 컬렉션 수준으로 개선 -> 여전히 동시성처리에 걸림돌이 됨
- 내장된 캐시기능이 없어 OS 캐시 활용
- OS 캐시를 사용해서 커널이 제공하는 시스템콜을 거치게 됨 -> 오버헤드가 큰 편
### MMAPv1 설정
- MongoDB 설정파일의 storage 섹션 egine옵션을 "mmapv1"으로 설정
  - MongoDB 서버 설정파일에서 결정하는 옵션 대부분이 MongoDB 서버 성능 좌우할만한 영향력을 가진게 없음
  - MongoDB 차원의 성능튜닝옵션이 거의 없음
  - MongoDB 서버 설정보다는 리눅스 커널의 파라미터 튜닝이 더 많이 필요

```
mmapv1:
    preallocDataFiles: <boolean>
    nsSize: <int>
    quota:
        enforced: <boolean>
        maxFilesPerDB: <int>
    smallFiles: <boolean>
```
- PreallocDataFile : 빈 데이터 파일을 미리 생성해서 데이터가 사용할것인지 결정하는 옵션 -> 백업 데이터 양만 늘리는.. 공간낭비일수도
- nsSize : 네임스페이스파일 크기 설정. 기본값 16MB
- quota : DB단위 디스크 사용공간 제약 옵션
- smallFiles : 컬렉션 단위로 생성하는 데이터 파일 초기 크기 작게 만들고, 데이터 파일 최대 크기도 512MB로 제한하는 옵션

### 데이터파일 구조
- 데이터파일이 DB단위로 생성된
- 컬렉션의 데이터가 하나의 DB파일에만 저장되는게 아니라, 크기에 따라 여러 데이터파일로 나뉘어 저장됨
- 최초는 64MB, 두번째는 128MB, 세번째는 256... 2048MB(2GB)까지 증가하면 그 이후는 더 증가하지 않고 2GB 유지 -> 디스크 공간을 효율적으로 사용하기 위한 방법
  - 컬렉션 데이터가 많지 않은데 처음부터 64MB로 시작하는게 낭비일 수 있음 -> storage.smallFiles 옵션 이용해서 생성되는 파일 크기 작게 가능(16MB시작 ~ 512MB까지만 증가 하도록 설정 가능)
  - 디스크 효율적 활용 위해 DB 너무 잘게 분리하는 모델링 자제 필요
- starge.directoryPerDB : 디스크 데이터 파일을 별도 디렉터리에 저장할건지 결정 가능(for 관리 편의성)
- *.ns 파일 : MongoDB서버의 DB와 컬렉션, 인덱스정보 저장

### MongoDB 서버상태 확인
mongostat 도구 사용
- flush : MMAPv1이 데이터파일 변경내용을 디스크에 동기화하는 과정. 몇 번이나 동기화 되었는지..
- mapped : MMAPv1에만 보여지는 메트릭. MongoDB 데이터파일이 리눅스 페이지 캐시에 얼마나 매핑되었는지
- vsize : MongoDB서버 프로세스가 현재 사용중인 가상메모리공간의 크기. 실제 사용중인 물리메모리는 "res" 컬럼에 보여지는 수준
- faults : 리눅스 페이지폴트에서 나온 개념.. 특정 주소 데이터 읽으려고 할 때, 데이터가 아직 물리적으로 메모리에 적재되어있지 않은 경우 "페이지폴트" 시그널 발생. 1초에 얼마나 많은 페이지폴트가 발생했는지. 디스크에서 데이터 읽은 회숫와 비슷한값. 크면 클수록 디스크에서 데이터 자주 읽는다는 의미 -> 메모리 부족!
- locked db : 잠금이 가장 심한 DB 보여줌

### 운영체제 캐시



## 2.3 WiredTiger 스토리지 엔진
- 내부적인 잠금경합 최소화를 위해 하자드 포인터(Hazard-Pointer), 스킵리스트(Skip-List) 등의 신기술을 채택함
- 최근의 RDBMS가 가진 MVCC(잠금없는 데이터 읽기), 파일 압축, 암호화 기능 가지고 있음

특징
- 컬렉션과 인덱스에 압축 설정이 디폴트
- MVCC를 통해 읽기와 쓰기 작업 격리 -> 데이터의 일관된 특정 시점 뷰를 볼 수 있게 함
- 체크포인팅으로 스냅샷 생성
- journaling : mongod 프로세스 실패 시 데이터 손실되는 시점 업게 함. 수정사항 적용 전에 저장하는 로그 선행 기입을 사용함

### 2.3.1 wiredTiger config
MongdDB config 중, wiredTiger와 관련있는 부분
```YAML
storage:
  dbPath: <string> # 데이터 파일 저장 경로
  indexBulidRetry: <boolean> # 인덱스 생성 비정상적으로 중단된 채 MongoDB서버 재시작하면 인덱스 생성 자동으로 시작할건지
  repairPath: <string> # 복구 스레드 디렉토리 지정
  directoryPerDB: <boolean> # DB단위로 디렉토리 나눠서 데이터 파일 저장할건지
  syncPeriodSecs: <int> # 동기화 주기

  journal:
    enabled: <boolean> # 서버 저널로그 활성화 여부
    commiIntervalMs: <num> # 저널로그 주기
```

```YAML
engine: wiredTiger

wiredTiger:
  engineConfig:
    cacheSizeGB: <number> # wiredtiger 공유 캐시 크기 -> 보통 (RAM//2)-1 크기로 설정함
    journalCompressor: <string>
    directoryForIndexes: <boolean>
  colletionConfig:
    blockCompresor: <string> # wiredTiger 데이터 압축 알고리즘 설정
  indexConfig:
    prefixCompression: <boolean> # 프리픽스 압축 사용 여부 결정
```

### 2.3.2 WiredTiger 저장 방식
WiredTiger가 가진 저장소
- 레코드(row, record) 스토어
  - 일반적인 RDBMS가 사용하는 저장방식
  - 기본적으로 B-Tree 알고리즘 사용
  - 테이블 레코드 한 번에 저장
- 컬럼 스토어
  - 대용량 분석(OLAP, DW) 용도로 사용
- LSM(Log Structured Merged Tree) 스토어
  - NoSQL에서 자주 사용됨. 읽기보다는 쓰기 능력에 집중
  - B-Tree 사용하지 않고 순차적으로 데이터 저장
  - 갓 저장된 파일을 Level-0, 얘네가 많아지만 병합해서 Level-n까지 데이터 파일로 저장함
  - 블록단위로 키 샘플링
  - N개의 데이터 파일을 검색

WiredTiger에는 레코드 기반의 저장소만 사용됨

### 2.3.3 데이터 파일 구조
`storage.directoryPerDB` 옵션으로 DB별 디렉토리 구분 가능.

메타 데이터파일
#### WiredTiger
- 스토리지 엔진 버전
#### storage.bson
- WiredTiger 디렉토리 구조

#### sizeStorer.wt
- 

### 2.3.4 WiredTiger 내부 작동 방식
B-Tree구조의 데이터 파일과 서버 크래시(비정상 종료)로부터 데이터 복구를 위한 저널 로그(WAL, Write Ahead Log)로 이루어짐.





### 참고 블로그
- https://rastalion.me/mongodb%EC%9D%98-wiredtiger-%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EC%97%94%EC%A7%84/

## 2.4 메모리 스토리지 엔진

## 2.5 기타 스토리지 엔진


