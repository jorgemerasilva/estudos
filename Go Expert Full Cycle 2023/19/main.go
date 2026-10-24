package main

import (
	"fmt"

	"github.com/google/uuid"
	"github.com/testes/matematica"
)

func main() {
	result := matematica.Soma(20, 30, 40, 50, 60, 70, 80, 90, 100)
	fmt.Println(result)

	//Gerando UUID
	fmt.Println(uuid.New())
}
