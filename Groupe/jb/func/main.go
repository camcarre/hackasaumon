package main

import (
	"fmt"
	"strings"
)

func main() {
	listUrl := []string{"https://www.google.com | accident autoroute a47 - Recherche Google","https://www.google.com | switch oled - Recherche Google"}

	fmt.Println(SepartUrls(listUrl))

}

func SepartUrls(list []string) [][]string {
	final := [][]string{}
	for _, i := range list{
		adresse := []string{}
		index := strings.Index(i,"|")
		if index == -1 {
			continue
		}
		adresse = append(adresse,i[:index-1])
		adresse = append(adresse,i[index+2:])
		final = append(final,adresse)
	}
	return final
}