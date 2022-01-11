# Installing and Understanding ElasticSearch

## ElasticSearch
[출처-Elastic 가이드북](https://esbook.kimjmin.net/01-overview/1.1-elastic-stack/1.1.1-elasticsearch)
- 오픈소스
  - 루씬으로 만들어짐
  - 루씬이 자바로 만들어졌기 때문에 ES도 자바로 코딩되어있음
- 실시간 분석(real-time) 시스템
  - ES 클러스터가 실행되고 있는 동안에는 계속 데이터가 입력(indexing)되고, 그와 동시에 실시간에 가까운 속도로 데이터 검색, 집계 가능
- 전문(full text)검색 엔진
  - indexing된 모든 데이터를 inverted file index구조로 저장해서 가곡된 텍스트를 검색. -> 이런 특성을 전문(full text)검색이라 함. 
  - 내부적으로는 inverterd file index 구조로 데이터 전달하지만, 사용자 관점에서는 JSON 형태로 데이터 전달
  - key-value 형식이 아닌 문서 기반이기 때문에 복합적인 정보를 포함하는 형식의 문서를 있는 그대로 저장 가능. -> indexing할 문서 가공하거나 다른 클라이언트 프로그램과 연동하기 간편함
  - 모든 데이터를 JSON 형태로 가공할 필요 있음 -> Logstash에서 변환 지원
- RESTful API
  - ES는 REST API를 기본적으로 지원. 데이터 조회, 입력, 삭제를 http 프로토콜을 통해 Rest API로 처리
- 멀티테넌시(multitenancy)
  - ES 데이터는 인덱스(Index)라는 논리적 집합 단위로 구성되며 서로 다른 저장소에 분산되어 저장됨.

## Installing ElascitcSearch
> Ubuntu에 엘라스틱서치 설치
1. [ElasticSearch 공식 사이트](https://www.elastic.co/kr/downloads/)에서 우분투 서버에 다운로드
   1. 다운로드 `curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.16.2-linux-x86_64.tar.gz`
   2. 압축 해제 `tar -xzvf elasticsearch-7.16.2-linux-x86_64.tar.gz`
2. 로그 폴더 생성 및 권한 부여
   1. `sudo mkdir /mnt/data`
   2. `sudo mkdir /mnt/logs`
   3. `chown dylee:dylee /mnt/data`
   4. `chown dylee:dylee /mnt/logs`

> 엘라스틱서치 환경 설정 (`config/elasticsearch.yml`)
1. cluster name 설정
```yml
# ---------------------------------- Cluster -----------------------------------
#
# Use a descriptive name for your cluster:
#
cluster.name: my-elasticsearch
#
```
2. node name 설정
```yml
# ------------------------------------ Node ------------------------------------
#
# Use a descriptive name for the node:
#
node.name: node-1
#
# Add custom attributes to the node:
#
#node.attr.rack: r1
#
```
3. path 설정
```yml
# ----------------------------------- Paths ------------------------------------
#
# Path to directory where to store the data (separate multiple locations by comma):
#
path.data: /mnt/data
#
# Path to log files:
#
path.logs: /mnt/logs
```
4. network 설정
```yml
# ---------------------------------- Network -----------------------------------
#
# By default Elasticsearch is only accessible on localhost. Set a different
# address here to expose this node on the network:
#
network.host: 0.0.0.0
#
# By default Elasticsearch listens for HTTP traffic on the first free port it
# finds starting at 9200. Set a specific HTTP port here:
#
http.port: 9200
#
# For more information, consult the network module documentation.
#
```
5. discovery 설정

```yml
# --------------------------------- Discovery ----------------------------------
#
# Pass an initial list of hosts to perform discovery when this node is started:
# The default list of hosts is ["127.0.0.1", "[::1]"]
#
discovery.seed_hosts: ["127.0.0.1"]
#
# Bootstrap the cluster using an initial set of master-eligible nodes:
#
cluster.initial_master_nodes: ["node-1"]
#
# For more information, consult the discovery and cluster formation module documentation.
#
# 
```
6. 위처럼 .yml 파일 설정 마친 후 `sudo /bin/systemctl daemon-reload`
7. `./bin/elasticsearch`

정상적으로 작동이 되면 아래와 같이 확인할 수 있다.    
![img](../.img/es/es_ch01_1.png)
### Error
```
ERROR: [1] bootstrap checks failed. You must address the points described in the following [1] lines before starting Elasticsearch.
bootstrap check failure [1] of [1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```
- [관련 사이트](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#_set_vm_max_map_count_to_at_least_262144)
- 에러 원인 : 
- sysctl.conf 파일을 수정한다
```
$ sudo vi /etc/sysctl.conf

vm.max_map_count=262144

```

## Intro to HTTP nad RESTful API's
- Method : GET, POST, PUT or DELETE
- Protocol : What flavor of HTTP
- Host : What web server you want to talk to
- URL : What resource is being requested
- Body : Extra data needed by the server
- Headers : User-agent, countent-type ... 


## Elasticsearch Basics: Logical Concepts
- Document : elasticsearch는 텍스트 뿐만 아니라 어떤 형태의 데이터도 저장 가능함. 데이터는 json 형태로 저장됨. 모든 도큐먼트는 Unique한 ID를 가짐.
- Indices
- 인덱스는 DB테이블로, 도큐먼트는 테이블의 row로 생각하면 됨.
- 도큐먼트 데이터타입 정의하는 scheme도 인덱스에 속함
- 단일 인덱스에는 하나의 도큐먼트만 허용
- cluster = database
- idices = tables
- documents = row in tables

## Term Frequency / Inverse Document Frequency (TF/IDF)
정보검색과 텍스트마이닝에서 이용하는 가중치. 어떤 단어가 특정 문서 내에서 얼마나 중요한 것인지 나타내는 통계적 수치. 문서의 핵심어를 추출하거나, 검색 엔진에서 검색 결과의 순위를 결정하거나, 문서들 사이의 비슷한 정도를 구하는 등의 용도로 사용.
- 출처 : [위키백과](https://ko.wikipedia.org/wiki/Tf-idf)

강의에서의 정의
- TF-IDF = Term Frequency * Inverse Document Frequency
- Term Frequency : 단어가 document에서 나온 회숫
- Documnet Frequency : 단어가 모든 documnts에서 나온 횟수
- Term Frequency/Document Frequency : document의 단어에 대해 관련성을 측정하는 것


## Using Elasticsearch
### Using Indices
- RESTful API
  - ElasticSearch 는 기본적으로 HTTP request와 JSON 데이터를 사용함.
- Client API's
- Analytic Tools

## How Elasticsearch Scales
- 문서들은 각 shard들로 해시됨
- 각각의 샤드들은 클러스터 안의 다른 노드들임
- 모든 샤드는 각각 자신의 Lucene 인덱스를 포함함

### Primary and Replica Shard
- 인덱스는 두 primary shard와 두 replica를가지고 있음.

강의로 이해가 힘들어 [Elastic가이드북](https://esbook.kimjmin.net/03-cluster/3.2-index-and-shards) 참고하여 Primary샤드와 Replica 샤드에 대해 정리함
- ES 데이터 단위 기본 개념
  - Document : 단일 데이터 단위
  - Index : document를 모아놓은 집합
  - indices : 데이터 저장 단위
  - shard : 인덱스가 분리되는 단위
- index 구성 시 별도의 설정을 하지 않으면, 7.0 버전부터는 디폴트로 1개의 샤드로 인덱스가 구성됨.
- 처음 생성된 샤드를 **Primary Shard**, 복제본을 **Replica**라 함.
