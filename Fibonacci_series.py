#Write a python program which takes total number of entities n as user input and prints Fibonacci series.
# Fibonacci series is a series where the current number is the sum of previous two terms
# i.e., 0, 1, 1, 2, 3, 5, 8, 13, 21, ((n- 1)+(n-2)). Use arrays.

def fibonacci_series(n):
    fib_series = [0, 1]  # Initialize the Fibonacci series with first two numbers

    for i in range(2, n):
        # Calculate the current Fibonacci number as the sum of the previous two numbers
        fib_num = fib_series[i-1] + fib_series[i-2]
        fib_series.append(fib_num)

    return fib_series

n = int(input("Enter the total number of entities (n): "))

fib_series = fibonacci_series(n)

print("\nFibonacci Series:")
for num in fib_series:
    print(num, end=" ")
