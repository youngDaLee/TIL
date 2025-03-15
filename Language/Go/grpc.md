# gRPC
## gRPC란?
- HTTP/2 기반의 구글에서 개발한 원격 프로시저 호출(RPC) 시스템
  - RPC : 언어와 환경에 구애받지 않고, 자신과 다른 주소공간에서 함수를 실행할 수 있도록 하는 API 호출 규약.
- 주고받는 메세지 형식 및 서비스 인터페이스 정의 용도로 프로토콜 버퍼(protocol buffer) 사용
- gRPC 클라이언트-서버는 서로 다른 언어로 작성 가능

gRPC 장점
- 데이터 교환 시 바이너리 형식을 사용하기 때문에 일반 텍스트 형식으로 주고받는 서비스보다 빠름
- 제공된 커멘드라인 도구가 더 쉽고 빠르게 작업을 도와줌
- gRPC서비스 함수와 메세지를 정의하고 나면 이를 사용하는 서버, 클라이언트를 RESTful 보다 쉽게 만들 수 있음
- 스트리밍 서비스에 사용 가능
  - 단순한 요청-응답 뿐만이 아니라 양방향 스트리밍을 지원...
- gRPC에서 데이터 교환 로직을 처리해서 개발자가 처리할 필요가 없음
- HTTP/2를 사용하기 때문에 멀티플렉싱, 헤더 압축등으로 성능을 최적화 함
  - 멀티플렉싱 : 하나의 연결(채널)에서 여러 데이터 스트림을 동시에 처리하는 기술

### 헷갈리는 개념 정리.. API? RPC? HTTP? REST? gRPC?
API(Application Programming Interface)
- 애플리케이션 간 소통하는 방식
- API를 호출해서 Request를 보내고, Response를 받는것.
- REST API(HTTP 기반) / RPC(Remote Procedure Call) / gRPC(Google RPC) 가 모두 API에 포함됨

RPC(Repmote Procedure Call)
- 네트워크를 통해 다른 서버 함수를 실행하는 방식
- 내 코드에서 다른 콤퓨터의 함수를 호출하는 것 처럼 동작하게 만드는것
- 클라이언트가 서버 함수를 호출하는 것 처럼 동작함(함수 호출 형태로 동작)
- API가 간단하고 성능이 빠름
- REST보다 네트워크 오버헤드가 적음

```
response = callRemoteFunction("getUserData", userID=1234)
```

HTTP(Hypertext Transfer Protocol)
- 웹에서 데이터를 주고받는 기본 프로토콜
- 브라우저와 서버간 통신에 사용됨
- Request / Response 방식
- HTTP/1.1과 HTTP2가 있음
- 보통 REST API 방식으로 사용됨 (URL기반)


REST(Representational State Transfer)
- HTTP 기반의 API 설계 방식
- HTTP 요청을 사용해 데이터를 주고받는 규칙
- REST 특징
  - HTTP 메서드(GET,POST,PUT,DELETE) tkdyd
  - url을 리소스 단위로 설계
  - JSON 혹은 XML 을 데이터 포맷으로 사용함
- HTTP 요청 마다 새로운 연결을 생성해야 해서 오버헤드가 큼
- JSON 텍스트로 요청을 주고받아서 데이터 크기가 큼
- HTTP/1.1 기반이라 멀티플랙식 미지원

```
GET /users/123  # user ID 123에 대한 데이터 요청
POST /users     # 새로운 사용자 추가
DELETE /users/123  # user ID 123 삭제
```

gRPC(Google Remote Procedure Call)
- HTTP/2.2 기반의 RPC 프레임워크
- ProtoBuf 사용하여 바이너리 데이터를 전송하기 때문에 JSON보다 가벼움
- .proto 로 자동으로 코드를 생성하기 때문에 여러 언어에서 사용 가능
- 양방향 스트리밍을 사용하기 때문에 REST보다 강력하게 실시간 통신 가능

```
syntax = "proto3";

service Greeter {
    rpc SayHello (HelloRequest) returns (HelloResponse);
}

message HelloRequest {
    string name = 1;
}

message HelloResponse {
    string message = 1;
}
```

### RPC vs REST
- RPC는 네트워크를 통해 "다른 서버 함수를 직접 호출하는 것"
  - 함수형 API 디자인
  - 동작(메서드)중심
  - 바이너리
  - HTTP/2
- REST는 네트워크를 통해 "리소스(데이터)를 주고받는것"
  - 리소스형 API 디자인
  - 데이터 중심(CRUD)
  - 텍스트
  - HTTP/1.1

|	| RPC |	REST |
|:--:|:--:|:--:|
|목적|원격 함수 호출|리소스(데이터) 조작|
|설계 철학|함수 중심|리소스 중심|
|예제|`getUserData(123`)|`GET /users/123`|
|데이터 구조|함수 호출과 유사|HTTP URI로 리소스 식별|
|표준 프로토콜|다양한 프로토콜 사용 (gRPC, JSON-RPC 등)|HTTP 기반|

### gPRC는 프로토콜인가?
- 아님. RPC 프레임워크
- RPC는 개념(네트워크를 이용한 함수 호출), gRPC는 RPC를 구현한 프레임워크.
- RPC의 프로토콜은 여러가지이며, 그 중 gRPC는 HTTP/2+ProtocolBuffer 프로토콜을 사용한 프레임워크임

그러면 REST는?
- 프토콜도, 프레임워크도 아닌 아키텍쳐 스타일, 설계 원칙...
- 네트워크에서 클라이언트-서버가 어떻게 소통해야 하는지를 정의하는 방식임.
- HTTP/1.1 vmfhxhzhfdmf tkdydgka

### HTTP vs gRPC 비교
| |HTTP|gRPC|
|:--|:--|:--|
|전송 프로토콜|HTTP/1.1, HTTP/2|HTTP/2|
|데이터 포맷|JSON, XML, HTML 등|Protocol Buffers (바이너리)|
|성능|요청당 새로운 연결 생성 (HTTP/1.1)|멀티플렉싱 지원 (HTTP/2)|
|압축 지원|Gzip 사용 가능|기본적으로 헤더 압축 지원|
|스트리밍|웹소켓 또는 SSE로 가능|서버/클라이언트/양방향 스트리밍 기본 제공|
|언어 독립성|JSON 기반으로 여러 언어 지원|Protocol Buffers를 사용하여 다국어 지원|
|자동 코드 생성|없음|.proto 파일로 자동 생성|

### protocol buffer
- 구조화된 데이터를 직렬화 하는 방식
  - 데이터 직렬화(Serialization)란? : 객체 또는 데이터를 다른 시스템에서도 사용할 수 있도록 byte 형식으로 변환하는 방식
- IDL(인터페이스 정의 언어)도 프로토콜 버퍼의 일부분
- 데이터 교환에 바이너리 형식을 사용해서 일반 텍스트를 사용하는 직렬화 방식보다 공간을 덜 차지 -> 다만 바이너리 형식으로 인코딩/디코딩 해야 함...

## 왜 golang에서 gRPC가 언급되는가?
- go는 MSA환경에서 많이 사용됨
- gRPC는 protocol buffer를 사용하기 때문에 여러 언어간 통신에 탁월함 -> MSA 통신을 위한 강력한 도구
- Go의 동시성 모델(고루틴)과 gRPC 스트리밍 기능을 활용하면 대규모 분산 시스템, 실시간 서비스에 효과적으로 사용 가능
