import random
import statistics

lst1 = []

for i in range(100):
    lst1.append(random.randint(100, 150))

print("Random Numbers:")
print(lst1)

print("Mean:", statistics.mean(lst1))
print("Median:", statistics.median(lst1))
print("Mode:", statistics.mode(lst1))