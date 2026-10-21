package main

import "fmt"

func main() {

	//Soma
	fmt.Println(sum(254, 102, 588, 456, 789, 1000, 2000, 3000, 4000, 5000))

	//Soma com função anônima
	total := func() int {
		return sum(10, 20, 30, 40, 50)
	}()
	fmt.Printf("O total da soma é: %d\n", total)
}

func sum(numeros ...int) int {
	total := 0
	for _, numero := range numeros {
		total += numero
	}
	return total
}
