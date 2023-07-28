
# Basic text colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Reset all formatting
RESET = "\033[0m"

questions = {
    "How do you run a python program from the file main.py?": "C",
    "What is the capital city of Germany?": "C",
    "Who was the president of the United States in 2023?": "B",
    "When was Google founded?":"B",
    "When was the first Youtube video posted?":"E"
}

options = [
    ["python3-run main.py", "run main.py", "py main.py"],  # 2D array for the possible answers
    ["Washington D.C.", "Montreal", "Berlin"],
    ["Donald Trump", "Joe Biden", "Barack Obama", "Ronald Reagan"],
    ["1997","1998","1999","2000","2001"],
    ["2001","2002","2003","2004","2005"]
]

right_answers = 0
wrong_answers = 0

for index, (question, correct_answer) in enumerate(questions.items(), start=1): # questions.items() returns key-value pairs which translate to question and correct_answer, start=1 transfers to index
    print(f"{CYAN}--------------------------------{RESET}")
    print(f"Your question {index} is: {CYAN}{question}{RESET}")
    for idx, possible_answer in enumerate(options[index-1], start=1):
        print(f"{YELLOW}{chr(idx+64)}{RESET} {MAGENTA}{possible_answer}{RESET}") # chr(idx+64) converts numbers to letters, 1=A, 2=B, etc (ASCII for A is 65, ASCII for B is 66, ...)
    user_input = input("Which answer do you think is correct? (Letter A/B/C/...)): ")
    if user_input == correct_answer:
        print(f"{GREEN}Correct, {user_input} is the correct answer!{RESET}")
        right_answers+=1
    else:
        print(f"{RED}Wrong, {user_input} is the wrong answer!{RESET}") # You could also add this -> The right answer is {GREEN}{correct_answer}{RESET}, but I don't like it, let them play again and find the right one :D
        wrong_answers+=1
print(f"{CYAN}--------------------------------{RESET}")
print(f"You got {GREEN}{right_answers}{RESET} correct answers and {RED}{wrong_answers}{RESET} wrong answers!")
    

