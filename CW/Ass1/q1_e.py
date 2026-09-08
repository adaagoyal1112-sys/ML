import numpy as np

g = np.matrix([4, 1, 9, 12, 3, 1, 4, 5, 6])
g = np.matrix([4, 1, 9, 12, 3, 1, 4, 5, 6])

print("Sum of all elements:", np.sum(g))
print("Row-wise sum:", np.sum(g, axis=1))
print("Column-wise sum:", np.sum(g, axis=0))