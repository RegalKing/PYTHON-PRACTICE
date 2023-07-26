
# In Python, kwargs stands for "keyword arguments." It allows you to pass a variable number of keyword arguments (also known as named arguments) to a function. The syntax for defining a function that accepts variable-length keyword arguments is to use double asterisks (**) before the parameter name.

#Here's how kwargs works:

#        **kwargs (Keyword Variable-length Argument):
#        When you prefix a parameter with ** in the function definition, it allows the function to accept any number of keyword arguments (zero or more). These arguments are collected into a dictionary #        inside the function.
#        It is useful when you want to create functions that can handle additional named parameters beyond the ones explicitly defined in the function signature.

def bonjour(**kwargs): # **kwargs is a DICTIONARY of KEY-VALUE components
    print(f"Hello {kwargs['first_name']} {kwargs['last_name']}")
    # As we can see above we can use kwargs['key'] to access a value

bonjour(first_name="Donald", last_name="Trump")

print()
def hello(**names): 
    for key, value in names.items():
        print (f"{key}:{value}")

hello(name = "Joe", surname = "Biden", age = 20)


