package main

import (
	"fmt"
	"net/http"
	"text/template"
	saumon "hackasaumon/funcGo"

)


const port = ":8080"

var page = saumon.Page {
	Api: "",
	Url: []saumon.Site{},
	Fichier: []string{},
}

var templates = template.Must(template.ParseFiles("../Site/html/index.html"))

func main() {
	http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.Dir("../Site/css"))))
	fmt.Println("(http://localhost:8090) Server is running on port", port)
	http.HandleFunc("/", Home)
	http.ListenAndServe(port, nil)
}

func Home(w http.ResponseWriter, r *http.Request) {
	page.Api = saumon.InitApi()
	page.Fichier,_ = saumon.ReadFileList("../Data/LastUsed.txt")
	urls, _ := saumon.ReadFileList("../Data/urls.txt")
	urlsList := saumon.SepartUrls(urls)
	for _, i := range urlsList {
		page.Url = append(page.Url, saumon.Site{Adresse:i[0],Nom:i[1]})
	}
	templates.Execute(w, page)
}

