
# Logical operators - AND, OR, NOT, etc.

# In most other languages you use different things for these logical operators:
# ! in python is the word "not"
# && in python is the word "and"
# || in python is the word "or"

# Python does not have a built-in XOR, NOR, NAND function but we can write them ourselves, for example XOR:
# def xor(a, b):
#  return (a and not b) or (b and not a)

temp = 30

if temp>=0 and temp <= 30:
    print("The temperature is nice today, go outside!")
elif temp<0 or temp>30:
    print ("It is either too cold or too hot, be careful!")

stevilka = 40
if not(stevilka==50):
    print("The number is not equal to 50!")

# Now lets write a function for the NAND operator for practice 

def NAND(a, b):
 return (not(a and b))

print (NAND(1,1))

