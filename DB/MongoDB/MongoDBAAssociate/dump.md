### Question No : 1

> Which of the following node is used during election in a replication cluster?
 A.primary
 B.arbiter
 C.hidden
 D.secondary

답안
* B.arbiter

정답
* B.arbiter

### Question No : 2

> In a replicated cluster, which of the following node would only be used during an election?
 A.arbiter
 B.primary
 C.hidden
 D.secondary

답안
* A.arbiter

정답
* A.arbiter

### Question No : 3

> Which are the ONLY ways to project portions of an array?
 A.$slice
 B.$
 C.All of the above
 D.$ elemMatch

답안
* D.$ elemMatch

정답
* C.All of the above

### Question No : 4

> MongoDB is
 A.None of the above
 B.Object-oriented DBMS
 C.Relational DBMS
 D.Document-oriented DBMS

답안
* D.Document-oriented DBMS

정답
* D.Document-oriented DBMS

### Question No : 5

> Dada una coleccion, cuales devuelve con la siguiente query db.coleccion.find({nombre:"ruben",apellido:"gomez"},{nombre:l,apellido:l,aficion:l});
 A.{ "-id" : Objectld("580a42b5dfblb5al7427d302"), "nombre" : "ruben", "apellido" : "gomez", "aficion" : v u "flipar" }
 B.{ "_id" : Objectld("580a42acdfblb5al7427d301"), "nombre" : "Luis", "apellido" : "gomez", "aficion" : u "flipar" }
 C.{ "_id" : Objectld("580a42acdfblb5al7427d301"), "nombre" : "ruben", "apellido" : "Pablo", "aficion" : u "flipar"}
 D.{ "_id" : Objectld("580a42acdfblb5al7427d301"), "nombre" : "ruben", "apellido" : "gomez">

답안
* A.{ "-id" : Objectld("580a42b5dfblb5al7427d302"), "nombre" : "ruben", "apellido" : "gomez", "aficion" : v u "flipar" }

정답
* A.{ "-id" : Objectld("580a42b5dfblb5al7427d302"), "nombre" : "ruben", "apellido" : "gomez", "aficion" : v u "flipar" }
* D.{ "_id" : Objectld("580a42acdfblb5al7427d301"), "nombre" : "ruben", "apellido" : "gomez">

### Question No : 6

> Which option can be used with update command so that a new document gets created if no matching document is found based on the query condition?
 A.upsert command instead of update command
 B.{update: true, insert: true} as the third parameter of update command
 C.This has to be handled in application code (Node.js, PHP, JAVA, C#, etc.) and cannot be handled in mongo shell query
 D.Specify {upsert : true } as the third parameter of update command

답안
* D.Specify {upsert : true } as the third parameter of update command

정답
* D.Specify {upsert : true } as the third parameter of update command

### Question No : 7

> In order to ensure that you can maintain high availability in the face of server failure, you should implement which of the following?
 A.Sharding
 B.Properly defined user roles
 C.Replication
 D.Put indexes on all of your documents
 E.The proper storage engine

답안
* C.Replication

정답
* C.Replication

### Question No : 8

> What does the totalKeysExamined field returned by the explain method indicate?
 A.Number of documents that match the query condition
 B.Number of index entries scanned
 C.Details the completed execution of the winning plan as a tree of stages
 D.Number of documents scanned

답안
* B.Number of index entries scanned

정답
* B.Number of index entries scanned

### Question No : 9

> Which command can be used to rebuild the indexes on a collection in MongoDB?
 A.db.collection.createlndex({relndex:l})
 B.db.collection.reIndex({author:l})
 C.db.collection.relndexQ
 D.db.collection.createIndex({author:l}).reIndex()

답안
* D.db.collection.createIndex({author:l}).reIndex()

정답
* C.db.collection.relndexQ

### Question No : 10

> Given a replica set with five data-bearing members, suppose the primary goes down with operations in its oplog that have been copied from the primary to only one secondary.
Assuming no other problems occur, which of the following describes what is most likely to happen?
 A.missing operations will need to be manually re-performed
 B.the secondary with the most current oplog will be elected primary
 C.reads will be stale until the primary comes back up
 D.the primary may roll back the operations once it recovers
 E.the most current secondary will roll back the operations following the election

답안
* E.the most current secondary will roll back the operations following the election

정답
* B.the secondary with the most current oplog will be elected primary

### Question No : 11

> That RSI and RS2 can be primary?
> You had to see the different configurations, RS3 could be hidden or priority 0 (But not a referee because we need 3 replicas), while RSI and RS2 could NOT have priority 0 or be hidden or anything like that .
> In a 4-member RS RSO, RSI, RS2 and RS3 + Referee, RSO (primary) falls after some write operations that have replicated RSI and RS2 (but NOT RS3), who can get up as the new primary?
> The configuration comes and in it we see that RS2 has a hidden: true (or a priority: 0, (I don't remember)
 A.ORS1
 B.ORS2
 C.ORS3
 D.O arbiter
 E.RSO

답안
 A.ORS1

정답
 A.ORS1

### Question No : 12

> Which of the following statements are true about the $match pipeline operator? Check all that apply.
 A.You should use it early as possible in the pipeline
 B.It can be used as many time as needed.
 C.It has a sintax similar to findQ commands.

답안
 A.You should use it early as possible in the pipeline
 B.It can be used as many time as needed.
 C.It has a sintax similar to findQ commands.

정답
 A.You should use it early as possible in the pipeline
 B.It can be used as many time as needed.
 C.It has a sintax similar to findQ commands.

### Question No : 13

> Using an arbiter allows one to easily ensure an odd number of voters in replica sets.
> Why is this important?
 A.To help in disaster recovery
 B.To protect agains network partitions
 C.To enable certain read preference settings
 D.To add greather redundancy
 E.For more efficient backup operations

답안
 A.To help in disaster recovery

정답
 B.To protect agains network partitions

### Question No : 14

> Which node in a replica set does accept write operation?
 A.arbiter
 B.hidden
 C.primary
 D.secondary

답안
 C.primary

정답
 C.primary

### Question No : 15

> What is the output of the following program?
 A.60 s
 B.1s
 C.100 s
 D.100 ms

답안
 D.100 ms

정답
 A.60 s
