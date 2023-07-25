
# break -    used to terminate the loop entirely [Same as in other programming languages]
# continue - immediately skips to the next iteration of the loop [Same as in other programming languages]
# pass -     does nothing, acts as a placeholder because a statement in python can't be empty [Unique to Python]

number = 5

if number!=5:
    pass

for i in range(1,10):
    if i%2==0:
        print(f"{i} is divisible by two!")
    else:
        continue # this else statement is completely unnecessary logic-wise and it changes absolutely nothing, but just for the sake of writing an example I wrote this extended logic

for i in range(10):
    if i==5:
        break; # the loop will exit once the loop hits its 6th iteration, because I set the counting of the loop to start with 0 -> as its the default value for in range statements in Python
    else:
        print(f"{i} is a number that is not higher than 5")