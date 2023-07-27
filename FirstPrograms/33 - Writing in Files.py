
text = "Yo\nwhats up\npeople!"
hello = "\nHello!"

with open ("write.txt","w") as file:
    file.write(text) # This will OVERWRITE THE ENTIRE FILE if some content already exists in the file!

with open ("write.txt","a") as file:
    file.write(hello) # This will NOT OVERWRITE the file but it will write from the last character of the file because we switched the mode to APPEND aka "a"

