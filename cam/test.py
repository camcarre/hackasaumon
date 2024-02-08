from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "ecrit moi test"},
        {"role": "user", "content": "ecrit moi test"},
    ]
)

print(completion.choices[0].message.content)