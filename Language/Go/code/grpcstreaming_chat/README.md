# Struct
```
.
├── client  // grpc client 코드
├── proto   // grpc protobuf 관련 코드
└── server  // grpc server 코드
```

루트 프로젝트 생성
```sh
go mod init grpcstreaming_chat    

# 필요 패키지 추가
go get google.golang.org/grpc
go get google.golang.org/protobuf
```

## proto 
go에서 사용할 protobuf 파일 생성
```sh
protoc --go_out=paths=source_relative:. \
       --go-grpc_out=paths=source_relative:. \
       chat.proto
```

## server
```go
type chatServer struct {
	pb.UnimplementedChatServiceServer
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	// gRPC Server Start
	grpcServer := grpc.NewServer()
	pb.RegisterChatServiceServer(grpcServer, &chatServer{})

	log.Println("gRPC server started on port :50051")
	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
```
- RegisterChatServiceServer : go 코드단에서 새로 생성할 구현체를 등록하는 함수. -> protoc에서 정의한 Chat()메서드를 호출할 방법을 알려주기 위해 필요. 서버에 서비스 핸들러를 등록하는 과정
- UnimplementedChatServiceServer : ChatServiceServer 인터페이스의 기본 구조체

```
go run ./server
```

## client
```go
func main() {
	// Create a connection to the server
	conn, err := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	// Create a new client
	client := pb.NewChatServiceClient(conn)

	// Start a new chat stream
	stream, err := client.Chat(context.Background())
	if err != nil {
		log.Fatalf("could not start chat stream: %v", err)
	}

	// Send messages to the server
	for i := 0; i < 10; i++ {
		msg := &pb.Message{
			User:      "User1",
			Text:      fmt.Sprintf("Hello from User1! Message %d", i),
			Timestamp: time.Now().Unix(),
		}
		if err := stream.Send(msg); err != nil {
			log.Fatalf("could not send message: %v", err)
		}
	}

	// Close the stream
	if err := stream.CloseSend(); err != nil {
		log.Fatalf("could not close stream: %v", err)
	}
}
```
- 커넥션 스트림을 생성한 뒤, 생성한 스트림으로 메세지를 10번 전송하는 로직


## 발생한 에러
한 번만 보내지고 아래 에러 발생
```
2025/04/05 22:47:51 gRPC server started on port :50051
2025/04/05 22:47:54 new Chat stream started
Received message from %s: %s User1 Hello from User1! Message 0
2025/04/05 22:47:54 error receiving message: rpc error: code = Unavailable desc = transport is closing
```
원인
- 클라이언트가 메세지 보낸 후 수신 기다리고 있는데 서버가 스트림을 종료함
``` go
// 1. 메시지 10개를 보냄
for i := 0; i < 10; i++ {
    stream.Send(...) // 클라이언트 -> 서버
}

// 2. 바로 CloseSend 호출
stream.CloseSend()

// 3. 서버 응답을 받지 않음 (또는 받더라도 그 전에 서버가 끊어짐)
```
- Send() 한 후 따로 받지 않음(서버 응답 무시)
- 서버가 응답을 보냈는데 클라이언트가 응답을 받지 않아 흐름이 꼬이고, 에러 발생한 뒤 스트리밍 종료

해결
```go
	// 서버로부터 메세지 수신하는 고루틴
	go func() {
		for {
			res, err := stream.Recv()
			if err != nil {
				log.Fatalf("could not receive message: %v", err)
				os.Exit(1)
			}
			ts := time.Unix(res.GetTimestamp(), 0).Format("2006-01-02 15:04:05")
			fmt.Printf("[%s]%s: %s\n", ts, res.GetUser(), res.GetText())
		}
	}()
```
- 클라이언트가 리시브를 받아야 함
- Bidirectional Streaming 에서는 Send() Recv()를 병렬(gorutine) 처리해야함

## 발생한 에러
```go
msg, err := stream.Recv()
if err == io.EOF { // 클라이언트가 스트림을 닫음(정상종료)
    log.Println("client closed the stream")
    return nil
}
if err != nil { // 에러 발생(비정상 종료)
    log.Printf("error receiving message: %v", err)
    return err
}
```
원하는건 위와 같이 정상종료(exit)했을때는 "client closed the stream" 이 뜨고, 그렇지 않을 때 에러 메세지가 떠야 하는데,
```
>  go run ./client
Enter your username: 다영
Start sending messages (type 'exit' to quit):
정식으로 끝내볼게요
[2025-04-05 23:15:10]다영: 정식으로 끝내볼게요
exit
Exiting chat...
```

```
[2025-04-05 23:15:10]다영: 정식으로 끝내볼게요
[2025-04-05 23:15:11]다영: exit
2025/04/05 23:15:11 error receiving message: rpc error: code = Unavailable desc = transport is closing
```

위와 같이 에러 코드를 타는 현상

원인
- 정상종료를 유도해야 EOF 감지 가능
```go
stream.CloseSend()
return // return 추가!!!
```
```go
defer stream.CloseSend()
```
위 두 방식중으로 해야 EOF 감지 가능