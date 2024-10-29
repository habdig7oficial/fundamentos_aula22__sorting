from ctypes import *

import pathlib

root = pathlib.Path(__file__).parent.resolve()
bubble_sort = CDLL(f"{root}/methods/bubble_sort/bubble_sort.so").bubble_sort

bubble_sort.argtypes = [POINTER(c_int), c_int]
bubble_sort.restype = POINTER(c_int)

def to_c_array(arr):
    return (c_int * len(arr))(*arr)


#teste = [1233, 15, 100]

#p_teste = to_c_array(teste)

#x = bubble_sort(p_teste, c_int(len(teste)))

#for i in range(len(teste)):
#    print(x[i])

