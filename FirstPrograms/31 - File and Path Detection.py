
import os

path = "C:\\Users\\Alex\\Desktop\\python\\PYTHON-PRACTICE\\FirstPrograms\\test.txt"
        # You need to change single backslashes \ to a double backslash \\
        # Or you can use a raw string like this:
path = r"C:\Users\Alex\Desktop\python\PYTHON-PRACTICE\FirstPrograms\test.txt"

if os.path.exists(path): # Check if a valid path exists on the system, this can be any path not just a path to a file
    print("That location exists!")

if os.path.isfile(path): # Check if there is a file on the specified path
    print("That file does exist!")

directory_path = "C:\\"

if os.path.isdir(directory_path): # Check if a directory exists on the specified path
    print("This directory exists!")
