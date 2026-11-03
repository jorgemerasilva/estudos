package main

import "fmt"

//Interfaces vazias

func main() {
	var x interface{} = 5          //interface vazia
	var y interface{} = "Olá, Go!" //interface vazia
	showType(x)
	showType(y)
}
func showType(t interface{}) {
	fmt.Printf("O tipo de t é: %T\nO valor de t é: %v\n", t, t)
}
