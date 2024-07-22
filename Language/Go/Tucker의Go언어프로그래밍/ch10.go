/*
ch10. switch
*/
package main

import "fmt"

func getAge() {
	// switch {초기식}; 비굣값
	switch age := 22; age {
	case 10:
		fmt.Println("Teenage")
	case 33:
		fmt.Println("pair 3")
	default:
		fmt.Println("my age is ", age)
	}

	// switch 를 if문처럼도 쓸 수 있음
	switch age := 10; true {
	case age < 20:
		fmt.Println("Teenage")
	case age == 33:
		fmt.Println("pair 3")
	default:
		fmt.Println("my age is ", age)
	}

	age := 10
	switch {
	case age < 20:
		fmt.Println("Teenage")
	case age == 33:
		fmt.Println("pair 3")
	default:
		fmt.Println("my age is ", age)
	}
}

// const 열거값과 switch
type ColorType int

const (
	Red ColorType = iota
	Blue
	Green
	Yellow
)

func colorToString(color ColorType) string {
	switch color {
	case Red:
		return "Red"
	case Blue:
		return "Blue"
	case Green:
		return "Green"
	default:
		return "Yellow"

	}
}

// fallthrought
func fallthroughtEx() {
	// 다른 언어와 다르게 case 이후 break을 안해도 switch 빠져나감
	// 하나의case 실행 후 다음 case까지 하고 싶으면 fallthrougt Tjdi gka
	a := 3
	switch a {
	case 1:
		println("a == 1")
	case 2:
		println("a == 2")
	case 3:
		println("a == 3")
		fallthrough
	case 4: // 여기까지 실행됨
		println("a == 4")
	case 5:
		println("a == 5")
	default:
		println("else")
	}
}
