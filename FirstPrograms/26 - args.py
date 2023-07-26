
# *args = parameter that will pack all arguments into a tuple -> useful so that a function can accept a varying amount of arguments

# def add (number_one, number_two):
#     return number_one + number_two

# print(add(1,2,3)) # This will not work, because add can only take in two parameters

def add (*numbers): # It does not have to be named *args, it can also be *numbers or something else
    sum = 0
    numbers = list(numbers) # We typecast the tuple to a list so we can make it mutable instead of immutable
    numbers.append(8) # We add 8 to the end of the numbers, so now we have 1+2+3+4+5+6+8
    for i in numbers:
        sum+=i
    return sum

print(add(1,2,3,4,5,6))