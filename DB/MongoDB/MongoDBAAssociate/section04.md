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

show log
* M10+ 클러스터에서 유효
* 최근 로그 이벤트들을 리턴
* 1024개의 엔트리를 저장


### Lesson 3. MongoDB Log Events

### Lesson 4. MongoDB Server Log Customization

### Lesson 5. MongoDB Server Log Rotation and Retention

### Unit 9 정리

## Unit 10. MongoDB Database Administrator Tools

## Unit 11. Self-Managed Server Administration
