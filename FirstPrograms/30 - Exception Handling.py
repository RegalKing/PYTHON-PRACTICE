
# Exception = events

try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a number to divide by:"))

    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

except Exception as e:
    print(e)
else: # If no exception occurs then the else statement will activate
    print(result)

finally: # This block of code will execute no matter if try fails or succeeds
    print("This will always execute no matter if we find an exception or not!")
