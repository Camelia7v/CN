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
        for i in range(n + 5, n + 5 + n - q):
            b.append(float(lines[i][:-1]))
        c = list()
        for i in range(n + 5 + n - q + 1, n + 5 + n - q + 1 + n - p):
            c.append(float(lines[i][:-1]))
    return n, p, q, a, b, c


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
    return matrix


def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        m = create_empty_list_of_dicts(n)
        for i in range(2, 25):
            if int(lines[i].split(',')[2]) in m[int(lines[i].split(',')[1])]:
                aux = m[int(lines[i].split(',')[1])].get(int(lines[i].split(',')[2]))
                m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = aux + float(lines[i].split(',')[0])
            else:
                m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])
    return m


def verifying_two_dictionaries(a, b):
    if len(a) != len(b):
        return False
    for i in a.keys():
        if abs(a[i] - b[i]) > 10 ** (-10):
            return False
    return True


def equal(a, b):
    count = 0
    for i in range(len(a)):
        if verifying_two_dictionaries(b[i], a[i]) is False:
            count += 1
    if count > 0:
        mesaj = "Matricele NU sunt egale!"
    else:
        mesaj = "Matricele SUNT egale!"
    return mesaj
