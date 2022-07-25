# Real MySQL - ch11 스토어드 프로그램
스토어드 프로시저(SP), 스토어드 함수, 트리거, 이벤트등을 모두 아우르는 말

## 11.1 스토어드 프로그램의 장단점
### 11.1.1 스토어드 프로그램 장점
- DB 보안 향상
  - 특정 테이블의 읽기, 쓰기, 특정 컬럼에만 권한 설정하는 등 세밀한 권한 제어 가능
  - SQL 인젝션을 피할 수 있음
  - 유효성 체크 한 후 동적인 SQL 문장 생성하기 때문에 SQL 문법적 취약점을 이요한 해킹이 어려움
- 기능의 추상화
- 네트워크 소요시간 절감
- 절차적 기능 구현
- 개발 업무의 구분

### 11.1.2 스토어드 프로그램의 단점
- 낮은 처리 성능
  - MySQL 서버가 스토어드 프로그램을 주목적으로 하지 않기 때문에 처리 성능이 상대적으로 떨어진다
  - 문자열 조작, 숫자 계산등의 연산을 수행하는 능력이 많이 떨어짐
  - 한 번에 많은 쿼리를 실행할 때 효과가 좋음
- 애플리케이션 코드의 조각화


-> 결론~ 언제 스토어드 프로그램 써야 하냐?
- SQL문에서 보안성을 높이고 싶을 때
- 한 번에 많은 쿼리를 실행해야 할 때


## 11.2 스토어드 프로그램의 문접
스토어드 프로그램 헤더 : 정의부. 스토어드 프로그램 이름, 입출력값 명시

스토어드 프로그램 본문 : 바디. 스토어드 프로그램이 호출됐을 때 실행하는 내용

### 11.2.1 예제 테스트 시 주의사항
- MySQL 설치 시 시스템 설정 하지 않았다면 스토어드 프로그램 실행 시 괄호, 공백등에 의해 프로시저, 함수를 인식 못할 수 있음
- 괄호 사이 공백 무시 : `IGNORE_SPACE` (7.1.1 SQL 모드)

### 11.2.2 스토어드 프로시저
- 여러 쿼리를 하나의 그룹으로 묶어 독립적으로 실행하기 위해 사용하는 것
- 반드시 독립적으로 호출되어야 함
- SELECT, UPDATE와 같은 SQL 문장에서는 SP를 참조 할 수 없음


#### 스토어드 프로시저 생성
```SQL
-- 헤더
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_sum`(
	 IN		i_param1	INT
    ,IN		i_param2	INT
    ,OUT	o_out_code	TINYINT
)
BEGIN -- 본문
	SET @param_3 = i_param1 + i_param2;
END
```
SP 파라미터 타입
- IN : 입력 전용 파라미터. 값 반환 x
- OUT : 출력 전용 파라미터
- INOUT : 입력, 출력 모든 용도 사용 가능


DELIMITER
- 명령의 끝을 알려주는 종료문자.
- CREATE 스토어드 프로그램을 할 때, 딜리미터를 `;;` 혹은 `//` 같은 연속된 두 문자로 해서 SP를 종료(생성)시킴
```SQL
DELEMETER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_sum`(
	 IN		i_param1	INT
    ,IN		i_param2	INT
    ,OUT	o_out_code	TINYINT
)
BEGIN -- 본문
	SET @param_3 = i_param1 + i_param2;
END;;
```
- DELTEMTER 변경하면 SELECT, INSERT 등의 SQL 구문에서도 종료문자를 변경한 딜리미터로 해야함..
- CREATE SP 하고 난 다음에는 DELEMTER를 다시 돌려야 함
<img src="https://user-images.githubusercontent.com/64643665/180801318-22d8ddcb-4f0e-430c-8be9-a78fac92b590.png">



## 11.3 스토어드 프로그램의 권한 및 옵션

## 11.4 스토어드 프로그램의 참고 및 주의사항

