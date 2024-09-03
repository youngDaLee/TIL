# MongoDB 데이터 모델링의 원리와 방법론

* RDBMS는 정규화를 통해 최적화된 형태로 데이터를 저장할 수 있다.
* NoSQL(Document) 데이터를 하나의 도큐먼트에 저장(array, document)
* Nested Document와 배열 중 어떤 모델을 사용해도 성능상 큰 차이는 없다. 데이터 유형을 고려한 선택이 필요하다
  * ex) 바퀴 데이터에서 해당 바퀴가 어디쪽 바퀴인지 필요하다->Object / 아니다 그냥 바퀴 종류만 필요하다 -> list


## Nested Document를 이용한 데이터 처리
one-to-one 관계형
* 특정 부분에 대한 형태를 nested 형채로 표현 가능

```json
{
    owner : "dayoung",
    make: "Audi",
    engine: {   // nested one-to-one
        power: 660hp,
        consuption: 10
    }
}
```
* 엔진 부분만 보고 싶으면 projection으로 해당 데이터만 골라서 볼 수 있다.

Tabular vs Document
* 모델 생성 단계
  * Tabular : 스키마정의 -> 앱과 쿼리 개발
  * MongoDB : Query도출 -> 스키마 정의
* 스키마 개선
  * Tabular : 어려우며 최적화 되지 않음. downtime 필요
  * MongoDB : 쉬움. no downtime -> 스키마 변경이 필요할 때, DB레이어에서 스키마변경으로 인한 downtime이 없다. 이 때문에 모델링이 개선된다.

Data Modeling Methodology
* Entities : 요구사항으로부터 도출
  * 해당 데이터가 어떤 데이터인지 파악(데이터 크기, 보존 기간, 분석 여부, 장애 모니터링 여부 등)
* Workloads
  * 해당 쿼리가 얼마나 수행되는지, CRUD중에 무엇인지, 어떤 정보를 write/read하는지, read시에 어떤 정보가 필요하고 어느 정도 시간당 어느 단위로 데이터가 오가는지, 트래픽이 어느정도인지...
  * 읽기에 대한것도 마찬가지.

Embedding vs Reference
* 읽는/쓰는 형태 중 workload 가 어떻게 이뤄져있는지를 파악하고 선택
* HeavyRead. 자동처 한번에 많이 읽는다 -> Embedding(합치는거)
* 각 콜렉션을 따로 보는 workload가 더 많다 -> Reference(분리)
* Havy write

관계
* Embedding
  * one-to-one : 한 번의 Read. Join 불필요
  * one-to-many : 한 번의 Read. Join 불필요
  * many-to-many : 한 번의 Read, Join 불필요, **데이터의 중복**
* Referenced
  * one-to-one : 몇 번의 Read. 다량의 Read
  * one-to-many : 몇 번의 Read. 다량의 Read
  * many-to-many : 한몇 번의 Read. 다량의 Read

패턴
* 4~50개 이상의 패턴으로 전략을 제공
* Computation
  * 근사값, 계산형
* Grouping
  * 버켓, 예외, 사전할당
* Life Cycle
  * 아카이브, 문서버져닝, envelope, 스키마 버져닝
* Polymorphism
  * 상속, 단일 컬렉션
* Relationships
  * Attribute, ...

## 패턴
Extended Refernce Pattern
* Join을 줄이기 위해 필요한 부분을 따로 가져가서 저장하는 형태
* 레퍼런스형태의 조인을 하지 않고 데이터를 읽을 수 있도록 하는 패턴.

Computed Pattern
* 미리 계산된 내용을 데이터에 집어넣는 패턴
* CPU 사용량을 줄여줌

Archive Pattenr
* 규제에 대해정의.
* 해당되는 곳에 데이터를 모아둠(S3같은)
* 사전에 메모해두고 찾기 위해서... 아카이브 해주는 것. 사전에 키를 넣어주는 것

Schema versioning Pattern
* 권고하는 패턴
* 기존 데이터에 스키마 구조가 변경이 되었을 때 마이그레이션 해야 하는 이슈가 있음 -> 사전에 스키마 버전에 대해 기재를 해주면 마이그레이션 시 downtime 갖지 않고 원하는 데이터만 갖춰서 마이그레이션 가능하다.
