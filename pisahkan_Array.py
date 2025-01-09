import numpy as np 


# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# a, b, c = np.array_split(arr, arr3)
# print(a, b, c)

# arr = np.array([1, 2, 3, 4, 5, 6], dtype=np.int64)
# pisahkan = np.split(arr, (2, 3))
# print(pisahkan)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# hasil1, hasil2 = np.vsplit(arr, 2)
# print(hasil1),

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
hasil_split = np.dsplit(arr3d, 2)
print(hasil_split)
