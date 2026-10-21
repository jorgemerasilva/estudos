package main

import "fmt"

type Conta struct {
	Numero  int
	Titular string
	Saldo   float64
	Ativa   bool
}

//func NewConta() *Conta {
//return &Conta{
//Numero:  0,
//Titular: "",
//Saldo:   0.0,
//Ativa:   false,
//}
//}

func (c *Conta) Depositar(valor float64) {
	if c.Ativa {
		c.Saldo += valor
	}
}

func (c *Conta) Sacar(valor float64) bool {
	if c.Ativa && c.Saldo >= valor {
		c.Saldo -= valor
		return true
	}
	return false
}

func (c *Conta) Extrato() string {
	if c.Ativa {
		return "Conta ativa. Saldo: " + fmt.Sprintf("%.2f", c.Saldo)
	}
	return "Conta inativa."
}

func main() {
	conta := Conta{
		Numero:  12345,
		Titular: "João",
		Saldo:   1000.0,
		Ativa:   true,
	}
	println(conta.Extrato())

	conta.Depositar(500.0)
	println(conta.Extrato())

	conta.Sacar(200.0)
	println(conta.Extrato())
}
