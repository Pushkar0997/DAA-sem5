# Matrix Multiplication


def multiply_matrix(A, B):
    rows_A = len(A)
    cols_A = len(A[0])

    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication is not possible")
        return

    C = [[0 for j in range(cols_B)] for i in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


print("Enter Matrix A")

r1 = int(input("Enter rows: "))
c1 = int(input("Enter columns: "))

A = []

for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input("Enter element: ")))
    A.append(row)


print("\nEnter Matrix B")

r2 = int(input("Enter rows: "))
c2 = int(input("Enter columns: "))

B = []

for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input("Enter element: ")))
    B.append(row)


C = multiply_matrix(A, B)

if C:
    print("\nResult Matrix:")

    for row in C:
        print(row)