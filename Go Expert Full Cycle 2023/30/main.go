package main

import (
	"html/template"
	"os"
)

type Curso struct {
	Nome         string
	CargaHoraria int
}

func main() {
	curso := Curso{"Go", 34}
	tmp := template.New("CursoTemplate")
	tmp, _ = tmp.Parse("Curso: {{.Nome}} - Carga Horária {{.CargaHoraria}}")
	err := tmp.Execute(os.Stdout, curso)
	if err != nil {
		panic(err)
	}
}
