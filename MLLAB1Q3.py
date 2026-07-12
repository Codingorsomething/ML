n = int(input("Enter number of elements in list 1: "))
lst1 = []

print("Enter elements:")
for i in range(n):
    lst1.append(int(input()))

m = int(input("Enter number of elements in list 2: "))
lst2 = []

print("Enter elements:")
for i in range(m):
    lst2.append(int(input()))

count = 0

for i in lst1:
    if i in lst2:
        count += 1

print("Number of common elements:", count)