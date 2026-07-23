number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

operation = input("multiplication, division, subtraction, addition?: ").lower()

if operation == "multiplication":
    result = int(number1) * int(number2)
    print(f"product: {result}")

elif operation == "division":
    if int(number2) == 0:
        print("Error. Division by zero is not allowed.")
    else:
        result = int(number1) / int(number2)
        print(f"Quotient: {result}")

elif operation == "subtraction":
    result = int(number1) - int(number2)
    print(f"Difference: {result}")

elif operation == "addition":
    result = int(number1) + int(number2)
    print(f"Sum: {result}")

else:
    print("Error. Enter a valid operation.")
