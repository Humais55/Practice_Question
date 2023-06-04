def selection_sort(lst):
    n = len(lst)

    for k in range(n - 1):
        min_idx = k
        for j in range(min_idx + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
            if k != min_idx:
                lst[k], lst[min_idx] = lst[min_idx], lst[k]
    return lst


size = int(input("Enter no of elements: "))
print("\n")
LisT = []

for i in range(size):
    x = int(input(f"Enter element {i+1}: "))
    LisT.append(x)

print("\nBefore Sorting: ", LisT)

sort = selection_sort(LisT)

print("\nAfter Sorting: ", sort)
