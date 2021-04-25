import random 

def guess (x):
    random_number = random.randint(1,x) #return a random number for guess
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a Number Between 1 and {x}:'))
        print(guess)
        if guess < random_number:
            print("Sorry, guess Again. Too Low.")
        elif guess > random_number:
            print("Sorry, Guess Again. Too High.")
    print(f"Yay, Congrats. you have guessed the numnber {random_number} correctly!")

guess (10)