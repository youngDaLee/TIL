/*
ch22. 자료구조
*/
package main

import (
	"container/list"
	"container/ring"
	"fmt"
)

// 리스트
func listEx() {
	v := list.New()
	e4 := v.PushBack(4)   // 뒤에 요소 추가
	e1 := v.PushFront(1)  // 앞에 요소 추가
	v.InsertBefore(3, e4) // 요소 앞에 요소 삽입
	v.InsertAfter(2, e1)  // 요소 뒤에 요소 삽입

	for e := v.Front(); e != nil; e = e.Next() { // 요소 순회
		fmt.Print(e.Value, " ")
	}

	for e := v.Back(); e != nil; e = e.Prev() { // 요소 역순 순회
		fmt.Print(e.Value, " ")
	}
}

// 링 -> 저장할 개수가 고정되고 오래된 요소는 지워도 되는 경우에 적합
func ringEx() {
	r := ring.New(5)
	n := r.Len()
	for i := 0; i < n; i++ {
		r.Value = 'A' + i
		r = r.Next()
	}
}

// 맵 - key value 형태
type Product struct {
	Name  string
	Price int
}

func mapEx() {
	m := make(map[string]string)
	m["감사"] = "합니다"

	p := make(map[int]Product)
	p[16] = Product{"볼펜", 500}
}
