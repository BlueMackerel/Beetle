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
import re

class BeetleCompiler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.variables = {}
        self.line_index = 0
        self.lines = []

    def read_file(self):
        """Reads the Beetle source code from the given file."""
        with open(self.file_name, 'r') as file:
            self.lines = file.readlines()

    def evaluate_expression(self, expr):
        """Evaluates a boolean or mathematical expression."""
        for var in self.variables:
            expr = expr.replace(var, str(self.variables[var]))
        return eval(expr)

    def execute_line(self, line):
        """Parses and executes a single line of Beetle code."""
        line = line.strip()

        # Ignore comments
        if line.startswith('/$'):
            return

        # Print statement
        if line.startswith("printc(") and line.endswith(")"):
            content = line[7:-1]
            if content.startswith("'") and content.endswith("'"):
                print(content[1:-1])
            elif content in self.variables:
                print(self.variables[content])
            else:
                print(f"Undefined variable: {content}")

        # Variable definitions
        elif line.startswith("dei:"):
            name, value = self.parse_assignment(line, "dei:")
            self.variables[name] = int(value)
        elif line.startswith("def:"):
            name, value = self.parse_assignment(line, "def:")
            self.variables[name] = float(value)
        elif line.startswith("des:"):
            name, value = self.parse_assignment(line, "des:")
            if not (value.startswith("'") and value.endswith("'")):
                print("String values must be enclosed in single quotes.")
            self.variables[name] = value[1:-1]
        elif line.startswith("del:"):
            name, value = self.parse_assignment(line, "del:")
            self.variables[name] = [int(x) for x in value.split(',')]
        elif line.startswith("det:"):
            name, value = self.parse_assignment(line, "det:")
            self.variables[name] = tuple(int(x) for x in value.split(','))
        elif line.startswith("ded:"):
            name, value = self.parse_assignment(line, "ded:")
            self.variables[name] = self.parse_dict(value)
        elif line.startswith("deb:"):
            name, value = self.parse_assignment(line, "deb:")
            self.variables[name] = value == "True"
        elif line.startswith("de:"):
            name, value = self.parse_assignment(line, "de:")
            self.variables[name] = set(value.strip("set()").split(','))

        # If statement
        elif line.startswith("when"):
            condition, body = self.parse_condition(line, "when")
            if self.evaluate_expression(condition):
                self.execute_body(body)

        # Else statement
        elif line.startswith("is not:"):
            body = line[8:].strip("{}").strip()
            self.execute_body(body)

        # While loop
        elif line.startswith("loop"):
            condition, body = self.parse_condition(line, "loop")
            while self.evaluate_expression(condition):
                self.execute_body(body)

        # Put statement (for loop equivalent)
        elif line.startswith("put"):
            iterable_name, target_var, body = self.parse_put(line)
            if iterable_name not in self.variables:
                print(f"Undefined iterable variable: {iterable_name}")
            
            iterable = self.variables[iterable_name]
            if not hasattr(iterable, '__iter__'):
                print(f"Variable {iterable_name} is not iterable.")
            
            for item in iterable:
                self.variables[target_var] = item
                self.execute_body(body)

        # Unsupported or invalid line
        else:
            print(f"Invalid syntax: {line}")

    def execute_body(self, body):
        """Executes a body of code enclosed in { }."""
        for statement in body.split(';'):
            if statement.strip():
                self.execute_line(statement.strip())

    def parse_assignment(self, line, prefix):
        """Parses a variable assignment statement."""
        pattern = re.escape(prefix) + r"(\w+)=(.+)"
        match = re.match(pattern, line)
        if not match:
            print(f"Invalid assignment syntax: {line}")
        return match.groups()

    def parse_condition(self, line, keyword):
        """Parses a conditional or loop statement."""
        pattern = re.escape(keyword) + r"\s*\{(.+)\}:\{(.+)\}"
        match = re.match(pattern, line)
        if not match:
            print(f"Invalid {keyword} syntax: {line}")
        return match.groups()

    def parse_put(self, line):
        """Parses a put statement."""
        pattern = r"put\s*\{(.+)\}\s*to\s*\{(.+)\}:\{(.+)\}"
        match = re.match(pattern, line)
        if not match:
            print(f"Invalid put syntax: {line}")
        iterable_name, target_var, body = match.groups()
        return iterable_name, target_var, body

    def parse_dict(self, value):
        """Parses a dictionary value."""
        result = {}
        entries = value.split(',')
        for entry in entries:
            key, val = entry.split(':')
            key = key.strip("'")
            val = val.strip("'")
            result[key] = val
        return result

    def run(self):
        """Runs the compiled code."""
        self.read_file()
        while self.line_index < len(self.lines):
            line = self.lines[self.line_index].strip()
            if line:
                self.execute_line(line)
            self.line_index += 1

# Example usage


# Example usage
if __name__=='__main__':
    if j_d.get("do you had filemakeing")=='Yes':
        option=argv[1]
        if option=='-c':
            file=argv[2]
            with open(f'{file}','r') as f:
                beetle_script=f.read()
            c=BeetleCompiler(file)
            c.run()
        elif option=='-v':
            print(ver)
    else:
        print('you need set up first.\n plase run BeetleSetup.exe.')
        from time import sleep
        sleep(5)