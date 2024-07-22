/*
ch07. 함수
*/
package main

// 멀티반환 함수
func Divide(a, b int) (int, bool) {
	if b == 0 {
		return 0, false
	}
	return a / b, true
}

// 변수명을 저장해 반환
func DivideName(a, b int) (result int, success bool) {
	if b == 0 {
		result = 0
		success = false
		return
	}
	result = a / b
	success = true
	return
}
