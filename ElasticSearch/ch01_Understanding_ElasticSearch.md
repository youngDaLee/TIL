# Installing and Understanding ElasticSearch

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

## Elastic Overview


## Intro to HTTP nad RESTful API's


## Elasticsearch Basics: Logical Concepts


