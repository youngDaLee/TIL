# MongoDB의 CreateIndex - 레플리카셋의 롤링 인덱스 빌드
레플리카셋으로 구성된 MongoDB에서의 인덱스 생성 방법

롤링 인덱스 빌드(Rolling Index Build)
* 한 번에 하나의 복제본 세트 노드만 중단시킴
* 세컨더리(정확히는 레플리카셋 두번째 노드)부터 시작해서 해당 노드에서 독립적으로 인덱스를 빌드

작업 순서
1. 세컨더리 노드 설정
   1. 세컨더리 노드를 유지보수 모드로 설정 rs.stepDown() -> 이 상태에서 세컨더리 노드는 클라이언트 요청 대신 레플리케이션 작업, 인덱스 생성만 관리
   2. 레플리케이션 로그 관리 -> 세컨더리는 프라이머리로부터 oplog 계속 수신 -> oplog 누적된 것을 재적용해서 데이터 일관성 유지함
   3. MongoDB 4.2 이전에는 인덱스 생성 시 전체 컬렉션에 락을 걸었었음 -> 이후 버전에서는 다음과 같은 비차단(non-blocking) 전략을 사용
      * **기본: 공유 락(Shared Lock)**으로 작업 중 데이터 읽기를 허용.
      * 단계적 빌드 처리: 일부 데이터 청크를 처리하고 락을 해제하며 다음 청크로 이동.
   4. 인덱스를 생성
   5. 작업이 완료되면 노드 복구 후 다음 세컨더리로 이동 -> 세컨더리는 프라이머리 상태를 재동기화 해서 최신 상태를 유지함
1. Primary 노드 처리
   1. 세컨더리 노드들 작업 완료되면 프라이머리를 **세컨더리로 강등** 후 작업 수행 -> 다른 세컨더리 중 하나가 프라이머리로 승격됨
   2. 작업 완료 후 해당 노드를 다시 프라이머리로 복구

```
// Secondary 노드 유지보수 모드
rs.secondaryOk(); 
db.getMongo().setSlaveOk(); // Secondary에서 작업 가능

// 인덱스 생성
db.collection.createIndex({ field: 1 });

// 작업 후 복구
rs.slaveOk(false);
```
