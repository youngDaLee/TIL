/*
ch20. 인터페이스

덕타이핑 -> 인터페이스를 구현하고 있다고 명시하지 않아도 인터페이스를 사용할 수 있게 하는것
*/
package main

import (
	"fmt"
)

type Stringer interface {
	String() string
}

type Student struct {
	Name string
	Age  int
}

func (s Student) String() string {
	return fmt.Sprintf("안녕 나는 %d살 %s라고 해", s.Age, s.Name)
}

func exInterface() {
	student := Student{"철수", 12}
	var stringer Stringer

	stringer = student
	fmt.Printf("%s\n", stringer.String())
}

// 인터페이스를 포함하는 인터페이스
type Reader interface {
	Read() (n int, err error)
	Close() error
}
type Writer interface {
	Write() (n int, err error)
	Close() error
}

// Read() Write() Close() 메서드를 갖는 인터페이스
type ReadWrite interface {
	Reader
	Writer
}

// 빈 인터페이스를 파라미터로 받는 함수
func PrintVal(v interface{}) {
	switch t := v.(type) {
	case int:
		fmt.Printf("v is int %d\n", int(t))
	case float64:
		fmt.Printf("v is float %f\n", float64(t))
	case string:
		fmt.Printf("v is float %s\n", string(t))
	default:
		fmt.Printf("Not supported type: %T:%v\n", t, t)
	}
}

func exInterface2() {
	PrintVal(10)
	PrintVal(3.14)
	PrintVal("hello")
	PrintVal(Student{"영희", 10})
}
