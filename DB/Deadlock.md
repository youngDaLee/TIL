### DeadLock(교착상태)이란
- 여러 트랜잭션이 자신의 데이터에 대해 lock을 획득한 상태에서 상대방 데이터에 접근하고자 대기를 할 때, 서로 영원히 기다리는 상태
- 해결 방법
  - 예방 : 트랜잭션 실행 전 필요 데이터 모두 lock
  - 회피 : 자원 할당시 timestamp로 데드락 발생하지 않게 회피
  - 탐지/회복 : 트랜잭션 실행 전 검사 하지 않고, 데드락이 발생 하면 그 때 감지하고 회복하는 방법