package main

import (
	"fmt"
	"os"
	"strings"
)

func displayFileContents(filePath string) ([]string, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	words := strings.Fields(string(content))
	return words, nil
}

func main() {
	filePath := "textes/test.txt"

	words, err := displayFileContents(filePath)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println(words)
}


