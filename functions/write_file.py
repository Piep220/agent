import os
import config

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