import numpy as np

n_array = np.array([[55, 25, 15],
                    [30, 44,  2],
                    [11, 45, 77]])

print(np.trace(n_array))

eigenvalues = np.linalg.eigvals(n_array)

print(eigenvalues)

eigenvalues, eigenvectors = np.linalg.eig(n_array)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

inverse = np.linalg.inv(n_array)

print("\nInverse:")
print(inverse)

det = np.linalg.det(n_array)

print("\n Determinant:")
print(det)

