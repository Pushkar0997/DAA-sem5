import random
import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


# Test for different values of n
sizes = [10, 100, 500, 1000]

for n in sizes:
    arr = [random.randint(1, 10000) for i in range(n)]

    start = time.time()

    sorted_arr = quick_sort(arr)

    end = time.time()

    print("n =", n)
    print("Time =", end - start, "seconds")
    print()