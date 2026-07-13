import os

from openai import OpenAI

MODEL = os.environ.get("MODEL", "gemma4")
API_URL = os.environ.get("API_URL", "http://localhost:11434/v1")

client = OpenAI(base_url=API_URL, api_key="OLLAMA")

question = input("What do you want to know?: ")
stream = client.chat.completions.create(
    model=MODEL, messages=[{"role": "user", "content": question}], stream=True
)

for chunk in stream:
    """ This specific value will contain a chunk of data returned by llm"""
    content = chunk.choices[0].delta.content
    if content:  # if the value of content is not empty, then only print it
        print(
            content, end="", flush=False
        )  # if the value of flush is True, then it will write output immediately.
print()
print()
print("--- done ---")
