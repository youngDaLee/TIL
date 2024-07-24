/*
ch25. 채널과 컨텍스트

채널 : 고루틴끼리 메세지를 전달할 수 있는 메세지큐. 뮤텍스 없이 동시성 프로그래밍 가능
*/
package main

import (
	"fmt"
	"sync"
	"time"
)

func channelEx() {
	var messages chan string = make(chan string)

	// 채널에 데이터 넣기
	messages <- "This is message"

	// 채널에서 데이터 빼기
	var msg string = <-messages
	fmt.Println(msg)
}

func gorutineChannerEx() {
	var wg sync.WaitGroup
	ch := make(chan int)

	wg.Add(1)
	go square(&wg, ch) // 고루틴 생성
	ch <- 9            // 채널에 데이터 넣음
	wg.Wait()          // 작업 완료 기다림
}

func square(wg *sync.WaitGroup, ch chan int) {
	n := <-ch // 데이터 빼옴

	time.Sleep(time.Second)
	fmt.Printf("Square: %d\n", n*n)
	wg.Done()
}

// 컨텍스트
