package main

func soma(a, b *int) int {
	*a = 10
	*b = 20
	return *a + *b
}

func main() {
	a := 200
	b := 100

	resultado := soma(&a, &b)
	println("A soma de", a, "e", b, "é:", resultado)
}
