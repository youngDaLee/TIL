package main

import (
	"context"
	"fmt"
	"os"
	"strconv"
	"time"
)

// f1 고루틴을 만들고 실행.
// c1 컨텍스트가 4초가 지나기 전 Done함수를 호출하면 고루틴이 끝날 시간이 없음
func f1(t int) {
	c1 := context.Background()
	// WithCancle은 기존 Context를 사용해서 캔슬레이션으로 자식을 생성.
	// CanceFunc()함수를 호출하면 부모가 자식을 가리키는 레퍼 삭제하고 타이머를 멈춤
	c1, cancel := context.WithCancel(c1)
	defer cancel() // context.CancelFunc() 값

	go func() {
		time.Sleep(5 * time.Second)
		cancel()
	}()

	select {
	case <-c1.Done():
		fmt.Println("f1() Done:", c1.Err())
		return
	case r := <-time.After(time.Duration(t) * time.Second):
		fmt.Println("f1():", r)
	}
}

// f2
func f2(t int) {
	c2 := context.Background()
	// WithTimeout은 ctx, duration 매개변수 필요 -> 시간 지나면 자동으로 cancel()호출됨
	c2, cancel := context.WithTimeout(c2, time.Duration(t)*time.Second)
	defer cancel() // context.CancelFunc() 값

	go func() {
		time.Sleep(5 * time.Second)
		cancel()
	}()

	select {
	case <-c2.Done():
		fmt.Println("f2() Done:", c2.Err())
		return
	case r := <-time.After(time.Duration(t) * time.Second):
		fmt.Println("f2():", r)
	}
	return
}

func f3(t int) {
	c3 := context.Background()
	// 데드라인이 지나면 자동으로 cancel 호출
	deadline := time.Now().Add(time.Duration(2*t) * time.Second)
	c3, cancel := context.WithDeadline(c3, deadline)
	defer cancel()

	go func() {
		time.Sleep(5 * time.Second)
		cancel()
	}()

	select {
	case <-c3.Done():
		fmt.Println("f3() Done:", c3.Err())
		return
	case r := <-time.After(time.Duration(t) * time.Second):
		fmt.Println("f3():", r)
	}
	return
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Need Parameter. Please Write Delay")
		return
	}

	delay, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("Delay:", delay)

	f1(delay)
	f2(delay)
	f3(delay)
}
