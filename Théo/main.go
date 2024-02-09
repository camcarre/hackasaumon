package main

import (
	"fmt"
	"os"
	"strings"
)
//binds the contents of the file and returns it as a list
func displayFileContents(filePath string) ([]string, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	words := strings.Fields(string(content))
	return words, nil
}
//call the file, call the function that links it and check for any possible errors
func main() {
	filePath := "textes/test.txt"

	words, err := displayFileContents(filePath)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println(words)
}


