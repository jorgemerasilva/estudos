package main

import "fmt"

type MyNumber int

type Number interface {
	~int | ~float64
}

//Função que soma floats
func Soma(m map[string]float64) float64 {
	var total float64
	for _, v := range m {
		total += v
	}
	return total
}

//Generics
func SomaM2[T int | float64](m map[string]T) T {
	var total T
	for _, v := range m {
		total += v
	}
	return total
}

func SomaM3[T Number](m map[string]T) T {
	var total T
	for _, v := range m {
		total += v
	}
	return total
}

func main() {
	m := map[string]float64{
		"jorge": 3000.0,
		"maria": 2500.0,
		"joao":  1500.0,
	}

	m2 := map[string]float64{
		"jorge": 3000,
		"maria": 2500,
		"joao":  1500,
		"ana":   2000,
	}

	m3 := map[string]MyNumber{
		"jorge": 3000,
		"maria": 2500,
		"joao":  1500,
		"ana":   2000,
	}

	fmt.Println(Soma(m))
	fmt.Println(SomaM2(m2))
	fmt.Println(SomaM3(m3))
}
