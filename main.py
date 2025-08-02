import os, sys

from dotenv import load_dotenv

from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function

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
    
    iter = 0
    while True:
        iter += 1
        if iter > config.MAX_ITERS:
            print(f"Maximum iterations ({config.MAX_ITERS}) reached.")
            sys.exit(1)
        try: 
            final_response = generate_content(client, messages, verbose_flag)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error generationg response:, {e}")
            break


def generate_content(client, messages, verbose_flag):
    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=config.SYSTEM_PROMPT
        ),
    )       

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
        
        if not response.function_calls:
            return response.text
    
    function_responses = []
    for func_call in response.function_calls:
        #print(f"Calling function: {func_call.name}({func_call.args})")
        function_call_result = call_function(func_call,verbose_flag)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose_flag:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))

    if verbose_flag == True:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
