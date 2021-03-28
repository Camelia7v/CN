import methods
import numpy
import copy

"""
p >= n
p - nr. linii
n - nr. coloane
"""

"""
1. Pentru p = n, sa se aproximeze valorile si vectorii proprii ale matricei simetrice A (A = AT) folosind metoda Jacobi.
"""

p = 3
n = 3
# A = [[4, 2, 8],
#      [2, 10, 10],
#      [8, 10, 21]]
# A_init = copy.deepcopy(A)

A = [[1, 0, 1],
     [0, 1, 0],
     [1, 0, 1]]
A_init = copy.deepcopy(A)

# A = [[0, 1, 0],
#      [1, 0, 1],
#      [0, 1, 0]]
# A_init = copy.deepcopy(A)

rezultat = methods.jacobi_method(A, n)
A = rezultat[0]
U = rezultat[1]
U_T = numpy.transpose(U)
inm = numpy.dot(U_T, numpy.array(A_init))
A_final = numpy.dot(inm, U)

print(A)

lambdaa = methods.get_lambda(A, n)
a = numpy.dot(A_init, U)
b = numpy.dot(U, lambdaa)
norma = numpy.linalg.norm(a - b)
print("Norma:", norma, "\n")


"""
2. 
"""

n = 3
A = [[4, 2, 8],
     [2, 10, 10],
     [8, 10, 21]]
A_factorizat = methods.factorizarea_choleski(A)
print(A_factorizat, "\n")


"""
3. 
"""

A = [[4, 2, 8],
     [2, 10, 10],
     [8, 10, 21]]
U, S, V = numpy.linalg.svd(A, full_matrices=True)
print("Valorile singulare ale matricei, S:", S)
print("Rangul matricei A:", numpy.linalg.matrix_rank(A))
print("Numarul de conditionare al matricei:", numpy.linalg.cond(A))
A_I = numpy.linalg.pinv(A)
print("Pseudoinversa Moore-Penrose a matricei:\n", A_I)
AT = numpy.transpose(A)
A_J = numpy.dot(numpy.linalg.inv(numpy.dot(AT, A)), AT)
print("Pseudoinversa in sensul celor mai mici patrate:\n", A_J)
print(numpy.linalg.norm(A_I - A_J))
