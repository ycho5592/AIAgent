import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        # Get absolute path for directory
        working_dir_abs = os.path.abspath(working_directory)
        # Constructing full path to the targte directory
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Check if target_dir falls within the absolute working directory path
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]

        if args != None:
            command.extend(args)
        
        run_command = subprocess.run(command, cwd=working_directory, capture_output=True, timeout=30, text=True)

        output_string = []

        if run_command.returncode != 0:
            output_string.append(f"Process exited with code {run_command.returncode}")
        
        if not run_command.stdout and not run_command.stderr:
            output_string.append("No output produced")
        else:
            if run_command.stdout:
                output_string.append(f"STDOUT: {run_command.stdout}")
            if run_command.stderr:
                output_string.append(f"STDERR: {run_command.stderr}")
        
        return "\n".join(output_string)

    except Exception as e:
        return f"Error: executing Python file: {e}"


 
