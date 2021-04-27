import random


def horner_method(polinom, x):
    """
    Calculeaza valoarea polinomului in punctul x
    """
    rezultat = polinom[0]
    for i in range(1, len(polinom)):
        rezultat = rezultat * x + polinom[i]
    return rezultat


def dehghan_hajarian_method(g, epsilon):
    """
     Aproximarea unui punct critic al functiei F
     Punct critic: radacina a functiei g(x) = F'(x)
    """
    k = 0
    k_maxim = 1000
    x0 = random.uniform(-100, 100)
    x = x0

    z = x + horner_method(g, x) ** 2 / (horner_method(g, x + horner_method(g, x)) - horner_method(g, x))
    delta_x = (horner_method(g, x) * (horner_method(g, z) - horner_method(g, x))) / \
              (horner_method(g, x + horner_method(g, x)) - horner_method(g, x))

    while epsilon <= abs(delta_x) <= 10 ** 8 and k <= k_maxim:
        if abs(horner_method(g, x + horner_method(g, x)) - horner_method(g, x)) <= epsilon:
            return x
        z = x + horner_method(g, x) ** 2 / (horner_method(g, x + horner_method(g, x)) - horner_method(g, x))
        delta_x = (horner_method(g, x) * (horner_method(g, z) - horner_method(g, x))) / \
                  (horner_method(g, x + horner_method(g, x)) - horner_method(g, x))
        x = x - delta_x
        k += 1

    if abs(delta_x) < epsilon:
        # convergenta
        return x
    else:
        # divergenta
        return


def F_derivat_o_data(F, x, h, i):
    """
    Calculeaza valoarea functiei F' in punctul x
    """
    if i == 1:
        return (3 * horner_method(F, x) - 4 * horner_method(F, x - h) + horner_method(F, x - 2 * h)) / (2 * h)
    elif i == 2:
        return (- horner_method(F, x + 2 * h) + 8 * horner_method(F, x + h) - 8 * horner_method(F, x - h)
                + horner_method(F, x - 2 * h)) / (12 * h)


def F_derivat_secund(F, x, h):
    """
    Calculeaza valoarea functiei F" in punctul x
    """
    return (- horner_method(F, x + 2 * h) + 16 * horner_method(F, x + h) - 30 * horner_method(F, x)
            + 16 * horner_method(F, x - h) - horner_method(F, x - 2 * h)) / (12 * (h ** 2))
