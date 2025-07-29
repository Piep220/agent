import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python file with optional args for execution, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the python file to be executed, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguemts to be passed to the python code to be run, defauls to none.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    joined_file_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(joined_file_path)
     
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ["python3", abs_file_path] + args,
            cwd=abs_working_directory,
            shell=False,
            text=True,
            capture_output=True,
            timeout=30
        )

        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

        #output = f"STDOUT: \n{result.stdout} \nSTDERR: \n{result.stderr}"
        #if result.returncode != 0:
        #    output += f"\nProcess exited with code: {result.returncode}"
        #if not result.stdout and not result.stderr:
        #    output = "No output produced."
        #
        #return output

    except Exception as e:
        return f"Error: executing Python file: {e}"