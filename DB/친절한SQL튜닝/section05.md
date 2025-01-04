# 소트 튜닝
## 5-1. 소트 연산에 대한 이해
소트 유형
* 메모리 소트(In-Memory Sort) : 메모리 내에서 정렬 완료(Internal Sort)
* 디스크 소트(To-Disk Sort) : 할당받은 메모리 내에서 완료하지 못해서 디스크 공간까지 활용하는 것(External Sort)

부분 범위 처리를 불가능하게 함으로서(?) OLTP 환경에서 애플리케이션 성능 저하 일으키는 주요인
* 소트 발생하지 않도록 SQL 작성하고, 불가피하면 메모리 내에서 처리 완료되도록 해야함

Sort Operation
* Sort Aggregate : 전체 로우 대상 집계. 실제로 정렬하는건 아니고 Sort Area를 사용한다는 뜻
* Sort Order By : 데이터 정렬 할 때 나타남
* Sort Group By : 소팅 알고리즘으로 그룹별 집계 할 때(10,20,30,40 별로 그룹핑 할 때 -> sorting)
* Sort Unique : 서브쿼리 Unnesting 과정에서 메인 쿼리에 조인하기 전 중복 레코드 제거시
* Sort Join : 소트 머지 조인수행 시
* Window Sort : 분석함수(윈도우함수) 수행 시

## 5-2. 소트가 발생하지 않도록 SQL 작성

Union vs Union All
* Union을 사용하면 상단/하단 두 집합간 중복 제거하려고 소트 작업함
* Union All 하면 중복 확인하지 않고 단순 결합
* => 가능하면 UnionAll 써라

Exists 활용
* 중복 레코드 제거 차원에서 Distinct 사용하면 -> 조건에 해당되는 데이터 모두 읽어서 중복 제거해야 함 -> 부분 범위 처리 불가하고 데이터 읽는 과정에 많은 I/O 발생....
* Exists는 데이터 존재 여부만 확인하므로 조건절 만족하는 데이터 모두 읽지 않음
* Minus, Distinct는 대체로 Exists로 대체 가능함

조인 방식 변경
* 인덱스를 이용해 적절하게 조인하면 Sort 생략 가능

