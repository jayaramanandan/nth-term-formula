from decimal import *
import math
from mpmath import mp, matrix, inverse

mp.prec = 200

def create_matrix_of_exponents(power):
    matrix_array = []
    
    for r in range(0, power + 1):
        matrix_array.append([1])
        
        for c in range(1, power + 1):
            matrix_array[r].append(math.pow(r, c))
    
    return matrix(matrix_array)

def create_matrix_of_pascal(power):
    pascal_matrix = matrix(power + 1, power + 1)
    
    for d in range(0, power + 1):
        pascal_matrix[d, d] = (mp.factorial(power - d) * mp.factorial(d)) / mp.factorial(power)
    
    return pascal_matrix

def nth_term_of(series):
    return inverse(create_matrix_of_exponents(len(series) - 1)) * matrix(series)



def get_layer(data, layer_n):
    layer_string = ""
    
    for i in range(data.cols):
        layer_string += data[layer_n, i]



def main(max_power):
    for p in range(1, max_power):
        inverse_exponent_matrix = inverse(create_matrix_of_exponents(p)) * mp.factorial(p)
        
        print(inverse_exponent_matrix * create_matrix_of_pascal(p))
        print("\n\n")
        
        
        
main(10)

print(nth_term_of([85, 26, 19, 14, 11]))