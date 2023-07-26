
import random

# Generate a random integer within a range
random_number = random.randint(1, 100)
print("Random integer:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float between 0 and 1:", random_float)

# Generate a random floating-point number within a specified range
random_range_float = random.uniform(10, 20)
print("Random float in range [10, 20]:", random_range_float)

# Generate a random element from a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
random_fruit = random.choice(fruits) # This also works on tuples and sets
print("Random fruit:", random_fruit)

# Shuffle a list 
random.shuffle(fruits)
print("Shuffled fruits:", fruits)

# Select multiple random elements from a list
random_sample = random.sample(fruits, 3)
print("Random sample of 3 fruits:", random_sample)

# Generate a random boolean (True or False)
random_bool = random.choice([True, False])
print("Random boolean:", random_bool)

# Randomly choose an element from multiple choices
choices = ["rock", "paper", "scissors"]
random_choice = random.choices(choices, weights=[1, 2, 1], k=1)[0] # weights assignt probabilities to each element in the list (choices is the list in this example)
print("Random choice:", random_choice)                             # this means the first element has 1/4 chance to be chosen, second 2/4 and third 1/4
                                                                   # the k parameter specifies how many elements you want chosen, in this example we want one element
                                                                   # the function usually returns a list but since we are returning one element we use [0] to print just the element of the list
                                                                   # if we wanted to for example get 2 elements we would write it like this:
random_choice = random.choices(choices, weights=[1, 2, 1], k=2)
print("Random choice of 2 elements:", random_choice) # This will print the chosen 2 elements as a list
print("Random choice of 2 elements:", random_choice[0], random_choice[1]) # This will print the chosen 2 elements individually

# Generate a random character from a string
random_char = random.choice("abcdefghijklmnopqrstuvwxyz")
print("Random character:", random_char)



# Shuffle characters in a string (convert to list and back to string)
word = "random"
shuffled_word = "".join(random.sample(word, len(word))) # This leverages a concept in Python that allows you to perform certain operations directly on strings as if they were lists of characters.
print("Shuffled word:", shuffled_word)
#Longer explanation of this below in more steps without leveraging a string as a list:


# Original string
word = "random"

# Step 1: Convert the string to a list of characters
# The 'list()' function splits the string into a list of its individual characters.
# Each character in the string becomes an element in the list.
character_list = list(word)

# Step 2: Shuffle the list of characters
# The 'random.sample()' function shuffles the elements in the list.
# It randomly selects elements from the list without replacement,
# and as many elements as there are in the original list (length of 'word').
shuffled_list = random.sample(character_list, len(word))

# Step 3: Convert the shuffled list back to a string
# The '"".join()' method concatenates the elements in the 'shuffled_list' back into a single string.
# The empty string "" is used as the separator, so each character is simply joined together.
shuffled_word = "".join(shuffled_list)

# Step 4: Print the shuffled word
print("Shuffled word:", shuffled_word)
