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
            suma += (x[k] ** i) * y[k]
        f[i] = suma
    # print("B:", B, B[0][0], "\n")
    # B = numpy.array(B)
    # f = numpy.array(f)
    a = numpy.linalg.solve(B, f)
    # print(numpy.allclose(numpy.dot(B, a), f))
    # a = numpy.array(a)
    print("B:", B)
    print("a:", a, a[0])
    print("f:", f)
    f_de_x_barat = horner_method(a, x_barat)
    return f_de_x_barat
