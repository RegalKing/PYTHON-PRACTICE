
try:
    # Open the file in read mode
    with open("read.txt", "r") as file: # Opening a file using "with open" will automatically close the file after the indented block is finished
                                        # read.txt = FILE PATH
                                        # "r" = OPEN THE FILE IN READ-ONLY MODE
        content = file.read()
        
except FileNotFoundError:
    print("File was not found!")


print(content)
print(f"Has the file been closed:{file.closed}")
