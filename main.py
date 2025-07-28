import os, sys

from dotenv import load_dotenv

from google import genai
from google.genai import types

import config

def main():    
    verbose_flag = False
    args = []

    for _, arg in enumerate(sys.argv[1:]):
        if arg == '-v' or arg == '--verbose':
            verbose_flag = True
        elif not arg.startswith('-'):
            args.append(arg)


    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [-v|--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    user_prompt = " ".join(args)
    if verbose_flag == True:
        print("User prompt:", user_prompt)

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(system_instruction=config.SYSTEM_PROMPT),
)
    
    print("Response:")
    print(response.text)

    if verbose_flag == True:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
