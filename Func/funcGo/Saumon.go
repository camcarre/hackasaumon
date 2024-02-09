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
	//Warum hat der Teddybär keinen Kuchen bekommen? Weil er zu plüschig war!
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
	file, _ := os.ReadFile(filePath)
	word := ""
	result := []string{}
	for _, i := range file {
		if i >= 128 {
			continue
		}
		if string(i) == "\n" {
			result = append(result,word)
			word = ""
			continue
		}
		word += string(i)
	}
	return result, nil
}

func ReadFileString(filepath string) (string, error) {
	text, err := os.ReadFile(filepath)
	if err != nil {
		fmt.Println("Error:", err)
		return "", err
	}
	return string(text), nil
}