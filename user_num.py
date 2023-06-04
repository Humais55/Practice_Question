#Write a program to enter the numbers till the user wants and at the end
# it should display the maximum and minimum number entered.

numbers = []

while True:
    num = input("\nEnter a number (or 'q' to quit): ")
    if num.lower() == 'q':
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("\nInvalid input. Please enter a number or 'q' to quit.")

if numbers:
    maximum = max(numbers)
    minimum = min(numbers)
    print(f"\nMaximum number entered: {maximum}")
    print(f"\nMinimum number entered: {minimum}")
else:
    print("\nNo numbers were entered.")
