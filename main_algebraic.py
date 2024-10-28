import sympy as sp
import math

'''
# Define the symbolic variables
a, p = sp.symbols('a p')

# Define the matrix A
A = sp.Matrix([
    [1, a, a**2, a**3],
    [1, a + p, (a + p)**2, (a + p)**3],
    [1, a + 2*p, (a + 2*p)**2, (a + 2*p)**3],
    [1, a + 3*p, (a + 3*p)**2, (a + 3*p)**3]
])

'''

def define_matrix_array(power):
    a, p = sp.symbols('a p')
    mat = []
    
    for r in range(power + 1):
        mat.append([])
        
        for c in range(power + 1):
            mat[r].append((a + r * p) ** c)
    
    return mat

def absolute_matrix(matrix_data):
    matrix_length = int(math.sqrt(len(matrix_data)))
    new_matrix = []
    
    for r in range(matrix_length):
        new_matrix.append([])
        
        for c in range(matrix_length):
            new_matrix[r].append(matrix_data[r, c] * sp.Pow(-1, r + c))
    
    return sp.Matrix(new_matrix)

def print_matrix_factorised(matrix_data):
    matrix_length = int(math.sqrt(len(matrix_data)))
    for r in range(matrix_length):
        for c in range(matrix_length):
            print(sp.factor(matrix_data[r, c]))
        print("\n")

def matrix_of_zeros(size):
    mat = []
    for i in range(size):
        mat.append([])
        for j in range(size):
            mat[i].append(0)
        
    return sp.Matrix(mat)

def create_matrix_of_pascal(power):
    pascal_matrix = matrix_of_zeros(power + 1)
    
    for d in range(power + 1):
        pascal_matrix[d, d] = (sp.factorial(power - d) * sp.factorial(d)) / sp.factorial(power)
    
    return pascal_matrix

def main(max_power):
    for po in range(0, max_power):
        a, p = sp.symbols('a p')
        
        power_matrix = sp.Matrix(define_matrix_array(po))
        
        modified_matrix = sp.simplify(power_matrix.inv()) # inverting matrix
        modified_matrix = modified_matrix * math.factorial(po) * p**po # multiplying matrix by constant factor (power! * p^power)
        modified_matrix = absolute_matrix(modified_matrix) # removing the alternating negatives
        modified_matrix = modified_matrix.multiply(create_matrix_of_pascal(po)) # divides by pascal's triangle for each layer
        
        print("po = ", po, "\n\n")

        print_matrix_factorised(modified_matrix)
        
        print("\n\n-------------------------------------------------------------------------------\n\n\n")
        
        

main(8)