# Queue


# Summary
## Queue
### Queue란?
- 선입선출 **FIFO(First In First Out)**의 자료구조
- 시간복잡도: enqueue O(1)  dequeue O(1)
  - enqueue : 뒤에서 데이터를 넣는 것. queue에서 데이터를 추가하는 것
  - dequeue : 앞에서 데이터를 빼는 것. queue에서 데이터를 추출하는 것
- 활용 예: Cache 구현, 프로세스 관리, 너비우선탐색(BFS)

### 구현 방식
- Array-Based queue: Array로 Queue를 구현. enqueue와 dequeue 과정에서 남는 메모리 발생. 따라서 메모리 낭비 줄이기 위해 Circular queue 형식으로 구현
- List-Based queue: Linked-List 이용해 Quque를 구현. 재할당이나 메모리 낭비가 없어짐

### 확장 & 활용
- deque(double-ended queue) : 양쪽에서 enqueue와 dequeue가 가능
- prioritiy queue: 시간순서가 아닌 **우선순위**가 높은 순서로 dequeue할 수 있음
- 활용 예시: 하나의 자원을 공유하는 프린터, CPU task scheduling, cache 구현, BFS 등..

### Circle queue(원형 큐)
- Array에서 dequeue를 해서 메모리가 빈 앞쪽(front)를 활용.
- Queue가 다 차면 Array 앞쪽에 enqueue해줌


## Stack
### Stack이란?
- 후입선출 LIFO(Last In First Out)
- 시간복잡도
  - push O(1)
  - pop O(1)
- 활용 예: 후위표기법 연산, 괄호 유효성 검사, 웹 브라우저 방문기록(뒤로가기), 깊이우선탐색(DFS)
- push : stack에 데이터를 추가하는 것
- pop : stack에 데이터를 추출하는 것.
  - push와 pop 모두 top에 원소를 추가하거나 삭제하는 형식으로 구현됨

### LIFO
- 가장 최근 추가한 데이터가 가장 먼저 나오는 후입선출(LIFO)형식으로 데이터를 저장함


## 면접 예상 질문
### Q) Array-Base와 List-Base의 차이
- Array-Base의 queue는 circle queue로 구현하는 것이 일반적. **메모리를 효율적으로 사용하기 위함**. enqueue가 계속 발생하면 fixed size를 넘어서기 때문에 dynamic array와 같은 방법으로 Array 확장시켜야 함. 그럼에도 불구하고 enqueue의 시간복잡도는 (amortized)O(1) 유지 가능
- List-Based는 singly-linked list로 구현. enqueue는 singly-linked list에서 append를 하는 걸로 구현(O(1)), dequeque는 맨 앞 원소 삭제하고 first head 변경(O(1))
- 두 가지 방식 모두 O(1)의 시간 복잡도.
- Array-Base는 전반적으로 performance가 좋지만 worst case의 경우는 훨씬 느림(resize)
- List-Base는 enqueue를 할 때 마다 memory allocation을 하기 때문에 전반적인 runtime이 느릴 수 있음


### Q) Stack 두 개를 이용해 Queue를 구현해라

