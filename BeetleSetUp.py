import winreg as reg
import os
import ctypes
import sys
from tkinter import *
import os
from json import *
data={
    "do you had filemakeing":"Yes"
}
def json_w():
    with open("lanch.json", "w", encoding="utf-8") as json_file:
        dump(data, json_file, indent=4, ensure_ascii=False)
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
    json_w()
win=Tk()
win.geometry('200x250')
win.option_add('*Font','Arial 50')
def is_admin():
    """Check if the script is running with admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Rerun the script with admin privileges if not already."""
    if not is_admin():
        # Relaunch the script with admin privileges
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

run_as_admin()

lab=Label(win,text="This program will set the beetle's\ndefault settings on your computer.")
lab.pack()

def set_file_association():
    # 1. .tle 확장자 등록
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, ".tle")
    reg.SetValue(key, "", reg.REG_SZ, "Beetle file")
    reg.CloseKey(key)

    # 2. tlefile에 대한 설정
    key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, "tlefile")
    reg.SetValue(key, "", reg.REG_SZ, "Beetle File")
    
    # 3. DefaultIcon 등록
    icon_path = os.path.abspath("BeetlefileLogo.ico")  # 아이콘 파일의 절대 경로
    icon_key = reg.CreateKey(key, "DefaultIcon")
    reg.SetValue(icon_key, "", reg.REG_SZ, icon_path)
    reg.CloseKey(icon_key)

    # 4. 연결 프로그램 등록
    shell_key = reg.CreateKey(key, r"shell\open\command")
    interpreter_path = os.path.abspath("Beetle.exe")  # 실행할 프로그램 경로
    reg.SetValue(shell_key, "", reg.REG_SZ, f'"{interpreter_path}" "%1"')
    reg.CloseKey(shell_key)


    reg.CloseKey(key)
    lab.config(text='setting end.\n you can stop this program.')

btn=Button(win,text='setting start',command=set_file_association)
btn.pack()

# 함수 실행

if __name__=='__main__':
    win.mainloop()