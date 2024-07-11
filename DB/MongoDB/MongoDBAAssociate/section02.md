# Section01: CRUD(26%)
## 자격증 목차

## Unit 5: MongoDB CRUD Operations: Insert and Find Documents
### Lesson 1: Inserting Documents in a MongoDB Collection
* `db.<collection>.insertOne({})`
* `db.<collection>.insertMany([{}, {}, ...])`
* 콜렉션이 없으면 콜렉션을 생성해준다
* 모든 콜렉션은 _id 필드를 가져야 한다
  * 해당 필드는 유니크해야하며, 지정하지 않을 시 ObjectID로 자동생성해준다

> Select an answer choice and then click "See Results" to submit.
> What methods are available in MongoDB for inserting a single document? (Select one.)

정답
* A. .insertOne()

> Select an answer choice and then click "See Results" to submit.
> What methods are available in MongoDB for inserting multiple documents? (Select one.)

정답
* D. .insertMany()

### Lesson 2: Finding Documents in a MongoDB Collection
* `db.<collection>.find()`
  * {<field>: <val>} === { <field>: { $eq : <val> }}
  * {<field>: {$in: [<vals>, ...]}}

> Select an answer choice and then click "See Results" to submit.
> What methods are available in MongoDB for finding documents? (Select one.)

* A. .find()

> You are searching for data on a small area in downtown Chicago with the following zip codes:
> Which of the following query documents should you use to ensure that only the documents with the specified zip codes are returned? (Select one.)

* B. { zip: { $in : [ "60601", "60602", "60603", "60604", "60605", "60606"] } }

### Lesson 3: Finding Documents by using Comparsion Operators
* `<field>: {<operator> : <value>}`
* operator
  * `$gt` : greater than
  * `$lt` : less than
  * `$gte` : greater than or equal
  * `$lte` : less than or equal

> Select an answer choice and then click "See Results" to submit.
> Your company is conducting research on the customer experience and is focused on identifying unsatisfied customers. You need to find all customers with a satisfaction rating of 1 or 2.
> Which of the following query documents would return all customers with a satisfaction rating of 1 or 2? (Select one.)

* D. { "customer.satisfaction" : { $lte : 2}}

오답
* B. { customer.satisfaction : { $lte : 2}}
  * subdocument를 검색할 때는 quotation mark( `"` )를 반드시 써야 함

> Select an answer choice and then click "See Results" to submit.
> Your company wants to offer a special discount for customers who are 65 or older. Your task is to find the records for these customers. Which of the following queries would return documents for all customers 65 or older? (Select all that apply.)

* C. { "customer.age" : { $gte : 65 }}
* B. { "customer.age" : { $gt : 64 }}

### Lesson 4: Querying on array elements in MongoDB
* 일반 `$eq` 구문으로도 배열 안의 특정 요소를 포함하는 데이터를 조회할 수 있음
* `$elemMatch`
  * 배열 안에 요소를 포함하는 도큐먼트를 리턴함
  * 서브 도큐먼트를 포함하는 조건을 리턴함
  * elemMatch의 조건 중 하나라도 일치하면 리턴함
  * ``

> Select one answer choice and then click "See Results" to submit. (Select one.)
> Which of the following operators can be used to find a subdocument that matches specific criteria in an array?

* B. $elemMatch

> Select one or more answer choices and then click "See Results" to submit.
> What will the following query return? (Select one.)

* A. All documents where the genre field is equal to either the scalar value of “Historical” or an array that contains “Historical”.

### Lesson 5: Finding Documents by Using Logical Operators
* `$and`
```
db.<collection>.find({
    $and: [
        {<expression>},
        {<expression>},
        ...
    ]
})

db.<collection>.find({<expression>, <expression>, ...})
```

* `$or`
```
db.<collection>.find({
    $or: [
        {<expression>},
        {<expression>},
        ...
    ]
})
```
    * 같은 depth에 $or이 같이 있어선 안됨

> Select one or more answer choices and then click "See Results" to submit.
> You want to know which mobile food trucks in your neighborhood, Astoria, are the best spots to eat. Using the inspections collection, you’re making a map of all mobile food trucks nearby that have passed inspection. What should you include in your query document to ensure that you find all the mobile food vendors in Astoria that passed inspection? (Select one.)

* C. { "sector": "Mobile Food Vendor - 881" , "address.city": "ASTORIA" , "result": "Pass"}

> Select one or more answer choices and then click "See Results" to submit.
> What will the following query return? (Select one.)
```
db.routes.find({
  $and: [
    { $or: [{ dst_airport: "IST" }, { src_airport: "IST" }] },
    { $or: [{ stops: 0 }, { airline.name: "Turkish Airlines"}] },
  ]
})
```
* A. All flights departing from or landing at the Istanbul airport (IST) that are nonstop or operated by Turkish Airlines.

### Unit 5 정리

Lesson 1 - Inserting Documents
- [MongoDB Docs: insertOne()](https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/)
- [MongoDB Docs: insertMany()](https://docs.mongodb.com/manual/reference/method/db.collection.insertMany/)

Lesson 2 - Finding Documents
- [MongoDB Docs: find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/)
- [MongoDB Docs: $in](https://docs.mongodb.com/manual/reference/operator/query/in/)

Lesson 3 - Finding Documents Using Comparison Operators
- [MongoDB Docs: Comparison Operators](https://docs.mongodb.com/manual/reference/operator/query-comparison/)

Lesson 4 - Querying on Array Elements
- [MongoDB Docs: $elemMatch](https://docs.mongodb.com/manual/reference/operator/query/elemMatch/)
- [MongoDB Docs: Querying Arrays](https://docs.mongodb.com/manual/tutorial/query-array-of-documents/#combination-of-elements-satisfies-the-criteria)

Lesson 5 - Finding Documents Using Logical Operators
- [MongoDB Docs: Logical Operators](https://docs.mongodb.com/manual/reference/operator/query-logical/)

## Unit 6: MongoDB CRUD Operations: Replace and Delete Documents
### Lesson 1: Replacing a Document in MongoDB
* `db.<collection>.replaceOne(<filter>, <replacement>)`
  * 리턴으로 변경된 document수를 리턴

> Which of the following statements regarding the `replaceOne()` method for the MongoDB Shell (`mongosh`) are true? (Select all that apply.)

* A. This method is used to replace a single document that matches the filter document.
* B. This method accepts a filter document, a replacement document, and an optional options document.
* D. This method returns a document containing an acknowledgement of the operation, a matched count, modified count, and an upserted ID (if applicable).

오답
* C. This method can replace multiple documents in a collection.
  * 필터에 매칭되는 도큐먼트 중 하나의 도큐먼트만 수정함

> You want to replace the following document from the birds collection with a new document that contains additional information on recent sightings, the scientific name of each species, and wingspan. What field should you use in the filter document to ensure that this specific document is replaced? (Select one.)
```
{ _id: ObjectId("6286809e2f3fa87b7d86dccd") },
  {
    common_name: "Morning Dove",
    habitat: ["urban areas", "farms", "grassland"],
    diet: ["seeds"]
  }
```

* A. { _id: ObjectId("6286809e2f3fa87b7d86dccd") }

### Lesson 2: Updating MongoDB Documents by Using updateOne()
* `db.<collecction>.updateOne(<filter>, <update>, {options})`
  * `$set` : 새 필드를 추가하거나, 필드의 값을 새로운 값으로 대체하거나
  * `$push` : array 필드에 값을 추가하거나, array필드를 추가하거나
* `upsert` : 도큐먼트가 없으면 insert하고, 있으면 update하고

> You want to add an element to the items array field in the sales collection. To do this, what should you include in the update document? (Select one.)

정답
* { $push: { items:[{ “name”: "tablet", “price”: 200}] } }
  * 리스트에 있는 값들을 모두 추가해줌

오답
*  { $set: { items:[{ “name”: "tablet", “price”: 200}] } }
   *  해당 플드로 대체가 되어버림

> Air France has recently passed inspection. In the following document, you need to update the results field from Fail to Pass. To do this, what should you include in your update document? (Select one.)
```
{
  _id: ObjectId("56d61033a378eccde8a837f9"),
  id: '31041-2015-ENFO',
  certificate_number: 3045325,
  business_name: 'AIR FRANCE',
  date: 'Jun  9 2015',
  result: 'Fail',
  sector: 'Travel Agency - 440',
  address: {
    city: 'JAMAICA',
    zip: 11430,
    street: 'JFK INTL AIRPORT BLVD',
    number: 1
  }
}
```

*  { $set: {result: ‘Pass’} }

### Lesson 3: Updating MongoDB Documents by Using findAndModify()
* `db.<collection>.findAndModify({query: <filter>, update: <update>, new: <true/false>})`
  * find하고 modify하면 두 번 쿼리를 하게 됨..
  * new를 true로 하면 원본이 아니라 업데이트 된 문서를 반환. 기본값은 false

> Using the zips collection, you write the following query. This query updates the population, which is stored in the pop field, in one zip code in Santa Fe, New Mexico. What will be returned? (Select one.)

```
db.zips.findAndModify({
  query: { _id: ObjectId("5c8eccc1caa187d17ca72ee7") },
  update: { $set: { pop: 40000 } },
  new: true,
})
```

* A. The updated document, which contains a population of 40000


> What would happen if you ran the following query on the zips collection? Note that there is currently no document for the city of Taos. (Select one.)
```
db.zips.findAndModify({
  query: { zip: 87571 },
  update: { $set: { city: "TAOS", state: "NM", pop: 40000 } },
  upsert: true,
  new: true,
})
```

* B. A new document would be inserted because the upsert option is set to true.

### Lesson 4: Updating MongoDB Documents by Using updateMany()
* `db.<collection>.updateMany(<filter>, <update>, {option})`
  * 여러 도큐먼트를 업데이트

> Three computer science classes, with the class_ids of 377, 259, and 350, have earned 100 extra credit points by competing in a hackathon. You need to update the database so that all students who are in these classes receive extra credit points. Note that you will use the grades collection, which is in the sample_training database. 
> Which of the following queries will accomplish this goal? (Select one).

```
db.grades.updateMany(
  {
    class_id: {
$in: [ 377, 259, 350 ]
    },
   },
  {
    $push: {
      scores: [ 
{ type : 'extra credit', score: 100 }
]
    }
  }
)
```

### Lesson 5: Deleting Documents in MongoDB
* `db.<collection>.deleteOne(<filter>, {options})`
* `db.<collection>.deleteMany(<filter>, {options})`

> United Airlines is the only airline that has a route from the Denver Airport (DEN) to the Northwest Arkansas Airport (XNA). It has decided to cancel this route due to low ridership.
> Which of the following queries will delete the route? (Select one.)
> Note that these documents are contained in the routes collection in the sample_training database.

```
db.routes.deleteOne({ src_airport: "DEN", dst_airport: "XNA"})
```

> Air Berlin has filed for bankruptcy and ceased operations. You need to update the routes collection to delete all documents that contain an airline name of Air Berlin. Which of the following queries should you use? (Select one.)

```
db.routes.deleteMany({ "airline.name": "Air Berlin"})
```

### Unit 6 정리
Lesson 01: Replacing a Document in MongoDB
- [MongoDB Docs: replaceOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/?_ga=2.56665699.810066485.1665291537-836515500.1666025886)

Lesson 02: Updating MongoDB Documents by Using `updateOne()`
- [MongoDB Docs: Update Operators](https://www.mongodb.com/docs/manual/reference/operator/update/?_ga=2.56665699.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: $set](https://docs.mongodb.com/manual/reference/operator/update/set/?_ga=2.56665699.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: $push](https://docs.mongodb.com/manual/reference/operator/update/push/?_ga=2.34644840.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: upsert](https://www.mongodb.com/docs/drivers/node/current/fundamentals/crud/write-operations/upsert/?_ga=2.123127490.810066485.1665291537-836515500.1666025886)

Lesson 03: Updating MongoDB Documents by Using `findAndModify()`
- [MongoDB Docs: findAndModify()](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/?_ga=2.123127490.810066485.1665291537-836515500.1666025886)

Lesson 04: Updating MongoDB Documents by Using `findAndModify()`
- [MongoDB Docs: updateMany()](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany/?_ga=2.123127490.810066485.1665291537-836515500.1666025886)

Lesson 05: Deleting Documents in MongoDB
- [MongoDB Docs: deleteOne()](https://www.mongodb.com/docs/v5.3/reference/method/db.collection.deleteOne/)
- [MongoDB Docs: deleteMany()](https://www.mongodb.com/docs/v5.3/reference/method/db.collection.deleteMany/?_ga=2.23103219.810066485.1665291537-836515500.1666025886)


## Unit 7: MongoDB CRUD Operations: Modifying Query Results
### Lesson 1: Sorting and Limiting Query Results in MongoDB
* cursor
  * 쿼리 결과값 포인터.
  * find()는 커서를 리턴함
  * Cursor methods는 쿼리를 변경하고 결과셋을 정렬하는 등 전처리 가능
* cursor.sort() : 정렬
* cursor.limit() : 제한
* projection : 쿼리에서 필요한 부분만 조회 가능
* limit : 성능 향상 가능

> Using the inspections collection within the sample_training database, you need to find all inspections that were passed. Your manager has requested that you organize this data by the certificate number in ascending order. Which query should you use? (Select one).

* `db.inspections.find( { result : "Pass" }).sort( {certificate_number: 1});`

> You are considering creating a new membership tier for your bike sharing service for users who take long trips. Using the trips collection within the sample-training database, you need to find the trips, taken by subscribers, with the longest trip duration. Return the top 5 results in descending order. Which query should you use? (Select one.)

* `db.trips.find( { usertype: "Subscriber"}).sort( { tripduration:  - 1 }).limit(5)`

### Lesson 2: Returning Specific Data from a Query in MongoDB
* projection : 쿼리의 특정 부분만 리턴해줌

> Which of the following statements are true about a projection document? (Select all that apply.)

* A. We can include fields in our results by setting their values to 1 in the projection document.
* B. We can exclude fields from our results by setting their values to 0 in the projection document.
* C. We can either include or exclude fields in the results, but not both. The _id field is the exception to this rule.

오답
* D. Inclusion and exclusion statements, not including _id statements, can be combined with each other in a projection document.

> If we don’t want to return the _id field, we can add it to the projection document and set it to which of the following values? (Select all that apply.)

* A. 0

### Lesson 3: Counting Documents in a MongoDB Collection
* `db.<collection>.countDocuments(<query>, <options>)`

> Which of the following statements are true about the countDocuments() collection method? (Select all that apply.)

* A. The method takes a query parameter, which selects the documents to be counted.
* B. We can use the method to count all documents in a collection.

오답
* C. The method does not support the use of operators in queries that are passed as a parameter.
  * Incorrect. The .countDocuments() method accepts queries that use operators, like $elemMatch or $lt.

> What can we expect to be returned by running db.inspections.countDocuments({})? (Select one.)

* C. This command returns the total number of documents in the inspections collection.

### Unit 7 정리
Lesson 01: Sorting and Limiting Query Results in MongoDB
- [MongoDB Docs: cursor.sort()](https://www.mongodb.com/docs/manual/reference/method/cursor.sort/?_ga=2.22528882.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: cursor.limit()](https://www.mongodb.com/docs/manual/reference/method/cursor.limit/?_ga=2.22528882.810066485.1665291537-836515500.1666025886)

Lesson 02: Returning Specific Data from a Query in MongoDB
- [MongoDB Docs: Project Fields to Return from Query](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/?_ga=2.22528882.810066485.1665291537-836515500.1666025886)
- [MongoDB Docs: Projection Restrictions](https://www.mongodb.com/docs/manual/reference/limits/?_ga=2.22528882.810066485.1665291537-836515500.1666025886#mongodb-limit-Projection-Restrictions)

Lesson 03: Counting Documents in a MongoDB Collection
- [MongoDB Docs: db.collection.countDocuments()](https://www.mongodb.com/docs/manual/reference/method/db.collection.countDocuments/?_ga=2.30900342.810066485.1665291537-836515500.1666025886)
