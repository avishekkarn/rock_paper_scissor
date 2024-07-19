import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/scissior or Q for Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissor = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "paper" and computer_pick == "rock":
        print("You won the game!")
        user_wins += 1
        print("Your Score is", user_wins)
        
    elif user_input == "rock" and computer_pick == "scissor":
        print("You won the game!")
        user_wins += 1
        print("Your Score is", user_wins)
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won the game!")
        user_wins += 1
        print("Your Score is", user_wins)
    elif user_input == "scissor" and computer_pick =="scissor" or user_input == "paper" and computer_pick =="paper" or user_input == "rock" and computer_pick =="rock":
        print("It's a tie!")
        
    else:
        print("You lost the game!")
        computer_wins += 1
        print("Computer Score is", computer_wins)
        
print("Your Total Score Is",user_wins)
print("Computer Total Score Is",computer_wins)
if user_wins > computer_wins:
    print("Cogratulations!, You are Pro")
else:
    print("You can't defeat me. LOL!")    
print("Good Bye!")
    