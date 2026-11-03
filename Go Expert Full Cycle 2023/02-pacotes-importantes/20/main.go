package main

func main() {
	//For 01
	for i := 0; i < 10; i++ {
		println(i)
	}

	//For 02
	numeros := []string{"um", "dois", "três"}
	for k, v := range numeros {
		println(k, v)
	}

	//For 03 - Esse o while em outras linguagens

	i := 1
	for i < 10 {
		println(i)
		i++
	}

	//For infinito

	for {
		println("Loop infinito")
	}

}
