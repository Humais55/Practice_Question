tempe = float(input("Enter temp to be converted: "))
choices = ["Fahrenheit to Celsius", "Celsius to Fahrenheit"]

print("Conversion Options: ")
for i, option in enumerate(choices, 1):
    print(f"{i}. {option}")

choice = int(input("Enter the conversion option number: "))

if choice == 1:
    C = (tempe - 32) / 1.8
    print(f"{tempe} degrees Fahrenheit is equal to {C:.2f} degrees Celsius.")
elif choice == 2:
    F = (tempe * 1.8) + 32
    print(f"{tempe} degrees Celsius is equal to {F:.2f} degrees Fahrenheit.")
else:
    print("Please select a valid option!")