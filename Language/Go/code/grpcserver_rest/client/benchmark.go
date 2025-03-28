package main

import (
	"bytes"
	"context"
	"fmt"
	"log"
	"net/http"
	"time"

	echopb "github.com/lee-dayoung/grpc-benchmark/grpc/proto"
	"github.com/vmihailenco/msgpack"
	"google.golang.org/grpc"
)

const (
	testCount = 10000
)

type EchoRequest struct {
	Message string `msgpack:"message"`
}

type EchoResponse struct {
	Message string `msgpack:"message"`
}

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

func callRESTMsgPack() {
	client := &http.Client{}
	url := "http://localhost:8080/echo"
	start := time.Now()

	// 1. JSON → MessagePack
	reqBody := EchoRequest{Message: "hello"}
	var buf bytes.Buffer
	if err := msgpack.NewEncoder(&buf).Encode(reqBody); err != nil {
		log.Fatalf("msgpack encode error: %v", err)
	}

	// 2. POST 요청
	req, err := http.NewRequest("POST", url, &buf)
	if err != nil {
		log.Fatalf("Failed to create request: %v", err)
	}
	req.Header.Set("Content-Type", "application/msgpack")

	resp, err := client.Do(req)
	if err != nil {
		log.Fatalf("Request failed: %v", err)
	}
	defer resp.Body.Close()

	// 3. MessagePack 응답 디코딩
	var resBody EchoResponse
	if err := msgpack.NewDecoder(resp.Body).Decode(&resBody); err != nil {
		log.Fatalf("msgpack decode error: %v", err)
	}

	elapsed := time.Since(start)
	fmt.Printf("[RESTMsgPack] Total time for %d requests: %v\n", testCount, elapsed)
}

func main() {
	/*
		=== Starting Benchmark ===
		[REST] Total time for 10000 requests: 2.489068375s
		[gRPC] Total time for 10000 requests: 495.642834ms
		[RESTMsgPack] Total time for 10000 requests: 1.451667ms
	*/
	fmt.Println("=== Starting Benchmark ===")
	callREST()
	callGRPC()
	callRESTMsgPack()
}
