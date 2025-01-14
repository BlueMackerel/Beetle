import os
import subprocess
filename=input("Enter the file name: ")
class TLECompiler:
    def __init__(self):
        self.output_python_code = ""
        self.variables = {}


    def read_tle_file(self, tle_file):
        """Reads the .tle file and converts it to Python code."""
        with open(tle_file, "r") as file:
            lines = file.readlines()
        self.parse_tle_lines(lines)

    def parse_tle_lines(self, lines):
        """Parses lines of the .tle file."""
        for line in lines:
            line = line.strip()
            if line.startswith("defs"):
                # Define a string variable
                _, name, value = line.split(maxsplit=2)
                self.output_python_code += f'{name} = "{value}"\n'
            elif line.startswith("defi"):
                # Define an integer variable
                _, name, value = line.split(maxsplit=2)
                self.output_python_code += f"{name} = {int(value)}\n"
            elif line.startswith("printsc<") and line.endswith(">"):
                # Print a string
                content = line[8:-1]
                self.output_python_code += f'print("{content}")\n'
            elif line.startswith("//"):
                # Comment, ignore
                continue
            else:
                raise ValueError(f"Unknown command in .tle: {line}")

    def save_python_code(self, output_file="output.py"):
        """Saves the generated Python code to a file."""
        with open(output_file, "w") as file:
            file.write(self.output_python_code)

    def compile_to_exe(self, python_file="output.py", exe_name="output.exe"):
        """Compiles the Python file to an .exe using PyInstaller."""
        try:
            # Use PyInstaller to generate the .exe
            subprocess.run(
                ["pyinstaller", "--onefile", "--name", exe_name, python_file],
                check=True
            )
            print(f"Executable {exe_name} created successfully.")
        except subprocess.CalledProcessError as e:
            print("Error during compilation:", e)

# Main usage
if __name__ == "__main__":
    tle_file =filename   # Replace with your .tle file
    compiler = TLECompiler()

    # Step 1: Read and parse the .tle file
    compiler.read_tle_file(tle_file)

    # Step 2: Save the generated Python code
    python_file = "output.py"
    compiler.save_python_code(python_file)

    # Step 3: Compile to .exe
    exe_name = "output.exe"
    compiler.compile_to_exe(python_file, exe_name)
