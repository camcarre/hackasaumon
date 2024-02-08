package main

import (
	"fmt"
	"net/http"
	"text/template"
	"os"
	
	"strings"
)

type Page struct {
	Api     string
	Url     []Site
	Fichier []string
}

type Site struct {
	Adresse string
	Nom     string
}

const port = ":8090"

var page = Page{
	Api: "",
	Url: []Site{},
	Fichier: []string{},
}

var templates = template.Must(template.ParseFiles("html/index.html"))

func main() {


	http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.Dir("css"))))

	fmt.Println("(http://localhost:8090) Server is running on port", port)
	http.HandleFunc("/", Home)
	http.ListenAndServe(port, nil)



}
func Home(w http.ResponseWriter, r *http.Request) {
	InitApi()
	templates.Execute(w, page)
}

func displayFileContents(filePath string) ([]string, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	words := strings.Fields(string(content))
	return words, nil
}

func InitApi() {
	var err error
	page.Api, err = openFiles("api.txt")
	if err != nil {
		fmt.Println("Erreur :", err)
		return
	}
}

func openFiles(filepath string) (string, error) {
	text, err := os.ReadFile(filepath)
	if err != nil {
		fmt.Println("Error:", err)
		return "", err
	}
	return string(text), nil
}