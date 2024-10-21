from decimal import *
import math
from mpmath import mp, matrix, inverse

mp.prec = 400
#mp.pretty = True

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

def to_list_matrix1D(matrix_data, layer_n):
    matrix_array = []
    for c in range(len(matrix_data)):
        matrix_array.append(matrix_data[layer_n, c])
        
    return matrix_array

def get_nth_term_of_top_layer(matrix_data):
    row_array = []
    for c in range(len(matrix_data) - 1):
        row_array.append(mp.fabs(matrix_data[1, c]))
    
    return nth_term_of(matrix(row_array))



def get_layer(data, layer_n):
    layer_string = ""
    
    for i in range(data.cols):
        layer_string += data[layer_n, i]



def find_diagonal(max_power, diagonal_n):
    nth_term_parts = []
    
    for p in range(1, max_power):
        
        inverse_exponent_matrix = inverse(create_matrix_of_exponents(p)) * mp.factorial(p)
        
        modified_matrix = inverse_exponent_matrix * create_matrix_of_pascal(p)
        
        nth_term_matrix = get_nth_term_of_top_layer(modified_matrix)
        
        nth_term_parts.append(mp.fabs(nth_term_matrix[p - diagonal_n, 0]))
        
        print("\n\n")
        
    print(matrix(nth_term_parts))

# multiplied by power factorial and divided by pascals triangle terms

def print_inverse_matrix(max_power):
    for p in range(1, max_power): 
        inverse_exponent_matrix = inverse(create_matrix_of_exponents(p)) * mp.factorial(p)
        
        modified_matrix = inverse_exponent_matrix * create_matrix_of_pascal(p)
        
        for c in range(len(modified_matrix)):
            column_array = []
            for r in range(len(modified_matrix)):
                column_array.append(mp.fabs(modified_matrix[r, c]))
            
            print(nth_term_of(matrix(column_array)) * mp.factorial(p))
            print("\n")
        
        print("\n-------------------------------------------------------------------------------\n")
        
print_inverse_matrix(5)
