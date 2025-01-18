// 추상 팩토리 인터페이스
package main

import "fmt"

type ISportsFactory interface {
	makeShoe() IShoe
	makeShirt() IShirt
}

func GetSportsFactory(brand string) (ISportsFactory, error) {
	if brand == "adidas" {
		return &Adidas{}, nil
	}
	return nil, fmt.Errorf("wrong brand type passed")
}
