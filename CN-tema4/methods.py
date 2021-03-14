import math
epsilon = 10 **(-13)

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
        b = list()
        for i in range(n + 5, n + 5 + n - 1):
            b.append(float(lines[i][:-1]))
        c = list()
        for i in range(n + 5 + n - 1 + 1, n + 5 + n - 1 + 1 + n - 1):
            c.append(float(lines[i][:-1]))
    matrix = list()
    matrix.append(a)
    matrix.append(c)
    matrix.append(b)
    return (n,p,q,matrix)


def convert_vectors_in_sparse_matrix(a, b, c, n, q, p):
    matrix = create_empty_list_of_dicts(n)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if i == j:
                matrix[i][j] = a[i]
            if j - i == q:
                matrix[i][j] = b[i]
            if i - j == p:
                matrix[i][j] = c[j]

def read_vector_from_file(filename):
    with open(filename, 'r') as f:
        # with open("bTestCase.txt", 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        a = list()
        for i in range(2, n+2):
            a.append(float(lines[i]))
        return a

def check_diagonala(a):
    not_zero = 0
    for i in range(len(a)):
        if abs(a[i]) < epsilon:
            not_zero=1
    if not_zero == 1:
        return "STOP"
    else:
        return "GO"

def verificare_posibilitate_calul(matrix):
    verificare = list()
    for vec in matrix:
        verificare.append(check_diagonala(vec))
    if "STOP" in verificare:
        print("Nu se poate calcula solutia.Diagonala cu elemente zero")
        exit()
    else:
        return


