import numpy as np
array = np.array([10, 52, 62, 16, 16, 54, 453])

print("Sorted array: ")
print(np.sort(array))

print("\nIndices of sorted array:")
print(np.sort(array))

print("\n 4 smallest elements: ")
print(np.sort(array)[:4])

print("\n5 largest elements:")
print(np.sort(array)[:5])