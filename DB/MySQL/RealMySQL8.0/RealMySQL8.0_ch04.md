# RealMySQL8.0 ch04. 아키텍쳐
## 4.1 MySQL 엔진 아키텍쳐
### 4.1.1 MySQL의 전체 구조
* 다른 DB와 마찬가지로 프로그래밍 언어로부터의 접근 모두 지원
* MySQL 엔진 + 스토리지 엔진 = MySQL 서버
  * MySQL 엔진 : 커넥션 핸들러(클라이언트 접속 및 쿼리 요청 처리) / SQL 파서 / 전처리기 / 옵티마이저. 표준 SQL 문법을 지원하여 다른 RDBMS와 호환됨
  * 스토리지 엔진 : SQL 분석 및 최적화, 실제 데이터를 디스크에 저장하고 읽어오는 부분. 각 스토리지 엔진은 성능 향상을 위해 키캐시(MyISAM)이나 버퍼풀(InnoDB)과 같은 기능을 내장함
* 핸들러 API : 쿼리 실행기에서 데이터 읽기/쓰기 시 스토리지 엔진에 요청하는 것. 스토리지 엔진은 핸들러API를 통해 MySQL엔진과 데이터를 주고받음.


### 4.1.2 MySQL 스레딩 구조
MySQL 은 프로세스가 아닌 스레드 기반으로 동작
- 포그라운드 스레드(foreground, 클라이언트 스레드)
  - 최소한 MySQL 서버에 접속한 클라이언트 수 만큼 존재
  - 주로 클라이언트가 요청하는 쿼리문장을 처리함
  - 클라이언트가 작업 마치고 커넥션 종료하면 다시 스레드 캐시로 돌아감 => 일정 개수 이상의 대기중인 스레드가 있으면 스레드를 종료.
  - 데이터를 데이터 버퍼나 캐시로부터 가져옴. => 버퍼,캐시에 없는 경우는 직접 디스크에서 읽어와서 처리
  - MyISAM : 디스크 작업까지 포그라운드가 처리 / InnoDB : 버퍼/캐시까지만 포그라운드. 디스크에 쓰는건 백그라운드
- 백그라운드 스레드(background)
  - MySQL 서버 설정에 따라 개수가 가변적. => 동일 이름 스레드 2개 이상인 경우는 MySQL서버 설정때문에 동일 작업 병렬처리하기 때문
  - InnoDB에서 백그라운드로 처리되는 작업(MyISAM은 해당 거의 없음)
    - 인서트 버퍼 병합
    - 로그를 디스크로 기록
    - InnoDB 버퍼풀의 데이터를 디스크에 기록
    - 데이터를 버퍼로 읽어오는 스레드
    - 잠금, 데드락을 모니터링
  - 쓰기 작업은 버퍼링 가능하지만, 읽기 작업은 버퍼링 처리되면 안되기 때문에 포그라운드 처리
  - MyISAM에서 일반적인 쿼리는 쓰기 버퍼링 불가(InnoDB는 가능)

스레드 목록 확인 법
```sql
SELECT thread_id, name, type, processlist_user, processlist_host
FROM performance_schema.threads
ORDER BY type, thread_id; 
```

### 4.1.3 메모리 할당 및 사용 구조
서버 내의 많은 스레드가 공유해서 사용하는 공간인지 여부에 따라 구분됨
- 글로벌 메모리 영역
  - 클라이언트 스레드 수와 무관하게 하나의 메모리 공간반 할당됨 => 필요에 따라 2개 이상 가능하지만 클라이언트 수와 무관
  - 글로벌 영역이 N개더라도 모든 스레드에 의해 공유됨
  - 대표적인 글로벌 메모리 영역
    - 테이블 캐시
    - InnoDB 버퍼풀
    - InnoDB 어댑티브 해시 인덱스
    - InnoDB 리두로그 버퍼
- 로컬 메모리 영역
  - 세션 메모리 영역. 클라이언트 스레드가 쿼리를 처리하는데 사용하는 메모리 영역
  - 스레드별로 독립적으로 할당되며,절대 공유되지 않음.
  - 최악의 경우 메모리 부족으로 멈출 수 있으므로 적절한공간 할당하는게 중요(가능성 매우 희박)
  - 커넥션이 열려 있는 동안 계속 남아있는 공간(커넥션 버퍼, 결과 버퍼) / 쿼리 실행 순간에만 할당했다 해제하는 공간(소트버퍼, 조인버퍼)
  - 대표적인 로컬 메모리 영역
    - 정렬 버퍼(Sort Buffer)
    - 조인 버퍼
    - 바이너리 로그 캐시
    - 네트워크 버퍼

### 4.1.4 플러그인 엔진 모델
- 이미 기본적으로 많은 스토리지 엔진을 가지고 있지만, 플러그인을 통해 부가적인 기능을 제공하는 스토리지 엔진을 사용할 수 있음(검색 등)

### 4.1.5 컴포넌트
8.0 부터는 기존 플러그인 아키텍쳐를 대체하기 위한 컴포넌트 아키텍쳐를 지원.   

MySQL 서버 플러그인 단점
- 플러그인은 오직 MySQL 서버와 인터페이스 할 수 있고, 플러그인끼리는 통신 불가
- 플러그인은 MySQL서버의 변수/함수를 직접 호출하기 때문에 안전하지 않음(캡슐화 x)
- 플러그인은 상호 의존 관계 설정 불가하기 때문에 초기화 어려움

### 4.1.6 쿼리 실행 구조
<img width="319" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/76f31b69-6030-424a-b7ad-3ad9f7dd6e89"/>

- 쿼리 파서 : 쿼리 문장을 MySQL이 인식할 수 있는 토큰으로 분리해서 트리 형태로 만드는 것 -> 기본 문법 오류가 이 과정에서 발견됨
- 전처리기 : 파서 트리를 기반으로 쿼리 문장에 구조적인 문제점을 확인. 객체 존재 여부와 접근 권한등을 확인.
- 옵티마이저 : 쿼리를 저렴한 비용으로 빠르게 처리할지 결정하는 역할. 두뇌 역할
- 실행 엔진 : 손과 발. 만들어진 계획대로 핸들러에 요청하고, 받은 결과를 또 다른 핸들러 요청 입력으로 연결. 일종의 PM?
- 핸들러(스토리지 엔진) : 가장 밑단에서 실행엔진 요청에 따라 데이터를 디스크로 저장하고 읽어오는 엵할을 담당.

### 4.1.7 복제
=> 16장에서....

### 4.1.8 쿼리 캐시
- SQL 실행 결과를 메모리에 캐시하고, 동일 SQL 쿼리가 나오면 테이블을 읽지 않고 결고 ㅏ반환
  - 테이블 데이터가 변경되면 테이블과 관련된 캐시 전체 삭제 => 동시 처리 성능 저하 유발
  - 데이터 변경이 없는 독특한 환경에서 훌륭한 기능이지만, 이런 환경이 거의 없었음
  - MySQL 성능 개선되는 과정에서 동시처리 성능 저하와 버그 원인이 되기도 함.
- MySQL 8.0 에서는 쿼리 캐시가 완전 삭제되었고, 관련 시스템 변수도 삭제됨.

### 4.1.9 스레드 풀
엔터프라이즈에서만 제공(커뮤니티에서 미제공) Percona에서 플러그인 형태로 제공(오픈소스)
- 스레드풀 목적 : 내부적으로 사용자 요청 스레드 개수를 줄여서 동시 처리되는 요청이 많아도 CPU가 제한된 개수 스레드 처리에만 집중할 수 있도록 하여 서버 자원 소모를 줄이는 것
  - 실제 서비스에서 눈에 띄는 성능 향상을 보여주는 것은 드물다
  - CPU 프로세서 친화도를 높히고, 불필요한 컨텍스트 스위치를 줄여 오버헤드를 방지함
- 일반적으로 CPU 코어 개수와 스레드 수를 맞추는게 프로세서 친화도를 높히는데 좋음

### 4.1.10 트랜잭션 지원 메타데이터
메타데이터 : 테이블 구조 정보, 스토어드 프로그램 등의 정보
- ~ 5.7 : 테이블 구조를 FRM 파일에 저장하고 일부 스토어드 프로그램도 파일 기반 관리함 => 파일 기반 메타데이터는 생성, 변경 작업이 트랜잭션을 지원하지 않기 때문에 서버 비정상 종료 시 일관되지 않은 상태로 남는 문제 => DB, 테이블이 깨졌다~
- 8.0 : 깨짐 현상 방지 위해 메타데이터를 InnoDB 테이블에 저장하도록 개선 => 시스템 테이블
  - 시스템 테이블, 데이터 딕셔너리 정보 모두 모아 mysql DB에 저장
  - mysql DB를 통째로 mysql.idb 라는 테이블 스페이스에 저장.

## 질문
* MySQL은 프로세스가 아닌 스레드 기반 동작이라 했는데, 프로세스 기반 동작과 스레드 기반 동작의 차이는 무엇이고, 프로세스 기반 동작을 하는 DB는 어떤게 있나요?
* 로컬메모리 생성에 제한이 있나요? 쿼리캐시는 글로벌 메모리에 속하나요, 로컬 메모리에 속하나요?
* 쿼리캐시가 사라진 8.0에서는 어떤 방식으로 자주 쓰는 쿼리의 성능을 높히나요?
* 클라이언트 단에서의 스레드풀과 MySQL 엔진단에서의 스레드풀은 어떻게 다른가요?