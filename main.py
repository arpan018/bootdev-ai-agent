import os
import argparse
import json

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    
    for _ in range(20):
        response = client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=messages,
            tools=available_functions,
            temperature=0,
        )

        if not response.usage:
            raise RuntimeError("API response appears to be malformed")

        if args.verbose:
            print(f'User prompt: "{user_prompt}"')
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)

                if not result_message["content"]:
                    raise Exception("Tool call returned an empty content")

                messages.append(result_message)

                if args.verbose:
                    print(f"-> {result_message['content']}")
        else:
            print(f"Final response:\n{message.content}")
            break
    else:
        print("Error: Maximum iterations reached without a final response.")
        raise SystemExit(1)

    

if __name__ == "__main__":
    main()

