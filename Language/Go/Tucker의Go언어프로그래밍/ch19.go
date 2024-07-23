/*
ch19. 메서드

메서드 필요성
* 해당 타입/구조체에 속한 기능으로 묶을 수 있다.
* 응집도를 높혀주는 역할
*/
package main

import "fmt"

type account struct {
	balance int
}

// 리시버(a *account)로 메서드 표현 && 포인터 메서드
func (a *account) withdrawMethod(amount int) {
	a.balance -= amount
}

// 리시버(a *account)로 메서드 표현 && 값타입 메서드
func (a account) withdrawMethodValue(amount int) {
	a.balance -= amount
}

// 리시버(a *account)로 메서드 표현 && 값타입 메서드 && 변경된 값 반환
func (a account) withdrawMethodValueReturn(amount int) account {
	a.balance -= amount
	return a
}

// 일반 함수 표현
func withdrawFunc(a *account, amount int) {
	a.balance -= amount
}

func exAccount() {
	a := &account{100}

	withdrawFunc(a, 30)
	a.withdrawMethod(30)

	fmt.Printf("%d \n", a.balance)
}

func exAccount2() {
	a := &account{100}

	a.withdrawMethod(30)
	fmt.Printf("%d \n", a.balance) // 70

	a.withdrawMethodValue(30)
	fmt.Printf("%d \n", a.balance) // 70

	b := a.withdrawMethodValueReturn(30)
	fmt.Printf("%d \n", b.balance) // 40

	b.withdrawMethod(30)
	fmt.Printf("%d \n", b.balance) // 10
}
