import numpy


def horner_method(polinom, x):
    rezultat = polinom[0]
    for i in range(1, len(polinom)):
        rezultat = rezultat * x + polinom[i]
    return rezultat


def metoda_celor_mai_mici_patrate(x_barat, x, y, n, m):
    """
    Interpolare prin metoda celor mai mici patrate.
    """
    # rezolvarea sistemului liniar B*a = f

    B = [[0 for i in range(m + 1)] for j in range(m + 1)]
    for j in range(m + 1):
        for i in range(m + 1):
            suma = 0
            for k in range(n + 1):
                suma += x[k] ** (i + j)
            B[i][j] = suma
    f = [0 for i in range(m + 1)]
    for i in range(m + 1):
        suma = 0
        for k in range(n + 1):
            suma += x[k] ** i * y[k]
        f[i] = suma
    B = numpy.array(B)
    f = numpy.array(f)
    a = numpy.linalg.solve(B, f)
    # a = numpy.array(a)
    # print("a:", a, float(a[1]))
    f_de_x_barat = horner_method(a, x_barat)
    return f_de_x_barat
