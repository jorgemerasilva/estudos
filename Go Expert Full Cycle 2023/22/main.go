package main

import (
	"fmt"
)

func main() {
	var nome string
	var idade int
	var altura float64
	var peso float64

	fmt.Println("##########	CALCULAR IMC ###########")
	fmt.Print("Digite seu nome: ")
	fmt.Scanln(&nome)

	fmt.Print("Digite sua idade: ")
	fmt.Scanln(&idade)

	fmt.Print("Digite sua altura: ")
	fmt.Scanln(&altura)

	fmt.Print("Digite seu peso: ")
	fmt.Scanln(&peso)

	fmt.Println("Nome:", nome)
	fmt.Println("Idade:", idade)
	imc := calcularImc(peso, altura)
	fmt.Printf("\nPeso: %.2f\nAltura: %.2f\nIMC: %.2f\n", peso, altura, imc)

}

func calcularImc(peso, altura float64) float64 {
	imc := peso / (altura * altura)
	return imc
}
