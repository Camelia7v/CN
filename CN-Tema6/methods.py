import numpy


def horner_method(polinom, x):
    rezultat = polinom[0]
    for i in range(1, len(polinom)):
        rezultat = rezultat * x + polinom[i]
    return rezultat


def metoda_celor_mai_mici_patrate(x_barat, y, n, m):
    """
    Interpolare prin metoda celor mai mici patrate.
    """
    # rezolvarea sistemului liniar B*a = f
    # a = numpy.linalg.solve(B, f)
