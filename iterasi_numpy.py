import numpy as np 


array_1D = np.array([1, 2, 3, 4], dtype=np.int64)

# for elemen in array_1D:
#     print(elemen)
array_2D = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)

# for dimensi_satu in array_2D:
#     for elemen in dimensi_satu:
#         print(elemen, end=" ")
#     print()

array_3D = np.array([[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]], dtype=np.int64)

# for dua_dimensi in array_3D:
#     for satu_dimensi in dua_dimensi:
#         for elemen in satu_dimensi:
#             print(elemen, end=" ")
#         print()
#     print()

for elemen in np.nditer(array_3D, op_flags=["readwrite"]):
    elemen[...] = elemen * 2
    print(elemen, end=" ")
