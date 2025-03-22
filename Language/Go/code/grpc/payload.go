package main

import (
	"encoding/json"
	"fmt"
	"log"

	userpb "github.com/lee-dayoung/TIL/Language/Go/code/grpc/proto"
	"google.golang.org/protobuf/proto"
)

type User struct {
	ID    int32  `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

func jsonPayloadSize(u User) {
	data, err := json.Marshal(u)
	if err != nil {
		log.Fatal("Failed to marshal JSON:", err)
	}
	fmt.Printf("JSON Payload Size: %d bytes\n", len(data))
}

func protoPayloadSize(u *userpb.User) {
	data, err := proto.Marshal(u)
	if err != nil {
		log.Fatal("Failed to marshal Proto:", err)
	}
	fmt.Printf("Protobuf Payload Size: %d bytes\n", len(data))
}

func comparePayloadSize() {
	u := User{
		ID:    1,
		Name:  "Dayoung",
		Email: "ldy0956@gmail.com",
	}
	jsonPayloadSize(u)

	pu := &userpb.User{
		Id:    1,
		Name:  "Dayoung",
		Email: "ldy0956@gmail.com",
	}
	protoPayloadSize(pu)
	/* 결과
	JSON Payload Size: 53 bytes
	Protobuf Payload Size: 30 bytes
	*/
}

func main() {
	comparePayloadSize()
}
