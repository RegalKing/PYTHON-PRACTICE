name = "alex writes python code"

print(len(name) ) # function LEN prints the length of the string
print(name.find("w") ) # finds the position of the first character of a certain string in a string, in this example the string is the character "w"

# LEN function can be used on any iterable thing in python such as a list, array, string, etc. 
# FIND method can ONLY BE USED ON STRINGS 

print(name.capitalize()) # capitalizes the first letter of the string
print(name.upper()) # uppercases the entire string
print(name.lower()) # lowercases the entire string
print(name.isdigit()) # checks if the string is a digit
print(name.isalpha()) # checks if the string contains only alphabetical letters
print(name.count("e")) # counts how many of said string are in your string
print(name.replace("e","EGG")) # replaces all appearances of said string with another string that you define

print(name*3) # prints the string 3 times!! NO NEED FOR A LOOP LIKE IN ALL OTHER LANGUAGES THIS IS PRETTY COOL DAMN