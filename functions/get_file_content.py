import os
import config
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns a string containing the content of a file, limited to the first {config.MAX_CHARS} characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file to be read, relative to the working directory.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(file_path)

    #print(file_path)
    #print(abs_file_path)

    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
     
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
    
        if len(file_content_string) == config.MAX_CHARS:
            file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"
        
        return file_content_string

    except Exception as e:
        return f"Error reading files: {e}"