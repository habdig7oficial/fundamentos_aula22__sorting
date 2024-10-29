
from lib.ordination import *


def my_sort(vec):
    pass

iterations = 1
while iterations != 0:
    iterations = int(input("Digite o número de Iteracões: ")) ## Input ak
    i = 0
    vec = []
    while i < iterations:
        gets = int(input(f"{i + 1}) Digite um Número: "))## Input ak
        vec.append(gets)
        i += 1
    print(vec)

    pointer_arr = to_c_array(vec)

    vec_sorted = bubble_sort(pointer_arr, c_int(len(vec)))
    
    add_zeros = len(str(vec_sorted[len(vec) - 1]))

    for i in range(len(vec)):
        print(str(vec_sorted[i]).zfill(add_zeros))
        
