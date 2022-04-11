# 배열(Array)


# Summary
## Array
### Array란
- Array는 연관된 데이터를 메모리상에 **연속적이며 순차적**으로 미리 할당된 크기만큼 저장하는 자료구조
- LinkedList와의 차이점: 메모리에 저장되는 방식, 이에 따른 Operation의 연산 속도

### Array의 특징
- 고정된 저장 공간(fixed-size)
- 순차적인 데이터 저장(order)

### Array의 operation들의 time comlexity(시간복잡도)
- 조회 : O(1)
- append(마지막 인덱스에 추가): O(1)
- pop(마지막 인덱스에 삭제): O(1)
- insert(삽입): O(n)
- delete(삭제): O(n)
- search(탐색): O(n)

### Array의 장점
- 조회와 append가 빠르다.
- 조회를 많이 해야 하는 작업에서는 Array를 많이 사용한다.

### Array의 단점
- fixed-size 특성 상 선언 시 Array의 크기를 미리 정해야 한다
  - 메모리 낭비나 추가적인 overhead를 발생시킬 수 있다.



## Dynamic Array
### Dynamic Array란 
- 저장공간이 가득 차면 **resize**를 해서 유동적으로 사이즈를 조절해 데이터를 저장하는 자료구조
- Array의 경우 size가 고정되었다면, 선언 시 설정한 size보다 많은 갯수의 data가 추가되면 저장 불가능.

### Dynamic Array의 resize 방식
Dynamic Array는 size를 자동으로 resizing하는 Array. 기존 고정된 size를 가진 Static Array의 한계점을 보안하고자 고안됨. data를 계속 추가하다가 기존에 할당된 memory를 초과하면 size를 늘린 배열을 선언하고 그곳으로 데이터를 옮김으로서 늘어난 크기의 size를 가진 배열이 됨. 다양한 resize방식이 있고, 대표적으로 기존 Array size의 2배를 할당하는 doubling이 있음.

#### Doubling
- 데이터를 추가(O(1))하다 메모리가 초과되면 기존 배열 size보다 2배 더 큰 배열을 선언하고, 데이터를 일일이 옮기는(O(n))방식

### 분할상환 시간복잡도 Amortized time complexity
- Dynamic Array에 데이터를 추가할 때 마다 O(1)시간이 걸리고, resize를 하는 순간만 O(n)의 시간이 걸림
- 가끔 발생하는 O(n)의 resize하는 시간을 자주 발생하는 O(1)의 작업들이 분담해서 나눠 가짐으로서 전체적으로 O(1)의 시간이 걸림
- 이를 **amortized O(1)**이라 함


## Linked List
### Linked List란
- Linked List는 Node 구조체로 구성.
  - *Node란: 데이터 값과 다음 Node의 address값을 저장하는 구조체
- Linked List는 **물리적 메모리상에서는 비연속적**으로 저장되지만, Linked List를 구성하는 Node가 다음 Node의 address를 가리킴으로서 **논리적 연속성**을 가진 자료구조
- 데이터가 추가되는 시점에 메모리를 할당하기 때문에 **메모리를 좀 더 효율적**으로 사용 가능.
- tree, graph 등 다른 자료구조를 구현할 때 자주 쓰이는 기본 자료구조.

### 논리적 연속적
- 각 Node를이 next address 정보를 가지고 있기 때문에 논리적으로 연속성을 가지고 있음.
- Array는 물리적 메모리상에서 순차적으로 저장하는 방식. 
- Linked list는 메모리에서 연속성을 유지하지 않아도 되기 때문에 사용이 더 자유로운 대신, Next address를 추가적으로 저장해야 하기 때문에 데이터 하나 당 차지하는 **메모리가 더 커지게** 된다.

### 시간복잡도
중간에 데이터 삽입/삭제(insertion/delete) 시 물리적으로 옮길 필요 없이 next address 값만 변경하면 되기 때문에 O(1)의 시간복잡도로 삽입/삭제 가능
- access: O(n)
- search: O(n)
- insertion: O(1)
- deletion: O(1)



## 면접 예상 질문
**Q) 미리 예상한 것 보다 더 많은 수의 data를 저장하느라 Array size를 넘어서게 되었을 때 어떻게 해결 가능한지**
- 기존 사이즈보다 더 큰 array를 선언하여 데이터를 옮겨 할당한다. 모든 데이터를 옮겼으면 기존 array는 메모리에서 삭제한다.
- 이렇게 배열의 크기를 조절하는 자료구조를 **Dynamic array**라 한다
- size를 예측하기 쉽지 않으면 Array 대신 Linked List를 사용함으로서 데이터가 추가될 때 마다 메모리 공간을 할당받는 방식을 사용한다


**Q) Dynamic Array를 Linked List와 비교하여 장단점을 설명**
- Linkied List와 비교했을 때 Dynamic Array의 장점은
  - 데이터 접근성과 할당이 O(1)로 굉장히 빠르다. 이는 index 접근 방식이 산술적 연산(배열 첫 data주소값)+(offset)으로 이루어져 있기 때문(random access)
  - Dynamic Array의 맨 뒤에 데이터를 추가 혹은 삭제하는 것이 상대적으로 빠름(O(1))
- Linkied List와 비교했을 때 Dynamic Array의 단점은
  - Dynamic Array의 중간에 insert, delete 시 느린 편(O(n)) -> 메모리 상 데이터가 연속적으로 저자오디어 있어서 insert, delete 시 마다 data를 shift 해야함
  - resize 시 예상보다 현저히 낮은 performance 발생
  - resize에 많은 시간이 걸려 필요 이상 메모리 공간 할당됨. **사용하지 않는 메모리 공간 발생**

**Q) Array vs Linked List를 비교해서 설명**
- Array는 메모리상에서 연속적으로 데이터를 저장하는 자료구조.
- Linked List는 메모리상에서 연속적이지 않지만, 각각의 원소가 다음 원소의 메모리 주소 값을 저장해 놓음으로서 논리적 연속성을 유지함.
- 따라서 각 Operation의 시간복잡도가 다르다.
  - 데이터 조회: Array O(1) / Linked List O(n)
  - 삽입/삭제: Array O(n) / Linked List O(1)

- 얼마만큼의 데이터를 저장할지 미리 알고 있고(정적 데이터), 조회 많이하면 **Array**
- 몇 개의 데이터가 저장될지 불확실하고, 삽입/삭제가 잦으면 **Linked List**

- **조회(lookup)**
  - Array: **O(1)**: 메모리 상 연속적으로 데이터 저장하였기 때문에 저장된 데이터 **즉시접근(random access)** 가능
  - Linked List: **O(n)**: 메모리상 불연속적으로 데이터 저장하였기 때문에 **순차접근(Sequential Access)** 가능. 특정 index 조회 위해 O(n)시간 소요

- **삽입/삭제(insert/delete)**
  - Array
    - 맨 마지막 원소 추가/삭제(push/pop) : O(1)
    - 중간 원소 삽입/삭제(insert/delete): O(n)
  - Linked List
    - 모든 위치에서: O(1) 다음 주소값으로만 변경하면 되기 때문에 shift 할 필요가 없음
    - 담나 추가/삭제를 위해 index까지 도달하는데 O(n)의 시간이 걸리므로 실질적으로 O(n)의 시간이 걸림

- **memory**
  - Array: (장점) 데이터 접근, append가 빠름 / (단점) 메모리 낭비 - 선언 시 fixed size를 설정하여 메모리 할당을 하기 때문에 데이터가 저장되어 있지 않아도 메모리를 차지함
  - Linked List: runtime 중에도 size를 늘리고 줄일 수 있음. initial size를 고민할 필요가 없고 필요한 만큼 메모리를 할당하여 메모리 낭비가 없음

**Q) 어느 상황에서 Linkded List를 쓰는게 Array보다 나을까**
- O(1)로 삽입/삭제를 자주 해야 할 때
- 얼마만큼의 데이터가 들어올지 예측을 할 수 없을때
- 조회작업을 별로 하지 않을때

**Q) 어느 상황에 Array를 쓰는게 Linked List보다 나을까**
- 조회작업 자주 할 때
- Array를 선언할 당시 데이터 갯수 미리 알고 있을 때(정적 데이터)
- 데이터를 반복문을 통해 빠르게 순회할 때
- 메모리를 적게 쓴느게 중요한 상황일 때. Linked List보다는 Array가 메모리를 적게 차지하기 때문에 미리 들어올 데이터 양을 알고만 있으면 Array가 메모리를 더 효율적으로 사용 가능

**Q) Array와 Linked List의 memory allocation은 언제 일어나며, 메모리의 어느 영역을 할당받는지**
- Array는 compile 단계에서 memory allcocation이 일어남. 이를 Static Memory Allocation이라 함. 이 경우 Stack memory 영역에 할당됨
- Linked List의 경우 runtime 단계에서 새로운 node가 추가될 때 마다 memory allocation이 일어남. 이를 Dynamic Memory Allocation이라 부름 .Heap 메모리 영역에 할당됨