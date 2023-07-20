
# If statetement - a block of code that will execute if the given condition is true

age = int(input("How old are you? "))

if age<18: 
 print("You are not an adult! You are only "+str(age)+" years old!")
elif age<100:
 print("You are a young soul! You are only "+str(age)+" years old!")
else:
 print("You are a century old! You are "+str(age)+" years old!")