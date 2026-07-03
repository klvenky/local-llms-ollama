import os

from openai import OpenAI

MODEL = os.environ.get("MODEL", "gemma4")


def main():
    client = OpenAI(
        base_url=os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434") + "/v1",
        api_key="Dhoom",
    )

    result = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "What are you?"}],
    )

    print(result.choices[0].message.content)


if __name__ == "__main__":
    main()
