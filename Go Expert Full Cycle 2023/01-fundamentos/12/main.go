package main

import (
	"errors"
	"fmt"
)

type Funcionario struct {
	ID           int
	NomeCompleto string
	CPF          string
	Email        string
	Cargo        string
	Salario      float64
	Ativo        bool
}

type Empresa struct {
	ID           int
	Nome         string
	CNPJ         string
	Rua          string
	Numero       int
	Cidade       string
	Estado       string
	Pais         string
	Ativo        bool
	Funcionarios []Funcionario
}

type Desativavel interface {
	Desativar()
}

func (e *Empresa) Desativar() {
	e.Ativo = false
	fmt.Println("Empresa desativada:", e.Nome)
}

func (f *Funcionario) Desativar() {
	f.Ativo = false
	fmt.Println("Funcionário desativado:", f.NomeCompleto)
}

func Desativar(item Desativavel) {
	item.Desativar()
}

func (e *Empresa) BuscarFuncionarioPorID(id int) (*Funcionario, error) {
	for i := range e.Funcionarios {
		if e.Funcionarios[i].ID == id {
			return &e.Funcionarios[i], nil
		}
	}

	return nil, errors.New("funcionário não encontrado")
}

func (e *Empresa) DesativarFuncionarioPorID(id int) error {
	funcionario, err := e.BuscarFuncionarioPorID(id)

	if err != nil {
		return err
	}

	Desativar(funcionario)

	return nil
}

func main() {
	empresa1 := Empresa{
		ID:     1,
		Nome:   "Empresa Exemplo",
		CNPJ:   "12.345.678/0001-90",
		Rua:    "Rua Exemplo",
		Numero: 123,
		Cidade: "São Paulo",
		Estado: "SP",
		Pais:   "Brasil",
		Ativo:  true,

		Funcionarios: []Funcionario{
			{
				ID:           1,
				NomeCompleto: "João da Silva",
				CPF:          "123.456.789-00",
				Email:        "joao@gmail.com",
				Cargo:        "Desenvolvedor",
				Salario:      5000,
				Ativo:        true,
			},
			{
				ID:           2,
				NomeCompleto: "Maria Souza",
				CPF:          "987.654.321-00",
				Email:        "maria@gmail.com",
				Cargo:        "Analista de Marketing",
				Salario:      4000,
				Ativo:        true,
			},
		},
	}

	fmt.Println("ANTES:")

	fmt.Println(
		"Empresa:",
		empresa1.Nome,
		"Ativa:",
		empresa1.Ativo,
	)

	for _, funcionario := range empresa1.Funcionarios {
		fmt.Println(
			funcionario.ID,
			funcionario.NomeCompleto,
			"Ativo:",
			funcionario.Ativo,
		)
	}

	fmt.Println()

	err := empresa1.DesativarFuncionarioPorID(2)

	if err != nil {
		fmt.Println("Erro:", err)
	}

	fmt.Println()
	fmt.Println("DEPOIS:")

	for _, funcionario := range empresa1.Funcionarios {
		fmt.Println(
			funcionario.ID,
			funcionario.NomeCompleto,
			"Ativo:",
			funcionario.Ativo,
		)
	}

	fmt.Println()

	Desativar(&empresa1)

	fmt.Println(
		"Empresa:",
		empresa1.Nome,
		"Ativa:",
		empresa1.Ativo,
	)
}
