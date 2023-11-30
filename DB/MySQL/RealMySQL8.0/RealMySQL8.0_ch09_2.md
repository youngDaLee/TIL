## 9.3 고급 최적화
#### 9.3.1.15 컨디션 팬 아웃
* 조인 테이블 순서는 성능에 매우 큰 영향을 미침
* 여러 테이블이 조인되는 경우는 일치하는 레코드가 적은 순으로 조인을 실행

<img width="607" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/d9df082e-6a82-48a5-81be-e8df42154c95">

1. employees 에서 인덱스 활용해 조건(`Matt`)에 일치하는 레코드 233건 가져옴
2. filtered 컬럼 값이 100 -> 233 건 모두가 hire_date 컬럼 조건 마족할것으로 예측함
3. 233건에 대해 salaries 테이블 레코드 읽음 -> employess 한 건당 10건 일치할것으로 예측함


<img width="612" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/efff91b8-3e30-431a-acdf-5c8a8341e9a3">

* 활성화 이후 first_name 컬럼 조건 외에 나머지 조건(hire_date) 에 대해서도 얼마나 조건 충족하는지를 고려함
* condition_fanout_filter 최적화가 된 경우 특정 조건을 만족하는 컬럼에 대한 **조건 만족하는 레코드 비율**을 계산 가능
  * WHERE 조건절에 사용된 컬럼에 대해 인덱스가 있는 경우
  * WHERE 조건절에 사용된 컬럼에 대해 히스토그램이 존재하는 경우
* 좀 더 정교한 계산을 거쳐 실행계획을 수립하는 기능
* 8.0 이하 버전에서도 쿼리 실행 계획이 잘못된 선택을 한 적이 별로 없으면 condition_fanout_filter 최적화는 성능 향상에 크게 도움이 안될지도...
* MySQL 서버가 처리하는 쿼리 빈도가 매우 높으면 오히려 실행계획 수립에 추가되는 오버헤드가 크게 보일 수있음... -> 업그레이드 실행 전 성능 테스트 먼저 하는게 좋음

#### 9.3.1.16 파생 테이블 머지(derived_merge)
* 이전 버전의 MySQL 서버는 FROM 절 서브쿼리 먼저 실행해서 결과를 임시테이블로 만든 뒤 쿼리 부분 처리함
* 임시테이블이 메모리에 상주할 만큼 크기가 작으면 성능에 영향 미치지 않지만 레코드 많아지면 쿼리 성능 떨어짐....
* 5.7 버전부터 파생테이블로 만들어지는 서브쿼리를 외부 쿼리와 병합해서 서브쿼리 제거하는 최적화 도입됨 (derived_merge)
  * 모든 쿼리에 대해 서브쿼리를 외부로 병합처리 하는 건 아니므로 가능하다면 서브쿼리 수동으로 병합해서 처리하는게 성능 향상이 좋음

서브쿼리 외부로 수동 병합하는 게 성능에 나은 경우..
* SUM(), MIN(), MAX() 같은 집계 함수, 윈도우 함수 사용된 서브쿼리
* DISTINCT가 사용된 서브쿼리
* GROUP BY, HAVING이 사용된 서브쿼리
* LIMIT이 사용된 서브쿼리
* UNION이나 UNION ALL 이 사용된 서브쿼리
* SELECT 절에 사용된 서브쿼리
* 값이 변경되는 사용자 변수가 사용된 서브쿼리

#### 9.3.1.17 인비저블 인덱스(use_invisible_indexes)
인덱스 가용 상태를 제어할 수 있는 기능
* 8.0 이전은 인덱스가 존재하면 옵티마이저가 항상 인덱스를 검토하고 사용함
* 8.0 부터는 인덱스 삭제하지 않고 인덱스 사용하지 못하게 제어함

```sql
-- // 옵티마이저가 ix_hiredate 인덱스를 사용 못하게 변경
ALTER TABLE employees ALTER INDEX ix_hiredate INVISBLE;

-- // 옵티마이저가 ix_hiredate 인덱스를 사용할 수 있게 변경
ALTER TABLE employees ALTER INDEX ix_hiredate VISBLE;
```

#### 9.3.1.18 스킵 스캔(skip_scan)
* (A, B, C) 컬럼으로 구성된 인덱스가 왼쪽에 있는 값만 조건에 추가한다면 사용 가능(A / A,B / A,B,C)
* (A, B, C) 에서 (B, C) 로는 인덱스 활용 불가 -> 인덱스 스킵 스캔 : 인덱스 제약 사항 뛰어넘을 수 있는 최적화 기법
* 8.0 부터는 인덱스 선행 컬럼이 조건절에 사용되지 않아도 후행 컬럼 조건만으로 쿼리 성능 개선 가능함
  * 선행 컬럼 값을 가져와 선행 컬럼 조건이 있는 것 처럼 쿼리를 최적화함
  * gender 와 같은 속성 처럼 선행 컬럼이 소수의 유니크한 값을 가질 땜나 인덱스 스킵 스캔 최적화함....

#### 9.3.1.19 해시조인(hash_join)
* 첫 번째 레코드를 찾는 데는 시간이 많이 걸리지만 최종 레코드 찾는 데 까지는 많이 걸리지 않음
* 최고 스르풋 전략에 적합
  * 네스티드 루프 조인은 최고 응답속도 전략에 적합 (최초 찾는데는 빠르지만 최종 레코드는 오래걸림)

해시 조인은 빌드 단계와 프로브 단계로 나뉘어 처리됨
* Build-phase : 조인 대상 테이블 중 레코드 건수가 적어 해시 테이블로 만들기 용이한 테이블 골라서 해시 테이블 생성하는 작업 수행
* Probe-phase : 나머지 테이블 레코드를 읽어서 해시 테이블 일치 레코드 찾는 과정

<img width="612" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/d0aa1093-baa9-4ef7-9851-782129767bce">

<img width="484" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/5f751bcd-5f1a-44cc-a2c1-8870e1ffc8d3">

* 실행 계획최하단 제일 안쪽의 dept_emp 테이블이 빌드 테이블로 선정됨
* 옵티마이저는 해시 조인을 위해 빌드 테이블의 레코드를 읽어서 메모리에 해시테이블을 생성
* 프로브 테이블로 선택된 employees 테이블을 스캔하면서 메모리에 생성된 해시 테이블에서 레코드를 찾아 결과를 사용자에게 반환


<img width="489" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/241388d0-1a67-4341-9fda-feed7434b835">

<img width="507" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/39cbdff7-7c94-47a6-9417-e8ff7c0ba94d">

* 해시 테이블 레코드 건수가 많아져 조인 버퍼 공간 부족한 경우, 빌드 테이블과 프로브 테이블을 적당한 크기로 디스크에 청크 분리하여 처리...

#### 9.3.1.20 인덱스 정렬 선호(prefer_ordering_index)
* ORDER BY 또는 GROUP BY를 인덱스를 사용해 처리 가능한 경우 실행 계획에서 인덱스 가중치를높이 설정해서 실행됨

<img width="611" alt="image" src="https://github.com/youngDaLee/TIL/assets/64643665/54791f11-bff4-4512-b221-fb5ac7b4d529">

위 쿼리는 2가지 실행계획 선택 가능
1. ix_hiredate 인덱스 이용해 조건 일치하는 레코드 찾고 emp_no로 정렬해서 반환
2. employees 테이블 PK가 emp_no 이므로 PK를 정순으로 읽으면서 hire_date 컬럼 조건에 일치하는 지 비교 후 결과 반환

조건 부합하는 레코드 건수가 많지 않으면 1이 효율적... 가끔 옵티마이저가 2번 실행계획을 ㅓㄴ택하는 경우가 잇음 -> 실수로 잘못된 실행계획 설정
* 8.0 이전은 옵티마이저 실수 발생하면 다른 실행계획 사용하게 하기 위해서 IGNORE INDEX 힌트를 사용
* 8.0 이후 부터는 ORDER BY를 위한 인덱스에 가중치 부여하지 않도록 prefer_ordering_index 옵티마이저 옵션 추가됨
  * 기본값 ON 이지만 , 옵티마이저가 너무 자주 실수하면 OFF 선택
```sql
-- // 현재 커넥션에서 옵션 비활성화
SET SESSION optimizer_switch='prefer_ordering_index=OFF';


-- // 현재 쿼리에서 옵션 비활성화
SELECT /*+ SET_VAR(optimizer_switch='prefer_ordering_index=OFF')* /
         ...
FROM ...;
```


## 9.3.2 조인 최적화 알고리즘



