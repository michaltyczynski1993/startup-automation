# startup-automation

A simple utility application created to speed up the start of the day at work by automating the process of file handling and applications
which must be run daily. 

1. To run the application correctly, the program requires that the file 'data.txt' be in the same folder as 'app.exe'
2. 'data.txt' should contain all the paths of the programs to be launched
3. Path convention to run
  a. For Excel + word files etc.
    The path should contain the word 'start' + the full path to the file using '\\'
    Example:
    start C:\\Users\\xxxx\\Desktop\\test.xls

  b. For the file from the .exe language and desktop program shortcuts\
    Only path + except single "\" use "\\"
    Example:
    C:\\Users\\xxxx\\AppData\\Local\\gb_studio\\gb-studio.exe

  c. For a .pdf file
    Same as for excel file.
  d. For folders
    i. when the path has spaces
      enter by example start "" "C:\Users\your path"
    ii. when the path has no spaces
      enter by example start C:\Users\xxxx\Documents
      
I hope it will help you to run all the necessary programs in your job faster so that you have more time to enjoy your morning coffee at the office :)
