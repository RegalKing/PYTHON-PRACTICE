
# Function = a block of code that is only executed when it is called, this is also known as invoking a function

def hello():
    print("Hello, world!")

for i in range(2):
    hello()

def greeting(name, surname):
    print(f"Hello, {name} {surname}!") # equivalent without f-string formatting: print("Hello, " + name + " " + surname + "!")

greeting("Bill","Gates")