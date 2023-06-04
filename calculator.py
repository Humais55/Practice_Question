num1 = float(input("\nEnter the First number: "))
num2 = float(input("Enter the Second number: "))

choices = ["Addition", "Subtraction", "Multiplication", "Division"]

print("\nCalculation options: ")
for i, option in enumerate(choices, 1):
    print(f"{i}. {option}")

choice = int(input("\nEnter the operation number: "))

if choice == 1:
    result = num1 + num2
    operation = "Addition"
elif choice == 2:
    result = num1 - num2
    operation = "Subtraction"
elif choice == 3:
    result = num1 * num2
    operation = "Multiplication"
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        operation = "Division"
    else:
        print("\nError: Cannot divide by zero.")
        exit()
else:
    print("\nError: Invalid operation number.")
    exit()

print(f"\nThe {operation} of {num1} and {num2} = {result:.2f}")