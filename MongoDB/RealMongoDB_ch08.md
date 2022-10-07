# Real MongoDB - ch08. 쿼리 개발과 튜닝
## 8.1 기본 CRUD 쿼리
|   SQL     |   MongoDB BSON    |
|:---------:|:-----------------:|
|INSERT|db.collection.insert()|
|Bathced DML(INSERT, UPDATE, DELETE)|db.collection.bulkWrite()|
|UPDATE / REPLACE / INSERT...ON DUPLICATE KY UPDATE....|db.collection.update() / db.collection.update({}, {$set:{}}, {upsert:true})|
|DELETE|db.collection.remove()|
|SELECT|db.collection.find()|
|SELECT...GROUP BY...|db.collection.aggregate() / MapReduce|

### 8.1.1 쿼리 작성
느낀점 : 전체적으로 RDBMS와 다르게, 각 스키마마다 테이블을 설계하고, 각 테이블에 데이터를 인서트 하는 것이 아닌, 그때그때 컬렉션(테이블)에 JSON형식 데이터를 인서트하는 식으로 동작하는 듯 하다. 8장 먼저 공부 후 7장을 공부할 예정이라.. 이 부분은 7장에서 더 공부할예정
#### INSERT
도큐먼트를 하나씩 저장
```
>>> db.book.insert({name:"test", author:"dylee"});
>>> db.book.insert({name:"test", author:"dylee2"});
```
![image](https://user-images.githubusercontent.com/64643665/194544552-719c0c8e-39c2-477e-95df-2cacfebeda90.png)


도큐먼트를 한 번에 저장
```
>>> db.book.insert([{name:"test", author:"dylee4"}, {name:"test", author:"dylee5"}]);
```
![image](https://user-images.githubusercontent.com/64643665/194545068-5f552e85-0bfc-4168-bf1d-3e6258a6cfb7.png)

JSON 문법 상 위 문법은 두 가지로 해석 될 수 있음
1. 도큐먼트 두 개
2. 2개의 서브도큐먼트를 배열로 가지는 도큐먼트 하나

MongoDB 서버는 1번으로 해석 -> **최상위 레벨 배열을 허용하지 않기 때문**
- 자세한 내용은 "7.1.6 제한사항" 절 참고


insert의 두 번째 절로 아래 두 가지가 올 수 있음
- writeConcern : 어떤조건에서 "완료" 응답 반환할지 결정
- ordered: 첫번째 인자가 배열일 때, ordered가 true이면 나열된 도큐먼트 순서대로 인서트 하기 위해 단일스레드로 동작, false이면 멀티스레드로 배분하여 동시에 insert 수행. 디폴트는 true
```
>>> db.book.insert([{name:"test", author:"dylee6"}, {name:"test", author:"dylee7"}, {name:"test", author:"dylee8"}], {ordered:false});
>>> db.book.insert({name:"test", author:"dylee9"}, {writeConcern:{w:1,j:true}});
```
- insert 시 조그마한 실패는 무시하고 최대한 빠르게 데이터 적재하고자 할 때 ordered 옵션 false로 사용.

미리 ObjectID를 생성해서 할당하는 방식으로 _id 필드 값 확인 가능
```
>>> var newId = new ObjectId()
>>> print(newId)
>>> db.book.insert({_id:newId,name:"id",author:"dylee"})
```


#### UPDATE
Insert와 달리 3개 인자 사용. 세번째 인자는 선택 옵션
```
>>> db.book.update(
    {author:"dylee"},           // 업데이트 대상 도큐먼트 검색 조건
    {$set: {name:"update"}},    // 업데이트 내용 -> $set 인자가 없으면 기존 도큐먼트 내용을 그대로 덮어씌워버림!!!(기존 도큐먼트 삭다 삭제하고 name:'update'만 남음)
    {upsert:true}               // 도큐먼트 업데이트 옵션
)
```
update 두 번째 인자에 사용가능한 오퍼레이터들
- $nc : 필드값을 주어진만큼 증가시켜 저장
- $mul : 필드의 값을 배수로 저장
- $rename : 필드 이름 변경
- $setOninsert : $set과 동일한 방식으로 사용하지만 upsert 옵션이 true인 경우, UPDATE 명령할 도큐먼트 찾지 못해 INSERT 실행할 경우 해당 내용 적용. 
- $set : 도큐먼트 필드 값 변경
- $unsert : 도큐먼트 필드 삭제
- $currentDate : 필드 값을 현재 시작으로 변경


update 세 번째 인자에 설정가능한 옵션들
- upsert : INSERT에서는효과 X... UPDATE에서만 사용 가능. 디폴트 false
  - false : UPDATE 조건에 맞는 도큐먼트 찾지 못해도 UPDATE 명령이 어떤 변경도 발생 x
  - true : UPDATE할 내용으로 새로운 도큐먼트 INSERT
- multi : 디폴트는 false
  - false : 검색조건에 일치하는 도큐먼트 2개 이상이어도 한개만 변경.
  - true : 조건에 일치하는 모든 도큐먼트 변경
- writeConcern : UPDATE 명령이 어떤 조건에서 완료 응답 반환할지 결정. 도큐먼트 포멧
- collation : 문자셋 콜레이션 명시


배열필드 업데이트 방식
```
>>> db.order_status.insert(
    {
        order_id:1,
        items:[
            {item_id:1,status:"complete"}, 
            {item_id:2,status:"delivery"}
        ]
    }
)

>>> db.order_status.update(
    {order_id:1},
    {
        $push: {
            items:{item_id:3, status:"complete"}
        }
    }
)
```

#### DELETE
2개 인자 사용. 2번째는 선택옵션
```
>>> db.book.remove(
    {name: "dylee"}, // 삭제 대상 도큐먼트 검색 조건
    {justoOne: true} // 도큐먼트 삭제 옵션
)
```
두 번째 옵션
- justOne : DELETE는 UPDATE와 달리, 여러 도큐먼트가 삭제되는게 디폴트. (justOne옵션 디폴트는 false) true로 변경시, 조건에 일치하는 첫번째 도큐먼트만 삭제함
- writeConcern : 어떤 조건에서 완료 응답 받을지
- collation : 삭제 대상 도큐먼트 콜레이션 명시.


컬렉션의 모든 도큐먼트 삭제할 시, 컬렉션 자체를 삭제하고 직접 생성하는게 빠름
```
>>> db.book.remove({})  // remove로 모든 도큐먼트 삭제 -> 느림
>>> db.book.drop()      // 컬렉션 자체를 삭제 -> 빠름
```

**격리된($isolated) UPDATE와 REMOVE**
- $isolation 옵션 사용 시, UPDATE, REMOVE 명령 완료 전 까지 다른 커넥션에서 변경 내용 확인 불가함
```
>>> db.book.remove({name: "dylee", $isolated:1},{justoOne: true})
```
- 꼭 필요한 경우에만 제한적으로 사용 권장.. -> 잠금을 걸기 때문에 수많은 쿼리와 업데이트 명령들이 일시적으로 처리를 멈추게 되고, db 응답 받지 못해 많은 스레드와 커넥션을 생성하며 처리 불가 상태로 전환될 수 있음


#### BulkWrite
데이터 변경 명령 다 모아서 처리 가능
```
>>> db.test.bulkWrite(
    [
        {
            insertOne: {
                document: {
                    _id: 4,
                    name: "test"
                }
            }
        },
        {
            insertOne: {
                document: {
                    _id: 5,
                    name: "dylee"
                }
            }
        },
        {
            updateOne: {
                filter: {name: "dylee"},
                update: {$set: {status: "aaa"}}
            }
        },
        {
            deleteOne: {
                filter: {name: "test"}
        },
        {
            replaceOne: {
                filter: {name: "dylee"},
                replacement: {name: "dylee2", class: "oracle"}
            }
        }
    ]
)
```


#### FIND
MongoDB에서 데이터를 조회하는 명령. 2개 인자 사용 - 첫 번째 인자는 도큐먼트 검색 조건, 두 번째 인자는 클라이언트 반환 필드 명시. 두 인자 다 선택 옵션임
```
>>> db.book.find()                              // 전체 조회
>>> db.book.find({})                            // 전체 조회
>>> db.book.find({}, {_id:0, name:1, score:1})  // _id 컬럼 조회 x, name, score 필드 조회
```
- 두 번째 인자에서, 조회할 필드는 1, 조회하지 않을 필드는 0으로 표기함.
  - MongoDB에서는 일부 필드에 대해 명시하면, 나머지 명시되지 않은 필드는 그 반대로 자동으로 설정됨


#### Find 연산자
**비교 오퍼레이터**
|연산자|SQL표기|사용예|
|:---:|:---:|:---|
|$eq | = | db.user.find({name: { $eq: "matt"}}) |
|$gt | > | db.user.find({score: { $gt: 86}}) |
|$gte | >= | db.user.find({score: { $gte: 86}}) |
|$lt | < | db.user.find({score: { $lt: 86}}) |
|$lte | <= | db.user.find({score: { $lte: 86}}) |
|$ne | <> 또는 != | db.user.find({name: { $ne: "matt"}}) |
|$n | IN | db.user.find({name: { $n: ["matt", "dy"]}}) |
|$nin | NOT IN | db.user.find({name: { $nin: ["matt", "dy"]}}) |


**논리 결함 오퍼레이터**
|연산자|SQL표기|사용예|
|:---:|:---:|:---|
|$or | OR | db.user.find({ $or : {name: { $eq: "matt"}}, {score: { $gt: 86}}}) |
|$and | AND | db.user.find({ $and : {name: { $eq: "matt"}}, {score: { $gt: 86}}}) |
|$not | NOT | db.user.find({ $not : {score: { $gt: 86 }}) |
|$nor | 배열로 주어진 모든 표현식에 일치하지 않는지 비교 | db.user.find({ $nor : {name: { $eq: "matt"}}, {score: { $gt: 86}}}) |
- 기본적으로 FIND 쿼리 검색조건은 AND


**필드 메타 오퍼레이터**
|연산자|SQL표기|사용예|
|:---:|:---:|:---|
|$exists | 도큐먼트가 필드를 가졌는지 확인 | db.user.find({name: { $exists:"matt"}}) |
|$type | 필드의 데이터타입을 비교 - 타입별 숫자 코드/명은 공식문서 참고 | db.user.find({name: { $type: 2}}) |


**평가 오퍼레이터**
|연산자|SQL표기|사용예|
|:---:|:---:|:---|
|$mod | 모듈러(%) 연산 수행 결과값 비교 | db.user.find({score: { $mod: [10, 0]}}) - score 필드값 10으로 나눈 값이 0인 도큐먼트 반환|
|$regex | 정규표현식 비교 수행 | db.user.find({name: { $regex: '^matt'}})|
|$text | 전문검색 비교 수행 | db.user.find({ $text: { $search: "matt"}})|
|$where | 주어진 자바스크립트 표현식에 이치하는 도큐먼트만 반환 | db.user.find({ $where: "obj.low_score>obj.high_score"})|


## 8.2 확장 검색 쿼리

## 8.3 스키마 변경(DDL)

