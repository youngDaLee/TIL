package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/davecgh/go-spew/spew"
	"github.com/pkg/errors"
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

func ex35() {
	// 외장패키지
	// go mod init main 으로 패키지 초기화 시켜준 다음에 외장패키지 설치 가능했음
	// mod가 env 같은건가..?
	x := "hello"
	spew.Dump(x)
}

func ex36() {
	// myContains("seafood", "foo")
}

func ex37(str1, str2 string) {
	num1, err := strconv.Atoi(str1)
	if err != nil {
		panic(err)
	}

	num2, err := strconv.Atoi(str2)
	if err != nil {
		panic(err)
	}

	fmt.Printf("%d / %d = %d\n", num1, num2, num1/num2)
}

func ex38() {
	err := fn()
	fmt.Printf("%+v", err)
}

func fn() error {
	e1 := errors.New("error")
	e2 := errors.Wrap(e1, "inner")
	return errors.Wrap(e2, "outer")
}

func ex39() {
	variadicExample("red")
	variadicExample("red", "green", "yellow")
}

func variadicExample(s ...string) {
	fmt.Printf("%#v\n", s)
}

func ex40(i ...int) {
	// 가변인자는 함수에서 하나만 사용 가능
	// 다른 인자와 섞어 사용할땐 마지막에 사용해야 함
	sum := 0
	for _, num := range i {
		sum += num
	}

	println(sum)
}

// ===== 구조체
type rectangle struct {
	length  float64
	breadth float64
	color   string
	geo     geometry
}

type geometry struct {
	area      int
	perimeter int
}

func ex41() {
	// spew.Dump(rectangle{10.5, 12.5, "red"})
}

func ex42() {
	var rect1 rectangle
	rect1.breadth = 15
	rect1.length = 10
	rect1.geo.area = int(rect1.breadth) * int(rect1.breadth)
	spew.Dump(rect1)

	rect2 := rectangle{10, 20, "Green", geometry{200, 60}}
	spew.Dump(rect2)

	rect3 := rectangle{length: 5, breadth: 10}
	spew.Dump(rect3)

	rect4 := new(rectangle)
	rect4.length = 5
	rect4.breadth = 12
	spew.Dump(rect4)
}

type Student struct {
	Name   string
	Age    int
	Scores []Score
}

type Score struct {
	Subject string
	Score   int
}

func ex43() {
	s1 := Student{
		Name: "Dy",
		Age:  26,
		Scores: []Score{
			Score{
				Subject: "Math",
				Score:   90,
			},
			{
				Subject: "Physics",
				Score:   80,
			},
		},
	}
	spew.Dump(s1)
}

// 메소드 리시버 -> 구조체의 메서드를 정의하는 방법
type rect struct {
	length  float64
	breadth float64
	color   string
}

func (r rect) area() float64 {
	return r.length * r.breadth
}

func (r rect) perimeter() float64 {
	return 2 * (r.breadth + r.length)
}

func ex44() {
	s1 := rect{
		length:  3,
		breadth: 5,
		color:   "blue",
	}
	spew.Dump(s1.area(), s1.perimeter())
}

func ex45() {
	r1 := rect{5, 4, "yellow"}
	r2 := r1  // 복사(주소복사X)
	r3 := &r1 // 주소복사
	r2.color = "blue"
	spew.Dump(r1) // yellow
	r3.color = "magenta"
	spew.Dump(r1) // magenta
}

func main() {
	ex45()
}
