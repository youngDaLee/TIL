/*
ch08. 상수
변수는 var, 상수는 const
*/
package main

func ConstEx() {
	// iota 열거값
	// iot는 0부터 시작해서 1씩 증가하는값. 소괄호 벗어나면 초기화
	const (
		Red   int = iota // 0
		Blue  int = iota // 1
		Green int = iota // 2
	)

	// 첫번재 값과 같은 규칙 적용되면 색략 가능
	const (
		C1 uint = iota + 1 // 1 = 0 + 1
		C2                 // 2 = 1 + 1
		C3                 // 3 = 2 + 1
	)
	const (
		BitFlag1 uint = 1 << iota // 1 = 1 << 0
		BitFlag2                  // 2 = 1 << 1
		BitFlag3                  // 4 = 1 << 2
	)

	// 타입 없는 상수 -> 타입 정해지지 않음 채 사용됨
	const PI = 3.14 // 타입없는 상수
	const FloatPI float64 = 3.14

	// var a int = PI * 100      // 오류X
	// var b int = FloatPI * 100 // 오류 발생
}
