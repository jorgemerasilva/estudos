package main

import "fmt"

func main() {
	//Declarando um array de inteiros com 5 posições
	var myArray [5]int
	myArray[0] = 10
	myArray[1] = 20
	myArray[2] = 30
	myArray[3] = 40
	myArray[4] = 50

	//Imprimir a ultima posição do array
	fmt.Println("Última posição do array:", myArray[len(myArray)-1])

	//Imprimir o tamanho do array
	fmt.Println("Tamanho do array:", len(myArray))

	//Imprimir valor da primeira posição do array
	fmt.Println("Valor da primeira posição do array:", myArray[0])

	//Imprimir valor da segunda posição do array
	fmt.Println("Valor da segunda posição do array:", myArray[1])

	//Imprimir valor da terceira posição do array
	fmt.Println("Valor da terceira posição do array:", myArray[2])

	//Imprimindo todos os valores do array usando um loop for
	for i, v := range myArray {
		fmt.Printf("Posição %d: %d\n", i, v)
	}

}
