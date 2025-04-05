package main

import (
	"bufio"
	"context"
	"fmt"
	"log"
	"os"
	"time"

	pb "grpcstreaming_chat/proto"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	// Create a connection to the server
	conn, err := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close() // Close the stream

	// Create a new client
	client := pb.NewChatServiceClient(conn)

	// Start a new chat stream
	stream, err := client.Chat(context.Background())

	if err != nil {
		log.Fatalf("could not start chat stream: %v", err)
	}

	// 유저 입력
	fmt.Print("Enter your username: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	username := scanner.Text()

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

	// Send messages to the server
	fmt.Println("Start sending messages (type 'exit' to quit):")
	for {
		scanner.Scan()
		text := scanner.Text()

		err := stream.Send(&pb.Message{
			User:      username,
			Text:      text,
			Timestamp: time.Now().Unix(),
		})
		if err != nil {
			log.Fatalf("could not send message: %v", err)
		}
		if text == "exit" {
			fmt.Println("Exiting chat...")
			break
		}
	}

	// Close the stream
	if err := stream.CloseSend(); err != nil {
		log.Fatalf("could not close stream: %v", err)
	}
	return
}
