//
//  bubble_sort.cpp
//  bubble_sort
//
//  Created by Mateus Felipe da Silveira Vieira on 29/10/24.
//

// Compilado com: clang++ -shared -Wl,-install_name,testlib.so -o bubble_sort.so -fPIC bubble_sort.cpp

#include "bubble_sort.hpp"
#include <iostream>
#include <vector>

using namespace std;
extern "C" {
    int * bubble_sort(int vec[], int len){
        cout << len << endl;
        for(int i = 0; i < len - 1; i++){
            for(int j = 0; j < len - 1; j++){
                int tmp;
                if(vec[j] > vec[j + 1]){
                    tmp = vec[j];
                    vec[j] = vec[j + 1];
                    vec[j + 1] = tmp;
                }
                //cout << "i: " << i << " j: " << j << endl;
            
            }
        }
        return vec;
    }
}
