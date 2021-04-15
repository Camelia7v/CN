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

    # print("B:", B)
    # print("a:", a, a[0])
    # print("f:", f)
    f_de_x_barat = horner_method(a, x_barat)
    return f_de_x_barat


def spline_patratice(x_barat, f_derivat_de_a, x, y, n):
    h = [0 for i in range(n+1)]
    A = [0 for i in range(n+1)]
    A[0] = f_derivat_de_a
    for i in range(n):
        h[i] = x[i+1] - x[i]
        A[i+1] = -A[i] + (2 * (y[i+1] - y[i])) / h[i]
    for i in range(n):
        if x[i] < x_barat < x[i+1]:
            S_de_x_barat = (A[i+1] - A[i]) / (2 * h[i]) * ((x_barat - x[i]) ** 2) + A[i] * (x_barat - x[i]) + y[i]
            return S_de_x_barat
