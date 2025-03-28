package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/vmihailenco/msgpack/v5"
)

type EchoRequest struct {
	Message string `msgpack:"message"`
}

func echoHandler(w http.ResponseWriter, r *http.Request) {
	var req EchoRequest
	if err := msgpack.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Bad Request", http.StatusBadRequest)
		return
	}
	resp, _ := msgpack.Marshal(req)
	w.Header().Set("Content-Type", "application/msgpack")
	w.Write(resp)
}

func main() {
	http.HandleFunc("/echo", echoHandler)
	fmt.Println("Binary REST server (MessagePack) listening on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
