package main

// Constantes
const keyApi = "sk-adsnabdiqbifbqf"

// Variáveis globais
var (
	b bool = true
	c string
	f int64
	a float64
)

func main() {
	//Variáveis locais
	var nome string = "Kaylanne"

	//Variáveis locais com inferência de tipo
	idade := 20
	sobrenome := "Merá"

	//Imprimindo na tela
	println("Meu nome é", nome, sobrenome, "e tenho", idade, "anos.")

	c = "python"
	f = 20
	a = 90.90
	println(c, f, a, b)

	println(keyApi)

}
