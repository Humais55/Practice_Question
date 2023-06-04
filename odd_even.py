# Write a program which prints odd and even numbers, separately, from 1 to n where n is user input
# (The output should be like: Odd Number: 1,3,5,... Even Numbers = 2,4,6,...).
# It should also calculate the sum of odd and even numbers (1 to n) separately and display both.

def print_odd_even_numbers(num):
    odd_numbers = []
    even_numbers = []
    for num in range(1, num + 1):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print(f"\nOdd Numbers: {', '.join(map(str, odd_numbers))}")
    print(f"\nEven Numbers: {', '.join(map(str, even_numbers))}")


def calculate_sum(numbers):
    return sum(numbers)


n = int(input("Enter a number (n): "))

odd_numbers = []
even_numbers = []

for num in range(1, n + 1):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"\nOdd Numbers: {', '.join(map(str, odd_numbers))}")
print(f"\nEven Numbers: {', '.join(map(str, even_numbers))}")

sum_odd = calculate_sum(odd_numbers)
sum_even = calculate_sum(even_numbers)

print(f"\nSum of Odd Numbers: {sum_odd}")
print(f"\nSum of Even Numbers: {sum_even}")
