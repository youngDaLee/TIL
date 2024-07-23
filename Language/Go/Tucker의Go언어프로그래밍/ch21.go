/*
ch21. 함수 고급 기능
*/
package main

import (
	"fmt"
	"os"
)

// 가변 인수 함수
func sum(nums ...int) int {
	sum := 0
	for _, v := range nums {
		sum += v
	}
	return sum
}

// defer 지연 실행 -> OS 내부 자원을 사용하여 함수 종료 직전 반드시 실행되어야 하는 코드에 유용
func exDefer() {
	f, err := os.Create("test.txt")
	if err != nil {
		fmt.Println("Failed to create a file")
	}

	defer fmt.Println("반드시 호출됨")
	defer f.Close()
	defer fmt.Println("파일 닫음")

	println("파일에 Hello World 작성")
	fmt.Fprintln(f, "Hello World")
}

// 함수 타입 변수
func add(a, b int) int {
	return a + b
}
func mul(a, b int) int {
	return a * b
}

func getOperator(op string) func(int, int) int {
	switch op {
	case "+":
		return add
	case "*":
		return mul
	default:
		return nil
	}
}

func funcTypeEx() {
	var operator func(int, int) int
	operator = getOperator("+")

	res := operator(3, 4)
	println(res)
}

// 함수 리터럴 - 이름없는 함수. 익명함수. 자바에서의 람다...
type opFunc func(a, b int) int

func getOperatorWithLiteral(op string) opFunc {
	switch op {
	case "+":
		return func(a, b int) int {
			return a + b
		}
	case "*":
		return func(a, b int) int {
			return a * b
		}
	default:
		return nil
	}
}
