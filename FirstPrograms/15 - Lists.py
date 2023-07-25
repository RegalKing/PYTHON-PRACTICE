
# A list in Python is enclosed by brackets [ ], it is like an ArrayList in other languages from my understanding so far

numbers = [1,5,10,15]

print(numbers[0]) # Print the first element of the list

numbers[3]=6 # Replace the element on index 3 with the number 6

print(numbers) # Print the entire list

for i in numbers: # Iterate through the list and print each element individually
    print(i)

numbers.append("Alex") # THIS METHOD IS USED TO ADD AN ELEMENT TO THE END OF A LIST (APPEND AN ELEMENT)

print(numbers) 

numbers.remove(5) # THIS METHOD WILL REMOVE ANY MATCHING ELEMENTS, SO IN THIS EXAMPLE ALL NUMBER 5'S

print(numbers) 

numbers.insert(0,50) # THIS METHOD WILL INSERT THE NUMBER 50 AT INDEX 0 (Moves the entire list to the right)

print(numbers) 

numbers.remove("Alex") # Removing the string from the list so I can sort it

print(numbers) 

numbers.sort(reverse=True) # THIS METHOD WILL SORT THE LIST IN REVERSE, BUT SORT ONLY WORKS ON LISTS OF THE SAME TYPES LIKE NUMBERS OR STRINGS

print(numbers) 