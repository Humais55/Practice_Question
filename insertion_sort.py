def insertion_sort(lst):
    for k in range(1, len(lst)):
        anchor = lst[k]
        j = k - 1
        while j >= 0 and anchor < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = anchor

    return lst


size = int(input("Enter no of elements: "))
print("\n")
LisT = []
for i in range(size):
    x = int(input(f"Enter element {i + 1}: "))
    LisT.append(x)

print("\nBefore Sorting: ", LisT)

sort = insertion_sort(LisT)

print("\nAfter Sorting: ", sort)