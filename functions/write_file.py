import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the contents of a string to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file to be writen, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string of content to be written to the file specified.",
            ),
        },
    ),
)

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(file_path)

    #print(file_path)
    #print(abs_file_path)
     
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(file_path):
            os.mkdir(file_path)
    except Exception as e:
        return f"Error writing file: {e}"
    
    try:
        with open(file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error writing file: {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'