# Write a menu-driven python program to do following operation on two-dimensional array A of size m x n.
# You should use user-defined functions which accept 2-D array A, and its size m and n as arguments.
# The options are:
# a. To input elements into matrix of size m x n
# b.To display elements of matrix of size m x n
# c.Sum of all elements of matrix of size m x n
# d. To display row-wise sum of matrix of size m x n
# e.To display column-wise sum of matrix of size m x n
# f.To create transpose of matrix B of size n x m

def input_elements(matrix, m, n):
    print("Enter the elements of the matrix:")
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter element at position ({i}, {j}): "))
            row.append(element)
        matrix.append(row)

def display_elements(matrix):
    print("Matrix elements:")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def sum_of_elements(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum += element
    print(f"Sum of all elements: {total_sum}")

def row_wise_sum(matrix):
    print("Row-wise sum:")
    for row in matrix:
        row_sum = sum(row)
        print(row_sum, end=" ")
    print()

def column_wise_sum(matrix, m, n):
    print("Column-wise sum:")
    for j in range(n):
        col_sum = 0
        for i in range(m):
            col_sum += matrix[i][j]
        print(col_sum, end=" ")
    print()

def create_transpose(matrix, m, n):
    transpose = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            transpose[j][i] = matrix[i][j]
    return transpose


# Main program
matrix = []
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

while True:
    print("\n-------- Menu --------")
    print("1. Input elements into matrix")
    print("2. Display elements of matrix")
    print("3. Sum of all elements of matrix")
    print("4. Display row-wise sum of matrix")
    print("5. Display column-wise sum of matrix")
    print("6. Create transpose of matrix")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        input_elements(matrix, m, n)
    elif choice == 2:
        display_elements(matrix)
    elif choice == 3:
        sum_of_elements(matrix)
    elif choice == 4:
        row_wise_sum(matrix)
    elif choice == 5:
        column_wise_sum(matrix, m, n)
    elif choice == 6:
        transpose = create_transpose(matrix, m, n)
        print("Transpose of matrix:")
        display_elements(transpose)
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please enter a valid option (1-7).")
