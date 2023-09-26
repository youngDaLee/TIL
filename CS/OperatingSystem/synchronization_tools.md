# Synchronization Tools
## 참고
* https://rebro.kr/176
* https://parksb.github.io/article/10.html
* https://8156217.tistory.com/41
* https://velog.io/@hidaehyunlee/Philosophers-%EC%98%88%EC%8B%9C%EC%98%88%EC%A0%9C%EB%A1%9C-%EB%B3%B4%EB%8A%94-%EB%AE%A4%ED%85%8D%EC%8A%A4%EC%99%80-%EC%84%B8%EB%A7%88%ED%8F%AC%EC%96%B4%EC%9D%98-%EC%B0%A8%EC%9D%B4
* https://m.blog.naver.com/dlaxodud2388/222201325948
* https://100100e.tistory.com/208
* https://murphymoon.tistory.com/entry/%EC%9E%84%EA%B3%84%EA%B5%AC%EC%97%AD%EC%9D%84-%EB%B3%B4%ED%98%B8%ED%95%98%EA%B8%B0-%EC%9C%84%ED%95%9C-%EA%B8%B0%EB%B2%95-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9COS-%EB%A9%B4%EC%A0%91%EC%A7%88%EB%AC%B8-6
* 

## Race Condition(경쟁 상태)
* 두 프로세스가 동시에 어떤 변수 값을 바꿀 때, 어떤 순서로 데이터에 접근하느냐에 따라 결과 값이 달라질 수 있음(race condition)
* 이 상황에서 프로세스간 실행 순서를 정해주는 동기화(synchronization)가 필요하다~

## Criticla Section(임계 구역)
* critical section 이란? : Race Condition이 발생할 수 있는 부분 => 공유 데이터를 접근하는 코드

Critical Section 문제 해결하기 위한 조건
1. Mutual Exclusion (상호 배제) : 이미 한 프로세스가 critical section에서 작업중이면, 다른 프로세스는 critical section에 접근하면 안됨
2. Progress (진행) : critical section에서 작업중인 프로세스가 없으면 진입할 수 있어야 함
3. Bounded Waiting (한정 대기) : critical section에 들어가기 위해 요청한 후 부터, 요청이 허용될 때 까지 기다리는 횟수 제한 필요 = 무한대기 안됨

Non-Preemtive kernel(비선점 커널)로 구현하면 critical section 문제 발생 안함 => 당연함 애초에 뺏기지도 않고 순서대로 실행되니까
* 그런데 비선점은 느리니까 잘 사용 안함..

## Synchronize Algorithms - Peterson's Solution
임계 영역 문제를 해결하기 위한 알고리즘.        
프로세스가 작업중인지 저장하는 변수 flag, critical section에 진입하고자 하는 프로세스 turn 으로 어떤 프로세스가 임계 영역 진입하면 flag lock, 나오면 unlock
```bash
do {
    flag[i] = true; // flag를 true로 바꾸면서 critical section에 진입
    turn = j;   // 상대방이 들어가게 함
    while (flag[j] && turn == j);   // 상대방이 들어가고 싶고, 상대방이 들어가 있으면(turn==j) rlekfla
    // Criticla section -> 상대방 턴이 끝나면 P1들어감
    flag[i] = false;    // critical section 나오면 바꿔줌
    // Remainder section
} while(true);
```
* Critical Section 진입을 기다리며 Busy Waiting 문제가 발생할수도..

## Synchronization Hardware
* 현재 상태를 확인하고 변경하는 Test & modify를 atomic 하게 수행할 수 있도록 지원.
  * atomic 하게 수행한다 : 누구도 interrupt 할 수 없다 ~
  * 변수를 이용해서 물리적으로 메모리 영역 자체를 분리하는 거라고 이해함...
* 기계어로 작성되어 있고, 프로그래머들이 사용하기에는 어렵다..

## Mutex Locks
Critical Section 문제를 해결하기 위한 소프트웨어 도구 방법 중 하나.

* **lock이 하나만** 존재할 수 있는 locking 메커니즘
* 이미 하나의 스레드가 critical section에서 작업중인 lock 상태에서 다른 스레드가 접근할 수 없게 함
* Busy Wating 단점 : Critical Section에 프로세스 존재할 때, 다른 프로세스가 계속 진입 시도해서 CPU 낭비가...

## Semaphores
여러 프로세스, 스레드가 critical section에 진입 가능한 locking 메커니즘.
* 카운터를 이용해 동시에 리소스에 접근할 수 있는 프로세스를 제한
* 한 프로세스가 값을 변경 할 때는 동시에 값을 변경하지는 못함
* P: 공유데이터 획득 연산 / V: 반납 연산
* 세마포어 종류
  * Binary Semaphore : 정수값이 0 or 1 -> MutexLock과 동일한 역할
  * Counting Semaphore : 정수 값 범위가 0 이상으로 제한 없음

## 질문
* 과연 화장실 비유가 맞는 표현일까...?
  * 결국 화장실 한 칸에 들어가는 프로세스가 하나라는 건 뮤텍스와 세마포가 동일한데....
  * `static int num1; static int num2;` 이런식으로 공유 자원 변수가 여러 개인 상황에서 두 프로세스가 각각 num1, num2에 접근하는 건 어떤 상황일까?
  * 위 상황은 문제가 되지 않는데, num1에 둘이 동시에 접근할때가 문제 되는게 아닌지...
  * https://m.blog.naver.com/dlaxodud2388/222201325948 https://100100e.tistory.com/208
  * 메인 메모리의 레디큐에 있다가, 세마포어 큐가 비어 있으면 프로세스 넣고 접근하게 해 줌
  * 더럽지만 많이 쓰는 화장실 비유로 따진다면;... 변기 여러 칸을 두는건 틀린 비유라고 느낌. 굳이 따지자면 뮤텍스락은 화장실 한 칸에 한 명만 들어가게 하는것, 세마포는 화장실 한 칸에 여러 명이 들어가게 하는 것이라고 느낌....
* 실무에서 뮤텍스와 세마포가 어떻게 쓰일까...