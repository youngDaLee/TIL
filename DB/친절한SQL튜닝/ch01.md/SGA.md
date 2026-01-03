# SGA(System Global Area)
> DB의 거대한 공유 작업실

- 오라클 인스턴스의 모든 서버 프로세스와 백그라운드 프로세스가 공동으로 액세스하는 공유 메모리 영역
- 목적 : 디스크 io 최소화 및 프로세스간 데이터 공유
- 특징
    - 인스턴스 시작 시 할당, 종료 시 해제
    - 여러 프로세스가 동시에 접근하여 Latch나 Enqueue와 같은 직렬화 매커니즘이 필수로 작동

SGA 핵심 컴포넌트
- 라이브러리 캐시(Shared Pool 내에 위치)
    - SQL 실행계획과 파싱트리 저장(하드파싱과 관련)
    - 이 때 바인드 변수를 쓰지 않으면 텍스트가 달라져 매번 새로운 해시키가 생성되고, 이는 Shared Pool 단편화와 CPU 부하 유발
- 데이터베이스 버퍼 캐시(DB Buffer Cache)
    - SGA에서 가장 큰 면적을 차지하는 경우가 많음
    - 디스크에서 읽어온 데이터 블록 복사본을 유지
    - LRU알고리즘 사용해서 자주 사용되는 데이터를 메모리에 유지하고 사용되지 않는 데이터는 밀어냄
    - Physical Read가 높으면 버퍼 캐시 효율이 떨어진다는 뜻
- 로그 버퍼(Redo Log Buffer)
    - 데이터 변경 사항(Undo/Redo)을 디스크(Redo Log File)에 기록하기전 임시 저장하는 공간
    - Commit 발생하거나 버퍼가 1/3 이상 차면 LGWR 프로세스가 디스크로 기록함

SGA가 성능에 미치는 영향
> SGA는 한정된 자원으로, 대부분의 SQL 성능 이슈는 SGA 내부의 경합에서 발생
- Shared Pool 경합
    - 바인드 변수 미사용 시 Library Cache Latch 경합 발생. => CPU 점유율 상승 및 시스템 응답 속도 저하
- Buffer Cache 경합
    - 동시에 너무 많은 프로세스가 같은 데이터블록 수정하려 할시 Buffer Busy Waits 대기 발생

SGA vs PGA
- SGA가 모든 프로세스가 공유하는 공유 메모리 영역이면, PGA(Program Global Area)는 개별 프로세스 전용 메모리 영역

| 구분 | SGA (System Global Area) | PGA (Program Global Area) |
|------|--------------------------|---------------------------|
| 성격 | 공유 메모리 영역 | 개별 프로세스 전용 메모리 영역 |
| 주요 용도 | 데이터 블록 캐싱, 실행 계획 공유 | 정렬(Sort), 해시 조인, 세션 변수 저장 |
| 액세스 | 모든 서버/백그라운드 프로세스 | 해당 프로세스만 독점 접근 |
| 경합 발생 | 발생함 (Latch 필요) | 발생 안 함 (독점 공간) |
| 부족 시 현상 | 하드 파싱 증가, 디스크 I/O 폭증 | Temp Tablespace 사용 (성능 급락) |

- PGA -> Order By, Group By 포함된 대량 데이터 처리 시 할당된 PGA 공간 부족하면 디스크(temp) 사용 -> PGA Spill to Disk 현상 발생하여 SQL 속도 수십배 느려짐

Latch
- SGA내 특정 구조물에 대한 동시 접근 제어를 위한 경량화된 동기화 메커니즘
- 특징
  - 매우 빠름 : Lock(Enqueue)보다 훨씬 가볍고 짤벡 유지됨
  - Queue가 없음 : 줄 서기가 없음. 선착순. 실패하면 잠시 쉬었다가(Spin) 다시 시도
- `Latch: Library Cache` 대기가 많으면 바인드 변수 미사용으로 실행계획 찾고 등록하는 Latch 싸움이 치열하단 뜻..

Wait Event
- DB가 느려졌을 때 `V$SESSION_WAIT`, `V$SYSTEM_EVENT` 뷰에서 대기 이벤트를 확인

SGA 관련 주요 대기 이벤트
- `latch: cache buffers chains` : Buffer Cache내 데이터 블록에 대한 동시 접근 경합
  - 너무 많은 쿼리가 동시에 동일 인덱스블록이나 테이블 블록 접근할 때 발생
- `enq: TX - row lock contention` : 동일 데이터 행에 대한 동시 수정 시도
  - 긴 트랜잭션이나 커밋 누락
- `db file sequential read` : 인덱스 블록 1개를 디스크에서 읽을 때 발생하는 대기
  - 인덱스 스캔이 비효율적이거나 메모리가 너무 작다는 신호