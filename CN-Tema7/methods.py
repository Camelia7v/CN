import random
import numpy


def calculeaza_intervalul(a):
    """
    Se calculeaza intervalul [−R, R] in care se gasesc toate radacinile reale ale polinomului P
    """
    A = max(a)
    R = (abs(a[0]) + A) / abs(a[0])
    return R


def horner_method(polinom, x):
    rezultat = polinom[0]
    for i in range(1, len(polinom)):
        rezultat = rezultat * x + polinom[i]
    return rezultat


def olver_method(p, R, epsilon):
    """
    Metoda de aproximare a radacinilor reale ale unui polinom
    """
    p1 = numpy.polyder(p)  # p'
    p2 = numpy.polyder(p, 2)  # p"

    # bonus
    # q = polynomials_gcd(p, p1, epsilon)
    # p = numpy.polynomial.polynomial.polydiv(p, q)

    k = 0
    k_maxim = 1000

    x = random.uniform(-R, R)
    x0 = x
    c = (horner_method(p, x) ** 2 * horner_method(p2, x)) / (horner_method(p1, x) ** 3)
    delta_x = horner_method(p, x) / horner_method(p1, x) + 1 / 2 * c

    while epsilon <= abs(delta_x) <= 10 ** 8 and k <= k_maxim:
        if abs(horner_method(p1, x)) <= epsilon:
            break
        x = x - delta_x
        c = (horner_method(p, x) ** 2 * horner_method(p2, x)) / (horner_method(p1, x) ** 3)
        delta_x = horner_method(p, x) / horner_method(p1, x) + 1 / 2 * c
        k += 1

    if abs(delta_x) < epsilon:
        return x, x0
    else:
        # divergenta...
        return


def polynomials_gcd(f, g, epsilon):
    if len(f) < len(g):
        return polynomials_gcd(g, f, epsilon)

    r = [0] * len(f)
    r_mult = 1 / g[0] * f[0]

    for i in range(len(f)):
        if i < len(g):
            r[i] = f[i] - g[i] * r_mult
        else:
            r[i] = f[i]

    while abs(r[0]) < epsilon:
        r.pop(0)
        if len(r) == 0:
            return g

    return polynomials_gcd(r, g, epsilon)
