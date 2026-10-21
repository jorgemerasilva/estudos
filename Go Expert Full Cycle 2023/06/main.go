package main

import "fmt"

func main() {

	s := []int{20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 158, 160, 165, 170, 175, 180, 185, 190, 195, 200}

	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

	fmt.Printf("len=%d cap=%d %v\n", len(s[1:]), cap(s[1:]), s[1:])

	fmt.Printf("len=%d cap=%d %v\n", len(s[:3]), cap(s[:3]), s[:3])

	fmt.Printf("len=%d cap=%d %v\n", len(s[1:3]), cap(s[1:3]), s[1:3])

	//Adicionando elementos a um slice
	s = append(s, 205)
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)

}
