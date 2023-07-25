# Let's draw a tree!

# ----x----
# ---xxx---
# --xxxxx--
# -xxxxxxx-
# xxxxxxxxx

tree_height = int(input("What will the height of the tree be? "))
print() # Newline for aesthetic purposes

# We can see by the height that the initial number of spaces equals the starting height and then decreases by 1 with each line
# the X's start with 1 and increase by +2 each time

number_of_chars=1

while tree_height > 0:
    print(" " * (tree_height-1),end="")
    print("x" * number_of_chars,end="")
    print()
    number_of_chars+=2
    tree_height-=1

# Let's make a reverse tree!

#       index|number_of_chars   
# xxxxxxx 0 7
# -xxxxx- 1 5 
# --xxx-- 2 3
# ---x--- 3 1

tree_height = int(input("What will the height of the tree be? "))
print() # Newline for aesthetic purposes

number_of_chars=1

for i in range(tree_height):
    if i==1:
        continue
    else:
        number_of_chars+=2

for i in range(tree_height):
    print(" " * i,end="")
    print("x" * number_of_chars,end="")
    number_of_chars -= 2
    print(" " * i,end="")
    print()

# I realized I do not even need a nested loop for the examples I made due to python having string multiplication :D nice, so let's write an actual nested loop for fun

print("Now time for an actual nested loop down below:")

for i in range(3):
    print("x",end="")
    for j in range(5):
        print("y",end="")
    print()


    
