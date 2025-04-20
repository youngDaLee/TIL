package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
)

type OllamaChunk struct {
	Response string `json:"response"`
	Done     bool   `json:"done"`
}

func main() {
	payload := `{"model": "llama3", "prompt": "What is the capital of France?"}`
	resp, err := http.Post("http://localhost:11434/api/generate", "application/json", strings.NewReader(payload))
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	scanner := bufio.NewScanner(resp.Body)
	var fullResponse string

	for scanner.Scan() {
		line := scanner.Text()
		var chunk OllamaChunk
		if err := json.Unmarshal([]byte(line), &chunk); err != nil {
			fmt.Println("JSON 파싱 오류:", err)
			continue
		}
		fullResponse += chunk.Response
		if chunk.Done {
			break
		}
	}

	fmt.Println("전체 응답:", fullResponse)
}
