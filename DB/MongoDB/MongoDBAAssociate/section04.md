# Section04: Server Administration(10%)
## Unit 9. MongoDB Logging Basic
### Lesson 1. MongoDB Logs in Atlas
* 로그를 다운받으려면 아틀라스 ReadOnly 롤 이상이 필요하다

Atlas CLI에서의 command
```
// role 확인
atlas project users list -o json

// 다운로드
atlas logs <hostname> <file>

// mongod 로그 파일(30일치)
atlas logs download uml3-shard-00-00.xwgj1.mongodb.net mongodb.gz

// gz파일 추출
gunzip mongodb.log.gz
```

> Which of the following are valid methods to download logs from M10-and-above Atlas clusters? (Select all that apply.)

* A. Using the Atlas UI
* C. Using the Atlas CLI

> What is the minimum privilege you need to download logs from an Atlas cluster? (Select one.)

* B. Project Data Access Read Only
  * GROUP_DATA_ACCESS_READ_ONLY

오답
* C. Project Read Only

### Lesson 2. MongoDB Logs on Self-Managed Instances
* mongod.conf 파일에 몽고 로그 위치를 지정할 수 있음
  * linux에서 디폴트는 `/var/log/mongodb/mongodb.log`

show log
* M10+ 클러스터에서 유효
* 최근 로그 이벤트들을 리턴
* 1024개의 엔트리를 저장
* `mongosh` 로 접속한 뒤 `show log <type>` 로 특정 로그를 접근할 수 있다.
* 또는 db.adminComment{getLog: <type>} 로 접근 가능

> While trying to access the mongod.log file for a self-managed deployment, you realize that it’s not in its default location. Which of the following options would help you find the location of the mongod.log file? (Select all that apply.)

정답
* b. The path for the log file can be found by viewing the value provided to the --logpath argument when viewing the mongod process information with a command such as “ps aux | grep mongod”.
* c. The path for the log file can be found by checking the systemLog.path value in the mongod.conf file.

오답
* a. The path for the log file can be found by running the db.getLogPath() helper method in mongosh.
  * 이런 명령 없다고 함
* d. The path for the log file can be found by running db.adminCommand({getLog: "global"}) in mongosh.
  * 램캐시에 저장된 글로벌 로그를 보여주는것. 로그패스를 보여주진 않음

> Which of the following users can successfully open a mongod.log file? (Select all that apply.)

* a. A user with access to the sudo command in Linux.
* b. A user that has been added to the mongodb group.

### Lesson 3. MongoDB Log Events
MongoDB에서 로그를 남기는 이벤트
* Conncetions
* Commands
* Queries
* Storage
* Replication
* ...

로그메세지
* mongod.log 파일에 저장된다
* JSON 포맷의 Key-value 짝으로 저장된다. 
* 로그메세지의 모든 필드는 축약어를 가지고 있다.

로그메세지 필드
* t : 시간
* s : 심각도
  * F : Fatal
  * E : Error
  * W : Warning
  * I : Info
  * D : Debug -> D1~D5로 세분화됨
* c : 로그 메세지에 대한 전체 컴포넌트 문자열
  * COMMAND : CURD
  * ACCESS : 
  * STORAGE
  * NETWORK
  * REPL
  * CONTROL
  * INDEX
* id : 로그메세지의 고유 id
* ctx : 컨텍스트. 로그메세지 프롬프트하는 운영체제 스레드 이름
* msg : MongoDB 컴포넌트 작성자가 생성한 실제 메세지
* attr : 속성. 로그메세지에 추가 속성이 포함된 경우에만 푯됨. 네임스페이스, 삭제할 인덱스 등...

로그에서 찾을 수 있는 데이터
* OS-levle warning
  * 운영체제 조건으로 발생
  * MongoDB 성능에 영향을 줄 수 있고, 심각한 이슈일 수 있음..
  * vm.max_map_count 이슈 등
* Authorization attemps
  * 액세스 권한이 부여되지 않은 사용자가 특정 자원에 액세스하려 할 때 생성됨
* Replica set elections
  * primary가 step down 되어 새로운 노드 선출할 때 발생하는 로그
  * REPL
  * ELECTION

> Given the following log message, identify the correct field name that relates to the operating system thread that prompted the log message. (Select one.)
```
{
 "t": {
   "$date": "2023-05-12T21:09:58.661+00:00"
 },
 "s": "I",
 "c": "REPL",
 "id": 21358,
 "ctx": "conn54",
 "msg": "Replica set state transition",
 "attr": {
   "newState": "SECONDARY",
   "oldState": "PRIMARY"
 }
}
```
* c. The "ctx" field

> Which of the following fields in a MongoDB log relates to the level of debugging verbosity? (Select one.)

* b. "s"

### Lesson 4. MongoDB Server Log Customization
Diagnostic log
* mongod.log 에서 확인 가능
* DB에서 발생하는 이벤트에 대한 정보를 포함
* slowms
  * 슬로우쿼리 기준 시간
  * 슬로우쿼리로 판단되면 diagnostic log에 기록됨
  * threshold 지정 방법
    * --slowms 파라미터
    * db.setProfilingLevel() mongosh
    * slowOpsThreshold 프로퍼티 conf파일 설정
  * Self-managed나 M10+ 아틀라스 클러스터에서 설정 가능

verbose level 설정
* setLevel
* systemLog.verbosity
* 아틀라스에서 지원하지 않음
* 디폴트는 0 -> 치명적인 오류,경고,정보 메세지만 로깅됨
* 1~5 로 설정 가능 (5로갈수록 정보 양 증가)

```
// 프로파일링 레벨, 슬로우쿼리 시간 설정
db.setProfilingLevel(0, { slowms: 30 })

// 슬로우쿼리 찾기
sudo grep "Slow query" /var/log/mongodb/mongod.log | jq
```

> Which of the following statements are true regarding the slowms property? (Select all that apply.)

* b. The slowms property defines the maximum amount of time for an operation to complete before it’s considered slow.
* c. The default value for the slowms property is set to 100 milliseconds.

> Which of the following options would successfully set a slowms threshold to 50 milliseconds in the MongoDB Shell? (Select one.)

* Option D. db.setProfilingLevel(0, { slowms: 50 })

> Which of the following statements are true regarding the verbosity of the logs? (Select all that apply.)

* a. The verbosity level refers to the amount of debugging information to include in the log file.
* b. To increase the verbosity for only one component, such as the INDEX component, edit the configuration file for a self-managed deployment.
* d. The verbosity level for a self-managed deployment can be adjusted by setting the verbosity property under the systemLog section of the configuration file.

### Lesson 5. MongoDB Server Log Rotation and Retention
적절히 로테이션 돌려야 성능 이슈를 막을 수 있다~

아틀라스
* 30일간의 로그 메세지를 보관
* 접근하기 위한 최소한의 권한은 `Project Data Access Read Only
* M10+ 에서 사용 가능

self-managed
* SIGUSR1
* db.adminCommand({logRatate:1})


rename
* SIGUSR1, db.adminCommand({logRatate:1}) 등의 신호를 받으면
* 파일이름을 UTC 타임스탬프로 바꾸고
* 새 로그를 열고
* 오래된 로그 파일을 닫고
* 모든 새 이벤트를 새 로그파일로 전송해서 신호에 응답
* `mongod -v --logpath /var/log/mongodb/server.log --logRotate rename`

reopen
* SIGUSR1, db.adminCommand({logRatate:1}) 등의 신호를 받으면
* 닫고 파일을 다시연다
* 외부 로그로테이션 도구(linux logRotation)을 사용하는 경우 reopen 옵션 필요
* logappend 옵션 필요 -> 동일한 파일에 로그 메세지 추가하려 할 시
* `mongod -v --logpath /var/log/mongodb/server.log --logRotate reopen logapped`

logrotate
* 활성 로그 파일 이름 바꾸면 시작
* 압축등으로 완료시킴
* mongodb.conf 파일에서 systemLog로 설정하고
* /etc/logrotate.d/ongod.conf 로. ㅓㄹ정

> What is the maximum number of days that MongoDB Atlas will retain logs for? (Select one.)

* a. 30 days

> Which of the following are valid methods for rotating mongod log files? (Select all that apply.)

* a. Using the db.adminCommand({ logRotate: 1 }) method in mongosh
* d. Issuing a SIGUSR1 signal to the mongod process manually or automatically by using the Linux logrotate utility


### Unit 9 정리
Lesson 1: MongoDB Logs in Atlas
- [Project Data Access Read Only](https://www.mongodb.com/docs/atlas/reference/user-roles/#mongodb-authrole-Project-Data-Access-Read-Only)
- [View and Download MongoDB Logs](https://www.mongodb.com/docs/atlas/mongodb-logs/)
- [atlas logs download](https://www.mongodb.com/docs/atlas/cli/stable/command/atlas-logs-download/)

Lesson 2: MongoDB Logs on Self-Managed Instances
- [Retrieve Recent Events from Log](https://www.mongodb.com/docs/manual/reference/command/getLog/#retrieve-recent-events-from-log)

Lesson 3: MongoDB Log Events
- [Log Messages](https://www.mongodb.com/docs/manual/reference/log-messages/)
- [View Database Access History](https://www.mongodb.com/docs/atlas/access-tracking/)
- [Recommended Values (Operations Checklist)](https://www.mongodb.com/docs/manual/administration/production-checklist-operations/)

Lesson 4: MongoDB Server Log Customizations
- [db.setLogLevel()](https://www.mongodb.com/docs/manual/reference/method/db.setLogLevel/?_ga=2.148385527.1926118966.1686611566-1191611927.1686611566)
- [db.setProfilingLevel()](https://www.mongodb.com/docs/manual/reference/method/db.setProfilingLevel/?_ga=2.80019927.1700198120.1686746185-1499070701.1686746185)
- [slowOpThresholdMs](https://www.mongodb.com/docs/manual/reference/configuration-options/?_ga=2.80019927.1700198120.1686746185-1499070701.1686746185#mongodb-setting-operationProfiling.slowOpThresholdMs)
- [Logging Slow Operations](https://www.mongodb.com/docs/manual/reference/log-messages/?_ga=2.80019927.1700198120.1686746185-1499070701.1686746185#logging-slow-operations)
- [Analyzing Slow Queries](https://www.mongodb.com/docs/manual/reference/log-messages/#analyzing-slow-queries)
- [Log Parsing Examples](https://www.mongodb.com/docs/manual/reference/log-messages/#log-parsing-examples)

Lesson 5: MongoDB Server Log Rotation and Retention
- [Rotate Log Files](https://www.mongodb.com/docs/manual/tutorial/rotate-log-files/)
- For more information on the `logrotate` service, try searching the web for resources on `logrotate` in Linux.

## Unit 10. MongoDB Database Administrator Tools
### Lesson 1: Get Started with DBA Tools

### Lesson 2: Backup Tools

### Lesson 3: Restore Tools

### Lesson 4: Data Export Tools

### Lesson 5: Data Import Tools

### Lesson 6: Diagnostic Tools: mongostat

### Lesson 7: Diagnostic Tools: mongotop

### Lesson 8: Diagnostic Tools: bsondump

### Lesson 9: MongoDB as a filesystem

### Unit 10 정리
Lesson 1: Get Started with DBA Tools
- [Install MongoDB](https://www.mongodb.com/docs/manual/installation/)
- [The MongoDB Database Tools Documentation](https://www.mongodb.com/docs/database-tools/)

Lesson 2: Backup Tools
- [mongodump](https://www.mongodb.com/docs/database-tools/mongodump/#mongodb-binary-bin.mongodump)

Lesson 3: Restore Tools
- [mongorestore](https://www.mongodb.com/docs/database-tools/mongorestore/)

Lesson 4: Data Export Tools
- [mongoexport](https://www.mongodb.com/docs/database-tools/mongoexport/)

Lesson 5: Data Import Tools
- [mongoimport](https://www.mongodb.com/docs/database-tools/mongoimport/)

Lesson 6: Diagnostic Tools: mongostat
- [mongostat](https://www.mongodb.com/docs/database-tools/mongostat/)

Lesson 7: Diagnostic Tools: mongotop
- [mongotop](https://www.mongodb.com/docs/database-tools/mongotop/)

Lesson 8: Diagnostic Tools: bsondump
- [bsondump](https://www.mongodb.com/docs/database-tools/bsondump/)

Lesson 9: MongoDB as a Filesystem
- [mongofiles](https://www.mongodb.com/docs/database-tools/mongofiles/)
- [GridFS](https://www.mongodb.com/docs/manual/core/gridfs/)

## Unit 11. Self-Managed Server Administration
