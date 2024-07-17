# Section03: Indexes(18%)
## Unit 8: MongoDB Indexes
### Lesson 1: Using MongoDB Indexes in Collections
* indexes : search 를 쉽게 해 주는 것...
  * speed up queries
  * reduse disk I/O
  * reduce resource 필요
* _id 필드에는 디폴트로 인덱스가 걸려 있음.
* write작업(insert/update) 할 때 인덱스 데이터도 업데이트 되어야 함...
  * 불필요하고 중요하지 않은 인덱스는 삭제해야 한다


인덱스 타입
* single field index : 하나의 필드에 대한 인덱스
* compound index : 두개 이상의 필드에 대한 인덱스
* multikey indexes : array의 콘텐츠에 대해 인덱스를 거는 기능
  * ex: `addr.zip`

> Which of the following statements about indexes are correct? (Select all the that apply.)
> 인덱스에 대한 설명으로 옳은것은?

* A. Indexes are data structures that improve performance, support efficient equality matches and range-based query operations, and can return sorted results.
  * 인덱스는 equal 매칭과 범위검색, 소팅 기능을 향상시켜주는 데이터 구조이다
* C. Indexes are used to make querying faster for users. One of the easiest ways to improve the performance of a slow query is create indexes on the data that is used most often.
  * 인덱스는 쿼리를 빠르게 해주기 위해 사용된다. 슬로우쿼리를 해결하는 가낭 쉬운 방법은 자주 사용되는 데이터에 인덱스를 새엇ㅇ하는 것이다.

오답
* B. Indexes are automatically created based on usage patterns.
  * (X) 인덱스는 사용 패턴에 따라 자동 생성된다
* D. When using an index, MongoDB reads every document in a collection to check if it matches the query that's being run.
  * (X) 인덱스를 사용할 때 MongoDB는 모든 도큐먼트를 읽어 실행중인 쿼리와 일치하는지 확인한다


> Which of the following statements about indexes are true? (Select one.)

* B. Indexes improve query performance at the cost of write performance.
  * 인덱스는 읽기 성능을 향상시켜주고 쓰기 성능 비용을 요구한다


### Lesson 2: Creating a single filed index in MongoDB
Single Field Indexes
* 하나의 필드에 대한 인덱스
* `db.<collection>.createIndex({<fieldname>: <1|-1>}, <options>)`
* unique 인덱스는 해당 필드에 중복된 값을 허용하지 않는다 -> 인서트 시 해당 필드에 이미 값이 존재하면 에러를 리턴


`db.<collection>.getIndexes()`
* 해당 콜렉션에 생성된 인덱스 모음


`db.<collection>.explain().find(<query>)`
* 해당 쿼리에 대한 실행계획을 보여줌
* 실행계획의 스테이지 필드에서 확인할 수 있는 값
  * IXSCAN : 쿼리가 인덱스를 사용할 때 사용하는 인덱스를 나타내는 스테이지
  * COLLSCAN : 인덱스를 사용하지 않을 때 나타나는 스테이지
  * FETCH : 컬렉션에서 문서를 읽을 때 -> 인덱스를 사용해도 프로젝션을 하지 않아 인덱스 스캔을 하지 않을 때.. 따라서 콜렉션에 접근해야 할 때
  * SORT : 문서가 메모리에서 정렬되고 있을 때 -> 정렬을 하면 나타남


> What is a single field index? (Select one.)

* A. An index that supports efficient querying against one field

> You have a collection of customer details. The following is a sample document from the collection:
```
{
  "_id": { "$oid": "5ca4bbcea2dd94ee58162a6a" },
  "username": "hillrachel",
  "name": "Katherine David",
  "address": "55711 Janet Plaza Apt. 865\nChristinachester, CT 62716",
  "birthdate": { "$date": { "$numberLong": "582848134000" } },
  "email": "timothy78@hotmail.com",
  "Accounts": [
    { "$numberInt": "462501" },
    { "$numberInt": "228290" },
    { "$numberInt": "968786" },
    { "$numberInt": "515844" },
    { "$numberInt": "377292" }
  ],
  "tier_and_details": {}
}
```
> You create a single field index on the email field, with the unique constraint set to true:
```
db.customers.createIndex({email:1}, {unique:true}) 
```
> What would happen if you attempt to insert a new document with an email that already exists in the collection? (Select one.)
> 위와 같은 형태의도큐먼트 컬렉션에 아래와 같은 인덱스를 만들었을 때 이미 존재하는 이메일을 인서트 하면 어떤 일이 발생하는지?

* D. MongoDB will return a duplicate key error, and the document will not be inserted.
  * 이미 존재하는 이메일 필드로 도큐먼트를 인서트 하려 한다면 에러 발생
  * 그 외에도... 이미 데이터가 존재하는 콜렉션에 유니크필드 인덱스를 생성핮고자 하면 인덱스 생성이 막힘

### Lesson 3: Creating a multikey filed index in MongoDB
Multikey Indexes
* array 필드에 인덱싱
* sigle field, compound 둘 다 가능
* `db.<collection>.createIndex({<fieldname>: <1|-1>}, <options>)` 생성은 싱글필드와 마찬가지로 생성


> What is a multikey index? (Select one.)

* B. An index where one of the indexed fields contains an array

> What is the maximum number of array fields per multikey index? (Select one.)

* A. 1
  * Correct! The maximum number of array fields per multikey index is 1. If an index has multiple fields, only one of them can be an array.
  * 컴파운드 인덱스에서도 멀티키 인덱스는 하나만 선택할 수 있음

### Lesson 4: Working with compount indexes index in MongoDB
Compount Indexes
* 여러 필드에 대해 인덱스를 생성하는것. array필드를 하나만 포함하면 멀티키인덱스도 가능
* prefix 형태로 사용가능(왼쪽부터 매칭되는 애들...)

실행계획
* PROJECTION_COVERED : 모든 정보가 인덱스 스캔만으로 충족됨(콜렉션 도큐먼트를 읽지 않음)

> What is a compound index? (Select one.)

* C. An index that contains references to multiple fields within a document

> What is the recommended order of fields in a compound index? (Select one.)
> 컴파운드 인덱스 순서로 추천하는 것

* C. Equality, Sort, Range


### Lesson 5: Deleting MongoDB Indexes
Indexes는 쿼리 성능을 향상시켜주지만 쓰기 성능을 저하시킴.
* 사용하지 않는 인덱스는 삭제해야 함
* 다만 삭제한 뒤에 다시 인덱스를 재생성하는건 리소스를 사용하고, 잘못 삭제하면 쿼리 성능 저하를 발생시킴...
* 인덱스를 삭제하기 전 먼저 hide 해보는걸 권장함
  * `db.<collection>.hideIndex(<index>)`


* `db.<collection>.dropIndex(<indexName>)` : 지정된 인덱스 삭제
* `db.<collection>.dropIndexes()` : _id 제외한 모든 인덱스 삭제
* `db.<collection>.dropIndexes(<indexName>)` : 지정된 인덱스 삭제
* `db.<collection>.dropIndexes([<indexName1>, <indexName2>, ... ])` : 인덱스들 삭제

> What are the ramifications of deleting an index that is supporting a query? (Select one.)
> 인덱스를 삭제했을 때 파급되는 결과

* B. The performance of the query will be negatively affected.

> You have a collection of customer details. The following is a sample document from this collection:
```
{
  "_id": { "$oid": "5ca4bbcea2dd94ee58162a6a" },
  "username": "hillrachel",
  "name": "Katherine David",
  "address": "55711 Janet Plaza Apt. 865\nChristinachester, CT 62716",
  "birthdate": { "$date": { "$numberLong": "582848134000" } },
  "email": "timothy78@hotmail.com",
  "Accounts": [
    { "$numberInt": "462501" },
    { "$numberInt": "228290" },
    { "$numberInt": "968786" },
    { "$numberInt": "515844" },
    { "$numberInt": "377292" }
  ],
  "tier_and_details": {}
}
```
> You have an index on the email field. Here’s the command you used to create the index:
```
db.customers.createIndex({email:1})
```
> Before deleting it, you want to assess the impact of removing this index on the performance of the query. To do this, which command should you use? (Select one.)
> 인덱스 삭제 전 사이드 이펙트 확인하기 위해 어떤 명령어 써야함?

* D. hideIndex()

### Unit8 정리
* single-field : 하나의 필드 인덱스
* compound : 2~32개 필드 인덱스

Lesson 1 - Using MongoDB Indexes in Collections
- [MongoDB Docs: Indexes](https://www.mongodb.com/docs/manual/indexes/?_ga=2.67626584.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Indexes Reference](https://www.mongodb.com/docs/manual/reference/indexes/?_ga=2.67626584.810066485.1665291537-836515500.1666025886)

Lesson 2 - Creating a Single Field Index in MongoDB
- [MongoDB Docs: createIndex()](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/?_ga=2.67626584.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Unique Indexes](https://www.mongodb.com/docs/manual/core/index-unique/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Measure Index Use](https://www.mongodb.com/docs/manual/tutorial/measure-index-use/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: getIndexes()](https://www.mongodb.com/docs/manual/reference/method/db.collection.getIndexes/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)

Lesson 3 - Creating a Multikey Index in MongoDB
- [MongoDB Docs: Multikey Indexes](https://www.mongodb.com/docs/manual/core/index-multikey/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)

Lesson 4 - Working with Compound Indexes in MongoDB
- [MongoDB Docs: Compound Indexes](https://www.mongodb.com/docs/manual/core/index-compound/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Indexing Strategies](https://www.mongodb.com/docs/manual/applications/indexes/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)

Lesson 5 - Deleting MongoDB Indexes
- [MongoDB Docs: dropIndex()](https://www.mongodb.com/docs/manual/reference/method/db.collection.dropIndex/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: dropIndexes()](https://www.mongodb.com/docs/manual/reference/method/db.collection.dropIndexes/?_ga=2.55479138.810066485.1665291537-836515500.1666025886)


## Unit 9: MongoDB Indexes 2
### Lesson 1: How Indexes Work
* MongoDB는 B-Tree 에 인덱스 필드 값을 저장
* B-Tree : 자체 밸런싱 트리.. (Binary Tree가 아니라 Balanced Tree임. B-Tree는 자식 2개 이상일 수 있음)
  * B-Tree는 저장된 데이터를 왼 -> 오 순서대로 저장
* 컴파운드 인덱스에 대해서 하나의 왼쪽부터 상위 depth에 저장되도록...

> Which of the following statements describe a B tree? (Select all that apply.)

* A. B trees sort the stored data in ascending sequential order from left to right
  * B-Tree는 데이터를 왼->오 순으로 저장한다
* B. Nodes in a B tree can have more than two child nodes
  * B-Tree는 2개 이상의 자식 노드를 가질 수 있다
* D. A B tree is a self-balancing tree data structure
  * B-Tree는 self-balancing 데이터 구조이다


> Which index would most effectively support the following query? (Select one.) 
```
db.collection.find({ username: "j0hnny", timestamp: { $gte: ISODate("2021-05-18T00:00:00.000Z"), $lt: ISODate("2021-05-18T13:00:00.000Z") }})
```

* A. db.collection.createIndex({ username: 1, timestamp: 1 })
  * equal -> sort -> range 순서!!
  * 예전에 Real시리즈의 B-Tree 이미지 보면 이해됨..(첨부 이미지는 MySQL이긴 하지만)

<img width="477" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/09f246ef-9d29-4ddd-855b-178351eb4a59">


> Which index would most effectively support the following query? (Select one.)
```
db.collection.find({ timestamp: { $gte: ISODate("2021-05-18T00:00:00.000Z"), $lt: ISODate("2021-05-19T00:00:00.000Z") }, username: "j0hnny"}).sort({ rating: 1})
```

* B. Option B
  * 최대한 많이 항목을 필터링하고(equal) 이후 정렬하고, 정렬한 데이터에서 범위 검색


### Lesson 2: Index Usage Details via explain
`explain()`
* Query plan
* Execution statistics
* find 말고도 무언가를 찾는 쿼리(update, aggregate, mapReduce, delete 등등)에는 모두 사용 가능함


query planner
* 쿼리가 실행 될 때 마다 가장 효율적인 쿼리 플랜을 채택하고 캐싱함
* 쿼리플래너 캐시는 모든 콜렉션에 대해 가장 최근에 사용된 항목(LRU) 스타일로 항목을 저장
* LRU는 공간이 필요할 때 초기화 되지만, 몽고 재시작/인덱스 변경/컬렉션 드롭/명시적인 캐시 초기화(`db.<collection>.getPlanCache().clear()`) 로도 초기화 가능


실행계획에서는 문자열 매개변수를 전달해서 상세 정보를 조회할 수 있음 `explain(<method>)`
* queryPlanner
  * 디폴트. 매개변수를 명시하지 않으면 디폴트로 queryPlanner 모드를 사용함
  * 쿼리 구문분석
  * 쿼리 옵티마이저의 후보쿼리플랜과 위닝플랜을 보여줌
* executionStats
  * 인덱스에 대한 더 많은 정보를 포함하는 필드
  * nReturend : 쿼리 조건과 일치하는 문서 수
  * executionTimeMillis : 계획을 선택하고 실행하는데 걸린 시간
  * totalKeysExamined : 스캔된 인덱스 항목, 키의 수
  * totalDocsExamined : 쿼리 실행 중 조사된 document 수
  * executionStages : MongoDB가 inMemory에서 정렬을 수행했는지 여부 등을 나타냄
* allPlansExecution
  * 최상단에는 queryPlanner, executionStats 정보 보여줌
  * allPlansExecution 필드에서는 MongoDB에서 각각의 계획을 어떻게 평가했는지에 대해 보여줌 -> scores는 쿼리플랜통계를 사용해서 위닝플랜을 판별하는 공식을 기반으로 함


> From the following explain output, select the option that describes what the explain output it telling us: (Select one.)
```
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'sample_airbnb.listingsAndReviews',
    indexFilterSet: false,
    parsedQuery: {},
    queryHash: 'DD1CE27D',
    planCacheKey: 'DD1CE27D',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'SORT',
      sortPattern: { host: -1 },
      memLimit: 104857600,
      type: 'simple',
      inputStage: { stage: 'COLLSCAN', direction: 'forward' }
    },
    rejectedPlans: []
  },
  executionStats: {
    executionSuccess: true,
    nReturned: 5555,
    executionTimeMillis: 256,
    totalKeysExamined: 0,
    totalDocsExamined: 5555,
    executionStages: {
      stage: 'SORT',
      nReturned: 5555,
      executionTimeMillisEstimate: 130,
      works: 11113,
      advanced: 5555,
      needTime: 5557,
      needYield: 0,
      saveState: 13,
      restoreState: 13,
      isEOF: 1,
      sortPattern: { host: -1 },
      memLimit: 104857600,
      type: 'simple',
      totalDataSizeSorted: 100493513,
      usedDisk: false,
      spills: 0,
      inputStage: {
        stage: 'COLLSCAN',
        nReturned: 5555,
        executionTimeMillisEstimate: 0,
        works: 5557,
        advanced: 5555,
        needTime: 1,
        needYield: 0,
        saveState: 13,
        restoreState: 13,
        isEOF: 1,
        direction: 'forward',
        docsExamined: 5555
      }
    }
  },
  command: {
    find: 'listingsAndReviews',
    filter: {},
    sort: { host: -1 },
    '$db': 'sample_airbnb'
  },
  serverInfo: {
    host: 'M-C02GG1X2MD6M',
    port: 27017,
    version: '6.0.6',
    gitVersion: '26b4851a412cc8b9b4a18cdb6cd0f9f642e06aa7'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600
  },
  ok: 1
}
```

* C. The explain method was used in the executionStats mode. The query was not supported by an index. The winning plan was SORT, requiring an in memory sort to return the results in order.


> Which of the following fields can help us determine the effectiveness of an index? (Select all that apply.)
> 어떤 필드가 인덱스를 효과적으로 사용했는지 알려주는지

* A. nReturned
* C. totalDocsExamined
* D. executionStages
* E. totalKeysExamined

### Lesson 3: Optimzed compound indexes

### Lesson 4: Wildcard Indexes

### Lesson 5: Partial Indexes

### Lesson 6: Sparse Indexes

### Lesson 7: Clustered Indexes

### Lesson 8: Time Series Collections

### Lesson 9: How to monitor indexes

