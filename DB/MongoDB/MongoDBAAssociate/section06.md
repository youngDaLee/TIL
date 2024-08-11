# Section06
## Unit 15. Replication in MongoDB
### Lesson 1: Introduction to Replication
Replication은 여러 데이터 사본을 저장하고 여러 서버에서 동기화된 상태로 유지하는 프로세스.

고가용성(High availability) : 시스템이 가용성이 부족한 상태에서도 데이터를 지속적으로 액세스 할 수 있도록 하는 개념

> Which of the following are benefits of using replication? (Select all that apply.)

* a. High availability
* d. Data durability

> Which term best matches the following definition? (Select one.)
> The concept of making sure that our data can be continuously accessed, even if there is an interruption in a system.

* b. High availability

### Lesson 2: Replication in MongoDB
* Components of a replica set
  * 레플리카셋은 3, 5, 7개의 mongodb 인스턴스(멤버) 로 구성되어 있다
  * 최대 50개의 멤버가 존재할 수 있고, 7개의 멤버까지 투표권을 가질 수 있다.
  * 레플리카셋은 Primary, Secondary 노드로 구성된다
  * Primary : Write를 하는 유일한 구성원. 세컨더리는 oplog를 통해 프라이머리 데이터를 복제한다. Primary는 읽기도 가능하긴 하지만 Secondary만 읽기조작 할 수 있도록 변경 할 수도 있다.
* Elections
  * Primary가 불능상태가 되면 새로운 Primary를 선출하기 위해 투표를 진행한다(Election)
  * 가장 많은 투표를 얻은 멤버가 Primary가 된다.
* Failover
  * Primary가 불능상태가 되었을 때 새Primary를 선출하고, 새 Primary로 정상조작 재개하는 프로세스

> Which replica set member accepts all write operations? (Select one.)

* c. Primary

> Which replica set member is responsible for replicating data? (Select one.)

* a. Secondary

### Lesson 3: Automatic Failover and elections
Automatic Failover는 장애복구에 중요 -> Election를 통해 Primary가 다운된 상황에서 Primary를 선정
* Election이 발생하는 상황
  * 새로운 Replica set 노드를 추가
  * Initiating Replica Set
  * rs.stepDown(), rs.reconfig() 등 레플리카셋 메인터넌스를 수행할 때
* voting member는 한 표씩 투표 가능하며, 최대 7명의 voting member가 존재할 수 있다.
  * 홀수의 voting member가 있는게 중요(3, 5, 7)
  * priority value : primary가 될 수 있는 우선순위 자격.... (0~1000 의 값을 부여할 수 있으며, 값이 클 수록 primary가 될 수 있음) priority가 0이면 primary도 될 수 없고 election도 할 수 없음


> In a three-member replica set, how many of the members are voting members by default? (Select one.)

* c. 3

> Which of the following scenarios will initiate an election? (Select all that apply.)

* a. The primary becomes unavailable.
* b. The secondaries lose connectivity to primary for longer than configured timeout.

> Given the replica set shown, which member is most likely to be elected if an election takes place? (Select one.)

* a. Priority 99

### Lesson 4: The MongoDB Operation Log
oplog : 데이터를 복제할 때 사용되는 유용한 정보 
* write가 발생할 때, primary는 데이터 변경 사항을 oplog에 기록
* secondary는 oplog스트림을 복사해온 뒤 oplog를 그대로 자신의 노드에서 수행
* oplog entries 는 멱등성(idempotent)을 보장한다 -> 데이터 최종결과에 여러 번 적용될 수 있다
* 50gb / disk의 5% 크기로 제한된다 => 설정으로 변경할 수 있지만 대체로 충분하다....


Replication Lag(복제지연) 이 발생할 수 있는 상황
* Network latency
* Disk throughput
* Long-running operations
* Not having the appropriate write concerns


RECOVERING state
* 어떠한 이유로 Replication Lag이 크게 발생할 때...
* 해당 멤버는 vote는 가능하지만 read는 불가한 상태가 됨.
* initial sync를 해야 정상 상태로 돌아옴 -> oplog를 포함한 모든 데이터를 레플리카셋 멤버로 복사하는 프로세스
  * Network, Disk, CPU usage 가 많이 든다....


```
db.oplog.rs.find({"ns" : "sample_supplies.sales"}).sort({$natural: -1}).limit(5)

rs.printReplicationInfo()
rs.printSecondaryReplicationInfo()
```

> What is the role of the oplog in relation to replication? (Select one.)

* a. It keeps a running record of operations on a given member.

> You want to retrieve the status of your oplog, including details such as the configured size of your oplog and the first recorded event time. Which command should you use? (Select one.)

* c. rs.printReplicationInfo()

> Which of the following are causes of replication lag? (Select all that apply.)

* a. Network latency
* b. Disk throughput
* c. Write concerns

### Lesson 5: Read and Write concerns with MongoDB Deployments
Write Concern : 쓰기가 완료 되려면 몇 개의 ReplicaSet 멤버의 복제가 완료되어야 하는지
* 높은 수준의 Write Concern은 Durability(내구성)을 자랑
* Majority : 쓰기가 완료되려면 과반수의 레플리카셋에 복제가 완료되어야 함
* <number> : 쓰기가 완료되기 위해 복제가 완료되어야 하는 레플리케이션 셋 수

Read Concern : 읽기 durability를 보장
* local : 최신데이터
* available
* majority : 복제본 대부분이 수신확인한 뎅터
* linearizable : read concern 시작 전 완료된 쓰기를 리턴

읽기 설정
* primary
* primaryPreferred
* secondary
* secondaryPreferred
* nearest

```
db.adminCommand({
    setDefaultRWConcern : 1,
    defaultReadConcern: { level : "majority" },
    defaultWriteConcern: { w: "majority" }
  })
```

> You want data to be read only from your secondary nodes. How do you achieve this? (Select one.)

* c. Set the read preference to secondary.

> In a replica set, you want to require acknowledgement that write operations have been durably committed to a calculated majority of the data-bearing voting members. How do you achieve this? (Select one.)

* a. Set the write concern to majority.

### Lesson 6: Deploying a Replica set in a MongoDB Deployment

> You want to update the primary node of a replica set. How do you initiate an election? (Select one.)

* b. rs.stepDown()

> Which of the following commands initiates a replica set? (Select one.)

* a. rs.initiate()

### Lesson 7: Configuring a Replica set in a MongoDB Deployment
Replicaset을 재구성하는 경우
* `rs.hello()` : 대략적인 정보
* `rs.conf()` : 멤버 설정들에 대한 정보
  * rs.conf().필드 = 값 으로 설정값을 변경할 수 있다.
* rs.conf().members.push({_id: <number>, "host": <host>}) 로 멤버추가
* rs.conf().members.splice(1,1) 로 멤버 삭제
* rs.reconfig(rs.conf()) 로 변경된 컨피그 정보 저장

> You run the rs.status() method on your replica set. Given the following output message, which host is the primary? (Select one.)
```
{
  set: 'atlas-9ame3j-shard-0',
  date: ISODate("2023-03-10T21:30:25.181Z"),
  myState: 1,
  term: Long("173"),
  syncSourceHost: '',
  syncSourceId: -1,
  heartbeatIntervalMillis: Long("2000"),
  majorityVoteCount: 2,
  writeMajorityCount: 2,
  votingMembersCount: 3,
  writableVotingMembersCount: 3,
  optimes: {
    lastCommittedOpTime: { ts: Timestamp({ t: 1678483825, i: 15 }), t: Long("173") },
    lastCommittedWallTime: ISODate("2023-03-10T21:30:25.162Z"),
    readConcernMajorityOpTime: { ts: Timestamp({ t: 1678483825, i: 15 }), t: Long("173") },
    appliedOpTime: { ts: Timestamp({ t: 1678483825, i: 15 }), t: Long("173") },
    durableOpTime: { ts: Timestamp({ t: 1678483825, i: 15 }), t: Long("173") },
    lastAppliedWallTime: ISODate("2023-03-10T21:30:25.162Z"),
    lastDurableWallTime: ISODate("2023-03-10T21:30:25.162Z")
  },
  lastStableRecoveryTimestamp: Timestamp({ t: 1678483819, i: 26 }),
  electionCandidateMetrics: {
    lastElectionReason: 'stepUpRequestSkipDryRun',
    lastElectionDate: ISODate("2023-03-03T20:13:03.058Z"),
    electionTerm: Long("173"),
    lastCommittedOpTimeAtElection: { ts: Timestamp({ t: 1677874382, i: 13 }), t: Long("172") },
    lastSeenOpTimeAtElection: { ts: Timestamp({ t: 1677874382, i: 13 }), t: Long("172") },
    numVotesNeeded: 2,
    priorityAtElection: 7,
    electionTimeoutMillis: Long("5000"),
    priorPrimaryMemberId: 2,
    numCatchUpOps: Long("0"),
    newTermStartDate: ISODate("2023-03-03T20:13:03.162Z"),
    wMajorityWriteAvailabilityDate: ISODate("2023-03-03T20:13:04.128Z")
  },
  members: [
    {
      _id: 0,
      name: 'host0.mongodb.net:27017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 609553,
      optime: { ts: Timestamp({ t: 1678483823, i: 17 }), t: Long("173") },
      optimeDurable: { ts: Timestamp({ t: 1678483823, i: 17 }), t: Long("173") },
      optimeDate: ISODate("2023-03-10T21:30:23.000Z"),
      optimeDurableDate: ISODate("2023-03-10T21:30:23.000Z"),
      lastAppliedWallTime: ISODate("2023-03-10T21:30:25.162Z"),
      lastDurableWallTime: ISODate("2023-03-10T21:30:25.162Z"),
      lastHeartbeat: ISODate("2023-03-10T21:30:23.193Z"),
      lastHeartbeatRecv: ISODate("2023-03-10T21:30:23.246Z"),
      pingMs: Long("0"),
      lastHeartbeatMessage: '',
      syncSourceHost: 'host1.mongodb.net:27017',
      syncSourceId: 1,
      infoMessage: '',
      configVersion: 9,
      configTerm: 173
    },
    {
      _id: 1,
      name: 'host1.mongodb.net:27017',
      health: 1,
      state: 1,
      stateStr: 'PRIMARY',
      uptime: 609583,
      optime: { ts: Timestamp({ t: 1678483825, i: 15 }), t: Long("173") },
      optimeDate: ISODate("2023-03-10T21:30:25.000Z"),
      lastAppliedWallTime: ISODate("2023-03-10T21:30:25.162Z"),
      lastDurableWallTime: ISODate("2023-03-10T21:30:25.162Z"),
      syncSourceHost: '',
      syncSourceId: -1,
      infoMessage: '',
      electionTime: Timestamp({ t: 1677874383, i: 1 }),
      electionDate: ISODate("2023-03-03T20:13:03.000Z"),
      configVersion: 9,
      configTerm: 173,
      self: true,
      lastHeartbeatMessage: ''
    },
    {
      _id: 2,
      name: 'host2.mongodb.net:27017',
      health: 1,
      state: 2,
      stateStr: 'SECONDARY',
      uptime: 609282,
      optime: { ts: Timestamp({ t: 1678483824, i: 24 }), t: Long("173") },
      optimeDurable: { ts: Timestamp({ t: 1678483824, i: 24 }), t: Long("173") },
      optimeDate: ISODate("2023-03-10T21:30:24.000Z"),
      optimeDurableDate: ISODate("2023-03-10T21:30:24.000Z"),
      lastAppliedWallTime: ISODate("2023-03-10T21:30:25.162Z"),
      lastDurableWallTime: ISODate("2023-03-10T21:30:25.162Z"),
      lastHeartbeat: ISODate("2023-03-10T21:30:24.509Z"),
      lastHeartbeatRecv: ISODate("2023-03-10T21:30:23.727Z"),
      pingMs: Long("0"),
      lastHeartbeatMessage: '',
      syncSourceHost: 'host2.mongodb.net:27017',
      syncSourceId: 1,
      infoMessage: '',
      configVersion: 9,
      configTerm: 173
    }
  ],
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1678483825, i: 15 }),
    signature: {
      hash: Binary(Buffer.from("31d47b93602c9412e9fb4c2eac2cadc5eae03b8a", "hex"), 0),
      keyId: Long("7148911878087901206")
    }
  },
  operationTime: Timestamp({ t: 1678483825, i: 15 })
}
```
* b. host1.mongodb.net:27017

> You run the rs.conf() command on a replica set, which returns the following output. Currently, mongod0.replset.com:27017 has the highest priority, but you want to change it so that mongod2.replset.com:27017 has the highest priority.
> 
> First, you assign rs.conf() to a variable called config. Which of the following commands should you use to ensure that server mongod2.replset.com:27017 has the highest priority? (Select one.)

```
{
  _id: 'mongodb-repl-example',
  version: 1,
  term: 3,
  members: [
    {
      _id: 0,
      host: 'mongod0.replset.com:27017',
      arbiterOnly: false,
      buildIndexes: true,
      hidden: false,
      priority: 10,
      tags: {},
      secondaryDelaySecs: Long("0"),
      votes: 1
    },
    {
      _id: 1,
      host: 'mongod1.replset.com:27017',
      arbiterOnly: false,
      buildIndexes: true,
      hidden: false,
      priority: 7,
      tags: {},
      secondaryDelaySecs: Long("0"),
      votes: 1
    },
    {
      _id: 2,
      host: 'mongod2.replset.com:27017',
      arbiterOnly: false,
      buildIndexes: true,
      hidden: false,
      priority: 1,
      tags: {},
      secondaryDelaySecs: Long("0"),
      votes: 1
    }
  ],
  protocolVersion: Long("1"),
  writeConcernMajorityJournalDefault: true,
  settings: {
    chainingAllowed: true,
    heartbeatIntervalMillis: 2000,
    heartbeatTimeoutSecs: 10,
    electionTimeoutMillis: 10000,
    catchUpTimeoutMillis: -1,
    catchUpTakeoverDelayMillis: 30000,
    getLastErrorModes: {},
    getLastErrorDefaults: { w: 1, wtimeout: 0 },
    replicaSetId: ObjectId("63dc64c2692d2589bcd1838c")
  }
}
```
* a. config.members[2].priority = 100


> You run the db.hello() method on your replica set. Given the following output message, which host is the primary? (Select one.)

```
{
  topologyVersion: {
    processId: ObjectId("640254427adc6d84361ce560"),
    counter: Long("6")
  },
  hosts: [
    'mongod0.replset.com:27017',
    'mongod1.replset.com:27017',
    'mongod2.replset.com:27017'
  ],
  setName: 'mongodb-repl-example',
  setVersion: 1,
  isWritablePrimary: true,
  secondary: false,
  primary: 'mongod0.replset.com:27017',
  me: 'mongod0.replset.com:27017',
  electionId: ObjectId("7fffffff0000000000000003"),
  lastWrite: {
    opTime: { ts: Timestamp({ t: 1675469681, i: 1 }), t: Long("3") },
    lastWriteDate: ISODate("2023-02-04T00:14:41.000Z"),
    majorityOpTime: { ts: Timestamp({ t: 1675469681, i: 1 }), t: Long("3") },
    majorityWriteDate: ISODate("2023-02-04T00:14:41.000Z")
  },
  maxBsonObjectSize: 16777216,
  maxMessageSizeBytes: 48000000,
  maxWriteBatchSize: 100000,
  localTime: ISODate("2023-02-04T00:14:44.847Z"),
  logicalSessionTimeoutMinutes: 30,
  connectionId: 130,
  minWireVersion: 0,
  maxWireVersion: 17,
  readOnly: false,
  ok: 1,
 '$clusterTime': {
    clusterTime: Timestamp({ t: 1679013170, i: 22 }),
    signature: {
      hash: Binary(Buffer.from("8b26846115473501007904a39a6e6a169c9b1fa3", "hex"), 0),
      keyId: Long("7148911878087901206")
    }
  },
  operationTime: Timestamp({ t: 1679013170, i: 22 })
}
```

* c. mongod0.replset.com:27017

### Unit 15 정리
Lesson 1: Introduction to Replication
- [Replication](https://www.mongodb.com/docs/manual/replication/)

Lesson 2: Replication in MongoDB
- [Replication in MongoDB](https://www.mongodb.com/docs/manual/replication/#replication-in-mongodb)
- [Replica Set Primary](https://www.mongodb.com/docs/manual/core/replica-set-primary/)
- [Replica Set Secondary Members](https://www.mongodb.com/docs/manual/core/replica-set-secondary/)

Lesson 3: Automatic Failover and Elections with MongoDB Deployments
- [Replica Set Elections](https://www.mongodb.com/docs/manual/core/replica-set-elections/)

Lesson 4: The MongoDB Operation Log
- [Replica Set Oplog](https://www.mongodb.com/docs/manual/core/replica-set-oplog/)
- [Check the Replication Lag](https://www.mongodb.com/docs/manual/tutorial/troubleshoot-replica-sets/#check-the-replication-lag)

Lesson 5: Read and Write Concerns with MongoDB Deployments
- [Write Concern](https://www.mongodb.com/docs/manual/core/replica-set-write-concern/)
- [Read Concern](https://www.mongodb.com/docs/manual/reference/read-concern/)
- [Read Preference](https://www.mongodb.com/docs/manual/core/read-preference/)

Lesson 6: Deploying a Replica Set in a MongoDB Deployment
- [Deploy a Replica Set](https://www.mongodb.com/docs/manual/tutorial/deploy-replica-set/)

Lesson 7: Configuring a Replica Set in a MongoDB Deployment
- [db.hello()](https://www.mongodb.com/docs/manual/reference/method/db.hello/)
- [Adjust Priority for a Replica Set Member](https://www.mongodb.com/docs/manual/tutorial/adjust-replica-set-member-priority/)
- [Configure Replica Set Tag Sets](https://www.mongodb.com/docs/manual/tutorial/configure-replica-set-tag-sets/)
- [rs.conf()](https://www.mongodb.com/docs/manual/reference/method/rs.conf/)
- [Add Members to a Replica Set](https://www.mongodb.com/docs/manual/tutorial/expand-replica-set/#overview)
- [Remove Members from a Replica Set](https://www.mongodb.com/docs/manual/tutorial/remove-replica-set-member/)
- [rs.status()](https://www.mongodb.com/docs/manual/reference/method/rs.status/)


## Unit 16. Self-Managed Database Security
### Lesson 1: Introduction to Security
Authentication
* id, pw

Authorization
* Role-Based Access Control(RBAC) : 사용자에게 직접 권하능ㄹ 주는게 아니라 역할에 권한을 부여함

Auditing
* 데이터, 데이터베이스 구성에 대한 변경사항을 모니터링하고 기록하는 프로세스

> A user is required to enter a valid username and password in order to access a database. This is an example of which security practice? (Select one.)

* a. Authentication

> You grant a user permission to create and modify roles and users on the sample_analytics database. This is an example of which security practice? (Select one.)

* c. Authorization

> At your company, you're in charge of making sure only the portions of data necessary for the Security team to complete their tasks are accessible. You must ensure that the team cannot access data they do not need. Which practice is the best choice for you to implement? (Select one.)

* b. Role-Based Access Control (RBAC)

> What is the purpose of auditing in the context of database security? (Select all that apply.)

* b. Support the analysis of security incidents
* d. Comply with regulatory requirements

### Lesson 2: Enabling Authentication for a Self-Managed MongoDB Deployment
Default : SCRAM
* 암호화 키에 의해 보호되는 응답을 교환함으로서 사용자를 판별

user administrator
* user 권한 관리 책임
* 역할을 작성하고 수정할 수 있는 super database    
```
db.createUser(
{
user: "globalUserAdmin",
pwd: passwordPrompt(),
roles: [
{ role: "userAdminAnyDatabase", db: "admin" }
]
}
)
```

> What is the default authentication mechanism for MongoDB? (Select one.)

* c. SCRAM

> You assign a user the userAdminAnyDatabase role. What types of actions can the user take with this role only? (Select all that apply.)

* a. Create users and roles
* c. Modify users and roles

### Lesson 3: Establishing Authorization for a Self-Managed MongoDB Deployment
Autorization : 유저에게 권한 부여

> You want to create users on a self-managed MongoDB deployment. What do you need to do before you can do so? (Select all that apply.)

* a. Enable access control
* c. Create a user administrator

> You need to create a new user and want to assign roles to them at the same time. What method should you use? (Select one.)

* b. db.createUser()

### Lesson 4: Security Auditing in MongoDB
Autiting : 모니터링, 감사를 위함. 규제요구사항 준수하고 사고분석을 지원하기 위함
* Syslog - JSON format
* Console - JSON format
* File - JSON or BSON format

autit message filed
* atype - action type
* result - error code of the action

> Which destinations can audit events be printed to when using a self-managed MongoDB instance? (Select all that apply.) 

* a. Console
* b. Syslog
* d. BSON file

> Given the following configuration file, where are audit events printed on this MongoDB instance? (Select one.)

```
# mongod.conf


storage:
 dbPath: /var/lib/mongodb


systemLog:
 destination: file
 logAppend: true
 path: /var/log/mongodb/mongod.log


net:
 port: 27017
 bindIp: 127.0.0.1


processManagement:
 timeZoneInfo: /usr/share/zoneinfo


security:
 authorization: enabled


auditLog:
 destination: file
 format: BSON
 path: /var/log/mongodb/auditLog.bson
```

* c. /var/log/mongodb/auditLog.bson

### Lesson 5: Introduction to Encryption Concepts
Encryption : 허용된 사용자만 읽을 수 있도록 데이터를 인코딩
* Transport encryption
  * TLS
* Encryption at rest
  * DB서버에서 데이터 파일을 암호화 하는 프로세스
* In-use encryption
  * CSFLE

> What are some limitations of encryption at rest? (Select all that apply.)

* a. Managing encryption keys can be a challenge.
* b. It does not protect against attacks on data in memory.
* d. It does not protect against insider threats.

> A doctor’s office stores patient medical records in a database. To provide an extra layer of security for medical diagnosis information, you want to use a method of encryption in which this data is encrypted in the client application before it’s sent over the network to the MongoDB servers. What type of encryption should you use? (Select one.)

* b. Client-Side Field Level Encryption (CSFLE)

### Lesson 6: Encryption in Self-Managed MongoDB Deployments
* Transport encryption
  * TLS
* Encryption at rest
  * DB서버에서 데이터 파일을 암호화 하는 프로세스
* In-use encryption
  * CSFLE

> How does MongoDB provide encryption at rest? (Select all that apply.)

* a. Client-Side Field Level Encryption (CSFLE)
* c. Encrypted Storage Engine

> How does MongoDB support encryption of data in transit? (Select all that apply.)

* c. Transport Layer Security (TLS)
* b. Client-Side Field Level Encryption (CSFLE)

> How does MongoDB support in-use encryption? (Select all that apply.)

* a. Client-Side Field Level Encryption (CSFLE)
* b. Automatic encryption

### Lesson 7: Enabling Network Encryption For a Self-Managed MongoDB Deployment
ReplicaSet 간 TLS연결 -> 자체 연결 배치에서 디폴트로 TLS 사용

> You want to enable Transport Layer Security (TLS) for a self-managed MongoDB deployment at your organization. Which certificate should you or your organization obtain prior to enabling TLS? (Select one.)

* b. A valid TLS certificate issued by a certificate authority for each server in the deployment

> You want to specify that a server uses and accepts only TLS-encrypted connections. What should you set the net.tls.mode configuration file setting to? (Select one.)

* c. requireTLS

### Unit 16 정리

Lesson 1: Introduction to Security
- [Authentication](https://www.mongodb.com/docs/manual/core/authentication/)
- [Role-Based Access Control](https://www.mongodb.com/docs/manual/core/authorization/)
- [Auditing](https://www.mongodb.com/docs/manual/core/auditing/cation/)

Lesson 2: Enabling Authentication for a Self-Managed MongoDB Deployment
- [Enable Access Control](https://www.mongodb.com/docs/manual/tutorial/enable-authentication/#std-label-enable-access-control)
- [Use SCRAM to Authenticate Clients](https://www.mongodb.com/docs/manual/tutorial/configure-scram-client-authentication/)
- [Localhost Exception](https://www.mongodb.com/docs/manual/core/localhost-exception/)

Lesson 3: Establishing Authorization for a Self-Managed MongoDB Deployment
- [Role-Based Access Control](https://www.mongodb.com/docs/manual/core/authorization/)
- [Create a User](https://www.mongodb.com/docs/manual/tutorial/create-users/)
- [Built-In Roles](https://www.mongodb.com/docs/manual/reference/built-in-roles/)
- [Authenticate a User](https://www.mongodb.com/docs/manual/tutorial/authenticate-a-user/)
- [List Users](https://www.mongodb.com/docs/manual/tutorial/list-users/)
- [Modify Access for an Existing User](https://www.mongodb.com/docs/manual/tutorial/manage-users-and-roles/#modify-access-for-an-existing-user)

Lesson 4: Security Auditing in MongoDB
- [Auditing](https://www.mongodb.com/docs/manual/core/auditing/)
- [System Event Audit Messages](https://www.mongodb.com/docs/manual/reference/audit-message/)
- [Audit Options](https://www.mongodb.com/docs/manual/reference/program/mongod/#audit-options)

Lesson 5: Introduction to Encryption Concepts
- [MongoDB Data Encryption](https://www.mongodb.com/products/capabilities/security/encryption#:~:text=Encryption%20at%2Drest%20is%20a,is%20AES%2D256%20via%20OpenSSL.)

Lesson 6: Encryption in Self-Managed MongoDB Deployments
- [Encryption at Rest](https://www.mongodb.com/docs/manual/core/security-encryption-at-rest/)
- [Configure Encryption](https://www.mongodb.com/docs/manual/tutorial/configure-encryption/)
- [TLS/SSL (Transport Encryption)](https://www.mongodb.com/docs/manual/core/security-transport-encryption/)
- [Client-Side Field Level Encryption](https://www.mongodb.com/docs/manual/core/csfle/)

Lesson 7: Enabling Network Encryption for a Self-Managed MongoDB Deployment
- [Upgrade a Cluster to Use TLS/SSL](https://www.mongodb.com/docs/manual/tutorial/upgrade-cluster-to-ssl/)
- [net Options](https://www.mongodb.com/docs/manual/reference/configuration-options/?_ga=2.149826678.1926118966.1686611566-1191611927.1686611566#net-options)