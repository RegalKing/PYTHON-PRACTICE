
# Slicing = create a substring by extracting characters from another string

# We can use one of the following:
# indexing [star_index : stop_index : step] 
# slice(start_index.stop_index.step)

# FIRST OPTION - indexing

name = "Alex_is_learning_Python"

first_name = name[0:4] # starting_index:stopping_index (THE STOPPING INDEX IS EXCLUDED!)

first_name = name[:4] # if the starting index is 0, we can just write :stopping_index
print(first_name)

funky = name [:8:2]
print(funky)

funky = name [::2] # if we dont write an ending index it assumes the end is the end of the string
print(funky)

reversed_name = name[::-1] # this is how to reverse a string in python using slicing
print(reversed_name)

# SECOND OPTION - slicing

website = "https://google.com"
website_two = "https://wikipedia.com"

# negative indexing in python: you can count backwards with -1, -2, -3 

slice_website = slice(8,-4) # slice_website is a SLICE OBJECT
print(website[slice_website])
print(website_two[slice_website])