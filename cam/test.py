from openai import OpenAI

def API():
  client = OpenAI()

  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
          {"role": "system", "content": "ecrit moi test"},
          {"role": "user", "content": "donne moi la capital de la france(20mots maximum)"},
      ]
  )
  return completion.choices[0].message.content

def WriteTxt(respons,file):
    with open(file,"w") as text:
        text.write(respons)
    return

response = API()
WriteTxt(response,"API.txt")