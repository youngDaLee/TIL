## context 기본 개념
context 패키지가 하는 역할
- 시간 초과, 취소, 요청 범위 데이터 전달을 관리하기 위한 기능을 제공하는 도구
- 고루틴 생명주기 제어
- HTTP 요청 처리
	- 클라이언트가 HTTP 요청 취소했을 시, 그와 관련된 DB조회/API 호출 등도 취소해야 리소스 낭비를 하지 않음
- DB쿼리, 타임아웃 관리
	- 특정 작업이 너무오래 걸리면 타임아웃 설정해서 자동으로 종료해야 함

context 패키지 주목적
- Context 타입을 정의하고, 캔슬레이션(cancellation, 취소) 지원
- 메타데이터 저장(gRPC)

기본 사용법
- Deadline(), Done(), Err(), Value() 로 구성된 인터페이스

## context 사용 방법
생성
1. context.Background()
	- 가장 기본이 되는 빈 Context
	- 보통 main() 함수나 초기 설정에서 사용
2. context.TODO()
	- 아직 어떤 Context를 사용해야 할지 모를 때 임시로 사용

context를 이용한 제어
1. context.WithCancel(parent)
	- cancel()을 호출하면 **모든 자식 Context도 취소됨**
	- 자식 Goroutine이 부모가 취소됐는지 체크할 수 있음
2. context.WithTimeout(parent, duration)
	- 설정한 시간(duration)이 지나면 자동으로 취소됨
3. context.WithDeadline(parent, time)
	- 특정 시각(time)까지 Context가 유효
4. context.WithValue(parent, key, value)
	- Context에 데이터를 저장해 자식 Goroutine에 전달

### context를 활용한 제어
```go
package main

import (
    "context"
    "fmt"
    "os"
    "strconv"
    "time"
)

// f1 고루틴을 만들고 실행.
// c1 컨텍스트가 4초가 지나기 전 Done함수를 호출하면 고루틴이 끝날 시간이 없음
func f1(t int) {
    c1 := context.Background()
    // WithCancle은 기존 Context를 사용해서 캔슬레이션으로 자식을 생성.
    // CanceFunc()함수를 호출하면 부모가 자식을 가리키는 레퍼 삭제하고 타이머를 멈춤
    c1, cancel := context.WithCancel(c1)

    defer cancel() // context.CancelFunc() 값

    go func() {
        time.Sleep(5 * time.Second)
        cancel()
    }()

    select {
    case <-c1.Done():
        fmt.Println("f1() Done:", c1.Err())
        return
    case r := <-time.After(time.Duration(t) * time.Second):
        fmt.Println("f1():", r)
    }
}

// f2
func f2(t int) {
    c2 := context.Background()
    // WithTimeout은 ctx, duration 매개변수 필요 -> 시간 지나면 자동으로 cancel()호출됨
    c2, cancel := context.WithTimeout(c2, time.Duration(t)*time.Second)
    defer cancel() // context.CancelFunc() 값

    go func() {
        time.Sleep(5 * time.Second)
        cancel()
    }()

    select {
        case <-c2.Done():
            fmt.Println("f2() Done:", c2.Err())
            return
        case r := <-time.After(time.Duration(t) * time.Second):
            fmt.Println("f2():", r)
        }
        return
    }

func f3(t int) {
    c3 := context.Background()
    // 데드라인이 지나면 자동으로 cancel 호출
    deadline := time.Now().Add(time.Duration(2*t) * time.Second)
    c3, cancel := context.WithDeadline(c3, deadline)
    defer cancel()

    go func() {
        time.Sleep(5 * time.Second)
        cancel()
    }()

    select {
    case <-c3.Done():
        fmt.Println("f3() Done:", c3.Err())
        return
    case r := <-time.After(time.Duration(t) * time.Second):
        fmt.Println("f3():", r)
    }

    return
}

  

func main() {

    if len(os.Args) != 2 {
        fmt.Println("Need Parameter. Please Write Delay")
        return
    }

    delay, err := strconv.Atoi(os.Args[1])

    if err != nil {
        fmt.Println(err)
        return
    }

    fmt.Println("Delay:", delay)

    f1(delay)
    f2(delay)
    f3(delay)
}
```

## 토픽 읽으며 생긴 의문 ChatGPT...

### 고루틴 부모-자식 관계에 대해
> 고루틴은 부모자식 관계가 없다고 이해하고 있는데, context를 설명할때는 Context패키지로 부모고루틴의 실행이 끝났을 때 자식 고루틴의 실행을 멈추는데 도움을 준다고 얘기하고 있어.
> 내가 고루틴에 대해 잘못 이해하고 있는걸까? context패키지를 설명할 때 얘기하는 부모-자식 고루틴에 대해 설명해줘

### 내가 이해한 내용
- gorutine에는 부모-자식 관계가 없는 것은 맞음
- 다만 context패키지를 이용해서 고루틴에 부모-자식 관계를 논리적으로 설정하고 제어할 수 있음

#### chat gpt 전문
너의 이해가 맞아. Go의 **Goroutine은 부모-자식 관계가 없고**, 독립적으로 실행돼.
하지만 context**를 사용하면 부모 Goroutine이 종료될 때 자식 Goroutine도 종료할 수 있는 구조를 만들 수 있어**. 이걸 “부모-자식 Goroutine 관계”라고 부르는 거야.

**🔹 Goroutine의 기본 동작: 부모-자식 개념이 없음**
Go에서는 함수를 go 키워드를 붙여 실행하면 새로운 Goroutine이 생성돼.
그런데, **Goroutine은 부모 Goroutine의 생명주기와 독립적이야.** 즉, **부모 Goroutine이 종료되더라도 자식 Goroutine이 계속 실행될 수 있어!**
**예제: 부모가 먼저 종료되면 자식 Goroutine은 살아있음**
```go
package main

import (
	"fmt"
	"time"
)

func worker() {
	for i := 0; i < 5; i++ {
		fmt.Println("작업 중...")
		time.Sleep(1 * time.Second)
	}
}

func main() {
	go worker()
	fmt.Println("메인 함수 종료")
}
```

**실행 결과 (메인 함수가 먼저 종료됨)**
```
메인 함수 종료
(그리고 프로그램 종료됨, worker() 실행 안 됨!)
```
  - worker() Goroutine이 **메인 함수가 끝나도 계속 실행될 것 같지만, 메인 함수가 종료되면 전체 프로세스가 종료되므로 실행되지 않음.**
  - **즉, 고루틴 자체는 부모-자식 관계가 없지만, 메인 Goroutine(프로세스의 시작점)이 끝나면 모든 Goroutine이 강제로 종료될 수 있음.**


**🔹 context를 사용하면 부모 Goroutine이 종료될 때 자식 Goroutine을 안전하게 멈출 수 있음**
Goroutine이 독립적이기 때문에 **부모 Goroutine이 종료되더라도 자식 Goroutine이 계속 실행될 수 있어**. 이때 context**를 사용하면 부모 Goroutine의 종료 시점에 맞춰 자식 Goroutine도 정리할 수 있어.**

**✅ Context를 사용한 부모-자식 Goroutine 제어 예제**
```go
package main

import (
	"context"
	"fmt"
	"time"
)

func worker(ctx context.Context) {
	for {
		select {
		case <-ctx.Done(): // 부모 Context가 취소되면 여기서 종료됨
			fmt.Println("작업이 취소됨!")
			return
		default:
			fmt.Println("작업 수행 중...")
			time.Sleep(1 * time.Second)
		}
	}
}

func main() {
	// WithCancel을 사용하여 취소 가능한 Context 생성
	ctx, cancel := context.WithCancel(context.Background())

	go worker(ctx) // worker Goroutine 실행

	time.Sleep(3 * time.Second) // 3초간 실행 후

	cancel() // Context 취소 -> worker Goroutine도 종료됨

	time.Sleep(1 * time.Second) // 종료 확인을 위한 대기
	fmt.Println("메인 함수 종료")
}
``` 

**🛠 실행 결과**
```
작업 수행 중...
작업 수행 중...
작업 수행 중...
작업이 취소됨!
메인 함수 종료
```
  **이제 부모 Goroutine(**main()**)이** cancel()**을 호출하면,** worker() **Goroutine도 안전하게 종료됨!**

즉, context를 사용해서 부모 Goroutine이 종료될 때 **의도적으로 자식 Goroutine도 종료할 수 있는 구조를 만든 것**이야.

**🔹 정리: 왜 “부모-자식 관계”라고 부를까?**
✔ **Goroutine은 원래 부모-자식 관계가 없음!**
✔ 하지만 context를 사용하면 특정 Goroutine(부모)이 취소되었을 때, 연관된 다른 Goroutine(자식)을 종료할 수 있음
✔ 이런 구조를 만들면 **“논리적인 부모-자식 관계”** 처럼 동작함
즉, **context는 Goroutine을 강제로 종료하는 기능이 아니라 “논리적인 부모-자식 관계를 만들어 주는 도구”** 라고 보면 돼. 😆

