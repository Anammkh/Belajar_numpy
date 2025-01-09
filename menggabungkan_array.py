import numpy as np 


# contoh_array1 = np.array([[1, 2, 3]])
# contoh_array2 = np.array([[4, 5, 6]])
# gabung = np.concatenate((contoh_array1, contoh_array2), axis=1)
# print(gabung)

# a = np.array([[1, 2, 3]])
# b = np.array([[6, 4, 5]])
# gabung = np.vstack((a, b), dtype=int)
# print(gabung)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# gabung = np.hstack((a, b), dtype=np.int64)
#
# print(gabung)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# gabung = np.column_stack((a, b))
# print(gabung)

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# gabung = np.dstack((a, b))
# print(gabung)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
gabung = np.stack((a, b), axis=1)
print(f"ini numpy stack \n {gabung}")
