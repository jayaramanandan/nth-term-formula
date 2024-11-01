from mpmath import mp, matrix, inverse

mp.prec = 400
mp.pretty = True

def create_matrix_of_exponents(power):
    matrix_array = []
    
    for r in range(0, power + 1):
        matrix_array.append([1])
        
        for c in range(1, power + 1):
            matrix_array[r].append(mp.power(r, c))
    
    return matrix(matrix_array)

def nth_term_of(series):
    return inverse(create_matrix_of_exponents(len(series) - 1)) * matrix(series)

def summation_series(limit, power):
    sum = 0
    series = []
    
    for r in range(1, limit + 1):
        sum += mp.power(r, power)
        series.append(sum)
        
    return series;

def nth_term_string(nth_term_matrix):
    nth_term_string = ""
    
    for r in range(len(nth_term_matrix)):
        nth_term_string += str(nth_term_matrix[r, 0]) + "*x^" + str(len(nth_term_matrix) - r - 1) + " +"
    
    return nth_term_string

def main(max_power):
    for p in range(0, max_power):
        print(p + 1)
        print("\n")
        print(nth_term_string(nth_term_of(summation_series(p + 2, p)) * mp.factorial(p + 1)))
        print("\n\n------------------------------------------------------\n\n")
        
main(6)