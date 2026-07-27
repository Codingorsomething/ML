
# ==========================================================
# AI Lab Assignments A3 - A11
# Marketing Campaign Dataset
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.spatial.distance import minkowski as scipy_minkowski

# ---------------- READ DATASET ---------------- #

df = pd.read_excel("marketing_campaign.xlsx")

# ==========================================================
# COMMON FUNCTIONS (Reused)
# ==========================================================

def average(values):
    total_sum = 0
    for item in values:
        total_sum += item
    return total_sum / len(values)


def variance_calc(values):
    avg = average(values)
    total = 0
    for item in values:
        total += (item - avg) ** 2
    return total / len(values)


def std_dev(values):
    return variance_calc(values) ** 0.5


def minkowski_distance(sample1, sample2, p):
    total = 0
    for i in range(len(sample1)):
        total += abs(sample1[i] - sample2[i]) ** p
    return total ** (1 / p)


def dot_product(vector1, vector2):
    ans = 0
    for i in range(len(vector1)):
        ans += vector1[i] * vector2[i]
    return ans


def euclidean_length(vector):
    total = 0
    for value in vector:
        total += value ** 2
    return total ** 0.5


# ==========================================================
# A3 - LABEL ENCODING
# ==========================================================

def label_encode(column):
    unique = []
    for value in column:
        if value not in unique:
            unique.append(value)

    mapping = {}
    for i in range(len(unique)):
        mapping[unique[i]] = i

    encoded = []
    for value in column:
        encoded.append(mapping[value])

    return encoded


encoded_df = df.copy()

for col in ["Education", "Marital_Status"]:
    if col in encoded_df.columns:
        encoded_df[col] = label_encode(encoded_df[col])

print("\n===== A3 COMPLETE =====")
print(encoded_df.shape)

# ==========================================================
# A4 / A5 / A6
# ==========================================================

records = encoded_df.select_dtypes(include="number")

sample_a = records.iloc[0].tolist()
sample_b = records.iloc[1].tolist()

print("\n===== A4 =====")
print("Manhattan:", minkowski_distance(sample_a, sample_b, 1))
print("Euclidean:", minkowski_distance(sample_a, sample_b, 2))

print("\n===== A5 =====")
orders = []
dist_values = []

for p in range(1,11):
    d = minkowski_distance(sample_a,sample_b,p)
    orders.append(p)
    dist_values.append(d)
    print("p =",p,"Distance =",d)

plt.figure()
plt.plot(orders,dist_values,marker="o")
plt.title("Minkowski Distance vs p")
plt.xlabel("p")
plt.ylabel("Distance")
plt.grid(True)
plt.show()

print("\n===== A6 =====")
for p in range(1,11):
    my_ans = minkowski_distance(sample_a,sample_b,p)
    scipy_ans = scipy_minkowski(sample_a,sample_b,p)
    print("p =",p,"Mine =",round(my_ans,4),"SciPy =",round(scipy_ans,4))

# ==========================================================
# A7
# ==========================================================

print("\n===== A7 =====")
print("My Dot:",dot_product(sample_a,sample_b))
print("NumPy Dot:",np.dot(sample_a,sample_b))

print("My Norm A:",euclidean_length(sample_a))
print("NumPy Norm A:",np.linalg.norm(sample_a))

print("My Norm B:",euclidean_length(sample_b))
print("NumPy Norm B:",np.linalg.norm(sample_b))

# ==========================================================
# A8
# ==========================================================

print("\n===== A8 =====")

for feature in records.columns:
    values = records[feature].tolist()
    print(feature)
    print("Mean:",average(values))
    print("Variance:",variance_calc(values))
    print("Std Dev:",std_dev(values))
    print("---------------------")

# ==========================================================
# A9
# ==========================================================

print("\n===== A9 =====")

my_mean=[]
my_std=[]

for feature in records.columns:
    vals = records[feature].tolist()
    my_mean.append(average(vals))
    my_std.append(std_dev(vals))

numpy_mean=np.mean(records,axis=0)
numpy_std=np.std(records,axis=0)

for i,col in enumerate(records.columns):
    print(col,
          round(my_mean[i],4),
          round(numpy_mean[i],4),
          round(my_std[i],4),
          round(numpy_std[i],4))

# ==========================================================
# A10
# ==========================================================

print("\n===== A10 =====")

feature_values = records["Income"].dropna()

print("Mean:",np.mean(feature_values))
print("Variance:",np.var(feature_values))

hist,bins=np.histogram(feature_values,bins=10)

for i in range(len(hist)):
    print("Bucket",i+1,bins[i],"to",bins[i+1],"Frequency:",hist[i])

plt.figure()
plt.hist(feature_values,bins=10,edgecolor="black")
plt.title("Income Histogram")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ==========================================================
# A11
# ==========================================================

dataset = records.values.tolist()

def find_center(group):
    center=[]
    total_features=len(group[0])

    for col in range(total_features):
        temp=[]
        for row in group:
            temp.append(row[col])
        center.append(average(temp))

    return center


def run_kmeans(dataset,k):

    centers=random.sample(dataset,k)

    while True:

        groups=[[] for _ in range(k)]

        for sample in dataset:

            dist_list=[]

            for center in centers:
                dist_list.append(minkowski_distance(sample,center,2))

            closest_index=dist_list.index(min(dist_list))
            groups[closest_index].append(sample)

        updated_centers=[]

        for grp in groups:
            if len(grp)==0:
                updated_centers.append(random.choice(dataset))
            else:
                updated_centers.append(find_center(grp))

        if updated_centers==centers:
            break

        centers=updated_centers

    return groups,centers

groups,centers=run_kmeans(dataset,3)

print("\n===== A11 =====")

for i in range(len(groups)):
    print("Cluster",i+1)
    print("Size:",len(groups[i]))
    print("Center:",centers[i])
    print()
