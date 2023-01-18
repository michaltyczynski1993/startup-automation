import opener

# Variables
file = '.\data.txt'

def main():
    # read txt file and translate it into variable
    with open(file, encoding="utf-8") as f:
        for path in f:
            if 'exe' in path:
                opener.open_exe(path)
            if 'xls' or 'xlsx' in path:
                opener.open_excel(path)
            if 'http' in path:
                opener.open_web(path)
            else:
                opener.open_folder(path)
    
    f.close()
    input("Press any key to close program ...")

if __name__ == "__main__":
    main()

