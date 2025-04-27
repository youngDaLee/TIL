package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"time"
)

func disk_vs_memory() {
	fmt.Println("=== [Disk vs Memory] ===")
	// 1. 디스크 파일 읽기
	file, err := os.Open("large_test_file.dat") // 100MB짜리 준비 필요
	if err != nil {
		panic(err)
	}
	defer file.Close()

	start := time.Now()
	io.Copy(io.Discard, file)
	fmt.Printf("Disk read time: %v\n", time.Since(start))

	// 2. 메모리 복사
	memData := make([]byte, 100*1024*1024) // 100MB 메모리 블록
	start = time.Now()
	_, _ = io.Copy(io.Discard, bytes.NewReader(memData))
	fmt.Printf("Memory read time: %v\n", time.Since(start))
}
