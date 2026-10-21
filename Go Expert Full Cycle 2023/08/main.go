package main

import (
	"errors"
	"fmt"
)

func main() {
	//Soma
	fmt.Println(sum(1, 2))

	//Divisão
	result, err := dividir(10, 2)
	if err != nil {
		fmt.Println("Erro:", err)
	} else {
		fmt.Println("Resultado da divisão:", result)
	}

	//Subtração
	result, ok := subtrair(5, 3)
	if ok {
		fmt.Println("Resultado da subtração:", result)
	} else {
		fmt.Println("Não é possível subtrair, o primeiro número é menor que o segundo.")
	}

	//Potenciação
	result, err = potencia(5, 3)
	if err != nil {
		fmt.Println("Erro:", err)
	} else {
		fmt.Println("Resultado da potenciação:", result)
	}

}

// Função de soma que retorna apenas o resultado da operação
func sum(a int, b int) int {
	return a + b
}

// Divisão com retorno de dois valores, o resultado e um erro caso a divisão seja inválida
func dividir(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("não é possível dividir por zero")
	}
	return a / b, nil
}

// Subtração com retorno de dois valores, o resultado e um booleano indicando se a operação foi bem sucedida
func subtrair(a, b int) (int, bool) {
	if a < b {
		return 0, false
	}
	return a - b, true
}

// Potenciação com retorno de dois valores, o resultado e um booleano indicando se a operação foi bem sucedida
func potencia(a, b int) (int, error) {
	if b < 0 {
		return 0, errors.New("não é possível calcular a potência com expoente negativo")
	}
	result := 1
	for i := 0; i < b; i++ {
		result *= a
	}
	return result, nil
}
