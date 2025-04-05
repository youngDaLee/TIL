package main

import (
	"fmt"
	pb "grpcstreaming_chat/proto"
	"io"
	"log"
	"time"
)

type chatServer struct {
	pb.UnimplementedChatServiceServer
}

func (s *chatServer) Chat(stream pb.ChatService_ChatServer) error {
	log.Println("new Chat stream started(새로운 유저 입장)")

	// Receive messages from the client
	for {
		msg, err := stream.Recv()
		if err == io.EOF { // 클라이언트가 스트림을 닫음(정상종료)
			log.Printf("client closed the stream")
			return nil
		}
		if err != nil { // 에러 발생(비정상 종료)
			log.Printf("error receiving message: %v", err)
			return err
		}

		// 채팅 출력부분
		ts := time.Unix(msg.GetTimestamp(), 0).Format("2006-01-02 15:04:05")
		fmt.Printf("[%s] %s: %s\n", ts, msg.GetUser(), msg.GetText())

		// 클라이언트에 메세지 전송
		if err = stream.Send(&pb.Message{
			User:      msg.GetUser(),
			Text:      msg.GetText(),
			Timestamp: msg.GetTimestamp(),
		}); err != nil {
			log.Printf("error receiving message: %v", err)
			return err
		}
	}
}
