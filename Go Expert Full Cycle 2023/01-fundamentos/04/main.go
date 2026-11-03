package main

import "fmt"

type ID string

var (
	nome      string  = "João"
	sobrenome string  = "Silva"
	age       int     = 30
	altura    float64 = 1.75
	casado    bool    = true
	id        ID      = "12345"
)

func main() {
	fmt.Printf("Nome: %s\n", nome)
	fmt.Printf("Sobrenome: %s\n", sobrenome)
	fmt.Printf("Idade: %d\n", age)
	fmt.Printf("Altura: %.2f\n", altura)
	fmt.Printf("Casado: %t\n", casado)
	fmt.Printf("ID: %s\n", id)

	//Como saber o tipo de uma variável
	fmt.Printf("Tipo de nome: %T\n", nome)
	fmt.Printf("Tipo de sobrenome: %T\n", sobrenome)
	fmt.Printf("Tipo de age: %T\n", age)
	fmt.Printf("Tipo de altura: %T\n", altura)
	fmt.Printf("Tipo de casado: %T\n", casado)
	fmt.Printf("Tipo de id: %T\n", id)
}
