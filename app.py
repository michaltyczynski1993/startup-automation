import os

#file extensions
exe_str = "exe"
pdf_str = "pdf"
excel_str = "xlsx"

# read txt file and translate it into variable
with open('data.txt', encoding="utf-8") as f:
    for path in f:
        try:
            os.system(path)
        except:
            print("Podana scierzka nie istnieje")
        
f.close()
input("Press any key to continue ...")

