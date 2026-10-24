package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	//Primeira forma
	f, err := os.Create("arquivo.txt")
	if err != nil {
		panic(err)
	}

	tamanho, err := f.WriteString("Hello, world!")
	if err != nil {
		panic(err)
	}
	fmt.Printf("\nArquivo criado com sucesso!\nTamanho: %d Bytes\n", tamanho)

	f.Close()

	//Segunda forma
	file, err := os.Create("arquivo02.txt")
	if err != nil {
		panic(err)
	}

	tamanho02, err := file.Write([]byte("Escrevendo dados no arquivo"))
	if err != nil {
		panic(err)
	}
	fmt.Printf("\nArquivo criado com sucesso!\nTamanho: %d Bytes\n", tamanho02)

	f.Close()

	//Leitura de arquivos
	arquivo03, err := os.ReadFile("arquivo.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(string(arquivo03))

	//Leitura de pouco em pouco abrindo o arquivo
	arquivo04, err := os.Open("arquivo04.txt")
	if err != nil {
		panic(err)
	}

	reader := bufio.NewReader(arquivo04)
	buffer := make([]byte, 30)
	for {
		n, err := reader.Read(buffer)
		if err != nil {
			break
		}
		fmt.Println(string(buffer[:n]))
	}

	//Excluir arquivo
	err = os.Remove("arquivo.txt")
	if err != nil {
		panic(err)
	}
}
