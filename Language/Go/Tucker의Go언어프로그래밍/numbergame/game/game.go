package game

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"time"
)

func isNumEqual(num, ans int) bool {
	if num < ans {
		fmt.Println("입력하신 숫자가 더 작습니다.")
		return false
	} else if num == ans {
		return true
	} else {
		fmt.Println("입력하신 숫자가 더 큽니다")
		return false
	}
}

func NumberGame(ans int) {
	cnt := 1
	for {
		num, err := getNumFromUser()
		if err != nil {
			fmt.Println("숫자만 입력하세요")
			continue
		}
		if isNumEqual(num, ans) {
			fmt.Printf("숫자를 맞췄습니다. 축하합니다. 시도한 횟수: %d\n", cnt)
			break
		}
		cnt++
	}
}

var stdin = bufio.NewReader(os.Stdin)

func getNumFromUser() (int, error) {
	var num int
	fmt.Printf("숫자값을 입력하세요: ")
	_, err := fmt.Scanln(&num)
	if err != nil {
		stdin.ReadString('\n') // 입력스트림 비우기
	}
	return num, err
}

func GetRandNum() int {
	rand.Seed(time.Now().UnixNano())

	n := rand.Intn(100)
	return n
}
