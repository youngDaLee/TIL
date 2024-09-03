# What's New in MongoDB 8.0
MongoDB Community 에서 Serch 가능
* Search
* Vector Search

-> 투자중이다~

다양한 환경에서 데이터 마이그레이션 하는 툴 개발중. 완전히 관리되는 툴 아틀라스로 지원해줌

8.0 에서 개선된것
* Optimal Performance : 개별로드, 개별유즈케이스, 고확장성 성능
  * 애플리케이션 고도화를 원할 때 workload 성능투자 
  * YCSB : 벤치마크?
  * LinkBench : 소셜..
  * TSBS : 시계열데이터 퍼포먼스 개선
  * TimeSeries 데이터 처리 가능하도록 5.0부터 지원 -> 8.0 부터는 개별문서에서 작업하는대신 높은 수준에서 readperformance 향상? $group에서 극적인 효과.
  * Query Execution Improvement : Command Path 최적화 - MongoDB에서 가장 자주 실행되는 섹션. 읽기/쓰기 최적화하게 되어 모든 커멘드 성능이 향상됨 / Plan Cache에도 투자함 / plan execution 패치수를 줄이기
  * 단일인덱스 single equality predicates 향상 -> EXPRESS Stage 새로 생김!! => 활용해서 17% 성능개선
  * **메모리 관리** Memory Allocator 활용 -> 대부분 fragmentation 신경 안씀 -> 메모리 부족해지면 그 때야 fragmentation 신경씀.=> 8.0 에서 memory fragmentation 을 18% 줄여ㅜㄹ 수 있게 됨. 메모리를 지능적으로 관리.. 더 나은 메모리관리
  * Replication Improvement  => 선은ㅇ/지연 없이 높은 가용성 제공하고자 함 replication protocol.
    * w:majoryty 사용시 20% 향상 
* workload 성능 향상
  * 시각화 개선
  * Query Profiler 패널을 통해 z쿼리 프로파일러 성능 모니터링 가능 -> 문제로 식별된 쿼리는 깊게 들어가서 확인가능.
  * Query Shape 해쉬 획득 가능 -> 8.0 에서 도입한 새롱누 개념 => 애플리케이션에서 실행중인 동일한 쿼리를 그룹화. x=1 / x=2 는 같은 쿼리다.
  * 쿼리에 Rejection 필터 설정 가능
  * Persistence Query Setting : MongoDB 8.0에서 제공 가능 -> 쿼리 옵티마이저가 완벽할수는 없다. 개발자들은 쿼리 엔진에서 생성된 액션플랜과 다른 액션플랜을 원할때가 있음 -> 인덱스 필터는 서버리스타트시 초기화되어 사용이 어려움. 8.0에서 Persistence Query Setting 지원하여 쿼리쉐입별로 지원. 다시 인덱스필터를 restart 할 때 마다 저장할필요가 없다~
  * Default Timeout Redad Operations : 일부 쿼리는 다른 Timeout이 필요할 경우 Operation에서 설정하여 조정 가능
* 샤등/수평적확장 유연하게 + 비용절감
  * MongoDB 확장은 수직/수평 -> MongoDB는 수평확장을 샤딩으로 지원. 샤딩 좋죠~ 무한한 확장성 제공하지만 일부 사용 어렵고 비용이 많이 든다.
  * MongoDB 8.0에서 샤딩을 쉽고 저렵하게.. 샤딩 아키텍쳐를 저렴하게. 데이터 배포를 샤딩간 쉽게 할 수 있도록 만듦.
  * 8.0에서는 샤딩되지 않은 컬렉션을 다른 컬렉션으로 이동할 수 있도록 함. 
  * 부하높은 단일샤드(핫샤드) 해결책 -> 데이터 재분배 : 대부분 샤딩되지 않은 컬렉션 포함되어 있음.. 다시 샤딩하는게 정답 아닐수도 있음. => 샤딩되지 않은 컬렉션에서 다른 컬렉셔능로 쉽게 옮길 수 있음
  * 최대 50배 빠르게 리샤딩 가능!! -> 리소스를 빠르게 재분배 가능. 샤딩 프로세스가 여러분 작업 방해하지 않음. 리샤딩이 온라인 상태라. 기존작업 영향주지 않음. 샤드키  변경하지 않고도 리샤드 가능. 리샤드테크닉같은 복잡한 기능이 필요치 않음.
  * 빠르게 리샤딩 가능. 동적으로 확장하여 위험부담 적게 샤딩 실행 가능. 향후 10배 이상의 데이터 증가에 대한 걱정 할 필요 없음. -> 리샤딩 쉬워졌기 때문ㅇ
  * 임베딩 샤딩 컨피그 서버 : config 데이터를 클러스터데이터와 함께 콜로케이션 가능. 스케일업/아웃이 쉬워짐/추가비용 없이 샤딩
* 보안 향상
  * OpenId Connect supprot
  * Queryable Encryption Range Support -> 암호화된 데이터를 쿼리실행으로 보전? 서버가 처리중인 데이터를 처리 가능. 항상 암호화된 상태로 유지. range znjfl wldnjs. 8.0에서도 암호화된 필드에 대한 range 사용 가능. 민감한 보안 요건을 가진 고객 지원을 위해 최선중이예요
  * OCSF Logging Format : 로그부분 표준화가 부족... -=> 로그 수집에 어려움. ->문제 해결 위해 새로운 스키마 형태 OCSF 도입함. 감사로그를 OCSF 형식으로 output 하도록 허용. 외부모니터링시스템 쉽게 통합 가능. 로그형식을 normalize 하기 위해 추가 개발 필요 없어 애플리케이션 구축에 집중 가능.
