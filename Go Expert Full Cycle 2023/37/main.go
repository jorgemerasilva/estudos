package main

import (
	"context"
	"io"
	"net/http"
)

func main() {
	ctx := context.Background()
	//Cancelar depois de 1 segundo ou ate cancelar
	// ctx, cancel := context.WithTimeout(ctx, time.Second)

	//Cancelar apenas
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	req, err := http.NewRequestWithContext(ctx, "GET", "http://google.com", nil)
	if err != nil {
		panic(err)
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}

	println(string(body))
}
