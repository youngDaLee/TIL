## 개념
- 구글에서 개발한 데이터 직렬화 도구
  - 데이터 직렬화(Serialization)란? : 객체 또는 데이터를 다른 시스템에서도 사용할 수 있도록 byte 형식으로 변환하는 방식
  - byte로 변환된 데이터를 다시 시스템 환경에 변환하는 것은 역직렬화(Deserialization)라고 함
- 웹서비스, RPC, DB에서 사용할 수 있는 구조화된 데이터를 저장하는 방식
- gRPC : 구글에서 개발한 RPC 시스템
  - RPC란? : 응용 프로그램이 네트워크를 통해 서로 통신할 수 있도록 하는 프로토콜. 상대방의 네트워크의 세부 상태를 알지 못해도 서비스를 요청하는 프로토콜.
  - API : 어떠한 프로토콜을 사용하여 두 소프트웨어가 서로 통신할 수 있도록 하는 메커니즘
  - RPC vs REST : 둘다 API 설계의 아키텍쳐 스타일. 차이점은 REST는 HTTP 프로토콜만 허용하고, RPC는 프로토콜 무관. 또한 REST 는 리소스 기반이며 RPC는 액션 기반으로 설계를 함. REST가 더 많은 규약을 가진 것으로 이해함.
  - 추가로 REST는 Stateless 방식. 즉 세션을 유지하지 않고 요청에 대한 응답만 유지하는 방식. RPC는 그러한 제약이나 규약이 따로 없다.

![image](https://github.com/youngDaLee/TIL/assets/64643665/a39e4a92-f04c-4a36-8d7d-845d40d673f8)


## 장단점
- 장점
  - 바이너리로 되어있기 때문에, JSON, XML 보다 훨씬 빠름
  - 시스템간 데이터 이식이 용이함

- 단점
  - 설정이 번거로움
  - 

## 쓰는 이유
- 시스템간 데이터 구조 호환
- 빠른 통신

## 의문점
- Protobuf 서버를 탄다고 하는데, 매번 데이터 request/response 때 마다 protobuf 서버에서 변환하는 것(gateway)이 JSON/XML을 그대로 사용하는 것 보다 더 빠른지

## 참고
- [Protobuf란 무엇인가요](https://appmaster.io/ko/blog/peurotobeopeuran-mueosibnigga)
- [Java에서의 데이터 직렬화](https://zakelstorm.tistory.com/82)
- [gRPC란](https://chacha95.github.io/2020-06-15-gRPC1/)
- [RPC란](https://velog.io/@jakeseo_me/RPC%EB%9E%80)
- [RPC vs REST](https://aws.amazon.com/ko/compare/the-difference-between-rpc-and-rest/) 
- [RPC vs REST](https://mindock.github.io/network/rest-rpc/) 
- https://appmaster.io/ko/blog/grpc-dae-hyusig
- https://jins-dev.tistory.com/entry/RPC-Remote-Procedure-Call-%EC%9D%98-%EA%B0%9C%EB%85%90
- [RPC의 개념](https://jins-dev.tistory.com/entry/RPC-Remote-Procedure-Call-%EC%9D%98-%EA%B0%9C%EB%85%90)