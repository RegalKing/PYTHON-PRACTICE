
# In Python, dictionaries are a fundamental data structure used to store and manage collections of key-value pairs. They are sometimes also referred to as associative arrays or hash maps in other programming languages. Dictionaries are extremely versatile and widely used in Python due to their efficiency and flexibility.
# Dictionaries are fast because they use hashing

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
             "China":"Beijing",
              "Russia":"Moscow" }
              # keys : values

# You can also use ' ' instead of " " for strings in dictionaries
#
# capitals = {'USA':'Washington D.C.',
#             'India':'New Delhi',
#              'China':'Beijing',
#               'Russia':'Moscow' }

print(capitals["China"])

print(capitals.get("Germany")) # for the key of Germany, if it exists, otherwise it will print NONE
print(capitals.keys()) # This will print all the keys 
print(capitals.values()) # This will print all the values
print(capitals.items()) # Print BOTH THE KEYS AND THE VALUES

print()
# We can also loop through dictionaries
for key, value in capitals.items():
    print(key, value)
    
capitals.update({"Germany":"Berlin"}) # Add a new key-value pair 
print(capitals)
capitals.update({"USA":"Los Angeles"}) # Change an existing key-value pair
print(capitals)

print()
capitals.pop("Russia") # Pop removes the key-value pair from the dictionary
print(capitals)
