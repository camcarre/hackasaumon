package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func displayFolderContents(folderPath string) (string, error) {
	var result string

	files, err := os.ReadDir(folderPath)
	if err != nil {
		return "", err
	}

	for _, file := range files {
		filePath := filepath.Join(folderPath, file.Name())

		if file.IsDir() {
			result += fmt.Sprintf("Dossier: %s\n", filePath)
		} else {
			result += fmt.Sprintf("Contenu de %s:\n", filePath)
			content, err := os.ReadFile(filePath)
			if err != nil {
				return "", err
			}
			result += string(content) + "\n"
			result += "-----------\n"
		}
	}

	return result, nil
}

func main() {
	folderPath := "textes"

	_, err := displayFolderContents(folderPath)
	if err != nil {
		fmt.Println("Erreur :", err)
		return
	}
}

