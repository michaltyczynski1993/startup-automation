import os

# Variables
file = '.\data.txt'

def main():
    # read txt file and translate it into variable
    with open(file, encoding="utf-8") as f:
        for path in f:
            try:
                os.system(path)
                print(path)
            except:
                print("Directory not existing")
    
    f.close()
    input("Press any key to close program ...")

if __name__ == "__main__":
    main()

