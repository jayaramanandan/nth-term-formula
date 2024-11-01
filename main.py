from mpmath import mp, matrix, inverse

mp.prec = 400
#mp.pretty = True

def create_matrix_of_exponents(power):
    matrix_array = []
    
    for r in range(0, power + 1):
        matrix_array.append([1])
        
        for c in range(1, power + 1):
            matrix_array[r].append(mp.power(r, c))
    
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

def find_diagonal(diagonal_n):
    nth_term_parts = []
    
    for p in range(1, diagonal_n * 2 + 3):
        
        inverse_exponent_matrix = inverse(create_matrix_of_exponents(p)) * mp.factorial(p)
        
        modified_matrix = inverse_exponent_matrix * create_matrix_of_pascal(p)
        
        nth_term_matrix = get_nth_term_of_top_layer(modified_matrix)
        
        nth_term_parts.append(round(mp.fabs(nth_term_matrix[p - diagonal_n, 0]), 2))
        
      
    print(nth_term_parts[diagonal_n - 1: diagonal_n * 2 + 3])

def nth_term_string(nth_term_matrix):
    nth_term_string = ""
    
    for r in range(len(nth_term_matrix)):
        nth_term_string += str(nth_term_matrix[r, 0]) + "*x^" + str(len(nth_term_matrix) - r - 1) + " +"
    
    return nth_term_string

# multiplied by
# power factorial and divided by pascals triangle terms
#find_diagonal(6)

#print(nth_term_string(nth_term_of([1764.0, 13132.0, 67284.0, 269325.0, 902055.0, 2637558.0, 6926634.0, 16669653.0, 37312275.0])))

print(nth_term_of([0, 1, 2, 0, 1, 2]))
