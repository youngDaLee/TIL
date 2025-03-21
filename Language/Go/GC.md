## Summary
Go의 GC
- 낮은 지연시간, 자동 메모리관리, 멀티 코어 활용, 효율적인 메모리 재사용
- GC를 쓰면서도 예측가능하면서 안정적인 성능 유지 가능
- 메모리 관리 신경 안쓰면서 효율적인 애플리케이션 설계 가능

참고
* [터커 유튜브 강의](https://www.youtube.com/watch?v=SH32PgYGYRY)
* [카카오 블로그 - Golang GC 튜닝 가이드](https://tech.kakao.com/posts/618)
* [라인 블로그 - Go언어의 GC에 대해](https://engineering.linecorp.com/ko/blog/go-gc)

## Go의 GC 알고리즘
> Tucker 프로그래밍 B.6 참고
### GC알고리즘
> 정적 유형 GC 알고리즘  -> heap내 객체를 재배치 하지 않음
> - heap 단편화가 발생하여 할당성능 악화되는 문제가 있다고 알려져있음

**표시하고 지우기(mark and sweep)**
- 메모리 블록 전수검사해서 있으면 1, 아니면 0 표시
- 전수검사해서 CPU 성능 많이 필요하고, 검사 도충 메모리 상태 변하면 안돼서 프로그램 멈추고 검사해야함

**삼색 표시(tri-color mar and sweep)**
- mark and sweep 발전 버전
- 0 : 아무도 사용 X, 1: 검사 X, 2: 검사 끝난 블록
- 1을 모두 찾아서 2로 바꾸고, 해당 블록에서 참조중인 모든 블록을 전부 1으로 바꿈 -> 1을 검사해서 사용하지 않으면 0으로 해제
- 프로그램 실행중에도 사용 가능해서 멈춤 현상은 줄일 수 있지만, 모든 메모리 전수조사해서 속도 느리고 계속 변화해서 언제 삭제할지 정하기 어려움
- 속도 느려서 메모리 삭제 속도를 할당 속도가 추월하면 메모리 누수 이슈로 멈추고 전체 검사 해야함

> 동적 유형 GC 알고리즘  -> heap내 객체를 재배치 하지 않음
> - 단편화 회피
> - bump allocation을 통해 고속 메모리 할당(재배치한 후 메모리를 삭제한 뒷쪽에서 할당하는 방식)

**객체 위치 이동(moving object)**
- 삭제할 메모리 표시하고 한 쪽으로 몰아서 한번에 삭제하는 방식
- 한 번에 삭제해서 메모리 단편화(fragmentation) 발생하지 않는 장점
- 메모리 이동이 쉽지 않음 -> 객체간 연관관계가 있기 때문에 연관된 블록에 대한 조작을 멈춘 뒤 가능... -> 여러 객체에 읽기/쓰기를 제한하고 난 뒤에 옮겨서 CPU성능이 많이 필요함
	- Go는 포인터를 직접 사용하는 방식의 언어라 위치 이동이 어려움
- **Go가 moving object 를 사용하지 않은 이유**
	- [TCMalloc](https://goog-perftools.sourceforge.net/doc/tcmalloc.html)기반의 메모리 할당자를 도입해서 단편화와 할당 속도 문제를 상당 부분 해결했다 함

**세대 단위 수집**
- 대부분의 객체가 할당된 뒤 얼마 안돼서 삭제되기 때문에, 전체 메모리를 검사하는게 아닌 할당 된 지 얼마 안된 메모리 블록을 검사하는 방식
- 방금 할당된 메모리를 1세대에 집어넣고, 1세대 정리할때 살아남은 목록은 2세대로... 총 4세대까지 늘어나는 형태
- 구현이 복잡하고 메모리블록을 세대별로 이동해야하는 뮨제가 있음
- - **Go가 세대 단위 수집을 사용하지 않은 이유**
	- 세대별 GC는 write barrier를 사용해서 세대간 포인터를 기록해야 하는데, write barrier 오버헤드를 허용 할 수 없어 도입하지 않았다 함
	- 컴파일러의 escape 분석 성능이 뛰어나고, 필요 시 heap에 할당되지 않도록 프로그래머가 제어할 수 있기 때문에 세대별의 가설에서 나오는 수명 짧은 객체는 heap이 아닌 stack 영역에 할당되곤함(=GC를 수행할 필요가 없음) -> GC로 얻을 수 있는 이점이 적음

### Go언어의 GC 알고리즘
1.16 -> 삼색 표시 수집 방식
* 여러 고루틴에서 병렬로 삼색검사를 함
* 세대 단위 수집을 하지 않기 때문에 메모리 이동 비용이 들지 않음
* 한 번 돌 때 1ms미만 멈춤으로 GC 가능

장점
* 매우 짧은 멈춤 시간(1ms이하)
단점
- 추가 힙 메모리 필요
- 실행 성능 저하
따라서 메모리 할당 빈번하게 하는건 좋지 않음(Go뿐만 아니라 GC있는 모든 언어는...)

GC가 빨라도 GC에 의존하기 보다는 가비지 자체를 줄이는게 중요
- 불필요한 메모리 할당을 없애고
- 메모리 쓰레기를 재활용


## GC 튜닝 가이드
> [카카오 블로그 - Golang GC 튜닝 가이드](https://tech.kakao.com/posts/618) 참고

### Profile
- 공식 블로그에서 얘기하는 프로파일 방법
	- 프로그램에서 직접 프로파일링한 뒤 cpu.profile로 저장
	- 웹으로 profiling 요청에 응답받도록 구동

```go
go tool pprof -http=0.0.0.0:8080 http://…..:6060/debug/pprof/profile
```


### GOGC -> GOMEMLIMIT 만으로 문제 해결
Go GC튜닝의 핵심 = STW(Stop The World, GC가 동작하는동안 프로그램 동작 멈추는 현상)
- 이를 해결하는 가장 쉬운 방법 = GOGC 끄고 GOMEMLIMIT사용

GOGC
- 현 시점 Heap 크기과 직전시점 Heap 증가율 바탕으로 GC 수행 여부 결정
- 디폴트는 기존 대비 Heap이 100%증가(2배)가 되면 GC를 수행 -> 이 %값을 낮추면 GC가 자주 수행되고, 높을수록 덜 수행됨
	- 너무 작아도, 너무 커도 문제가 생김
- GOGC값 작은 경우
	- 너무 빈번하게 GC가 수행됨. 프로그램 막 시작되어 메모리 소비량 적은 경우에도 수행됨...
- GOGC값 큰 경우
	- OOM 이슈
	- 기존 사용량이 40GB고 GOGC가 50이면 1.5배 상승한 60GB가 되어야만 GC가 수행됨
=> 극복 위해 프로그램 시작하자마자 더미 메모리 할당하는 ballast 기법도 존재하지만 GOMELIMIT 등장!! 으로 더 좋아짐

GOMELIMIT
- 프로그램이 사용할 수 있는 메모리 사용량 한계선을 정하는 설정. GOMELIMIT값만큼 메모리 사용량 올라가는 경우만 GC가 수행됨
- 프로그램이 사용할 수 있는 최대 메모리 한계선 정한 뒤, 그보다 작은 값을 GOMELIMIT으로 설정하여 튜닝

### Heap Proflie의 alloc_space, alloc_objects가 높은 값을 튜닝
- Heap영역이 GC튜닝의 핵심. Stack은 GC없이도 함수 호출/종료로 자연스럽게 관리되지만 Heap메모리 영역은 GC 관리가 필요한 객체들이 있는 메모리 영역
- Heap 메모리 관련 지표
	- inuse_objects : 현재 사용중인 객체 수
	- inuse_space : 현재 사용중인 메모리 양
	- alloc_objects : 프로그램이 시작된 후 할당된 총 객체 수  -> GC과정에서 일어나는 marking작업에서 CPU 자원을 소모하게됨
	- alloc_space : 프로그램이 시작된 후 할당된 총 메모리 양 -> 얘가 크면 프로그램 동작 과정에서 사용되는 Heap 메모리가 빠르게 증가함=GC가 자주 수행됨

### Flame graph로 튜닝 포인트 찾기
- 프로파일링은 어떤 함수가 리소스를 많이 소모했는지 Flame graph로 표현함

### -gcflags='-m -m'을 통해 왜 Heap메모리로 객체가 할당되었는지 확인
- 왜 특정 개체가 GC가 수행되어야 하는 Heap메모리 영역에 할당되었는지를 알아야 GC 필요한 객체를 줄이고 튜닝 가능 -> 이 때 사용할 수 있는 golang 빌드 옵션이 gcflags

### Benchmark 중심으로 확인
- gcflags 옵션으로 일일이 힙 영역 할당 확인은 어려우므로 benchmark(시스템 성능 측정 테스트) 중심으로 집중 튜닝

```go
% go test -bench=. -benchmem -benchtime=10s -cpuprofile=cpu.prof -memprofile=mem.prof -gcflags='-m'
```

- -benchmem : 한 번에 bench loop(벤치마크 테스트에서 특정 코드 블록 반복 실행하는 루프)에서 오브젝트 할당이 얼마나 자주, 크게 할당되었는지 확인
- -cpuprofile, -memprofile : bench가 동작하는 동안 프로파일링 결과를 파일로 저장하는 옵션
- -gcflags=’-m’ : 어디서, 왜 heap 메모리로 할당 일어났는지

### Heap 할당 줄이는 팁
- 비정형 인자는 heap에 할당됨
- type을 정해서 출력하는 logger를 선택하자 (비정형 인자를 가장 많이 사용하는 경우가 Logging임... -> 타입을 명확히 하여 Heap메모리 할당 줄이자)
- pointer변수는 무조건 heap에 할당된다
- slice 생성 시 capacity가 상수인 경우 stack에 들어갈 수 있다 (make할 때 가능한 var 아니고 const로!!)
- Pool은 heap 메모리 할당을 줄일 수는 있지만 CPU가 많이 소모될 수 있다
- 최신 패키지를 잘 살펴보자 -> 더 나은게 나올수도!!!


# GC를 튜닝하는 방법
* STW(Stop The World, GC가 동작하는동안 프로그램 동작 멈추는 현상)를 줄이자
* 불필요한 Heap영역 할당을 줄이자

## STW 줄이는 방법
GOMELIMIT
- GOGC 단점을 보완하여 나온 방법
- 프로그램이 사용할 수 있는 메모리 사용량 한계선을 정하는 설정. GOMELIMIT값만큼 메모리 사용량 올라가는 경우만 GC가 수행됨
- 프로그램이 사용할 수 있는 최대 메모리 한계선 정한 뒤, 그보다 작은 값을 GOMELIMIT으로 설정하여 튜닝

### GOMELIMIT 실제 실행 결과
실행 로그 분석
```shell
gc 1 @0.014s 1%: 0.021+1.0+0.043 ms clock, 0.21+0.36/1.4/0.21+0.43 ms cpu, 3->4->1 MB, 4 MB goal, 0 MB stacks, 0 MB globals, 10 P
```
- `gc 1` : 프로그램 실행 후 첫 번째 GC 이벤트 발생
- `**@0.014s**` → 프로그램 시작 후 **0.014초(14ms) 경과** 시점에서 GC 실행됨
- `**1%**` → GC가 애플리케이션 실행 중 차지한 **CPU 비율** (낮을수록 좋음)
- `0.021+1.0+0.043 ms clock` : GC 시간 분석
	- **0.021ms** → GC의 **STW(Stop-The-World) 시작 시간**(GC실행을 위해 모든 고루틴 중지하는 시간)
	- **1.0ms** → **Mark 단계 (병렬 실행)** : 살아있는 객체 마킹
	- **0.043ms** → **STW 종료 시간** 
- `0.21+0.36/1.4/0.21+0.43 ms cpu` : CPU 사용량 분석
	- **0.21ms** → **STW 시작 시 CPU 사용량**
	- **0.36ms / 1.4ms / 0.21ms** → **각 단계별 CPU 사용 시간**
		- 0.36ms → Initial mark 단계
		- 1.4ms → Mark + Sweep 단계 (병렬 실행)
		- 0.21ms → Final mark 단계
	- **0.43ms** → **STW 종료 시 CPU 사용량**
- `3->4->1 MB` : 힙 메모리 변화
	- 3MB: GC 시작 전 사용된 힙메모리
	- 4MB: GC 실행 중 최대 힙 메모리 사용량
	- 1MB: GC 완료 후 남은 살아있는 객체 크기
- `4 MB goal` : 힙 크기 목표
- 0 MB stacks, 0 MB globals 스택, 글로벌 변수 메모리
- 10 P : 프로세서 수(go 런타임에 할당된 프로세서 수)

GOMELIMIT 설정이 있는 로그
```shell
  GODEBUG=gctrace=1 GOMEMLIMIT=4GiB ./main  
gc 1 @0.014s 1%: 0.021+1.0+0.043 ms clock, 0.21+0.36/1.4/0.21+0.43 ms cpu, 3->4->1 MB, 4 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 2 @0.019s 2%: 0.046+0.90+0.038 ms clock, 0.46+0.14/1.6/0.51+0.38 ms cpu, 4->5->3 MB, 4 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 3 @0.075s 1%: 0.086+0.70+0.004 ms clock, 0.86+0.048/1.8/2.1+0.041 ms cpu, 8->8->5 MB, 8 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 4 @0.173s 0%: 0.081+0.92+0.020 ms clock, 0.81+0.069/2.2/3.1+0.20 ms cpu, 10->11->6 MB, 11 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 5 @0.209s 0%: 0.044+1.0+0.004 ms clock, 0.44+0.084/2.7/4.2+0.043 ms cpu, 13->13->8 MB, 14 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 6 @0.260s 0%: 0.048+1.0+0.13 ms clock, 0.48+0.058/2.8/4.9+1.3 ms cpu, 16->16->9 MB, 17 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 7 @0.321s 0%: 0.046+1.2+0.014 ms clock, 0.46+0.064/3.3/5.3+0.14 ms cpu, 19->19->11 MB, 20 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 8 @0.339s 0%: 0.059+1.2+0.009 ms clock, 0.59+0.055/3.3/5.7+0.099 ms cpu, 22->22->13 MB, 23 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 9 @0.442s 0%: 0.043+1.4+0.13 ms clock, 0.43+0.12/3.9/5.9+1.3 ms cpu, 26->26->15 MB, 28 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 10 @0.785s 0%: 0.15+4.0+0.035 ms clock, 1.5+0.31/11/21+0.35 ms cpu, 29->31->23 MB, 32 MB goal, 0 MB stacks, 0 MB globals, 10 P
```

GOMELIMIT 설정이 없는 로그
```shell
 GODEBUG=gctrace=1 ./main
gc 1 @0.041s 0%: 0.025+1.0+0.013 ms clock, 0.25+0.89/1.5/0.26+0.13 ms cpu, 3->4->1 MB, 4 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 2 @0.049s 0%: 0.029+0.83+0.015 ms clock, 0.29+0.26/1.1/1.8+0.15 ms cpu, 3->3->3 MB, 4 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 3 @0.073s 0%: 0.040+0.73+0.025 ms clock, 0.40+0/1.4/1.8+0.25 ms cpu, 7->7->4 MB, 7 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 4 @0.216s 0%: 0.060+0.83+0.009 ms clock, 0.60+0.63/2.0/3.0+0.090 ms cpu, 9->9->5 MB, 9 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 5 @0.235s 0%: 0.081+0.72+0.003 ms clock, 0.81+0.31/1.9/3.3+0.034 ms cpu, 11->11->7 MB, 12 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 6 @0.254s 0%: 0.065+1.0+0.009 ms clock, 0.65+0.23/2.8/4.6+0.096 ms cpu, 14->14->8 MB, 15 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 7 @0.280s 0%: 0.046+1.1+0.059 ms clock, 0.46+0/3.0/4.5+0.59 ms cpu, 17->17->9 MB, 18 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 8 @0.307s 0%: 0.050+1.3+0.012 ms clock, 0.50+0.056/3.5/5.7+0.12 ms cpu, 19->20->11 MB, 20 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 9 @0.325s 0%: 0.071+1.1+0.004 ms clock, 0.71+0.093/3.3/5.8+0.045 ms cpu, 22->23->14 MB, 24 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 10 @0.371s 0%: 0.079+1.6+0.004 ms clock, 0.79+0/4.5/7.3+0.046 ms cpu, 27->27->15 MB, 28 MB goal, 0 MB stacks, 0 MB globals, 10 P
gc 11 @0.507s 0%: 0.057+3.2+0.079 ms clock, 0.57+0.069/9.3/17+0.79 ms cpu, 30->31->25 MB, 32 MB goal, 0 MB stacks, 0 MB globals, 10 P
```
1. **GC 실행 빈도 (GC 횟수)**
	- GOMEMLIMIT O 
		- 총 10회 실행
		- GC 실행 간격이 점점 늘어남 (0.014s → 0.019s → 0.075s → ... → 0.785s)
	- GOMEMLIMIT X
		- 총 11회 실행
		- GC 실행 빈도가 더 **짧은 간격**으로 이루어짐 (0.041s → 0.049s → 0.073s → ... → 0.507s)
2. **힙 크기 변화 (X->Y->Z MB**)
	- GOMEMLIMIT O
		```
		3->4->1 MB
		4->5->3 MB
		8->8->5 MB
		10->11->6 MB
		13->13->8 MB
		16->16->9 MB
		19->19->11 MB
		22->22->13 MB
		26->26->15 MB
		29->31->23 MB
		```
		남은 메모리, 목표 힙 크기 점진적 증가
	- GOMEMLIMIT X
		```
		3->4->1 MB
		3->3->3 MB
		7->7->4 MB
		9->9->5 MB
		11->11->7 MB
		14->14->8 MB
		17->17->9 MB
		19->20->11 MB
		22->23->14 MB
		27->27->15 MB
		30->31->25 MB
		```
		마찬가지로 점진적으로 증가하긴 하지만 더 많이 GC가 실행되었음에도 힙 크기가 비슷한 속도로 증가함 
3. **GC 수행 시간 및 CPU 사용량 (clock / cpu)
- GOMEMLIMIT O
```
0.021+1.0+0.043 ms clock, 0.21+0.36/1.4/0.21+0.43 ms cpu
0.046+0.90+0.038 ms clock, 0.46+0.14/1.6/0.51+0.38 ms cpu
0.086+0.70+0.004 ms clock, 0.86+0.048/1.8/2.1+0.041 ms cpu
...
0.15+4.0+0.035 ms clock, 1.5+0.31/11/21+0.35 ms cpu
```
	초반에는 GC 시간이 짧고 후반으로 갈수록 시간 증가 -> 사용률 빈도 줄이게 됨
- GOMEMLIMIT X
```
0.025+1.0+0.013 ms clock, 0.25+0.89/1.5/0.26+0.13 ms cpu
0.029+0.83+0.015 ms clock, 0.29+0.26/1.1/1.8+0.15 ms cpu
0.040+0.73+0.025 ms clock, 0.40+0/1.4/1.8+0.25 ms cpu
...
0.057+3.2+0.079 ms clock, 0.57+0.069/9.3/17+0.79 ms cpu
```
	초반부터 일정한 GC 시간 유지
