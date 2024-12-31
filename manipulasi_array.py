import numpy as np 


array_1dimensi = np.array([1, 2, 3, 4, 5, 6])


array_2dimensi = np.array([[2, 3, 4], [3, 4, 5], [4, 5, 6]])
array_2dimensi[1, 0] = 10
array_reshape = array_1dimensi.reshape(2, 3)
array_transpose = array_reshape.T
# indexing

# print(array_reshape)
# print(array_transpose)
# print(array_2dimensi)
# print(array_1dimensi[:3])
# print(array_2dimensi[1, 2])

a = np.array([1, 2, 3])
b = np.array([5, 6, 7])
gabungkan = np.concatenate((a, b))
# print(gabungkan)
arr_split = np.split(array_1dimensi, 2)
# print(arr_split)
mean = np.mean(array_1dimensi)
print(mean)
print(np.max(array_1dimensi))
print(np.sum(array_1dimensi))

