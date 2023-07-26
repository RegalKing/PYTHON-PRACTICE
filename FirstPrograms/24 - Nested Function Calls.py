
# Nested function calls in Python refer to the situation where you call a function inside another function's argument list. It means the return value of one function is used as an argument for another function.

def square(x):
    return x * x

def add(a, b):
    return a + b

# Nested function calls
result = add(square(2), square(3))
print(result)  # Output: 13 (2 * 2 + 3 * 3)

# num = input("Input number:")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Input your number: ")))))
