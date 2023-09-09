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
### Priority Scheduling
### Round Robin (RR)
### Multilevel Queue Scheduling
### Multilevel Feedback Queue Scheduling
