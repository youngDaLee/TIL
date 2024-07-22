package main

import "goproject/numbergame/game"

func main() {
	num := game.GetRandNum()
	game.NumberGame(num)
}
