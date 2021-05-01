print("Simple Calculator Using Python")
unit = (input("Enter The Unit, C or F: ")).lower()
temp = float(input("Enter any number: "))

if unit == "c":
    result = (temp * 9/5) + 32
    print(f"Converted Unit is {result} F")

else:
    result = (temp * 1.8) + 32
    print(f"Convereted Unit is {result} C")