import numpy as np

array_2d: np.ndarray = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int64)
flatten_array = array_2d.flatten()
flatten_array[0] = 17
print(array_2d)

contoh_Array = np.array([[1, 2, 3], [4, 5, 6]])
array = contoh_Array.ravel()
array[0] = 17
print(contoh_Array)
contoh_array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
array_1d = contoh_array.reshape(-1)
print(array_1d)

