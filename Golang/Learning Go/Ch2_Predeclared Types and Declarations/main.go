package main

import "fmt"

func main() {
	fmt.Println("Exercise 1")
	var i int = 20
	var f = float64(i)
	fmt.Println(i)
	fmt.Println(f)

	fmt.Println("Exercise 2")
	const value = 10
	z := value
	var y float64 = value
	fmt.Println(z)
	fmt.Println(y)

	fmt.Println("Exercise 3")
	var b byte = 255
	b += 2
	fmt.Println(b)
}
