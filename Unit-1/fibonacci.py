import time


# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Iterative Fibonacci
def fibonacci_iterative(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


n = int(input("Enter n: "))

# Recursive
start = time.time()
result1 = fibonacci_recursive(n)
end = time.time()

print("Recursive Fibonacci:", result1)
print("Recursive Time:", end - start, "seconds")

# Iterative
start = time.time()
result2 = fibonacci_iterative(n)
end = time.time()

print("Iterative Fibonacci:", result2)
print("Iterative Time:", end - start, "seconds")