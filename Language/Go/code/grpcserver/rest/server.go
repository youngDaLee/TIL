package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type EchoRequest struct {
	Message string `json:"message"`
}

func echoHandler(w http.ResponseWriter, r *http.Request) {
	var req EchoRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Bad Request", http.StatusBadRequest)
		return
	}
	resp, _ := json.Marshal(req)
	w.Header().Set("Content-Type", "application/json")
	w.Write(resp)
}

func main() {
	http.HandleFunc("/echo", echoHandler)
	fmt.Println("REST server listening on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
