# Recursive Binary Search
def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search_recursive(arr, key, low, mid - 1)
    else:
        return binary_search_recursive(arr, key, mid + 1, high)


# Iterative Binary Search
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print("1. Search ISBN")
print("2. Search Title")

choice = int(input("Enter choice: "))

n = int(input("Enter number of books: "))

books = []

for i in range(n):
    if choice == 1:
        books.append(int(input("Enter ISBN: ")))
    else:
        books.append(input("Enter Title: "))

# Sorting is necessary for binary search
books.sort()

print("\nSorted records:")
print(books)

key = int(input("Enter ISBN to search: ")) if choice == 1 else input("Enter Title to search: ")

# Recursive search
position = binary_search_recursive(books, key, 0, len(books) - 1)

if position != -1:
    print("Recursive: Record found at position", position)
else:
    print("Recursive: Record not found")

# Iterative search
position = binary_search_iterative(books, key)

if position != -1:
    print("Iterative: Record found at position", position)
else:
    print("Iterative: Record not found")