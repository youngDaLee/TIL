# RealMySQL8.0 ch04. 아키텍쳐
## 4.3 MyISAM 스토리지 엔진 아키텍쳐
<img width="282" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/24b00dd7-011d-426a-85e4-3eabc41cb152">

### 4.3.1 키 캐시
InnoDB의 버퍼풀 역할을 하는 MyISAM의 키 캐시
```agsl
키 캐시 히트율(hit rate) = 100 - (key_reads/key_read_requests * 100)
```
* 키 캐시가 얼마나 효율적으로 작동하는지 확인하는 수식
* `key_reads` : 인덱스를 디스크에서 읽은 횟수
* 99% 이상으로 유지하라고 권장함

### 4.3.2 운영체제의 캐시 및 버퍼
* MyISAM 인덱스는 키캐시로 디스크를 검색하지 않아도 빠르게 검색 가능
* MyISAM이 주로 사용되는 MySQL에서 키캐시는 물리메모리 40% 이상을 넘지 않도록 설정하고, 나머지는 운영체제 파일시스템 캐시공가능로 비워두는걸 권장함
    * 메모리 문제 날 수 있음~

### 4.3.3 데이터 파일과 프라이머리 키(인덱스) 구조
InnoDB는 PK가 클러스터링되어 저장되지만, MyISAM은 클러스터링 없이 Heap 공간처럼 활용됨.    
즉 레코드가 PK와 무관하게 INSERT되는 순으로 데이터파일에 저장됨 -> 레코드 ROWID 값을 포인터로 가짐

ROWID 값 저장 방법
* 고정길이 ROWID
* 가변길이 ROWID
