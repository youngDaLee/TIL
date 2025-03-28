package main

import (
	"bytes"
	"context"
	"fmt"
	"log"
	"net/http"
	"time"

	echopb "github.com/lee-dayoung/grpc-benchmark/grpc/proto"
	"google.golang.org/grpc"
)

const (
	testCount = 1000
)

func callREST() {
	client := &http.Client{}
	url := "http://localhost:8080/echo"
	body := []byte(`{"message":"hello"}`)

	start := time.Now()
	for i := 0; i < testCount; i++ {
		_, err := client.Post(url, "application/json", bytes.NewBuffer(body))
		if err != nil {
			log.Fatalf("REST request failed: %v", err)
		}
	}
	elapsed := time.Since(start)
	fmt.Printf("[REST] Total time for %d requests: %v\n", testCount, elapsed)
}

func callGRPC() {
	conn, err := grpc.Dial("localhost:9090", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to gRPC server: %v", err)
	}
	defer conn.Close()

	client := echopb.NewEchoServiceClient(conn)

	start := time.Now()
	for i := 0; i < testCount; i++ {
		_, err := client.Echo(context.Background(), &echopb.EchoRequest{Message: "hello"})
		if err != nil {
			log.Fatalf("gRPC request failed: %v", err)
		}
	}
	elapsed := time.Since(start)
	fmt.Printf("[gRPC] Total time for %d requests: %v\n", testCount, elapsed)
}

func main() {
	/*
		=== Starting Benchmark ===
			[REST] Total time for 1000 requests: 279.148958ms
			[gRPC] Total time for 1000 requests: 53.305833ms
	*/
	fmt.Println("=== Starting Benchmark ===")
	callREST()
	callGRPC()
}
