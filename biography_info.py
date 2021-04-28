print("Welcome to Biography Data! \n")
print("Enter The Information Asked \n")

def biography():
    name = input("Enter Your Name: ")
    dob = input ("Enter Your Date Of Birth in MM DD YYYY Format: ")
    address = input("Enter Your Address: ")
    goals = input ("What are your Personal Goals: ")


    user_choice = print(input("are you satisfied with the details you filled? \n"))

    if user_choice == 'y' or 'Y':
        print(f"You Name is {name}.")
        print(f"You were Born in {dob}.")
        print(f"Your Address is {address}.")
        print(f"Your Goals are {goals}.")

    else:
        print("Run the Program Again!")

biography()
