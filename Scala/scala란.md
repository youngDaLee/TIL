# Scala란
객체지향 언어의 특징과 함수형 언어의 특징을 함께 가지는 다중 패러다임 프로그래밍 언어

## 특징
- JVML
  - 자바 가상머신(JVM)에서 동작하는 언어
  - 자바 모든 라이브러리 사용 가능
- 함수형 언어
  - 자바에 비해 코드가 짧다
- 바이트코드 최적화
  - 자바보다 20% 정도 빠르다.
- 동시성에 강함
  - 변경 불가능한 Immutable 변수를 많이 가지고 있음 -> 이를 통해 속성 변경 불가능하게 함
  - 순수 함수 사용하여 병렬 프로그램 처리에 강함


### 함수형 언어
자료 처리를 수학정 함수의 계산으로 취급. 상태 변화와 가변 데이터를 비하는 것

#### 순수 함수(pure funciton)
- 함수의 실행이 외부에 영향을 끼치지 않는 함수

```scala
public int add(int a, int b){
    return a + b;
}
```

### 익명 함수 (anonymous function)
- 전통적인 명령현 언어는 이름이 있지만, 함수형 언어는 선언부가 없는 익명 함수 만들 수 있음

```scala
Arrays.asList(1,2,3).stream().reduce((a,b) -> a-b).get();
```

### 고차 함수(higher-order fucntion)
- 함수를 인수로 취급하는 함수. 입력파라미터는 출력값 처리 가능

```scala
Collections.sort(now ArrayList<Integer>(), (x,y) -> x >= y ? -1 : 1);
```

