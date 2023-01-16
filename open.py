import subprocess
import os
import webbrowser

# open excel files
def open_excel(path: str):
    subprocess.Popen([path], shell=True)

# open web apps
def open_web(path: str):
    webbrowser.open(path)

# open exe apps
def open_exe(path: str):
    subprocess.Popen(path)

# open folders
def open_folder(path: str):
    os.startfile(path)

    