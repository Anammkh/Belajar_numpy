import numpy as np


# arr_int = np.array([-1, 2, 3], dtype=np.int8)
# print(arr_int)
# print(arr_int.dtype)

# arr_uint = np.array([1, 2, 3], dtype=np.uint8)
# print(arr_uint)
# print(arr_uint.dtype)

# arr_float = np.array([0.1, 5.3, 2,5], dtype=np.float16)
# print(arr_float.dtype)

# arr_complex = np.array([1 + 2j, 4 + 8j], dtype=np.complex128)
# print(arr_complex)
# print(arr_complex.dtype)boole

# arr_boolean = np.array([True, False, False], dtype=bool)
# print(arr_boolean)
# print(arr_boolean.dtype)

# arr_string = np.array(["apple", "banana"], dtype='<U10')
# print(arr_string)
# print(arr_string.dtype)

arr_objek = np.array([1, "text", [1, 2, 3]], dtype=object)
print(arr_objek)
print(arr_objek.dtype)


def tambah(a: int, b: int) -> int:
    try:
        if a <= 0 and b <= 0:
            print("yang bener aja bro")
    except ValueError:
        print("kocak lu")
    except Exception as e:
        print(f"errorr bro {e}")
    finally:
        return f"hasil tambah adalah {a + b}"


if __name__ == "__main__":
    a = int(input("masukkan angka pertama: "))
    b = int(input("masukkan angka kedua :"))
    print(tambah(a, b))
