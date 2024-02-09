package main

import (
	"fmt"
	"net/http"
	"text/template"
	saumon "hackasaumon/funcGo"
)

const port = ":8080"

var page = NullPage()
var templateIndex = template.Must(template.ParseFiles("../Site/html/index.html"))

func main() {
	http.Handle("/css/", http.StripPrefix("/css/", http.FileServer(http.Dir("../Site/css"))))
	fmt.Println("(http://localhost:8080) Server is running on port", port)
	http.HandleFunc("/", Home)
	http.HandleFunc("/secret.html",func(w http.ResponseWriter, r *http.Request) {
        http.ServeFile(w, r, "../Site/html/secret.html")
    })
	http.ListenAndServe(port, nil)
}

func Home(w http.ResponseWriter, r *http.Request) {
	page := NullPage()
	page.Api, _ = saumon.ReadFileString("../Data/API.txt")
	page.Fichier,_ = saumon.ReadFileList("../Data/LastUsed.txt")
	urls, _ := saumon.ReadFileList("../Data/urls.txt")
	urlsList := saumon.SepartUrls(urls)
	for _, i := range urlsList {
		page.Url = append(page.Url, saumon.Site{Adresse:i[0],Nom:i[1]})
	}
	
	fmt.Println(page.Fichier[0])
	templateIndex.Execute(w, page)
}

func NullPage() saumon.Page {
	return saumon.Page {
		Api: "",
		Url: []saumon.Site{},
		Fichier: []string{},
	}
}