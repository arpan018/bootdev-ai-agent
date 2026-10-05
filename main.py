import os
import argparse

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

if api_key is None:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    user_prompt = args.user_prompt

    messages = [
    {"role": "user", "content": args.user_prompt},
    ]

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=messages,
    )

    if not response.usage:
        raise RuntimeError("API response appears to be malformed")

    if args.verbose:
        print(f'User prompt: "{user_prompt}"')
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    print(response.choices[0].message.content)
    

if __name__ == "__main__":
    main()

