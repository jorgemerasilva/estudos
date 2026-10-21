package main

import "fmt"

type Endereco struct {
	Rua    string
	Numero int
	Cidade string
	Estado string
	Pais   string
}

type Pessoa interface {
	Desativar()
}

type Cliente struct {
	Nome      string
	Sobrenome string
	Idade     int
	Altura    float64
	Email     string
	Senha     string
	Ativo     bool
	Endereco  Endereco
}

func (c Cliente) Desativar() {
	c.Ativo = false
	fmt.Println("Cliente desativado:", c.Nome)
}

func DesativarPessoa(pessoa Pessoa) {
	pessoa.Desativar()
}

func main() {

	jorge := Cliente{
		Nome:      "Jorge",
		Sobrenome: "Silva",
		Idade:     30,
		Altura:    1.75,
		Email:     "jorge@gmail.com",
		Senha:     "123456",
		Ativo:     true,
		Endereco: Endereco{
			Rua:    "Rua Exemplo",
			Numero: 123,
			Cidade: "São Paulo",
			Estado: "SP",
			Pais:   "Brasil",
		},
	}

	DesativarPessoa(jorge) // Chamando a função para desativar o cliente

	jorge.Endereco.Numero = 456 // Alterando o número do endereço

	fmt.Printf("Pessoa: %s %s, Idade: %d, Altura: %.2f\n", jorge.Nome, jorge.Sobrenome, jorge.Idade, jorge.Altura)
	fmt.Printf("Email: %s, Senha: %s\n", jorge.Email, jorge.Senha)
	fmt.Printf("Ativo: %t\n", jorge.Ativo)
	fmt.Printf("Endereço: %s, Número: %d, Cidade: %s, Estado: %s, País: %s\n", jorge.Endereco.Rua, jorge.Endereco.Numero, jorge.Endereco.Cidade, jorge.Endereco.Estado, jorge.Endereco.Pais)
}
