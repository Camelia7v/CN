import random


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


def olver_method(a, epsilon):
    """
    Metoda de aproximare a radacinilor reale ale unui polinom
    """
    x = random.randint(0, 1000)
    k = 0
    k_maxim = 1000
    while k <= k_maxim:
        k += 1
