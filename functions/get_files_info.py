import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.join(working_directory, directory)
    target_dir = os.path.abspath(target_dir)

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    if not target_dir.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    #print(abs_working_directory)
    #print(target_dir)
    #print(directory)
   
    try:
        file_details = []
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            file_details.append(
                f" - {file}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(file_details)

    except Exception as e:
        return f"Error listing files: {e}"
