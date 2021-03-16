import math
import numpy

epsilon = 10 ** (-13)
def create_empty_dict_of_dicts(n):
    # print("enter template")
    matrix_template = {}
    for i in range(0,n):
        matrix_template[i]={}
    # print("exit template")
    return matrix_template





def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        p = int(lines[1])
        q = int(lines[2])
        a = list()
        for i in range(4, n + 4):
            a.append(float(lines[i][:-1]))
        c = list()
        for i in range(n + 5, n + 5 + n - 1):
            c.append(float(lines[i][:-1]))
        b = list()
        for i in range(n + 5 + n - 1 + 1, n + 5 + n - 1 + 1 + n - 1):
            b.append(float(lines[i][:-1]))
    matrix = list()
    matrix.append(a)
    matrix.append(c)
    matrix.append(b)
    return n, q, p, matrix


def convert_vectors_in_sparse_matrix(a, b, c, n, q, p):
    # print("enter convert")
    matrix = create_empty_dict_of_dicts(n)
    for i in matrix.keys():
        for j in range(0, n):
            if i == j:
                matrix[j][i] = a[i]
            if j - i == q:
                matrix[j][i] = b[i]
            if i - j == p:
                matrix[j][i] = c[j]
    return matrix


def read_vector_from_file(filename):
    with open(filename, 'r') as f:
        # with open("bTestCase.txt", 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = list()
        for i in range(2, n + 2):
            a.append(float(lines[i]))
    return a


def check_diagonala(a):
    not_zero = 0
    for i in range(len(a)):
        if abs(a[i]) < epsilon:
            not_zero = 1
    if not_zero == 1:
        return "STOP"
    else:
        return "GO"


def verificare_posibilitate_calul(matrix):
    verificare = list()
    verificare.append(check_diagonala(matrix[0]))
    if "STOP" in verificare:
        print("Nu se poate calcula solutia! Diagonala cu elemente zero...")
        exit()
    else:
        return
def fill_with_zeros(n):
    return [0.0 for j in range(n)]
def norma_vector(v):
    suma = sum(numpy.array([x * x for x in v]))
    norma = math.sqrt(suma)
    return norma


def calcul_norma(a, x, f,n):
    # b = a*x
    x = numpy.array(x)
    b = fill_with_zeros(n)
    for i in range(0,n):
        for j in a[i].keys():
            if 0 in a[j].keys():
                 b[i] += a[j][0] * x[j]
    z = numpy.array(numpy.subtract(b, f))
    return norma_vector(z)