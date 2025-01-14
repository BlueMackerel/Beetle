import re
from sys import argv
ver="""
made with Chat GPT
made by BlueMakel
version:1.0.0
type -c to compile.
"""
class BeetleC:
    def parse_beetle_code(self,code):
        """
        Parse Beetle code and translate it into Python code.
        """
        python_code = []
        lines = code.split('\n')

        for line in lines:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('/$'):
                continue

            # Print statement
            if line.startswith('printc('):
                content = line[len('printc('):-1]  # Extract content inside printc()
                python_code.append(f"print({content})")

            # Integer variable
            elif line.startswith('dei:'):
                var, value = line[len('dei:'):].split('=')
                python_code.append(f"{var.strip()} = int({value.strip()})")

            # Float variable
            elif line.startswith('def:'):
                var, value = line[len('def:'):].split('=')
                python_code.append(f"{var.strip()} = float({value.strip()})")

            # String variable
            elif line.startswith('des:'):
                var, value = line[len('des:'):].split('=')
                python_code.append(f"{var.strip()} = {value.strip()}")

            # List variable
            elif line.startswith('del:'):
                var, value = line[len('del:'):].split('=')
                python_code.append(f"{var.strip()} = [{value.strip()}]")

            # Tuple variable
            elif line.startswith('det:'):
                var, value = line[len('det:'):].split('=')
                python_code.append(f"{var.strip()} = ({value.strip()})")

            # Dictionary variable
            elif line.startswith('ded:'):
                var, value = line[len('ded:'):].split('=')
                python_code.append(f"{var.strip()} = {{{value.strip()}}}")

            # Boolean variable
            elif line.startswith('deb:'):
                var, value = line[len('deb:'):].split('=')
                python_code.append(f"{var.strip()} = {value.strip()}")

            # Set variable
            elif line.startswith('de:'):
                var, value = line[len('de:'):].split('=')
                python_code.append(f"{var.strip()} = set({value.strip()})")

            else:
                print(f"Unknown syntax: {line}")

        return '\n'.join(python_code)

# Example usage
option=argv[1]
if option=='-c':
    file=argv[2]
    with open(f'{file}','r') as f:
        beetle_script=f.read()
    c=BeetleC()
    python_code =c.parse_beetle_code(str(beetle_script))
    exec(python_code)
elif option=='-v':
    print(ver)