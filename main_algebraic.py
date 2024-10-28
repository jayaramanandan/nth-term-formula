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

def main(max_power):
    for po in range(0, max_power):
        a, p = sp.symbols('a p')
        
        power_matrix = sp.Matrix(define_matrix_array(po))
        
        modified_matrix = sp.simplify(power_matrix.inv()) * math.factorial(po) * p**po
        
        print("po = ", po)

        print_matrix_factorised(absolute_matrix(modified_matrix))
        
        print("\n\n-------------------------------------------------------------------------------\n\n\n")
        
        

main(6)