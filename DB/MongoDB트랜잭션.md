# MongoDB 에서 트랜잭션을 다루는 방법
트랜잭션이 없는 몽고DB에서도 유저 결제 등에서는 트랜잭션이 꼭 필요한 순간이 있다.  
MongoDB 4.0에서 부터 제공하는 transaction 기능에 대해서 알아보자

## MongoDB 의 트랜잭션
* 트랜잭션은 세션 내에서 실행됨
  * 세션: 클라이언트와 MongoDB 서버 간의 연결
* 단일 문서 작업에서 원자성을 보장(임베디드 문서 사용하면 분산 트랜잭션 필요성 최소화 가능). 동일한 replica set이나 shard 내 데이터 간의 트랜잭션에 대해 ACID 속성을 보장
* 분산 트랜잭션: MongoDB 4.2 이상에서는 sharded cluster에서도 트랜잭션을 지원. 다중문서, 다중콜렉션 작업에 원자성이 필요한 경우 사용

* 단일 문서 작업의 원자성
  * 임베디드 문서와 배열 사용으로 단일 문서 내 데이터 관계를 모델링하여 다중 문서 트랜잭션 필요성을 줄임
* 분산 트랜잭션
  * 여러 작업, 컬렉션, 데이터베이스, 샤드에 걸쳐 원자성을 보장
  * 트랜잭션은 커밋되거나 롤백되며, 커밋 전까지 외부에서 볼 수 없음
  * 커밋 후에도 샤드 간 데이터 일관성은 읽기 설정에 따라 다를 수 있음
  * 대부분의 경우 분산 트랜잭션은 단일 문서 쓰기에 비해 더 큰 성능 비용이 발생하므로 분산 트랜잭션의 가용성이 효과적인 스키마 설계를 대체할 수는 없다 -> 비정규화된 데이터 모델 (내장된 문서 및 배열) 권장 -> 적절한 모델링으로 트랜잭션 최소화 필요..


* 트랜잭션 API
  * withTransaction 콜백 API를 통해 트랜잭션 관리.
  * 주요 기능
    * 트랜잭션 시작
    * 작업 수행 및 오류 시 종료
    * 커밋 또는 롤백 처리
```javascript
  // Step 1: Start a Client Session
  const session = client.startSession();
  // Step 2: Optional. Define options to use for the transaction
  const transactionOptions = {
    readPreference: 'primary',
    readConcern: { level: 'local' },
    writeConcern: { w: 'majority' }
  };
  // Step 3: Use withTransaction to start a transaction, execute the callback, and commit (or abort on error)
  // Note: The callback for withTransaction MUST be async and/or return a Promise.
  try {
    await session.withTransaction(async () => {
      const coll1 = client.db('mydb1').collection('foo');
      const coll2 = client.db('mydb2').collection('bar');
      // Important:: You must pass the session to the operations
      await coll1.insertOne({ abc: 1 }, { session });
      await coll2.insertOne({ xyz: 999 }, { session });
    }, transactionOptions);
  } finally {
    await session.endSession();
    await client.close();
  }
```

스키마 설계와 성능 고려
* 대부분의 시나리오에서 비정규화된 스키마 설계를 통해 트랜잭션 필요성을 최소화.
* 분산 트랜잭션은 성능 비용이 크므로 신중히 사용.

읽기/쓰기 설정
* 트랜잭션 작업은 트랜잭션 수준 설정을 우선적으로 사용.
* 설정이 명시되지 않은 경우 세션 또는 클라이언트 수준 기본값 적용.

### 1. 트랜잭션의 기본 사용법
1) 세션 시작: 트랜잭션은 세션을 통해 실행되며, 세션을 명시적으로 생성해야 한다
```go
session, err := client.StartSession()
if err != nil {
    log.Fatalf("Failed to start session: %v", err)
}
defer session.EndSession(context.Background())
```

2) 트랜잭션 실행 : 세션의 WithTransaction 메서드를 사용하여 트랜잭션을 실행합니다.

```go
ctx := context.Background()
err = session.WithTransaction(ctx, func(sessCtx mongo.SessionContext) (interface{}, error) {
    collection := client.Database("test").Collection("orders")

    // 첫 번째 작업
    _, err := collection.InsertOne(sessCtx, bson.D{{"item", "apple"}, {"qty", 10}})
    if err != nil {
        return nil, err
    }

    // 두 번째 작업
    _, err = collection.UpdateOne(sessCtx, bson.D{{"item", "banana"}}, bson.D{{"$set", bson.D{{"qty", 20}}}})
    if err != nil {
        return nil, err
    }

    return nil, nil
})

if err != nil {
    log.Fatalf("Transaction failed: %v", err)
}
```

3) 트랜잭션 옵션 설정 : 트랜잭션의 읽기 및 쓰기 일관성 수준을 설정할 수 있다

```go
txnOpts := options.Transaction().
    SetReadConcern(readconcern.Snapshot()).
    SetWriteConcern(writeconcern.New(writeconcern.WMajority()))
err = session.WithTransaction(ctx, txnFunc, txnOpts)
```

### 2. 트랜잭션의 한계
* 트랜잭션은 MongoDB의 장점인 빠른 쓰기 성능을 저하시킬 수 있다 -> 가능한 최소한의 데이터만 포함하도록 설계
* 메모리에 유지되는 작업 집합이 너무 크면 제한이 발생할 수 있습니다.
* TTL: 트랜잭션은 기본적으로 60초 후에 타임아웃(필요시 연장 가능)

### 3. 제약 사항
* 특정 시스템 컬렉션이나 제한된 작업 사용 불가
* 고정 크기 컬렉션에서 "snapshot" 읽기 설정 불가

### 4. 주의 사항
* Replica Set 또는 Sharded Cluster 환경에서만 트랜잭션이 지원됨 -> Standalone MongoDB 서버에서는 사용할 수 없다
* 트랜잭션의 주요 원칙은 작게 유지하고 빠르게 커밋하는 것 -> 이는 시스템의 성능을 유지하는 데 중요
* 트랜잭션을 설정하기 전에 필요한 컬렉션이 존재하도록 준비
* 복잡한 작업을 수행할 때는 트랜잭션의 성능 비용과 제약 사항을 고려
* MongoDB 드라이버 및 버전이 트랜잭션 지원 여부와 호환성을 보장하도록 최신 상태 유지
* MongoDB의 트랜잭션은 데이터 모델링 설계와 성능 최적화의 균형을 잘 맞춰야 효율적으로 가능


## 추가
* 충돌 발생했을 때 디폴트로 어떻게 DB에서 처리되는지 
* 드라이버에서 타임아웃 되었을 때 롤백되는지
* 락이 가능하지, 롤백 가능한지

## 회사 코드에서 MongoDB 트랜잭션


