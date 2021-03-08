import math
from math import sqrt
import numpy


def fill_with_zeros(n):
    return [[0.0 for i in range(n)] for j in range(n)]


def calcul_elem_diagonal(p, L, A):
    suma = 0
    for j in range(0, p):
        suma += L[p][j] ** 2
    if A[p][p] - suma < 0:
        return 0
    return sqrt(A[p][p] - suma)


def calcul_restul_elem(i, p, L, A):
    suma = 0
    for j in range(0, p):
        suma += L[i][j] * L[p][j]
    return (A[i][p] - suma) / L[p][p]


def diag_principala(A, n):
    return [A[i][j] for i in range(n) for j in range(n) if i == j]


def calcul_determinant(L, n):
    d = diag_principala(L, n)
    det = 1
    for i in range(0, n):
        det *= d[i]
    return det ** 2


def isSymmetric(A, n):
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    return True


# matrice inferior triunghiulara
def calcul_x_Chol_substitutia_directa(A, b, n):
    y_Chol = [1.0] * n
    b = numpy.array(b)
    for i in range(0, n):
        elem_suma = 0
        for j in range(0, i):
            elem_suma += A[i][j] * y_Chol[j]
        y_Chol[i] = (b[i] - elem_suma) / A[i][i]
    return y_Chol


# matrice superior triunghiulara
def calcul_x_Chol_substitutia_inversa(A, y, n):
    x_Chol = [1.0] * n
    y = numpy.array(y)
    for i in range(n - 1, -1, -1):
        elem_suma = 0
        for j in range(i + 1, n):
            elem_suma += A[i][j] * x_Chol[j]
        x_Chol[i] = (y[i] - elem_suma) / A[i][i]
    return x_Chol


def norma_vector(v):
    suma = sum(numpy.array([x * x for x in v]))
    norma = math.sqrt(suma)
    return norma


def calcul_norma(A_init, x_Chol, c):
    A = numpy.array(A_init)
    x_Chol = numpy.array(x_Chol)
    b = fill_with_zeros(len(c))
    for i in range(len(c)):
        b[i] = numpy.float64(c[i])
    # y = numpy.array(numpy.dot(A, x_Chol))
    y = numpy.array(A @ x_Chol)
    z = numpy.array(numpy.subtract(y, b))
    return norma_vector(z)


def inversa(n, L, LT):
    A_chol_inv = fill_with_zeros(n)
    for j in range(0, n):
        e_j = [0] * n
        e_j[j] = 1
        b = e_j
        y_star = calcul_x_Chol_substitutia_directa(L, b, n)
        x_star = calcul_x_Chol_substitutia_inversa(LT, y_star, n)
        A_chol_inv[j] = x_star
    return numpy.array(A_chol_inv)
