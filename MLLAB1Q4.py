# Matrix Transpose

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

A = []

print("Enter the matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    A.append(row)

print("Transpose of the matrix:")

for i in range(c):
    for j in range(r):
        print(A[j][i], end=" ")
    print()