/*
ch10.for
*/
package main

// 무한루프
func infinity() {
	i := 0
	for {
		i++
		if i > 10 {
			break
		}
	}
	// go 에는 while이 없는 대신 for를 while 처럼 사용 가능하다
	for i < 10 {
		i++
	}

	// 배열의 range 순회
	var t [5]int = [5]int{1, 2, 3, 4, 5}
	for i, v := range t {
		println(i, v) // index, value
	}
}
