
# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"
age = 69

print("1 The "+animal+" jumped over the "+item+" at "+str(age)+" years old!")

# A cleaner way to write this print statement is using the F-string formatting
print(f"2 The {animal} jumped over the {item} at {age} years old!")

# An equivalent version would also be the code below, but it is ugly and do not use it
print("3 The {} jumped over the {} at {} years old!".format(animal,item,age))

# You can also use indexing like this:
print("4 The {1} jumped over the {0} at {2} years old!".format(animal,item,age))

#Keyword arguments
print("5 The {animal} jumped over the {item} at {age} years old!".format(animal="cow",item="moon",age=69))
print("6 The {animal} jumped over the {animal} at {animal} years old!".format(animal="cow",item="moon",age=69)) # You can pass more key-value pairs than you use in the print statement
print(f"7 The {animal} jumped over the {item} at {age} years old!".format(animal="cow", item="moon", age=69)) # Adding an F-string ahead of the string also works



text = "8The {} jumped over the {} at {} years old!"
print(text.format(animal,item,age))

print("Hello, my name is {:10}!".format("Jeff")) # {}:10} allocates 10 spaces to padding the name
print("Hello, my name is {:>10}!".format("Jeff")) # {}:10} allocates 10 spaces to padding the name # > means right-alignment, < also works but it's the default
print("Hello, my name is {:<10}!".format("Jeff")) # As we can see this is the same as :10 because the default formatting is right-alignment

# Numbers time!

number=3.1415
print("The number pi is {:.3f}".format(number)) # This rounds pi to 3 decimal places

number=100000 # 100.000
print("The number is {:,}".format(number)) # Formats the number with a ',' every 10^3 (thousand) sections
print("The number is {:b}".format(number)) # Displays the number in binary
print("The number is {:o}".format(number)) # Displays the number in octal -> octal is made from numbers [0,7] 
print("The number is {:x}".format(number)) # Displays the number in hexadecimal

print()

# The equivalent of these with fstrings would be:
number = 1234567890
print(f"The number is {number:,}")
print(f"The number is {number:b}")
print(f"The number is {number:o}")
print(f"The number is {number:x}")
