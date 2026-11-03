package main

func main() {

	a := 10

	//Imprimir valor de a
	println(a)

	//Imprimir o endereço de memória de a
	println(&a)

	b := 50
	var ponteiro *int = &b
	*ponteiro = 100

	//Imprimir valor de b
	println(b)

	//Imprimir o valor do ponteiro
	c := 200
	//Apontando para o endereço de memória de c
	d := &c
	//Imprimir o valor de c através do ponteiro d
	println(*d)

	//Alterando o valor de c através do ponteiro d
	*d = 300
	//Imprimir o valor de c após a alteração
	println(c)

}
