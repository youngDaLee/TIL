/*
패키지 실행 메인

실행 방법
1) 빌드 파일 생성
* go mod init {패키지명}
* go build
* ./{패키지명}

2) 해당 디렉토리 내의 main 패키지의 main 함수 실행
* go run .
*/
package main

import "fmt"

func main() {
	c, success := DivideName(5, 0)
	fmt.Println(c, success)
}
