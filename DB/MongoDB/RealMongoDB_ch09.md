# Real MongoDB - ch09. 실행 계획 및 쿼리 최적화
사용할 인덱스 선별, 그룹핑 등 작업에 인덱스를 이용할건지 등의 절차를 수립하는 과정이 필요.


### 실행계획을 보는 방법 - `.explain()`
```
db.collection.find({쿼리..}).explain();
```

## 9.1 실행 계획
- FETCH -> IXSCAN
  - 인덱스 레인지스캔 실행 후 다음 컬렉션 데이터 파일에서 도큐먼트 읽는 실행 계획
- SORT -> COLLSCAN
  - 컬렉션 풀스캔으로 조건 일치하는 도큐먼트 읽은 후 정렬 수행
- SORT -> FETCH -> IXSCAN
  - 인덱스 레인지 스캔 실행 후 다음 컬렉션 데이터파일에서 도큐먼트 읽고, 그 결과 정렬하는 실행계획
- FETCH -> SORT_MERGE -> (IXSCAN, IXSCAN)
  - 인덱스 인터섹션(2개 서로 다른 인덱스에 대해 레인지 스캔 실행 후, 다음 결과 병합)으로 레인지 스캔 실행 후, 다음 컬렉션 파일에서 도큐먼트 읽는 실행계획


실행계획 트리의 최상위 스테이지를 루트 스테이지라 함. 쿼리가 실행되면 루트스테이지가 자식 스테이지를 호출. 각 스테이지를 호출하는 API 이름을 **work()**. 각 스테이지가 자기 자식 스테이지의 work()함수 호출하며 쿼리 처리.

work() 함수 호출
- ADVANCE : 한 건의 도큐먼트 ID값 반환
- NEED_TIME : 스테이지 처리는 완료되었으나, ID값 반환되지 않음 -> 블록킹스테이지 일 때 발생
- IS_EOF : 스테이지 처리 완료되었으며, 더이상 읽을 ID 없음

### 실행계획 수립
- MongoDB는 한 번 실행되었던 쿼리 실행결과는 캐시에 저장해둠, 같은 패턴 쿼리 오면 실행계획 재사용
  - 이를 알기 위해 아래 3가지 정보 사용(Query Shape)
  - 쿼리 조건(Query predicate)
  - 정렬조건(Sort)
  - 조화 필드(프로젝션, Projection)
```
>>> db.user.find({user_id:100}).sort({name:1})
// 실행계획 같은 경우
>>> db.user.find({user_id:121}).sort({name:1})
>>> db.user.find({user_id:121}).sort({name:1}).limit(10)


//실행계획 다른 경우
>>> db.user.find({user_id:100})
>>> db.user.find({user_id:100}).sort({age:1})
>>> db.user.find({user_id:100}, {_id:1, age:1}).sort({name:1})
```

- 컬렉션이 삭제되거나, 해당 컬렉션의 인덱스가 추가,삭제되는 경우 해당 컬렉션의 캐시된 실행계획은 모두 삭제됨

### 옵티마이저 옵션


## 9.2 쿼리 최적화
