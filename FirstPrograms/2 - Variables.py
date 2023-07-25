name = "Bro"
print(name)
print(type(name)) # string

name=5
print(name)
print(type(name)) # int

name=0.5242
print(name)
print(type(name)) # float

name=True
print(name)
print(type(name)) # boolean

num_one = 20
num_two = 0.42242
print(num_one + num_two) # we can easily combine an int and a float

name="Alex has this many years: "
# print(name + num_one) this wont work, we need to convert num_one to string first to be able to print a STRING and a different datatype together
print(name + str(num_one) ) # this will work, by enclosing it in str() we have converted num_one to a string and can now print it alongside another string