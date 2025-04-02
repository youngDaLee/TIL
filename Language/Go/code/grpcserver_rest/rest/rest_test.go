package rest_test

import (
	"bytes"
	"net/http"
	"testing"
)

func CallREST(b *testing.B) {
	client := &http.Client{}
	url := "http://localhost:8080/echo"
	body := []byte(`{"message":"hello"}`)

	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			resp, err := client.Post(url, "application/json", bytes.NewBuffer(body))
			if err != nil {
				b.Error(err)
				continue
			}
			resp.Body.Close()
		}
	})
}
