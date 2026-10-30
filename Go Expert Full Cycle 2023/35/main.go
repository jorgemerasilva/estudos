package main

import (
	"bytes"
	"io"
	"net/http"
	"os"
)

func main() {
	c := http.Client{}
	jsoVar := bytes.NewBuffer([]byte(`{"name": "jorge"}`))
	resp, err := c.Post("http://google.com", "application/json", jsoVar)
	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	// body, err := io.ReadAll(resp.Body)
	// if err != nil {
	// 	panic(err)
	// }
	// println(string(body))

	io.CopyBuffer(os.Stdout, resp.Body, nil)
}
