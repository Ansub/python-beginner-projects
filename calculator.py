operations = input("Would you like to add/subtract/multiply/divide? ").lower()

if operations == "add" or "subtract" or "multiply" or "divide": 
    print(f"You chose {operations}")
else: 
    print("Wrong Inputs have been Entered")
#taking numbers input
num1= (input("Enter The First Number: "))
num2 = (input("Enter The Second Number: "))

#program
try: 
    num1, num2 = float(num1), float(num2)
    if operations == "add":
        result = num1 + num2
        print(f"sum of two numbers are: {result}")

    elif operations == "subtract":
        result = num1 - num2
        print(f"subtraction of two number are: {result}")


    elif operations == "multiply":
        result = num1 * num2
        print(f"multiplication of two numbers are: {result}")


    elif operations == "divide":
        result = num1 / num2
        print(f"divison of two numbers are: {result}")

except:
    print("Sorry, Wrong Numbers have been used.")
 