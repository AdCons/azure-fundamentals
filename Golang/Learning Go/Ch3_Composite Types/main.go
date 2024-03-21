package main

import (
	"fmt"
)

type Employee struct {
	firstName string
	lastName  string
	id        int
}

func main() {
	fmt.Println("Exercise 1")
	greetings := []string{"Hello", "Hola", "नमस्कार", "こんにちは", "Привіт"}
	xSlice1 := greetings[:2]
	xSlice2 := greetings[1:4]
	xSlice3 := greetings[3:]
	fmt.Printf("Greetings: %v\n", greetings)
	fmt.Printf("xSlice1: %v\n", xSlice1)
	fmt.Printf("xSlice2: %v\n", xSlice2)
	fmt.Printf("xSlice3: %v\n", xSlice3)

	fmt.Println("\nExercise 2")
	message := []rune("Hi 👧 and 🧑")
	fmt.Println(string(message[3]))

	fmt.Println("\nExercise 3")
	adrian1 := Employee{"adrian", "reload", 777}
	adrian2 := Employee{
		firstName: "adrian",
		lastName:  "reload",
		id:        777,
	}
	var adrian3 Employee
	adrian3.firstName = "adrian"
	adrian3.lastName = "reload"
	adrian3.id = 777

	fmt.Println(adrian1)
	fmt.Println(adrian2)
	fmt.Println(adrian3)
}
