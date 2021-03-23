import math
import numpy

epsilon = 10 ** (-13)


def create_empty_list_of_dicts(n):
    return [{} for i in range(0, n)]


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
        for i in range(n + 5, n + 5 + n - p):
            c.append(float(lines[i][:-1]))
        b = list()
        for i in range(n + 5 + n - p + 1, n + 5 + n - p + 1 + n - q):
            b.append(float(lines[i][:-1]))
    matrix = list()
    matrix.append(a)
    matrix.append(b)
    matrix.append(c)
    return n, q, p, matrix


def convert_vectors_in_sparse_matrix_list(a, b, c, n, q, p):
    matrix = create_empty_list_of_dicts(n)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                matrix[i][j] = a[i]
            if j - i == q:
                matrix[i][j] = b[i]
            if i - j == p:
                matrix[i][j] = c[j]
    return matrix


def read_vector_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = list()
        for i in range(2, n + 2):
            a.append(float(lines[i]))
    return a


def check_diagonala(a):
    for i in range(len(a)):
        if abs(a[i]) < epsilon:
            return "STOP"
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


def calcul_norma(a, x, f, n):
    x = numpy.array(x)
    b = fill_with_zeros(n)
    # calculam b = a * x
    for i in range(0, n):
        suma = 0
        for k in a[i].keys():
            suma += a[i][k] * x[k]
        b[i] = suma
    print("A * x ~= f:", "\n", b)
    # calculam z = b - f
    z = numpy.array(numpy.subtract(b, f))
    # return norma_vector(z)
    return numpy.linalg.norm(max(abs(z)))


def gauss_seidel(a, f, n):
    # initiere vector x
    # x = [float(i) for i in range(1, n+1)]
    x = [0.0] * n
    delta_x = 1
    epsilon = 10 ** (-13)
    k_max = 10000
    k = 0

    # conditiile de terminare
    while (k <= k_max) and (delta_x >= epsilon) and (delta_x <= 10 ** 8):
        elem_diag = 1.0
        for i in range(0, n):
            suma1 = 0.0
            suma2 = 0.0

            # calcularea sumelor necesare pe baza formulei
            for j in a[i].keys():
                if j == i - 1:
                    suma1 += x[j] * a[i][j]
                elif j == i + 1:
                    suma2 += a[i][j] * x[j]
                if j == i:
                    elem_diag = a[i][j]
            x_curent = (f[i] - suma1 - suma2) / elem_diag
            x_anterior = x[i]

            # calcul norma
            norma = pow(x_curent - x_anterior, 2)
            delta_x = math.sqrt(norma)

            x[i] = x_curent
            k += 1
    return x
