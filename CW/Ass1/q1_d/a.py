import numpy as np
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
values, counts = np.unique(x, return_counts=True)

most_frequent = values[np.argmax(counts)]
indices = np.where(x == most_frequent)[0]

print("Most frequent value:", most_frequent)
print("Indices:", indices)