# LG U+ Cloud Management Platform의 MongoDB 활용 사례

## UCMP
* LG Uplus의 내부 개발자 플랫폼.
* 보안/규졍을 준수하는 개발환경 자동 구축하는 내부 개발자 플랫폼.
* 개발환경 자동 구축 / 개발 환경 관리 / 보안 상태 관리
  * 깃헙 저장소 생성 관리/ AWS 생성 관리 / 클라우드 인프라 상태 관리
  * 인프라 프로비저닝을 자동화해주는 플랫폼

## MongoDB 도입 방법
인프라 보안 도입 이전에는 RDB만 사용중이었음.

MongoDB 도입 배경
* 점검 결과 정보는 외부 시스템(prowler)에 의해 데이터 구조가 결정되는데, 오픈소스이기 때문에 버전 업데이트가 활발하고, 버전 업데이트에 따라 점검 결과 형식이 변경됨.
* 점검 결과 형식이 변경될 때 마다 스키마 변경 대응에 많은 시간과 노력이 소요됨.

Backgroupnd
* Relational Model
  * 테이블 구조가 고정되어 있기 때문에 점검 결과 형식이 변경될 때 마다 스키마 변경이 필요함.
* Document Model을 채택하여 JSON 형식으로 데이터를 유연하게 처리 가능. 점검 결과 형식이 변경되어도 필요한 데이터를 바로 저장하고 읽기가 가능핟.

Data Modeling
* 취약점 정보별 리소스 정보
  * 임베딩 방식으로 저장.
  * 단일 조회 작업으로 필요한 모든 데이터를 가져올 수 있어 성능상 이점을 제공함.

Low Learning Curve
* Spring Data MongoDB를 활용하면 쉽게 쿼리 할 수 있음.
* Custom Repository Impementations -> MongoRepository + Mongo Template의 장점만 취득한 Spring MongoDB Driver

Easy Provisioning
* HA구성. 레플리카셋을 통해 데이터를 복제하여 데이터 안정성 제공

## 쿼리 개선
Aggregation Pipeline
* 효율적인 데이터 필터링, grouping 및 aggregation
* 여러 stage를 조합해 원하는 결과를 생성
* 각 stage는 이전 stage결과를 입력으로 사용.
* $match stage를 통해 다음 stage로 보내는 데이터 양을 줄여주는게 중요. -> $group이나 $sort 스테이지가 실행시간 증가의 주요 원인이 될 수 있음.

예시
* 검색 조건을 기반으로 취약점을 그룹화하고 등급순 정렬하는 페이지
* ->검색조건이 없는 경우 전체 계정에 대한 통계를 위해 컬렉션 내 전체 스캔이 불가피했음
* $group zjffprtusdptj tjdsmd wjgkrk qkftodgka -> rkr rmfnqdml wjdqhfmf apahfldp dbwlgodi 
* $group 기준이 되는 필드를 최소화 해야 했다. -> 쿼리를 둘로 분리
  * 집계와 직접적으로 관련 없는 필드 -> 점검 결과 컬렉션 내 취약점 정보 컬렉션에서 조회 / match&project만 하는 단순 쿼리로 튜닝
  * 집계와 직접적으로 관련 있는 필드 -> 리소스, 취약점 상태 필드는 점검 결과 컬렉션에서 리소스 및 취약점 상태를 기준으로 채ㅕㅜㅅ wlqrP. flxjsehlsms ehzbajsxm tnsst수는 동일하지만 기준필드가 줄어들어 튜닝됨.
* => 기존 대비 쿼리 실행시간 99.11% 감소. 쿼리 튜닝, 인덱스 적용, 캐시 적용순으로 점점 튜닝했음

## 향후 계획
* 정기 점검 배치 시 쓰기 작업 트래핑 일시적 증가
  * functions & triggers dhqtusdmfh dlfwjd wkrdjqdmf wlwjd tlrksdp tlfgodehlehfhr tjfwjd
  * function에 대한 스케일 다운에 대해 작성하고, 예정된 정기배치 작업 종료 시간에 스케줄링(업/다운)할 수 있어 비용 효율 최적화 할 수 있다.

유연한 인덱싱
* 중요한 데이터가 임베딩 되어 있어서 쿼리 성능 개선/인덱싱에 어려움이 있었음.
* Performance Advisor를 이용하여 쿼리 성능 개선에 도움이 됨. 느리게 실행되는 쿼리에 대해 제안..

TTL
* 시간 지나면 자동적으로 데이터 제거하는 설정.
* 한번에 대규모 삭제 작업이 발생할 경우에 대한 성능 이슈 검토 필요
