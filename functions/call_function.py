import os
from google.genai import types

import config
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    working_directory = config.WORKING_DIR
    function_name = function_call_part.name
    function_args = function_call_part.args

    functions = {
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
        "get_file_content": get_file_content,
    }

    if not function_call_part.name in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_result = functions[function_name](working_directory, **function_args)

    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
        )
    ],
)