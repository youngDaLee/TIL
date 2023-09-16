# CPU 스케줄링
context switch : CPU가 다른 프로세스로 넘어갈 때, 이전 프로세스의 상태를 저장하고, 새로운 프로세스의 상태를 불러오는 과정
* 누가 해줘? : dispatcher
* overhead : context switch에 걸리는 시간

CPU 스케줄링이란?
* CPU가 여러 프로세스를 실행할 때, 어떤 프로세스를 먼저 실행할지 결정하는 것
* Preemptive(선점) vs Non-Preemptive(비선점)
  * Preemptive: 우선순위가 더높은 프로세스가 CPU를 뺏어 쓰는것
  * Non-Preemptive: 우선순위가 높은 프로세스가 있어도 CPU를 뺏을수 없는 것
* CPU Utiilization(CPU 이용률) : CPU가 얼마나 활용되는지. 100% 활용되는게 좋음!
* Throughput(처리량) : 단위 시간당 몇개의 프로세스를 처리하는지. 많을수록 좋음.
* Turnaround Time(반환시간) : 프로세스가 실행되기 시작한 시간부터 끝날 때까지 걸린 시간(=프로세스 총 시간). 짧을수록 좋음.
* Waiting Time(대기시간) : 프로세스가 CPU를 할당받기 위해 대기한 시간. 짧을수록 좋음.
* Response Time(응답시간) : interactive system에서 중요함. 프로세스가 처음 CPU를 할당받기까지 걸린 시간. 짧을수록 좋음.

## 스케줄링 알고리즘
### First-Come, First-Served (FCFS)
* Non-Preemptive scheduling
* 먼저 온 프로세스를 먼저 처리하는 것
* 가장 간단하고 공평함
* Convoy Effect(호위 효과) : CPU를 오래 사용하는 프로세스가 먼저 온 경우, 뒤에 있는 프로세스들이 오래 기다려야 하는 현상
* 평균 대기시간이 길다. 대기시간 면에서 좋은 방법은 아니구나~

### Shortest-Job-First (SJF)
* 실행시간이 제일 **짧은걸 먼저** 실행하는 것
* Provably optimal : 가장 이상적으로 실행시간을 줄일 수 있지만, 비현실적이다. 해당 프로세스가 얼마나 실행될 지 예측을 할 수 있어야 한다... -> 예측 불가
  * 뭔가 머신러닝으로 SJF를 발전시키고 있지 않을까 생각이 들어서 알아봄 : [링크](https://medium.com/@dixitvibhu20/enhancing-shortest-job-first-sjf-with-machine-learning-bridging-the-gap-between-theory-and-ee204a85ae1a)
  * 데이터 품질 이슈와 **모델 오버헤드 및 복잡성** 문제가 있어 아직 사용하기는 부족하다~
* preemptive(선점) SJF (Shortest Remaining Time First. SRJF)
  * 새로운 프로세스가 주어질 때 Remaining Time 이 작은 것 부터 선택
* non-preemptive(비선점) SJF
  * CPU가 프로세스에 주어지면 실행되는 프로세스가 끝날 때 까지 허용
* SRJF가 AWT(평균 대기 시간)가 더 짧음

### Priority Scheduling
* 우선순위가 높은 걸 먼저 서비스
* 우선순위 선정 기준
  * 내부 : time limit이 짧은 것, 메모리 적게 차지하는걸 먼저, IO가 길고 CPU Burst 짧은거
  * 외부
* starving(기아) process 문제 발생 할 수 있음 : 우선순위가 낮은 프로세스에 대해 오래 기다려도 계속 선택되지 못할 수 있ㅇ
  * 해결 방법 : 오래 될 수록 age를 높여줌.

### Round Robin (RR)
* time sharing(시분할) 시스템. 시간을 쪼개서 실행.
* 모든 프로세스를 time quantum(time slice) 단위로 잘라준 뒤 돌아가며 실행.
* Preemtimve 방식만 존재
* time quantum 사이즈에 따라 성능이 달라지므로, time quantum 사이즈에 의존적
  * 만약 time quantum 사이즈가 무한대가 되면 FCFS 방식과 동일해짐
  * 스위칭이 빈번하게 일어나기 때문에 프로세스가 동시에 동작되는 것 처럼 보임
  * 다만 너무 짧게 잡으면 context switching  으로 인한 오버헤드로 성능 저하.

### Multilevel Queue Scheduling
* Process Groups
  * System Process
  * Interactive Process : 사용자와 상호작용 하는 프로그램(ex: 게임)
  * Interactive Editing Process : 워드프로세스와 같은 편집기 프로그램
  * Batch Process : 백단에서 일괄적으로 실행하는 프로세스. Non-Interactive process
  * Student Process
* 시스템 프로세스는 긴급하지만, 배치는 늦게 실행되어도 상관 없다~
* 각각의 프로세스 그룹별로 줄을 세운 뒤, 긴급한 프로세스(System Process) 에게 우선순위를 주어서 먼저 실행되게 하는 프로세스

### Multilevel Feedback Queue Scheduling
* Multilevel Queue와 같이 복수 개의 Queue를 갖고 실행
* 다만 상위 큐에서 CPU Time이 너무 많이 사용될 경우, 하위 Queue로 이동하게 됨
* starving 우려 시 높은 Queue로 이동하게 됨
