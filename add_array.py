# Write a program to add two array A and B of size m x n

def add_arrays(A, B, m, n):
    result = [[0 for _ in range(n)] for _ in range(m)]  # Initialize the result array with zeros

    for i in range(m):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]  # Add corresponding elements of A and B

    return result

# Main program
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

# Input array A
A = []
print("\nEnter the elements of Array A:")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    A.append(row)

# Input array B
B = []
print("\nEnter the elements of Array B:")
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(element)
    B.append(row)

# Add arrays A and B
result = add_arrays(A, B, m, n)

# Display the result
print("\nResultant Array (Sum of A and B):\n")
for row in result:
    for element in row:
        print(element, end=" ")
    print()
