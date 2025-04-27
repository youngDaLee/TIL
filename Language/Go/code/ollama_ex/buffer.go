package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
)

// 단순 파일 시뮬레이션용 데이터
var data = []byte("ABCDEFGHIJK")

func withoutBuffer() {
	fmt.Println("=== Without Buffer ===")
	r := bytes.NewReader(data)

	// 현재 위치: 0 (A)
	r.Seek(2, io.SeekCurrent) // 현재 위치 기준 +2 이동
	b := make([]byte, 1)
	r.Read(b)
	fmt.Printf("Read after seek: %s\n", b)
}

func withBuffer() {
	fmt.Println("=== With Buffer (bufio.Reader) ===")
	r := bytes.NewReader(data)
	br := bufio.NewReaderSize(r, 4) // 버퍼 사이즈 4바이트

	// 버퍼: [A][B][C][D] 미리 읽어옴

	// A 읽기
	b := make([]byte, 1)
	br.Read(b)
	fmt.Printf("Read first byte: %s\n", b)

	// 현재 위치는 "논리적으로" B를 읽을 차례인데,
	// 실제 r (파일 핸들)은 아직 0번(A) 포지션에 있음!

	// 이제 현재 위치 기준으로 +2 이동하고 싶어함
	// Seek을 제대로 하려면?
	seekOffset := int64(2 - br.Buffered())
	r.Seek(seekOffset, io.SeekCurrent)
	br.Reset(r)

	// 다음 읽기
	br.Read(b)
	fmt.Printf("Read after corrected seek: %s\n", b)
}

func bufferread() {
	fmt.Println("=== [Buffer Read] ===")
	withoutBuffer()
	fmt.Println()
	withBuffer()
}
