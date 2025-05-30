# gRPC Streaming
클라이언트 - 서버 간 데이터를 스트리밍 방식으로 주고받는 기능
## gRPC 종류
### Unary RPC
- 일반적인 요청-응답 구조
- [grpc](./grpc.md)

### Server Streaming RPC
- 클라이언트 -> 서버 요청 1번
- 서버 -> 클라이언트 응답 여러번
- 서버에서 클라이언트로 데이터를 지속적으로 흘려보내는 경우
- ex) 스트리밍, 실시간 알림

### Client Streaming RPC
- 클라이언트 -> 서버 요청 여러범
- 서버 -> 클라이언트 응답 1번
- 클라이언트가 서버로 데이터를 모아서 전송하는 구조
- ex) 대용량 업로드, 센서 데이터 모으기 등

### Bidirectinal Streaming RPC
- 클라이언트 <-> 서버 요청-응답 여러번
- 완전한 스트림 기반 통신
- ex) 채팅, 실시간 게임 데이터

## 다른 통신 방식과 차이점
### gRPC Streaming vs Redis Pub/Sub
- gRPC Streaming 은 단일 연결에서 지속적인 송수신
- Redis Pub/Sub은 subscriber에게 메세지를 broadcast 하는 구조
  - 채널을 통해 단방향 메세지를 뿌림

### gRPC Streaming vs Socket
- Socket은 자유도는 높지만 고현 복잡성도 큼
- gRPC Streaming은 gRPC문법에 따라 흐름제어, 메세지 타입 정의까지 포함하여 유지보수가 용이하고 타입 안정성이 큼
