
# Tuples are IMMUTABLE LISTS, which means its elements cannot be CHANGED (REMOVED, ADDED OR CHANGED)

student = (19, 20, "Alex", 20)

print(student)
print(student.count(20))
print(student.index(20)) # Finds the first index that matches the value 20

print()

for i in student: # Prints each element of the Tuple individually
    print(i)

if ("Alex") in student:
    print("Cool, Alex is a student!")