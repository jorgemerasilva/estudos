package main

import (
	"html/template"
	"net/http"
)

type Curso struct {
	Nome         string
	CargaHoraria int
}
type Cursos []Curso

func main() {
	templates := []string{
		"header.html",
		"Content.html",
		"footer.html",
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		t := template.Must(template.New("Content.html").ParseFiles(templates...))
		err := t.Execute(w, Cursos{
			{"Go", 30},
			{"mojo", 20},
			{"python", 40},
		})
		if err != nil {
			panic(err)
		}

	})
	http.ListenAndServe(":8080", nil)
}
