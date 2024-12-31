import numpy as np 


data_list: list[int] = [1, 2, 3, 4]
data_tuple: tuple[int] = (2, 3, 4, 5)
# data_list_numpy = np.array(data_list)
# print(data_list_numpy)

# as_array = np.asarray(data_list)
# print(as_array)
copy_array = np.copy(data_tuple)
print(copy_array)


def tambah(a: int, b: int) -> int:
    return a - b


arr_func = np.fromfunction(tambah, (2, 3), dtype=int)
# print(arr_func)

iterable = range(10)
arr_iter = np.fromiter(iterable, dtype=int)

print(arr_iter)
