package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func displayFolderContents(folderPath string) error {
	files, err := os.ReadDir(folderPath)
	if err != nil {
		return err
	}

	for _, file := range files {
		filePath := filepath.Join(folderPath, file.Name())

		// Vérifiez si c'est un dossier
		if file.IsDir() {
			fmt.Printf("Dossier: %s\n", filePath)
		} else {
			// Afficher le contenu du fichier
			fmt.Printf("Contenu de %s:\n", filePath)
			content, err := os.ReadFile(filePath)
			if err != nil {
				return err
			}
			fmt.Println(string(content))
			fmt.Println("-----------")
		}
	}

	return nil
}

func main() {
	// Spécifiez le chemin du dossier à afficher
	folderPath := "textes"

	err := displayFolderContents(folderPath)
	if err != nil {
		fmt.Println("Erreur :", err)
	}
}
