import numpy as np
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
values, counts = np.unique(y, return_counts=True)

max_count = np.max(counts)
most_frequent = values[counts == max_count]

print("Most frequent values:", most_frequent)

for value in most_frequent:
    print(value, "indices:", np.where(y == value)[0])
    