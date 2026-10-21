package matematica

func Soma[T int | float64](numeros ...T) T {
	var total T
	for _, n := range numeros {
		total += n
	}
	return total
}
