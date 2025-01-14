import re
from sys import argv
from json import *
ver="""
made with Chat GPT
made by BlueMakel
version:1.0.0
type -c to compile.
"""
def json_r():
    with open("lanch.json", "r", encoding="utf-8") as json_file:
        global j_d
        j_d= load(json_file)
import os
# 실행 횟수를 기록할 파일 이름
COUNT_FILE = "count.txt"

# 파일이 존재하지 않으면 0으로 초기화
if not os.path.exists(COUNT_FILE):
    with open(COUNT_FILE, "w") as file:
        file.write("0")

# 파일에서 실행 횟수 읽기
with open(COUNT_FILE, "r") as file:
    count = file.read()
    count = int(count) if count.isdigit() else 0

# 실행 횟수 증가
count += 1

# 파일에 실행 횟수 저장
with open(COUNT_FILE, "w") as file:
    file.write(str(count))
if count==1:
    json_r()
else:
    json_r()
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
if __name__=='__main__':
    if j_d.get("do you had filemakeing")=='Yes':
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
    else:
        print('you need set up first.\n plase run BeetleSetup.exe.')
        from time import sleep
        sleep(5)