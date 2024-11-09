# Relational Migrator를 이용한 애플리케이션 현대화

애플리케이션 마이그레이션 주요 도전과제
* 기회 분석 - 후보 애플리케이션과 전략 선택
  * 어떤애를 골라서 마이그레이션 할지
  * 해당 애플리케이션을 초기 설계했던 사람이 아직 우리 조직에 있는가
  * 어떤 전무지식이 필요한지/비즈니스 사례는 어떻게 구축할ㅈ
* 데이터 모델 - 최신 데이터 플랫폼 설계
  * NoSQL 데이터 패턴을 어떻게 채택할지
  * 누가 이 기본 데이터에 이해하고 있는지
  * 유연성과 확정성을 위해 어떻게 설계할지
* 마이그레이션 플랜 - 데이터 전환 및 생산/서비스 중단
  * 프로덕션 전환 프로세스는 무엇인지
  * 마이그레이션 계획을 테스트하고 발전시킬 수 있는지
  * 데이터 무결설을 어떻게 검증할것인지
  * 실제 프로토타입으로 리스크를 줄일 수 있는지
* 애플리케이션 리팩토링 - 애플리케이션 코드 리팩토링 및 재설계
  * ORM/데이터계층을 어떻게 리포인팅 할건지
  * 다른 어플리케이션이 이 데이터에 접근하는지
  * 저장 프로시저나 트리거를 어떻게 마이그레이션 할지

관계형 워크로드를 안심하고 MongoDB로 가져오세요
* MongoDB에서는 MongoDB 스키마 설계를 지원. RDB->NoSQL 매핑 권고안
* 소스 데이터를 마이그레이션 하고 변환
* 데이터와 관련된 데이터 오브젝트들.. 저장 프로시저/sql/ 등등을 Mql로 변환할 수 있도록 코드 생성도 지원함.

MongoDB애서 지원하는 DB
* 오라클
* SQL Server
* MySQL
* PostgerSQL
* Sybase

## 데모 1) 데이터 변환하기(Transforming)
* NoSQL 데이터 패턴 필터링 등...
* Relational Migrator를 로컬에 설치하면 -> 

## 애플리케이션 현대화
* SQL(애플리케이션 코드, 트리거, 프로시저 등)을 현대화

## 마무리
* 무료임 -> Realtional Migrator 다운로드