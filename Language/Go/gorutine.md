### 고루틴이란?
- ==Go에서 만든 경량 스레드==
- Go의 최소 실행 단위
- Go의 모든 것이 고루틴 형태로 실행됨
- Go프로그램에는 최소 하나 이상의 고루틴을 가지고 있다(main고루틴)
- Go scheduler가 고루틴을 실행할 책임을 가지고 있고, 각각의 고루틴은 스케줄러 명령에 따라 운영체제 스레드에서 실행됨
- 고루틴끼리는 통신 할 수 없어 데이터 공유는 channel(채널)이나 shared memory(공유메모리)로 구현
- 여러 채널과 고루틴을 조합하면 데이터 흐름을 만들 수 있음 = 파이프라인(pipline)
- 아무리 많은 고루틴을 써도 컨텍스트 스위칭 비용이 들지 않음

### Go 스케줄러
> Go런타임에 고루틴 실행을 담당하는 스케줄러

m:n 스케줄링 기법을 사용함
- m: 실행되는 고루틴 개수
- n: 고루틴을 멀티플랙싱할 운영체제 스레드 개수

**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcKSOX5MdFhh0Deg2sH79qXxV1mx-c7av-Ngxkl3V94h0GPtK993fkAwHvNK9UNOlVJC4wTipQ3YBAfQAnNxfU35ojTJzxtVrEkT6j1j7ECPxqEFLV5IN-YSEOG_jlS4AjwbjmHwg?key=mocCDgZQLr1_iZGP-W_fjccx)
- G : goroutine
- M : machine (OS 스레드)
- P : processor (논리적 프로세서)
Blocking Gorutine : 대기상태
- 채널만 생성해두고 실제 작업이 할당되지 않은상태

Processor가 동적 할당되는 기준이 무엇인지
- 

### 고루틴
- 고루틴을 사용하면 함수는 즉시 반환되지만 실제 실행은 백그라운드에서 고루틴 형태로 실행됨
- 따라서 고루틴 순서는 예측하거나 제어할 수 없음 -> OS스케줄러, Go스케줄러에 따라 달라짐
**사용방법**
```
// 익명함수를 고루틴으로 생성하는 방법
go func() {
	...
}()

// 일반 함수를 고루틴으로 호출하는 방법
go printMe(15)

// Go프로그램은 고루틴 실행이 끝날 때 까지 기다리지 않기 때문에 수동으로 지연시켜줌
time.Sleep(time.Second)
```
- 고루틴과 데이터를 주고받고자 한다면 공유메모리나 채널 사용 필요

- time.Sleep
	- 끝나는걸 보장하지는 않음
- waitGroup
	- 실제로 끝나는걸 보장

GOMAXPROCS
```
fmt.Printf("cpu num=%d\n", runtime.NumCPU())  
fmt.Printf("GOMAXPROCS=%d\n", runtime.GOMAXPROCS(0))  
fmt.Printf("GOMAXPROCS=%d\n", runtime.GOMAXPROCS(runtime.NumCPU()))

cpu num=10
GOMAXPROCS=10
GOMAXPROCS=10
```
