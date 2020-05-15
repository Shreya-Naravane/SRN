
fname = input("Enter name of file with extension to be opened \n")
mode = input("Enter mode in which file is to be opened\n")
try : 
    fp = open(fname,mode)
    print(fp.read())
    fp.write("Trial text is written to test the code\n")
except UnicodeDecodeError :
    print("Something went wrong, Check whether the opened file is readable? \n")
except FileNotFoundError :
    print("Something went wrong, Check whether filename and path is correct?\n")
except IsADirectoryError :
    print("Something went wrong, Cant open a directory.\n")
except PermissionError :
    print("Something went wrong, Check permissions of file to be opened.\n")
except :
    print("Cant predict what exacty went wrong.\n")
else :
    print("Your job of file management successfully done!\n")
