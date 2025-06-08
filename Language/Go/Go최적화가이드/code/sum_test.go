// sum_test.go
package main

import "testing"

func TestSum(t *testing.T) {
	ret, _ := Sum("sumtest.txt")
	print("Sum: ", ret, "\n")
}
