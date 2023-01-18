import subprocess
import os
import webbrowser

# open excel files
def open_excel(path: str):
    try:
        subprocess.Popen([path], shell=True)
    except:
        print('Excel file is not available')

# open web apps
def open_web(path: str):
    try:
        webbrowser.open(path)
    except:
        print('web page is not available')

# open exe apps
def open_exe(path: str):
    try:
        subprocess.Popen(path)
    except:
        print('exe file is not available')

# open folders
def open_folder(path: str):
    try:
        os.system(path)
    except:
        print('Folder path is not available')

