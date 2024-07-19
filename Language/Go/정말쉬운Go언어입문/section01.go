package main

import (
	"fmt"
	"strconv"
)

func variable() {
	var x int = 1 // Go 정수 선언 기본
	y := 1        // 축약형. 오른쪽 데이터 타입에 따라 바로 변수 선언
	println(x, y)
}

func ex1() {
	println("안녕하세요")
}

func ex2() {
	fmt.Printf("%d\n", 3+5*2)
}

func ex3() {
	x := 5
	y := 2*x + 1
	fmt.Printf("x=%d\ny=%d\n", x, y)
}

// func ex4() {
// 	var x int8 = 200
// 	fmt.Printf("x=%d\n", x+56) // overflow
// 	var y uint8 = -120
// 	fmt.Printf("y=%d\n", y-3) // underflow
// }

func ex6() {
	// string 타입 선언
	x, y := "hello", " world"
	fmt.Println(x + y)
}

func ex7() {
	// byte 타입 선언 (byte=문자)
	var b byte = 'B'
	r := '한'
	fmt.Printf("%s %s\n", string(b), string(r))
}

func ex8() {
	// casting
	var x uint8 = 200
	var y int8 = -100
	var z int = int(x) + int(y)
	println(z)
}

func ex9() {
	var x uint8 = 200
	var y float32 = -100.0
	var z float64 = float64(x) + float64(y)
	println(z)
}

func ex10() {
	// 정수 -> 문자열 / 문자열 -> 정수는 문제가 생길 수 있기 때문에 strconv 패키지 이용
	x := "200"
	println(strconv.Atoi(x)) // 문자열 -> 정수

	y := -100.0
	println(strconv.FormatFloat(y, 'f', -1, 64)) // float63 -> string
}

func ex11() {
	// 논리현 포메팅
	var x bool
	println(x)
	x = true
	println(x)
}

func ex12() {
	// 문자열형 포메팅
	a, b, c, d := "nice", "to", "meet", "you"
	fmt.Printf("%3s %3s %3s %3s", a, b, c, d)
}

func ex13() {
	// 정수형 포메팅 = c랑 똑같음
	x := 31
	fmt.Printf("%b %o %x %d\n", x, x, x, x)
	y := 12
	fmt.Printf("%03d %3d\n", y, y)
}

func ex14() {
	// 실수형 포메팅 = c랑 똑같음
	x := 1234567890.123
	fmt.Printf("%g %f %e\n", x, x, x)
}

func ex15() {
	// %T : 어떤 타입인지 알려줌
	// %v : 알아서 타입 판단해서 출력
	x, y, z := true, "nice", 3.141592
	fmt.Printf("%T: %v\n%T: %v\n%T: %v\n", x, x, y, y, z, z)
}

func ex16() {
	x := 4
	x += 2
	y := 3
	y -= 1
	println(x % y)
}

func ex17() {
	a, b, c, d := 2, 3, 4, 5
	println((b >= a) && !(c < d))
}

func ex18() {
	// 비트연산자
	x, y := 7, 2
	println(x & y)
	println(x | y)
	println(x ^ y)
	println(x << y)
	println(x >> y)
}

func ex19() {
	// 대입 & 포인터 연산자
	x := "hello"
	var y *string
	y = &x // 변수의 주소를 가리키게 됨
	println(x)
	*y = "world"
	println(x)
}

// Go 언어는 모두 main 패키지의 main 함수로부터 시작함. 필수
func main_() {
	ex19()
}
