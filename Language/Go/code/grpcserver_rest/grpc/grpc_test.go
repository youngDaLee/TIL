package grpc_test

import (
	"context"
	"log"
	"testing"

	echopb "github.com/lee-dayoung/grpc-benchmark/grpc/proto"
	"google.golang.org/grpc"
)

func CallREST(b *testing.B) {

	conn, err := grpc.Dial("localhost:9090", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to gRPC server: %v", err)
	}
	defer conn.Close()

	client := echopb.NewEchoServiceClient(conn)

	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			_, err := client.Echo(context.Background(), &echopb.EchoRequest{Message: "hello"})
			if err != nil {
				b.Error(err)
				continue
			}
		}
	})
}
