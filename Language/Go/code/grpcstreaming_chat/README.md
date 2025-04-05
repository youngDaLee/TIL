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


## client