package main

import "fmt"

//Type assertion

func main() {
	var x interface{} = "Hello, World!"

	// Type assertion to convert interface{} to string
	str, ok := x.(string)
	if ok {
		fmt.Println("The value is:", str)
	} else {
		fmt.Println("The value is not a string.")
	}
}
