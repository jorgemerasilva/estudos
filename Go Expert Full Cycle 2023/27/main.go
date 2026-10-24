package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

type ViaCEP struct {
	Cep         string `json:"cep"`
	Logradouro  string `json:"logradouro"`
	Complemento string `json:"complemento"`
	Unidade     string `json:"unidade"`
	Bairro      string `json:"bairro"`
	Localidade  string `json:"localidade"`
	Uf          string `json:"uf"`
	Estado      string `json:"estado"`
	Regiao      string `json:"regiao"`
	Ibge        string `json:"ibge"`
	Gia         string `json:"gia"`
	Ddd         string `json:"ddd"`
}

func main() {
	log.Println("Servidor rodando na porta 8080")
	mux := http.NewServeMux()
	mux.HandleFunc("/", BuscaCepHandler)
	http.ListenAndServe(":8080", mux)
}

func BuscaCepHandler(w http.ResponseWriter, r *http.Request) {

	log.Println("Método:", r.Method)
	log.Println("URL:", r.URL.Path)
	log.Println("Host:", r.Host)
	log.Println("IP:", r.RemoteAddr)
	log.Println("User-Agent:", r.UserAgent())

	if r.URL.Path != "/" {
		w.WriteHeader(http.StatusNotFound)
		return
	}

	cepParam := r.URL.Query().Get("cep")
	if cepParam == "" {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	cep, error := BuscaCep(cepParam)
	if error != nil {
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	//Primeira forma de resposta
	//json.NewEncoder(w).Encode(cep)

	//Segunda forma de resposta
	result, err := json.Marshal(cep)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	w.Write(result)
}

func BuscaCep(cep string) (*ViaCEP, error) {

	resp, error := http.Get("http://viacep.com.br/ws/" + cep + "/json/")
	if error != nil {
		return nil, error
	}

	defer resp.Body.Close()

	body, error := io.ReadAll(resp.Body)
	if error != nil {
		return nil, error
	}
	var c ViaCEP
	error = json.Unmarshal(body, &c)
	if error != nil {
		return nil, error
	}

	return &c, nil

}
