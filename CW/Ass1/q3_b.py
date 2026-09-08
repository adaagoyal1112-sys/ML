import numpy as np
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
integer_elements = array[array % 1 == 0]
print("Integer elemnts only : ")
print(integer_elements)
print(integer_elements.astype(int))

float_elements = array[array % 1 != 0]
print("\n float elements only:")
print(float_elements)

