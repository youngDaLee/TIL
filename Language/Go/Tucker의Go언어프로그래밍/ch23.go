/*
ch23. 에러핸들링
*/
package main

import (
	"fmt"
	"math"
)

// 에러 반환
func Sqrt(f float64) (float64, error) {
	if f < 0 {
		// 사용자 에러 반환
		return 0, fmt.Errorf(
			"제곱근은 양수여야 합니다. f:%g", f)
	}
	return math.Sqrt(f), nil
}

// 패닉 -> 프로그램 정상 진행이 어려운 상황에서 프로그램 흐름 중지키는 기능 (일종의 throw?)
func device(a, b int) {
	if b == 0 {
		panic("b는 0일 수 없습니다")
	}
	fmt.Printf("%d / %d = %d\n", a, b, a/b)
}

// 복구 recover 함수가 호출되는 시점에 패닉이 전파중이면 panic 반환하고 그렇지 않으면 nil 반환
func rec(a, b int) {
	fmt.Println("함수 시작")
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("panic 복구 - ", r)
		}
	}()

	device(a, b) // 패닉
	fmt.Println("함수 끝")
}
