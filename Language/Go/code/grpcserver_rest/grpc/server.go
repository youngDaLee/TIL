package grpc

import (
	"context"
	"fmt"
	"log"
	"net"

	echopb "github.com/lee-dayoung/grpc-benchmark/grpc/proto"
	"google.golang.org/grpc"
)

type echoServer struct {
	echopb.UnimplementedEchoServiceServer
}

func (s *echoServer) Echo(ctx context.Context, req *echopb.EchoRequest) (*echopb.EchoResponse, error) {
	return &echopb.EchoResponse{Message: req.Message}, nil
}

func main() {
	listener, err := net.Listen("tcp", ":9090")
	if err != nil {
		log.Fatalf("Failed to listen: %v", err)
	}

	server := grpc.NewServer()
	echopb.RegisterEchoServiceServer(server, &echoServer{})

	fmt.Println("gRPC server listening on :9090")
	if err := server.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
