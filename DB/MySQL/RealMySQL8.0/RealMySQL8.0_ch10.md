# ch10. 실행 계획
## 10.1 통계 정보
5.7 버전 까지는 테이블, 인덱스에 대한 개괄적 정보로 실행계획 수립 -> 8.0 부터는 데이터 분포도 저장하는 히스토그램(histogram) 정보 도입됨.

### 10.1.1 테이블 및 인덱스 통계 정보
비용기반 최적화에서 가장 중요한것은 통계정보... 부정확한 통계 때문에 인덱스 레인지 스캔이 아니라 풀테이블 스캔을 해서 많은 시간 소요될 수 있음.    

MySQL 서버의 통계 정보
* 5.6 버전 부터는 InnoDB를 사용하는 테이블에 대한 통계 정보를 영구적으로 관리할 수 있게 개선됨.
  * 5.5 까지는 테이블 통계 정보 메모리에서만 관리됨...
* 5.6 부터 테이블 통계 정보를 `mysql` DB의 `innodb_index_stats` `innodb_table_stats` 에서 관리할 수 있게 됨.
* 5.6 부터 테이블 생성할 때 `STATS_PERSISTENT` 옵션 설정 -> 테이블 단위로 통계 정보 영구 보관할지 여부 결정
  * 0 : 5.5 버전 이전 대로 관리..  `innodb_index_stats` `innodb_table_stats` 에 저장하지 않음
  * 1 : `innodb_index_stats` `innodb_table_stats` 에 저장함
  * DEFAULT : `innodb_stats_persistent` 설정 변수에 따라 결정
* 5.5 버전까지는 관리자가 알지 못하는 순간에 특정 이벤트가 발생하면 자동으로 통계 정보가 갱신 -> `innodb_stats_auto_recalc` OFF 해서 갱신 막음

### 10.1.2 히스토그램
5.7 버전까지는 인덱스된 컬럼 유니크 값 개수 정도 가지고 있었다면, 8.0 부터 컬럼 데이터 분포도 확인할 수 있는 히스토그램 정보 활용    

히스토그램 정보 수집 및 삭제
* 8.0 버전에서 컬럼 단위로 관리되는데, `ANALYZE TABLE ... UPDATE HISTOGRAM`명령으로 수동 수집 됨.
* 서버 시작될 때 히스토그램 정보를 `information_schema` `column_staticstics` 테이블로 로드함
* 8.0에서 지원하는 2종류의 히스토그램 타입
  * singleton : 컬럼값 개별로 관리하는 히스토그램. value-based 히스토그램이라고도 함
  * equi-height : 컬럼값 범위를 균등한 개수로 구분해서 관리하는 히스토그램. Height-Balanced 히스토그램이라고 불리기도함


## 10.2 실행 계획 확인

## 10.3 실행 계획 분석


### 10.3.7 key 컬럼