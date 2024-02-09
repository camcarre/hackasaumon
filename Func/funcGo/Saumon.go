package hackasaumon

import (
	"fmt"
	"strings"
	"os"

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

func SepartUrls(list []string) [][]string {
	final := [][]string{}
	for _, i := range list{
		adresse := []string{}
		index := strings.Index(i,"|")
		if index == -1 {
			continue
		}
		adresse = append(adresse,i[:index-1])
		if index+2 > len(i){
			adresse = append(adresse,"")
		} else {
			adresse = append(adresse,i[index+2:])
		}
		final = append(final,adresse)
	}
	return final
}
func ReadFileList(filePath string) ([]string, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	words := strings.Split(string(content),"\n")
	return words, nil
}

func ReadFileString(filepath string) (string, error) {
	text, err := os.ReadFile(filepath)
	if err != nil {
		fmt.Println("Error:", err)
		return "", err
	}
	return string(text), nil
}