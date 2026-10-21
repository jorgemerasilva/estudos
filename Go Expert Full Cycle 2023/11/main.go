package main

import "fmt"

// Definindo a interface Pagamento
type Pagamento interface {
	Pagar(valor float64)
}

// Implementando a interface Pagamento para Pix
type Pix struct{}

// Implementando a interface Pagamento para Cartao
type Cartao struct{}

// Implementando o método Pagar para Pix
func (p Pix) Pagar(valor float64) {
	fmt.Println("Pagamento via PIX:", valor)
}

// Implementando o método Pagar para Cartao
func (c Cartao) Pagar(valor float64) {
	fmt.Println("Pagamento via cartão:", valor)
}

// Função que recebe a interface Pagamento e chama o método Pagar
func processarPagamento(p Pagamento, valor float64) {
	p.Pagar(valor)
}

func main() {
	// Criando instâncias de Pix e Cartao
	pix := Pix{}
	cartao := Cartao{}

	// Chamando a função processarPagamento com diferentes implementações da interface Pagamento
	processarPagamento(pix, 100.0)
	processarPagamento(cartao, 200.0)
}
