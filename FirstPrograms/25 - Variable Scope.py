
# Okay, now I am seeing that all of these recent tasks are the exact same as in other languages that I've written a million times, but I'll do it anyways just to practice writing Python and to help people if anyone will use this repository to help learning programming in Python specifically.

# Variable scope in Python refers to the area of the code where a particular variable is accessible and can be referenced. The scope of a variable is determined by where it is defined in the code, and it can be classified into two main categories: global scope and local scope.

# Global variable
global_var = 100

def my_function():
    # Local variable
    local_var = 5
    print(f"Inside the function - local_var: {local_var}")

    # Accessing the global variable inside the function
    print(f"Inside the function - global_var: {global_var}")

my_function()
# Output:
# Inside the function - local_var: 5
# Inside the function - global_var: 100

# Attempting to access 'local_var' outside the function will raise an error
# print(local_var)  # This line would raise a NameError

# Local variable within a nested function
def outer_function():
    outer_var = "I am from an outer function"

    def inner_function():
        # Nested function can access variables from the enclosing function
        print(outer_var)

    inner_function()

outer_function()
# Output: I am from outer function

# Local variable in a nested scope has priority over a global variable
count = 100

def my_function():
    count = 10  # This is a local variable, it has priority and thus overwrites the global variable 'count' in this function
    print(f"Inside the function - count: {count}")

my_function()
# Output: Inside the function - count: 10

print(f"Outside the function - count: {count}")
# Output: Outside the function - count: 100 (global 'count' remains unchanged)
