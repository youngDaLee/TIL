package main

import (
	"fmt"
	"sort"
	"sync"
	"sync/atomic"
	"time"

	"github.com/davecgh/go-spew/spew"
)

// 익명함수
// 다른 함수 인자로 넘ㄱ주거나 다른 함수 리턴값으로 쓰임
func ex46() {
	var area = func(l int, b int) int {
		return l * b
	}
	spew.Dump(area(20, 30))

	// 더짧게
	func(l, b int) {
		spew.Dump(l * b)
	}(20, 20)
}

func ex47() {
	people := []struct {
		Name string
		Age  int
	}{
		{"kim", 27},
		{"lee", 43},
		{"jung", 36},
	}
	sort.Slice(people, func(i, j int) bool { return people[i].Age < people[j].Age })
	spew.Dump(people)
}

// 클로저 - 함수 외부의 변수에 접근
func ex48() {
	for i := 10.0; i < 100.0; i += 10.0 {
		cv := func() float64 {
			return i * 39.370
		}
		fmt.Printf("%.0f미터 => %6.1f인치\n", i, cv())
	}
}

// defer -> 함수 종료될 때 까지 실행을 미루는 기능 (스택에 쌓는다는 느낌.. -> 속도 떨어지긴 하지만 커넥션 닫거나 할 때 등등 finaly처럼 사용 가능 강추)
func ex49() {
	var fn = func(i int) {
		fmt.Println(i)
	}
	defer fn(3)
	defer fn(2)
	fn(1)
}

// 인터페이스
type Employee interface {
	PrintName() string
	PrintAddress() [3]string
}

type Emp struct {
	// extends, implemnets가 없기 때문에 모든 메서드를 리시버로 구현해야 함
	Name, PostNumber, Address1, Address2 string
}

func (e Emp) PrintName() string {
	return e.Name
}

func (e Emp) PrintAddress() [3]string {
	return [3]string{e.Address1, e.Address2, e.PostNumber}
}

func ex50() {
	var e Employee = Emp{"John", "12345", "add31....", "addr2...."}
	spew.Dump(e.PrintName(), e.PrintAddress())
}

type Polygons interface {
	Perimeter() float64
}
type Object interface {
	NumberOfSide() int
}

type Square float64

func (s Square) Perimeter() float64 {
	return float64(s * 4.0)
}
func (s Square) NumberOfSide() int {
	return 4
}

func ex51() {
	var s Polygons = Square(5.0)
	fmt.Println(s.Perimeter())
	var t = s.(Object) // 타입캐스팅
	fmt.Println(t.NumberOfSide())
}

type Printer interface {
	Print()
}
type Empl struct {
	// Go에서 필드명이 소문자면 private / 대문자면 public
	name, address string
}

func (e *Empl) Print() {
	fmt.Printf("Name: %s\nAddress: %s\n", e.name, e.address)
}
func (e *Empl) Assign(n, a string) {
	e.name = n
	e.address = a
}
func ex52() {
	var e Empl
	e.Assign("John", "longlonglonglonfognlonglonglno glnoglnog")
	var p Printer
	p = &e
	p.Print()
}

func ex53() {
	var vary interface{} // 빈 인터페이스는 모든 유형의 데이터를 담을 수 있음
	vary = 123
	spew.Dump(vary)
	vary = map[string]int{"Mark": 10, "Jane": 20}
	spew.Dump(vary)
	vary = [3]string{"Korea", "Japan", "China"}
	spew.Dump(vary)
}

// 고루틴 - 동시에 함수가 실행될 수 있도록 도와주는 유용한 방법
func sum(start, end int) {
	s := 0
	for i := start; i <= end; i++ {
		s += i
	}
	fmt.Printf("sum(%d ~ %d) = %d\n", start, end, s)
}

func ex54() {
	startTime := time.Now().UnixMilli()
	sum(1234567, 3456789012)
	sum(1234568, 3456789012)
	sum(1234569, 3456789012)
	sum(1234560, 3456789012)
	sum(1234561, 3456789012)
	fmt.Printf("Elasped Time: %dms\n", time.Now().UnixMilli()-startTime) // 5426ms%
}
func ex55() {
	startTime := time.Now().UnixMilli()
	go sum(1234567, 3456789012)
	go sum(1234568, 3456789012)
	go sum(1234569, 3456789012)
	go sum(1234560, 3456789012)
	go sum(1234561, 3456789012)
	time.Sleep(2 * time.Second)
	fmt.Printf("Elasped Time: %dms\n", time.Now().UnixMilli()-startTime) // 2002ms
}

var wg sync.WaitGroup // waitGroup 선언
func sumwg(start, end int) {
	defer wg.Done() // 하나의 작업 끝날 때 마다 호출
	s := 0
	for i := start; i <= end; i++ {
		s += i
	}
	fmt.Printf("sum(%d ~ %d) = %d\n", start, end, s)
}
func ex56() {
	startTime := time.Now().UnixMilli()
	wg.Add(5) // 5개의 작업 처리
	go sumwg(1234567, 3456789012)
	go sumwg(1234568, 3456789012)
	go sumwg(1234569, 3456789012)
	go sumwg(1234560, 3456789012)
	go sumwg(1234561, 3456789012)
	wg.Wait()                                                            // 작업 끝나기를 기다림
	fmt.Printf("Elasped Time: %dms\n", time.Now().UnixMilli()-startTime) // 1157ms
}

// atomic - lock, unlock을 편하게 해줌
func sumatomic(start, end int, sum *uint64, wg *sync.WaitGroup) {
	defer wg.Done() // 하나의 작업 끝날 때 마다 호출
	s := 0
	for i := start; i <= end; i++ {
		s += i
	}
	atomic.AddUint64(sum, uint64(s)) // var uint64 변수 sum에 s만큼을 더해줌
}

func ex57() {
	var s = uint64(0)
	var wg sync.WaitGroup
	wg.Add(5) // 5개의 작업 처리
	go sumatomic(1, 100000000, &s, &wg)
	go sumatomic(100000001, 200000000, &s, &wg)
	go sumatomic(200000001, 300000000, &s, &wg)
	go sumatomic(300000001, 400000000, &s, &wg)
	go sumatomic(400000001, 500000000, &s, &wg)
	wg.Wait() // 작업 끝나기를 기다림
	fmt.Println(atomic.LoadUint64(&s))
}

// 채널 - Go언어에서 스레드끼리 통신하기 위해 만들어놓은 기능
func ex58() {
	finished := make(chan bool) // 채널 생성
	go func() {
		fmt.Println("Hello world")
		finished <- true // 채널에 데이터 전송
	}()
	<-finished // 채널에서 데이터 받을 때 까지 block
	println("Program Ended")
}

// bufferd 채널 -> 채널이 다 찰 때 까지 block걸리지 않음
func ex59() {
	n := 10
	c := make(chan int, n) // 10개의 bufferd 채널생성
	go func() {
		x, y := 0, 1
		for i := 0; i < n; i++ {
			c <- x // 채널에 피보나치 수열 보냄
			x, y = y, x+y
		}
		close(c) // 연산 끝난 후 채널을 닫음
	}()
	for i := range c { // 10개의 채널에서 하나씩 꺼내옴
		fmt.Println(i)
	}
}
