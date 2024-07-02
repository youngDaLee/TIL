# Section01: PHILOSOPHY AND FEATURES(7%)
## Unit1: MongoDB and the Document Model
### Lesson1 : Introduction to mongodb
* document DB
* Scalability
* Resilience
* Spped of development
* Privacy and Security

용어
* document : mongodb 데이터 최소단위 (row)
* collection : document 모음
* database : collection 모음

> What is the relationship between the MongoDB database and MongoDB Atlas? (Select one.)
> MonogDB와 MongoDB 아틀라스의 차이점

정답
* B. The MongoDB database is a core element of MongoDB Atlas, which is a multi-cloud developer data platform.
  * MongoDB는 MonogDB 아틀라스의 코어모델. 아틀라스는 full-text search, data visualization, data lacke storage, 모니터링 등을 지원하는 MongoDB의 클라우드 서비스임

오답
* A. The MongoDB database is the locally deployed version of MongoDB Atlas.
  * MonogDB 아틀라스는 클라우드 버전...
* B. The MongoDB database is a core element of MongoDB Atlas, which is a multi-cloud developer data platform.
  * 아틀라스도 무료로 제공할 수 있음


> Jenni works at an e-commerce start-up that uses MongoDB for its customer data managament, product catalog and payment processing. Her startup now wants to add personalized recommendations for customers using real-time analytics. Jenni and her team will need to move data to a separate analytics database to handle this new use case.
> 데이터 분석을 위해 별도의 DB로 옮겨야 함

정답 
* False
  * 몽고에서 다 제공 해 줌

> What is the basic unit of data in MongoDB? (Select one.)

정답
* Document

### Lesson 2:  MongoDB Document Model
* JSON 형태로 보여지면서, BSON 형태로 저장됨
  * BSON은 JSON의 추가적인 형태...
  * JSON 모든 데이터 타입을 포함하면서 Dates, ObjectID 등 특별한 ID를 가지는 형태
  * _id 필드는 항상 몽고디비의 Primary Key임.
  * _id 를 따로 지정하지 않으면 ObjectID로 저장됨
* MongoDB는 Flexible Schema...
* RDB는 필드 변경이 어려움... MongoDB는 필드 추가가 아주 자유로움


> Which of the following are data types that are supported by MongoDB by using BSON? (Select all that apply.)

정답
* 32-bit integer
* Object
* Array
* ObjectID

오답
* _id
  * _id는 필드명임. 데이터타입이 아님

> Which of the following statements are true about the _id field in MongoDB? (Select all that apply.) 

정답
* B. The _id field is required for each document.
  * 필수 필드임. 그냥 몽고는 무조건 PK 이름이 _id로 고정
* C. The _id field must be unique.
  * PK니까 ㅇㅇ
* D. The _id field is automatically included and populated with an ObjectId if the _id field is omitted in an inserted document.
  * ㅇㅇ PK 지정되어 자동 생성됨. 뭐 안넣으면 그냥 ObjectID 지정됨

오답
* A. The user must specify the _id field for each inserted document.
    * ㄴㄴ 따로 지정 안하면 자동으로 ObjectId 지정해줌

> Use the following documents labeled Document A and Document B to answer this question.
> Elena's company has been storing customer data in records that are structured like Document A. Her company wants to add a new field to their customer records so that they are structured like Document B. Before inserting records like Document B, Elena and her team must update all older records to include the new field.`
> 엘레나 회사가 A처럼 저장된 형태를 B처럼 바꾸고 싶은데 엘레나는 그러면 모든 도큐먼트에 필드를 업뎃해야함?

```
Document A
{
  "username": "vreddy",
  "name": "Vasanti Reddy",
  "email": "vreddy1@gmail.com",
  "location": {
    "city": "Delhi",
    "country": "India"
  }
}
Document B
{
  "username": "avasa",
  "name": "Asad Vasa",
  "email": "avasa1@yahoo.com",
  "social_media": {
    "Twitter": "avasa",
    "Instagram": "Asad101",
    "LinkedIn": "AsadVasa"
  },
  "location": {
    "city": "Los Angeles",
    "country": "United States"
  }
}
```

정답
* False
  * 몽고는 플랙시블한 데이터 모델이기 때문에 다 달라도 됨

### Lesson3 : Managing Databases, Collections, and Documents in Atlas Data Explorer
* 그냥 몽고 설명....

### Unit 1 총정리
* 데이터는 documents, collections, databases 로 구성됨
* 도큐먼트는 BSON 형태로 저장됨.
  * BSON은 JSON의 모든 형태를 아우르면서 dates, ObjectIds, numbers 등의 특수 필드를 포함한 형태
* 모든 도큐먼트는 필수로 _id 필드를 가짐. 따로 지정하지 않으면 MongoDB가 자동 생성하여 ObejctId를 인서트함
* MongoDB는 플랙시블한 스키마 구조를 가짐. 한 콜렉션 내의 도큐먼트는 같은 형태를 보장하지 않음

관련 공식 문서
* Lesson01
  * [What Is MongoDB?](https://www.mongodb.com/what-is-mongodb?_ga=2.198890287.165168422.1719881510-1288624444.1714412087)
  * [MongoDB Use Cases](https://www.mongodb.com/solutions/use-cases?_ga=2.228848284.165168422.1719881510-1288624444.1714412087)
* Lesson 02: The MongoDB Document Model
  * [MongoDB Docs: Documents](https://www.mongodb.com/docs/manual/core/document/?_ga=2.232380959.165168422.1719881510-1288624444.1714412087)
  * [MongoDB Docs: BSON Types](https://www.mongodb.com/docs/manual/reference/bson-types/?_ga=2.263789324.165168422.1719881510-1288624444.1714412087)
  * [Explaining BSON with Examples](https://www.mongodb.com/basics/bson?_ga=2.263789324.165168422.1719881510-1288624444.1714412087)
  * [JSON and BSON](https://www.mongodb.com/json-and-bson?_ga=2.259576330.165168422.1719881510-1288624444.1714412087)
* Lesson 03: Managing Databases, Collections, and Documents in Atlas Data Explorer
  * [MongoDB Docs: Create, View, and Drop Databases](https://www.mongodb.com/docs/atlas/atlas-ui/databases/?_ga=2.259576330.165168422.1719881510-1288624444.1714412087)
  * [MongoDB Docs: Databases and Collections](https://www.mongodb.com/docs/manual/core/databases-and-collections/?_ga=2.2749104.165168422.1719881510-1288624444.1714412087)

## Unit2: MongoDB Data Modeling Intro
### Lesson1: Introduction to Data Modeling
* 데이터 모델링을 잘 해서 리소스를 절약하자...

> Which of the following statements is/are true about data modeling? (Select all that apply.)

정답
* A. Data modeling is the process of defining how data is stored.
* B. Data modeling is the process of defining the relationships that exist among different entities in your data.

오답
* C. Data modeling is the process of collecting data.

> Which of the following are benefits of a proper data model? (Select all that apply.)

정답
* A. A proper data model makes it easier to manage your data.
* B. A proper data model makes queries more efficient.
* C. A proper data model uses less memory and CPU.
* D. A proper data model reduces costs.

> Which of the following is a benefit of the document model?

정답
* A. The document model does not enforce any document structure by default. This means that documents even in the same collection can have different structures.

오답
* The document model makes having a schema useless.
* The document model supports only simple relationships among data to make data wrangling easier.

### Lesson 2: Types of Data Relationships
* One to One
  * MongoDB에서는 single document에 대해 1:1 관계를 가질 수 있음
* One to Many
  * 단일 문서에서의 1:n 표현 => 배열에 중첩된 데이터 타입을 넣어서 표현 가능(임베딩방식)
* Many to Many

형태
* Embedding
  * 관련 데이터를 하나의 문서에 다 때려박는 형식 = 비정규화
  * ex: {_id: a, casting: [{actor: "a", charactor: "luke"}, {actor: "b", charactor: "han"}, ...]}
* Referencing
  * 문서에 있는 다른 콜렉션 문서를 참조하는 경우 = 정규화
  * ex: {_id: a, casting: [ObjectId(), ObjectId(), ...]}

> Which of the following are common types of relationships that are found in every database? (Select all that apply.)

정답
* A. One-to-one relationship
* B. One-to-many relationship
* C. Many-to-many relationship

> What is the type of relationship shown in the following document?

```
{
    "_id": ObjectId("00000001"),
    "name": "Marnie Dupree",
    "grade": "Freshman",
    "studentId": 123456,
    "email": "mdupree@college.edu"
}
```
정답
* One-to-one relationship

### Lesson 3: Modeling Data Relationships
> A legacy bank database has been ported to MongoDB, resulting in a set of collections that were mapped to their original tables.
> You're tasked with redesigning the accounts collection of the banking database to make the information clearer. The bank would like you to keep the customers' contact information and account information separate.
> The following is a sample document in the accounts collection:
>
```
{
  "account_id": "MDB653115886",
  "account_holder": "Herminia Mckinney",
  "account_type": "savings",
  "balance": 6617.34,
  "street_num": 123,
  "street": "Main St",
  "city": "Tulsa",
  "state": "OK",
  "zip": 74008,
  "country": "USA",
  "home_phone": 1234567890,
  "cell_phone": 1111111111,
  "transfers": [
    ...
  ],    
}
```
> Which of the following actions can be made to improve this schema? Consider the following requirements:
> * Preserve the one-to-one relationship among all the fields.
> * Keep the contact and account information separate.
> * Store data together that is accessed together.

정답
* A. Create two collections: one for accounts and one for customer_info.
* 내가 놓친 정답
  * B. Embed the phone numbers as a subdocument. 

오답
* C. Create two collections that have no overlapping fields.
  * 중복되는 필드가 없는 두 컬렉션이면 두 컬렉션을 연결할 수 없음.
* D. Keep the current schema as is.

### Lesson 4: Embedding Data in Documents
* Embeding
  * 1:1, 1:n 매핑을 위함...
  * 어떤 관계 모델에서도 모두 가능함
* 필드가 1:1 매핑 관계일수도 있고, 특정 필드는 1:n 관계일 수 있음.
* 모든 종류의 관련 정보를 싱글 도큐먼트에 저장할 수 있음 -> 쿼리를 단순화 할 수 있음
* 조인을 피하고 쿼리를 최소화
* 단일 쓰기 동작에서 데이터를 조작할 수 있음
* 단점
  * 도큐먼트 하나의 크기가 커질 수 있음 -> 메모리가 과도하게 발생하고, 읽기 대기시간이 발생 가능
  * 한 번의 읽기 작업으로 거대한 도큐먼트가 메모리에 올라가면서 읽기 성능 이슈가 발생할 수 있음
  * 문서 크기가 초과될 수 있음.. -> 안티패턴

> Which of the following statements is/are true about embedding data in documents? (Select all that apply.)

정답
* A. Embedding data in documents simplifies queries.
* B. Embedding data in documents improves the overall performance of queries.

오답
* C. Embedding data in documents makes your document smaller over time.
* D. Embedding data in documents never results in an unbounded document.

> Which of the following relationship types often use embedding? (Select all that apply.)

* A. One-to-one relationship
* B. One-to-many relationship
* C. Many-to-many relationship

### Lesson 5: Referencing Data in Documents


### Lesson 6: Scaling Data Model

### Lesson 7: Using Atlas Tools for Schema help

### Unit 2 정리


## 자격증 목차
### 1.1 Idntify the characteristics of MongoDB
### 1.2 Identify the diffrences between a MongoDB and RDBMS database
### 1.3 Identify the methods to access and administer a MongoDB
### 1.4 Identify the function of sharding
