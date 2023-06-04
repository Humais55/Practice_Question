def bubblesort(lst):
    n = len(lst)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


size = int(input("Enter no of elements: "))
print("\n")
LisT = []

for i in range(size):
    x = int(input(f"Enter element {i+1}: "))
    LisT.append(x)

print("\nBefore Sorting: ", LisT)

sort = bubblesort(LisT)

print("\nAfter Sorting: ", sort)

