import numpy as np
arr = np.array([[-1, 2, 3],
                [-4, 5, -6]])
print(np.abs(arr))

print("25th percentile:", np.percentile(arr.flatten(), 25))
print("50th percentile:", np.percentile(arr.flatten(), 50))
print("75th percentile:", np.percentile(arr.flatten(), 75))

print("25th:", np.percentile(arr, 25, axis=0))
print("50th:", np.percentile(arr, 50, axis=0))
print("75th:", np.percentile(arr, 75, axis=0))

print("25th:", np.percentile(arr, 25, axis=1))
print("50th:", np.percentile(arr, 50, axis=1))
print("75th:", np.percentile(arr, 75, axis=1))

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard deviation:", np.std(arr))

print("Column mean:", np.mean(arr, axis=0))
print("Column median:", np.median(arr, axis=0))
print("Column std:", np.std(arr, axis=0))

print("Row mean:", np.mean(arr, axis=1))
print("Row median:", np.median(arr, axis=1))
print("Row std:", np.std(arr, axis=1))