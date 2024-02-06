from openai import OpenAI

client = OpenAI()

image_data = client.files.content("chemin dossier ou se trouve l'image ou le fichier a resumer.")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "tu est un application de resumer de texte / documents / page internet je veux que tu soit simple et consis."},
    {"role": "user", "content": image_data_bytes  "je voudrais que tu me fasse un resumer de tout les documents/texte/page internet que tu va recevoir en 150 mots maximum."}
  ]
)


print(completion.choices[0].message.content)




