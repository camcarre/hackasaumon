import os

def display_folder_contents(folder_path):
    try:
        files = os.listdir(folder_path)
    except OSError as e:
        return e

    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            print(f"Dossier: {file_path}")
        else:
            print(f"Contenu de {file_path}:")
            try:
                with open(file_path, 'r') as file_content:
                    content = file_content.read()
                    print(content)
            except OSError as e:
                return e

            print("-----------")

    return None

def main():
    folder_path = "textes"

    error = display_folder_contents(folder_path)
    if error is not None:
        print("Erreur :", error)

if __name__ == "__main__":
    main()
    