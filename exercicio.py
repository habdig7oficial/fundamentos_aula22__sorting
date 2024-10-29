
 # Copyright ©️ 2024 Mateus Felipe da Silveira Vieira
 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>5.


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
        
