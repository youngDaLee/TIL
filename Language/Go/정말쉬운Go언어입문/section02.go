package main

import (
	"fmt"
	"strings"
)

func ex20() {
	a, b := 4, 3
	if a > b {
		println("크다")
	} else {
		println("작다")
	}
}

func ex21() {
	age := 19
	if age < 10 {
		println("10대 이하")
	} else if age < 20 {
		println("10대")
	} else if age < 30 {
		println("30대")
	} else if age < 40 {
		println("40대")
	} else {
		println("40대 이상")
	}
}

func ex22() {
	x := 3
	if x%4 == 1 {
		fmt.Println("나머지는 1 입니다")
	} else if x%4 == 2 || x%4 == 3 {
		fmt.Println("나머지는 2 또는 3 입니다")
	} else {
		fmt.Println("나머지는 0 입니다")
	}
}

func ex23() {
	age := 19
	switch {
	case age < 10:
		println("10대 이하")
	case age < 20:
		println("10대")
	case age < 30:
		println("30대")
	case age < 40:
		println("40대")
	default:
		println("40대 이상")
	}
}

func ex24() {
	sum := 0
	for i := 1; i < 200; i += 2 {
		sum += i
	}
	println(sum)
}

func ex25() {
	// go의 for는 조건식만 넣어 사용 가능 -> 다른 언어 while처럼 사용
	sum, i := 0, 1
	for i < 200 {
		sum += i
		i += 2
	}
	println(sum)
}

func ex25_2() {
	// go의 for는 조건식만 없이도 사용 가능 -> 다른 언어 while 무한루프 처럼 사용 가능
	sum, i := 0, 1
	for {
		if i > 200 {
			break
		}
		sum += i
		i += 2
	}
	println(sum)
}

func ex26() {
	// 배열 -> 원소 개수 지정되어 있음
	// var greetings [4]string;
	greetings := [...]string{"good morning", "good afternoon", "good evening", "good night"}
	for i := 0; i < 4; i++ {
		println(greetings[i])
	}
}

func ex27() {
	// 슬라이스 -> 원소 개수 정해져있지 않음
	numbers := []int{}
	sum := 0
	for i := 100; i <= 120; i++ {
		numbers = append(numbers, i)
		sum += i
	}
	println(sum)
}

func ex28() {
	// 슬라이싱 : 배열 자르는거
	alphabet := []string{"a", "b", "c", "d", "e"}
	print(alphabet[:2])
}

func ex29() {
	myArray := [2][3]int{
		{1, 2, 3},
		{4, 5, 6},
	}

	sum := 0
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			sum += myArray[i][j]
		}
	}
	println(sum)
}

// 배열과 슬라이스 복사
// 배열 : 복사 시에 새로 생성하여 붙여넣음... 주소가 다르게 생성됨
// 슬라이스 : 주소를 복사함

func ex30() {
	// 맵-> key-value 자료구조
	// data := make(map[string]int)
	fruites := map[string]int{"apple": 1000, "banana": 3000}

	sum := 0
	for key, val := range fruites {
		fmt.Printf("%s: %d\n", key, val)
		sum += val
	}
	println(sum)
}

func ex31(x int, y int) {
	println(x + y)
}

func ex32(x, y int) {
	println(x + y)
	println(x - y)
	println(x * y)
	println(x / y)
}

func ex33() {
	// Pass By Reference : 주소를 넘겨주는 것 -> 주소를 넘겨주기 때문에 데이터 값이 변경될 수 있다..
	// Pass By Value : 값을 넘겨주는 것 -> 값이 복사되어 복사
	num, str := 4, "hello"
	println(num, ":", str)
	change(&num, &str)
	println(num, ":", str)
}

func change(n *int, s *string) {
	*n *= 2
	*s += " word"
}

func ex34() {
	// 패키지 : 코드를 재사용하기 위한 매커니즘
	// 내장패키지 -> Go 설치할 때 GOROOT 에 설치되는 패키지
	println(strings.Contains("seefood", "foo"))
	println(strings.Contains("seefood", "bar"))
}

func main() {
	ex34()
}
