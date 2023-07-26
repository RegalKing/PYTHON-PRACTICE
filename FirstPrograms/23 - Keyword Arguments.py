
# In Python, keyword arguments are a way of passing arguments to a function by explicitly specifying the parameter names along with their corresponding values. When calling a function with keyword arguments, you provide the parameter names followed by an equal sign (=) and the values you want to assign to those parameters.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with keyword arguments
greet(name="Alice", age=30)
greet(age=25, name="Bob")
