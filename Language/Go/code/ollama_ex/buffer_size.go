package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"time"
)

// 버퍼가 너무 작으면 읽기가 많아져서 느려짐
// 버퍼가 너무 크면 메모리 낭비 + 복사 비용
// 적당한 버퍼 사이즈를 찾는 것이 중요
func measure(bufferSize int) {
	data := bytes.Repeat([]byte("A"), 100*1024*1024) // 100MB 메모리 블록
	reader := bufio.NewReaderSize(bytes.NewReader(data), bufferSize)

	start := time.Now()
	io.Copy(io.Discard, reader)
	duration := time.Since(start)

	fmt.Printf("Buffer size: %6d bytes => Read time: %v\n", bufferSize, duration)
}

func buffer_size() {
	fmt.Printf("=== [Buffer Size] ===\n")
	sizes := []int{512, 4096, 16384, 65536, 262144, 1048576} // 512B, 4KB, 16KB, 64KB, 256KB, 1MB
	for _, size := range sizes {
		measure(size)
	}
}
