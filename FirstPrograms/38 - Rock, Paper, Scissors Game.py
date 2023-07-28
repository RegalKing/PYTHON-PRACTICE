
import random

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


player_stopped = False
wins = 0
losses = 0
draws = 0
percentage = 0

choices = ["rock", "paper", "scissors"]
while player_stopped != True:
    try:
        computer = random.choice(choices)
        print(f"{MAGENTA}++++++++++++++++++++++++++++++++{RESET}")
        user_choice = input("The computer has randomly selected {YELLOW}rock{RESET} or {YELLOW}paper{RESET} or {YELLOW}scissors{RESET}\nType \"stop\" if you want to quit playing\nType \"rock\", \"paper\" or \"scissors\" to try and win versus the computer: ")
        print(f"{MAGENTA}++++++++++++++++++++++++++++++++{RESET}")

        if user_choice == "stop":
             player_stopped = True
             continue
        if user_choice not in choices: # Not in - my first time using this thing in Python
            raise ValueError
        print(f"{CYAN}--------------------------------{RESET}")

        if (user_choice==computer): # Handle the draw edge case
            print(f"It's a draw! You have both picked {computer}")
            draws+=1

        elif ((user_choice=="rock" and computer=="paper") or (user_choice=="paper" and computer=="scissors") or (user_choice=="scissors" and computer=="rock")): # Check if user wins
            print(f"You {GREEN}win{RESET}! You picked {GREEN}{user_choice}{RESET} while the computer picked {RED}{computer}{RESET}")
            wins+=1

        else:
            print(f"You {RED}lose{RESET}! You picked {RED}{user_choice}{RESET} while the computer picked {GREEN}{computer}{RESET}") # Print out the other cases where the user loses
            losses+=1

        if (wins==0):
            percentage = 0
        elif wins!=0 and losses==0:
            percentage = 100
        else:
            percentage = (wins/(wins+losses))*100
                

        print(f"Your win/loss ratio: {CYAN}{percentage:.2f}%{RESET} ({GREEN}{wins}W{RESET}/{RED}{losses}L{RESET}/{draws}D)")
        print(f"{CYAN}--------------------------------{RESET}")

    except ValueError:
        print(f"Invalid input, please type either {YELLOW}\"rock\"{RESET} or {YELLOW}\"scissors\"{RESET} or {YELLOW}\"paper\"{RESET}")
print (f"{RED}The game has ended!{RESET}")
print (f"Your final win/loss ratio is: {CYAN}{percentage:.2f}%{RESET}\nTotal results: {GREEN}{wins}{RESET} Wins, {RED}{losses}{RESET} Losses and {draws} Draws!")
