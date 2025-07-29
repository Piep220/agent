import os, sys

from dotenv import load_dotenv

from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file

import config

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

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
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=config.SYSTEM_PROMPT
        ),
)
    
    print("Response:")
    #print(response.text)
    print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")

    if verbose_flag == True:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
