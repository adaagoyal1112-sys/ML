import numpy as np
p = np.array([[1, 2],
              [2, 3]])

q = np.array([[4, 5],
              [6, 7]])
result = np.matmul(p, q)
print("matrix mult:")
print(result)

covariance = np.cov(p.flatten(), q.flatten())
print("\n covariance: ")
print(covariance)