/*
ch24. 고루틴과 동시성 프로그래밍
*/
package main

import (
	"fmt"
	"time"
)

func PrintHangul() {
	hanguls := []rune{'가', '나', '다', '라', '마', '바', '사'}
	for _, v := range hanguls {
		time.Sleep(300 * time.Microsecond)
		fmt.Printf("%c ", v)
	}
}

func PrintNumbers() {
	for i := 1; i <= 5; i++ {
		time.Sleep(400 * time.Microsecond)
		fmt.Printf("%d ", i)
	}
}

func routineEx() {
	go PrintHangul()
	go PrintNumbers()

	time.Sleep(3 * time.Second)
}

// 뮤텍스 - 상호배재. Lock을 획득하여 고루틴 하나만 자원에 접근하도록 조정함 > 잘못 사용하면 데드락 이슈
