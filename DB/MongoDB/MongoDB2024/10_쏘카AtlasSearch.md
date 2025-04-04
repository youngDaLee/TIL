# 쏘카에서 MongoDB Atlas Search로 쉽고 빠르게 검색엔진 구축하기

## About 쏘카
* 숙박 예약 서비스를 도입 -> 숙박 리스트 리턴하는 검색 엔진이 필요했음

## MongoDB Altas Search
* 샤딩을 통한 수평확장 지원, HA 지원...
* 빠른 Read/Write 지원하여 트랜잭션 볼륨 큰 어플리케이션에서도 적합함.
* 복잡한 쿼리/분석에도 도움됨

Atlas Search
* 텍스트 검색, 랭킹, 복합쿼리 등등 다양한 쿼리 지원
* Atlas Search는 시스템 아키텍쳐도 단순화했기 때문에 관리도 용이함

## 쏘카에서 Atlas Search를 검색엔진으로 구현한 사례
### Problem & Choice
* 통합검색과 같이 고도화된 검색조건 필터링이 필요했음
* -> MongoDB는 러닝커브가 높지 않았고, 유연하게 대응 가능해야 했고(검색은 추후 고도화 될 수 있음), 안정성/성능에서 검증되었다고 생각함

서비스
* 코드로 전처리하는 과정,...
* 검색용 배치(SpringBatch)로 데이터 전처리

### Index & Query
* 이름/주소는 한글로 의미를 나눠 검색하기 때문에 Analyzer를 nori로 설정하고,
* 정확한 필터링이 필요한 경우는 -> (다른 analyzer 놓침)

검색용 DB로 MongoDB 따로 관리하고 있었음..
* 필터 추가하는것만으로 검색 필터링 가능
* aggregation 만으로 원하는 검색 기능 구현 가능했음

### Deploy & Monitoring
* 빠른 응답으로 사용자 경험에 불편함이 없엇다..
