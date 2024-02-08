package main

import (
	"fmt"
	"net/http"
	"text/template"
	
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

var templates = template.Must(template.ParseFiles("index.html"))

func main() {
	http.HandleFunc("/", Home)

	http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.Dir("/css"))))

	fmt.Println("(http://localhost:8090) Server is running on port", port)

	http.ListenAndServe(port, nil)



}
func Home(w http.ResponseWriter, r *http.Request) {

	templates.ExecuteTemplate(w, "index.html", nil)
}
