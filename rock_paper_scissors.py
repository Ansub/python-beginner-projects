import random 

user_input = input ("Enter a Choice (Rock, Paper, Scissors): ")
actions = random.choice(["rock", "paper","scissors"])
print(f"\n you chose {user_input}, computer chose {actions}. \n")

# tie situation
if user_input == actions:
    print(f"Both of the Players Selected {user_input} it's a tie")

# rock situation
elif user_input == "rock":
    if actions == "scissors":
        print("Rock Smashes Scissors! You Win!")
    else:
        print("paper covers rock! You Lose.")

# paper situation

elif user_input == "paper":
    if actions == "rock":
        print("Paper Covers Rock, You Win")
    else:
        print("Scissor cuts Paper, You Lose")
        
# scissors situation
elif user_input == "scissors":
    if actions == "paper":
        print("Scissors Cuts Paper, You Win")
    else:
        print("Rock Breaks Scissors, You Lose")
