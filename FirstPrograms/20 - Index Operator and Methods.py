
# Index operator [] = gives acces to a sequence's element (string, list, tuples)

name = "los Angeles"

if(name[0].islower()):
    print("The first letter is lowercase!")
    name = name.capitalize()

print(name)

name = "Los Angeles"

first_name = name[:3].upper() # name[0:3] is the same as name[:3]
print(first_name)

last_name = name[4:].lower()
print(last_name)

last_character = name[-1]
print(last_character)