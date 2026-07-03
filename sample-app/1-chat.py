import os

import openai

client = openai.OpenAI(
    base_url=os.environ.get("OLLAMA_URL", "http://localhost:11434/v1"),
    api_key="Alright let's go",
)

question = input("Ask Me Anything:")

result = client.chat.completions.create(
    model=os.environ.get("MODEL", "gemma4"),
    messages=[{"role": "user", "content": question}],
)

print(result.choices[0].message.content)
