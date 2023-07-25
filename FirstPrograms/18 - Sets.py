
# Set = a collection that is UNORDER, UNINDEXED. Sets DO NOT ALLOW DUPLICATE VALUES.

# A set is FASTER than a list if you need to check if SOMETHING EXISTS IN A COLLECTION OF THINGS

numbers = {5, 10, 15, 20, 25, 30}
print(numbers)

numbers.add(50) # Adds the number 50 to the set numbers
print(numbers)

numbers.remove(15) # Removes the number 15 from the set
print(numbers)

numbers.clear() # Empties the set
print(numbers) # 'set()' ouput represents an empty set

numbers = {5, 10, 15, 20, 25, 30}
triple_digit_numbers = {100,200,300}
numbers.update(triple_digit_numbers) # Adds the entire set triple_d_n to the set numbers (Combines them into the set numbers)
print(numbers)

numero = {0,1,2,3}
numeroDos = {5,6,7,8}

union_of_numero = numero.union(numeroDos) # numeroDos.union(numero) would do the same, because A union B == B union A
print (union_of_numero)

# What if I want to check what one set has that the other doesn't? We need to use the DIFFERENCE method!

hola = {0,1,2}
hello = {2,3,4}

print(hola.difference(hello)) # This will print what HOLA has that HELLO does not

# What if we want to check what they have in common? We need the INTERSECTION method

print(hola.intersection(hello))
