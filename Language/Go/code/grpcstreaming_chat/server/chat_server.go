package main

import (
	pb "grpcstreaming_chat/proto"
	"io"
	"log"
)

type chatServer struct {
	pb.UnimplementedChatServiceServer
}

func (s *chatServer) Chat(stream pb.ChatService_ChatServer) error {
	log.Println("new Chat stream started")

	// Receive messages from the client
	for {
		msg, err := stream.Recv()
		if err != nil {
			log.Printf("error receiving message: %v", err)
			return err
		}
		if err == io.EOF {
			log.Println("client closed the stream")
			return nil
		}

		// Process the message (e.g., print it)
		println("Received message from %s: %s", msg.GetUser(), msg.GetText())

		// Send a response back to the client
		if err = stream.Send(&pb.Message{
			User:      msg.GetUser(),
			Text:      "Message received: " + msg.GetText(),
			Timestamp: msg.GetTimestamp(),
		}); err != nil {
			log.Printf("error receiving message: %v", err)
			return err
		}
	}
}
