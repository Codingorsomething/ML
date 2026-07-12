r1 = int(input("Rows of Matrix A: "))
c1 = int(input("Columns of Matrix A: "))

A = []
print("Enter Matrix A:")
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(int(input()))
    A.append(row)

r2 = int(input("Rows of Matrix B: "))
c2 = int(input("Columns of Matrix B: "))

B = []
print("Enter Matrix B:")
for i in range(r2):
    row = []
    for j in range(c2):
        row.append(int(input()))
    B.append(row)

if c1 != r2:
    print("Cannot multiply the matrices.")
else:
    C = []

    for i in range(r1):
        row = []
        for j in range(c2):
            row.append(0)
        C.append(row)

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    print("Result:")
    for i in C:
        print(i)