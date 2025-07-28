import os
import config

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