package main

func main() {

	//Verificando idade
	idade := 18
	if idade > 12 && idade < 18 {
		println("Adolescente!")
	} else if idade >= 18 && idade < 60 {
		println("Adulto!")
	} else if idade >= 60 {
		println("Idoso!")
	} else {
		println("Operação invalida!")
	}

	//Verificando cor
	corFavorita := "Azul"
	if corFavorita == "Azul" || corFavorita == "Vermelho" {
		println("Cor favorita é Azul ou Vermelho!")
	} else {
		println("Cor não cadastrada ainda!")
	}

	//Switch
	diaDaSemana := 5
	switch diaDaSemana {
	case 1:
		println("Domingo!")
	case 2:
		println("Segunda")
	case 3:
		println("Terça-feira")
	case 4:
		println("Quarta-feira")
	case 5:
		println("Quinta-feira")
	case 6:
		println("Sexta-feira")
	case 7:
		println("Sábado")
	default:
		println("Dia não indenficado!")
	}
}
