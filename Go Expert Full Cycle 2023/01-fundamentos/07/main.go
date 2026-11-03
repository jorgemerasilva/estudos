package main

import "fmt"

func main() {
	// Criando um mapa de usuários
	usuarios := map[string]string{
		"João":  "joao@example.com",
		"Maria": "maria@example.com",
		"Pedro": "pedro@example.com",
	}
	fmt.Println(usuarios)

	// Imprimindo o email de um usuário específico
	fmt.Println("Email de João:", usuarios["João"])

	// Adicionando um novo usuário
	usuarios["Ana"] = "ana@example.com"
	fmt.Println(usuarios)

	// Removendo um usuário
	delete(usuarios, "Pedro")
	fmt.Println(usuarios)

	// Verificando se um usuário existe
	email, ok := usuarios["Maria"]
	if ok {
		fmt.Println("Email de Maria:", email)
	} else {
		fmt.Println("Maria não encontrada")
	}

	// Iterando sobre o mapa de usuários
	for nome, email := range usuarios {
		fmt.Printf("Nome: %s, Email: %s\n", nome, email)
	}

	//Ignorando nome e pegando apenas o email com blank identifier
	for _, email := range usuarios {
		fmt.Printf("Email: %s\n", email)
	}

	//Iniciando um mapa vazio
	novoMapa := make(map[string]int)
	novoMapa["um"] = 1
	novoMapa["dois"] = 2
	novoMapa["tres"] = 3

	fmt.Println(novoMapa)

	//Iniciando um mapa vazio com map
	novoMapa2 := map[string]int{}
	novoMapa2["quatro"] = 4
	novoMapa2["cinco"] = 5
	novoMapa2["seis"] = 6

	fmt.Println(novoMapa2)

}
