import numpy as np
x = np.array([[2, 3, 4],
              [3, 2, 9]])

y = np.array([[1, 5, 0],
              [5, 10, 3]])
print("Inner product: ")
print(np.inner(x, y))

print("\nOuter product: ")
print(np.outer(x, y))

from itertools import product

cartesian = list(product(x.flatten(), y.flatten()))
print("\nCartesian product: ")
print(cartesian)
