package main

import "fmt"

func main() {
	fmt.Println("Hello World")

	var a, b int
	n, err := fmt.Scan(&a, &b)
	if err != nil {
		fmt.Println(n, err)
	} else {
		fmt.Println(n, a, b)
	}
}
