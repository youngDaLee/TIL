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
* References
  * _id 필드로 서로 다른 콜렉션을 연결하는 것
  * Embedding : 데이터를 접근하기 위해 하나의 쿼리로 접근 가능 / update&delete를 위해 하나의 쿼리만 사용 // 데이터 복제가 일어나고 도큐먼트가 커짐
  * Referencing : 데이터 복제가 없고 도큐면트 크기가 작아짐 // 데이터 접근을 위해 join이 필요함

> Which of the following statements is/are true about referencing data in documents? (Select all that apply.)

정답
* A. Referencing data in documents avoids duplication of data.
* B. Referencing data in documents may result in smaller documents.
* C. Referencing data in documents links documents by using the same field.

오답
* D. Referencing data in documents improves read performance.

### Lesson 6: Scaling Data Model
성능에 영향을 미치는 옵션
* Query result times 
* memory usage
* cpu usage
* storage

unbounded document : 제한이 없는 도큐먼트
* 도큐먼트가 엄청나게 커지면 문제가 생김
  * memory 공간 차지
  * 쓰기 성능 영향
  * 데이터에 대해 pagination 어려움
  * 도큐먼트 사이즈 맥시멈이 16MB

임베디드 모델에서 피해야 할 것
* 16MB보다 큰 도큐먼트
* 나쁜 쿼리 성능
* 나쁜 쓰기 성능
* 많은 메모리가 사용되는 것

> What are the effects of creating unbounded documents when embedding data? (Select all that apply.)

* A. Unbounded documents impact write performance.
  * 데이터가 다시 써지기 때문에 쓰기성능에 영향...
* C. Unbounded documents cause storage problems.

오답
* B. Unbounded documents improve pagination performance.

> What is the recommended way to avoid the unbounded document sizes that may result from embedding?

* Break data into multiple collections and use references.

> What is MongoDB's principle for how you should design your data model?

* Data that is accessed together should be stored together.

오답
* Data that is collected in the same day should be stored together.
* Data that is not in a one-to-one relationship should be stored together.

### Lesson 7: Using Atlas Tools for Schema help
안티패턴 스키마
* Massive arrays
* Massive number of collections
* Bloated document
* unnecessary indexs
* queries without indexes
* data that's accessed together, but stored in diffrent collections

아틀라스가 이런 안티패턴 데이터를 감지해줌...
* Data Explorer : 무료. 안티패턴 감지해줌
* Performance Advisor : M10 이상.. 

> Which tab in Data Explorer shows ways to improve your schemas?

정답
* Schema Anti-Patterns

오답
* Indexes
* Find

> What is the minimum Atlas Cluster tier that you must have to use the Performance Advisor tool?

* M10

### Unit 2 정리
* 데이터 관계
* Embedded vs references
* 스키마 매니징 툴
* 원문
  * Explain the purpose of data modeling.
  * Identify the types of data relationships (one to one, one to many, many to many).
  * Model data relationships.
  * Identify the differences between embedded and referenced data models.
  * Scale a data model.
  * Use Atlas Tools for schema help.

공식 문서
* Lesson 01: Introduction to Data Modeling
    * [Data Modeling Introduction](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/?_ga=2.11339316.108633906.1720224355-1288624444.1714412087)
    * [Separating Data That is Accessed Together](https://www.mongodb.com/developer/products/mongodb/schema-design-anti-pattern-separating-data/?_ga=2.60935781.810066485.1665291537-836515500.1666025886)
* Lesson 02: Types of Data Relationships
    * [Data Model Design](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/)
    * [Model Relationships Between Documents](https://www.mongodb.com/docs/v4.2/applications/data-models-relationships/?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
    * [Embedding MongoDB](https://www.mongodb.com/basics/embedded-mongodb?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
    * [MongoDB Schema Design Best Practices](https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
* Lesson 03: Modeling Data Relationships
    * [Data Model Design](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/)
    * [Model Relationships Between Documents](https://www.mongodb.com/docs/v4.2/applications/data-models-relationships/?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
* Lesson 04: Embedding Data in Documents
    * [Embedding MongoDB](https://www.mongodb.com/basics/embedded-mongodb?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
    * [Model One-to-One Relationships with Embedded Documents](https://www.mongodb.com/docs/manual/tutorial/model-embedded-one-to-one-relationships-between-documents/?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
    * [Model One-to-Many Relationships with Embedded Documents](https://www.mongodb.com/docs/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/?_ga=2.19332209.810066485.1665291537-836515500.1666025886)
* Lesson 05: Referencing Data in Documents
    * [Normalized Data Models](https://www.mongodb.com/docs/manual/data-modeling/#references)
    * [Model One-to-Many Relationships with Document References](https://www.mongodb.com/docs/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/?_ga=2.64006886.810066485.1665291537-836515500.1666025886)
* Lesson 06: Scaling a Data Model
    * [Operational Factors and Data Models](https://www.mongodb.com/docs/manual/core/data-model-operations/?_ga=2.64006886.810066485.1665291537-836515500.1666025886)
    * [Performance Best Practices: MongoDB Data Modeling and Memory Sizing](https://www.mongodb.com/blog/post/performance-best-practices-mongodb-data-modeling-and-memory-sizing?_ga=2.64006886.810066485.1665291537-836515500.1666025886)
* Lesson 07: Using Atlas Tools for Schema Help
    * [A Summary of Schema Design Anti-Patterns and How to Spot Them](https://www.mongodb.com/developer/products/mongodb/schema-design-anti-pattern-summary/?_ga=2.64006886.810066485.1665291537-836515500.1666025886)

## Unit 3
### Lesson 1: Installing and Connecting to the Mongo Shell
* ubuntu에 mongosh 설치
* Atlas와 연결

#### Install
1. Update apt and install gnupg. Then add the MongoDB public GPG key to the system.
```
apt update 
apt install <code>gnupg</code>
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add - 
```

2. Create a list file for MongoDB.
```
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu 
focal/mongodb-org/6.0 multiverse" | sudo tee 
/etc/apt/sources.list.d/mongodb-org-6.0.list
```

3. Update apt and install mongosh.
```
apt update
apt install -y mongodb-mongosh
```

4. Check that mongosh is installed.
```
mongosh --version
```

5. Exit mongosh.
```
exit
```

#### Connect Atlas
1. Run the mongosh command followed by your connection string.
```
mongosh "mongodb+srv://<username>:<password>@<cluster_name>.example.mongodb.net"
```
Alternatively, you can log in by providing the username and password as a command line argument with -u and -p.
```
mongosh -u exampleuser -p examplepass "mongodb+srv://myatlasclusteredu.example.mongodb.net"
```

2. After connecting to the Atlas cluster, run db.hello(), which provides some information about the role of the mongod instance you are connected to.
```
db.hello()
```

3. Finally, run the exit command inside mongosh to go back to the terminal.
```
exit
```

> Which of the following commands can be used to connect to a database called students on a local MongoDB instance? (Select one.)

* D. mongosh students

> Which of the following are valid methods for connecting mongosh to a MongoDB Atlas cluster and selecting the sample_training database? (Select all that apply.)

정답
* mongosh "mongodb+srv://<username>:<password>@<clustername>.mongodb.net/sample_training"
* mongosh "mongodb+srv://<clustername>.mongodb.net/sample_training" --username <username>

오답
* mongosh "mongodb+srv://<clustername>.mongodb.net/" –username <username> --db sample_training
* mongosh "mongodb+srv://<clustername>.mongodb.net/?database=sample_training" –username <username>


### Lesson 2: Configuring the mongodb shell
* config API
  * shell에서 세팅을 선택해주는 툴
  * `config.get(세팅키)` 로 현재 설정 확인
  * `config.set(세팅키, 설정값)` 으로 설정값 변경
  * `config.reset(세팅키)` 으로 초기화
* mongosh.conf 파일
  * configAPI 값을 파일로 만들어줌...
  * configAPI를 오버라이딩
  * 유저가 생각하고 OS에 종속적
* javascript 코드 또는 eval로 직접 설정값을 전달하는 방법
  * `mongosh --eval "disableTelemetry()"`
  * `mongosh --eval "db.accounts.find().limit(3)" --quiet`


> What method from the config API allows you to set a configuration option in mongosh? (Select one.)

* B. config.set()

> Which of the following settings can be adjusted by editing an option in the mongosh.conf file? (Select all that apply.)
> 틀림ㅠ

정답
* B. How many items per batch are displayed when using the “it” iterator
  * displayBatchSize
* C. The editor used by mongosh when using the edit() method
  * editor

오답
* A. The color of the font that’s displayed in mongosh
* B. How many items per batch are displayed when using the “it” iterator

### Lesson 3: Using the mongodb shell
스크립트를 불러오는 방법
```
load('randomPost.js')
```

```
db = db.getSiblingDB("sample_training");
console.log(`\nCurrent database: ${db.getName()}`);
console.log("Random post sample of 500 words:\n");
let result = db.posts.aggregate({
 $sample: { size: 1 },
});
printjson(result.next().body.slice(0, 500) + " ...");
```

다른 에디터로 커멘드를 편집하는 방법
```
config.set("editor", "vim")
```

> You want to use an external JavaScript file within an active mongosh session. What method should you use? (Select one.)

* A. load()

> What method is used to change databases within a script by using the load() method in mongosh? (Select one.)

* D. db.getSiblingDB()


### Lesson 4: Using the mongodb shell library(.mongoshrc.js)
`db.adminCommand()`
* 어드민 디비에 대해 명령을 실행
* 명령 이름은 도큐먼트 키 중 하나여야 함

`fcv()`
* 위 명령으로 헬퍼펑션 사용
* 너무 긴 명령을 짧게...

.mongoshrc.js 파일은 mongosh 가 시작할 때 사용될 수 있다.
```
> touch ~/.mongoshrc.js
> const fcv = () => db.adminCommand({getParameter: 1, featureCompatibilityVersion: 1})
> prompt = () => {
 let returnString = "";
 const dbName = db.getName();
 const isEnterprise = db.serverBuildInfo().modules.includes("enterprise");
 const mongoURL = db.getMongo()._uri.includes("mongodb.net");
 const nonAtlasEnterprise = isEnterprise && !mongoURL;
 const usingAtlas = mongoURL && isEnterprise;
 const readPref = db.getMongo().getReadPrefMode();
 const isLocalHost = /localhost|127\.0\.0\.1/.test(db.getMongo()._uri);
 const currentUser = db.runCommand({ connectionStatus: 1 }).authInfo
   .authenticatedUsers[0]?.user;
 if (usingAtlas) {
   returnString += `Atlas || ${dbName} || ${currentUser} || ${readPref} || =>`;
 } else if (isLocalHost) {
   returnString += `${
     nonAtlasEnterprise ? "Enterprise || localhost" : "localhost"
   } || ${dbName} || ${readPref} || =>`;
 } else if (nonAtlasEnterprise) {
   returnString += `Enterprise || ${dbName} || ${currentUser} || ${readPref} || =>`;
 } else {
   returnString += `${dbName} || ${readPref} || =>`;
 }
 return returnString;
};

```

* 요약정리
  * .mongoshrc.js 에 mongo 명령어 단축어 설정 가능(예시에서는 fcv)
  * .mongoshrc.js 에 prompt로 mongosh 커넥팅 실행 시 수행할 명령어 입력 가능

> Where should the .mongoshrc.js file be located? (Select one.)

* B. The user's home directory.

> Which of the following methods terminate an active mongosh session? (Select one.)

* A. exit

### Lesson 5: MongoDB Shell Tips and tricks
쿼리 결과를 JSON 파일로 만들기

```
> const customers = db.sales.aggregate([
 {
   $project: {
     _id: 0,
     customer: 1
   }
 }
]).toArray()

> fs.writeFileSync('customers.json', EJSON.stringify(customers, null, 2));
```

가라데이터 넣기
```
// 직접 추가
> const faker = require('faker');
> for (let i = 0; i < 10; i++) {
 users.push({
   name: faker.name.findName(),
   email: faker.internet.email(),
   phone: faker.phone.phoneNumber(),
   address: faker.address.streetAddress()
 })
}

// 불러오기
> db.getSiblingDB('test_data').users.insertMany(users)
```

> Which of the following examples demonstrates the correct usage of the EJSON.stringify() method in mongosh to convert an extended JSON object into a string? (Select one.)
> A. EJSON.stringify({ name: “Test User”, dob: new Date(“1990-01-01”)})
> B. EJSON.stringify(name: “Test User”, dob: new Date(“1990-01-01”)
> C. ({name: “Test User”, dob: new Date(“1990-01-01”)}).EJSON.stringify()
> D. EJSON.stringify = { name: “Test User”, dob: new Date(“1990-01-01”)}

* A

> In mongosh, what Node.js fs module API method can be used to write the results of a query to a file? (Select one.)

* B. fs.writeFileSync()

> You want to load a script into mongosh that requires an npm package. To do so, where should the npm package be installed? (Select all that apply.)

* A. An option for using an npm package in an external script is to install the package globally and then require it in the script.
* B. The package can be installed in the node_modules directory in your current working directory. Then it can be added to a mongosh script that can be used with the load() method.

오답
* C. mongosh will automatically download and install the necessary dependencies when the script is run in the shell with the load() method.

### Unit 3 정리
* mongosh 설치 -> atlas dusruf
* config API 사용법 / mongosh.conf 사용법 / --eval 사용법
* load() 사용법, js로 쿼리 다루는 방법 사용법ㅡ db.getSiblingDb() 로 스크립트 변경 방법
* .mongoshrc.js 로 단축어, 시작 명령 설정 방법

General
- [Getting Started with MongoDB Atlas](https://learn.mongodb.com/courses/getting-started-with-mongodb-atlas)
- [mongodb-js/mongosh (GitHub)](https://github.com/mongodb-js/mongosh)

Lesson 1: Installing and Connecting to the MongoDB Shell
- [Install mongosh](https://www.mongodb.com/docs/mongodb-shell/install/)
- [Connect to a Deployment](https://www.mongodb.com/docs/mongodb-shell/connect/)
- [Connect to a Database Deployment (for Atlas)](https://www.mongodb.com/docs/atlas/connect-to-database-deployment/)
- [MongoDB Shell Options](https://www.mongodb.com/docs/mongodb-shell/reference/options/)
    - [Host](https://www.mongodb.com/docs/mongodb-shell/reference/options/#std-option-mongosh.--host)
    - [Port](https://www.mongodb.com/docs/mongodb-shell/reference/options/#std-option-mongosh.--port)
    - [Username](https://www.mongodb.com/docs/mongodb-shell/reference/options/#std-option-mongosh.--username)

Lesson 2: Configuring the MongoDB Shell
- [Configure mongosh](https://www.mongodb.com/docs/mongodb-shell/configure-mongosh/)
- [Configure Settings Using the API](https://www.mongodb.com/docs/mongodb-shell/reference/configure-shell-settings-api/#std-label-configure-settings-api)
- [Configure Settings Using a Configuration File](https://www.mongodb.com/docs/mongodb-shell/reference/configure-shell-settings-global/#std-label-configure-settings-global)
- [Configure Settings](https://www.mongodb.com/docs/mongodb-shell/reference/configure-shell-settings/#std-label-mongosh-shell-settings)

Lesson 3: Using the MongoDB Shell
- [Write Scripts](https://www.mongodb.com/docs/mongodb-shell/write-scripts/)
- [db.getSiblingDB()](https://www.mongodb.com/docs/manual/reference/method/db.getSiblingDB/)
- [Use an Editor for Commands](https://www.mongodb.com/docs/mongodb-shell/reference/editor-mode/)
- [Gist for randomPost.js](https://gist.github.com/nol166/298d1c0f02fb1837f546e16163e097f5)
- [Gist for giveMeADate.js](https://gist.github.com/nol166/16565bcf9705e086aac6e80a44254e16)

Lesson 4: Using the MongoDB Shell Library (.mongoshrc.js)
- [Run Code From a Configuration File](https://www.mongodb.com/docs/mongodb-shell/write-scripts/#std-label-mongosh-write-scripts-config-file)
- [Customize the mongosh Prompt](https://www.mongodb.com/docs/mongodb-shell/reference/customize-prompt/#std-label-customize-the-mongosh-prompt)
- [Gist for featureCompatibityVersion Helper](https://gist.github.com/nol166/63d84e25f4de0a27a0e0b93c284f8295) (.mongoshrc.js)
- [Gist for Additional Information in the mongosh Prompt](https://gist.github.com/nol166/c93e1b52b31488f7a17b50e0f66114ea) (.mongoshrc.js)

Lesson 5: MongoDB Shell Tips and Tricks
- [MongoDB Shell Tips and Tricks](https://dev.to/mongodb/mongodb-shell-tips-and-tricks-1ceg)
- [writeFileSync() (Node.js Documentation)](https://nodejs.org/api/fs.html#fswritefilesyncfile-data-options)
- [Faker npm Package](https://fakerjs.dev/guide/)
- [load() in mongosh](https://www.mongodb.com/docs/v5.2/reference/method/load/)
- [require() in mongosh](https://www.mongodb.com/docs/mongodb-shell/write-scripts/require-external-modules/#require-a-local-file)


## Unit 4. Connecting to a MongoDB Database
### Lesson 1: Using Mongo DB Connection Strings
standard format
* cluster, replica set, sharded clust에 연결할 때 사용

DNS Seed List format
* DNS server list에 접속할 수 있도록 함
* flexiblilty

아틀라스에서 shell/application/compass 방식으로 접속할 때의 커넥션 스트링을 확인할 수 있음
```
mongodb+srv://<username>:<password>@{dns}:{port(default 27017)}/{params}
* srv: TLS 옵션을 true로 설정하고 MongoDB DNS 시드목록 사용하도록 지시
```

> Which of the pre-formatted connection strings are available in the Atlas dashboard? (Select all that apply.)

* A. Connect with the MongoDB Shell
* B. Connect your application
* C. Connect using MongoDB Compass

오답
* D. Connect with MongoDB Charts


### Lesson 2: Connecting to a MongoDB Atlas Cluster with the shell
> Which REPL environment does the MongoDB Shell use? (Select one.)

* B. Node

> To connect your Atlas cluster with the MongoDB Shell, what do you need to run in the command line? (Select one.)

* C. Your connection string

### Lesson 3: Connecting to a MongoDB Atlas Cluster wiht compass
MongoDB Compass는 MongoDB 관리 툴.... Studio3T같은

> Which of the following describes MongoDB Compass? (Select one.)

* D. A graphical user interface (GUI) for querying, aggregating, and analyzing data in MongoDB

오답
* A. A Node.js REPL environment that is used to interact with the database
* B. A data visualization tool that allows you to create and embed visualizations in your application
* C. A tool that allows you to query, transform, and move data across Amazon S3 and Atlas clusters

### Lesson 4: Connecting to a MongoDB Atlas Cluster from an application
MongoDB Drivers
* 프로그래밍 언어에서 MongoDB에 연결할수 있도록 도와주는 드라이버
* 공식 문서를 따라서 시작할 수 있다.

> What does a MongoDB driver do? (Select one.)

* B. Connects MongoDB to applications via programming languages

> Visit the official [MongoDB driver documentation](https://www.mongodb.com/docs/drivers/?_ga=2.204809744.108633906.1720224355-1288624444.1714412087). Which of the following languages have drivers that are supported by MongoDB? (Select all that apply.)

*  Pascal 빼고 다..

### Lesson 5: Trobleshooting MongoDB Atlas Connection Errors
MongoDB에 연결할 때 발생할 수 있는 이슈들
* Network access errors
  * Atals > Security > Network Access
  * Add IP Address로 해당 DB에 접속 가능한 IP 주소를 추가함
* User authentication errors
  * 커넥션스트링에 password 추가
  * 로그인 정보 확인하기

> How can you fix the following error? (Select one.)
> MongoServerSelectionError: connection <monitor> to 34.239.188.169:27017 closed

* B.Add your IP address in the Network Access panel in Atlas.

오답
* Update database access with the correct user credentials.
* Create a new database on your Atlas cluster.

> How can we fix the following error? (Select all that apply.)
> MongoServerError: bad auth : Authentication failed.

* A. Check that you are connecting to the correct database deployment.
* C. Check that your username and password are spelled correctly in your connection string.

오답
* B. Update your IP address in the Network Access panel.

### Unit 4 정리

Lesson 01: Using MongoDB Connection Strings
- [MongoDB Docs: Get Connection String](https://www.mongodb.com/docs/guides/atlas/connection-string/?_ga=2.2826361.818394043.1666026366-33697719.1666026366)
- [MongoDB Docs: Connection String URI Format](https://www.mongodb.com/docs/manual/reference/connection-string/)

Lesson 02: Connecting to a MongoDB Atlas Cluster with the Shell
- [MongoDB Docs: The MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/)

Lesson 03: Connecting to a MongoDB Atlas Cluster with Compass
- [MongoDB Docs: MongoDB Compass](https://www.mongodb.com/products/compass/)

Lesson 04: Connecting to a MongoDB Atlas Cluster from an Application
- [MongoDB Docs: Connect via Your Application](https://www.mongodb.com/docs/atlas/driver-connection/)

Lesson 05: Troubleshooting MongoDB Atlas Connection Errors
- [MongoDB Docs: Troubleshoot Connection Issues](https://www.mongodb.com/docs/atlas/troubleshoot-connection/)


## 자격증 목차
### 1.1 Idntify the characteristics of MongoDB
### 1.2 Identify the diffrences between a MongoDB and RDBMS database
### 1.3 Identify the methods to access and administer a MongoDB
### 1.4 Identify the function of sharding
