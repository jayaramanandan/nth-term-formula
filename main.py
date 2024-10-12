from decimal import *
from numpy import matrix
import math

def create_matrix_of_exponents(power):
    matrix_array = []
    
    for r in range(0, power + 1):
        matrix_array.append([1])
        
        for c in range(1, power + 1):
            matrix_array[r].append(math.pow(r, c))
    
    return matrix(matrix_array, dtype="float64")

def get_layer_string(data, layer_n):
    layer_string = ""
    
    for i in range(len(data[layer_n])):
        layer_string += str(data[layer_n][i]) + ", "
    
    return layer_string

def main(max_power):
    for p in range(0, max_power):
        inverse_exponent_matrix = create_matrix_of_exponents(p).getI() * math.factorial(p)
        
        get_layer_string(inverse_exponent_matrix, p - 1)
        print(inverse_exponent_matrix)
        
        
        
main(10)