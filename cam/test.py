from openai import OpenAI

def API():
  client = OpenAI()

  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
          {"role": "system", "content": "ecrit moi test"},
          {"role": "user", "content": "ecrit moi test"},
      ]
  )
  return completion.choices[0].message.content