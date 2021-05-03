def horner_method(polinom, x):
    """
    Calculeaza valoarea polinomului in punctul x
    """
    rezultat = polinom[0]
    for i in range(1, len(polinom)):
        rezultat = rezultat * x + polinom[i]
    return rezultat


def F_derivat_o_data(F, x, h, i):
    """
    Calculeaza valoarea functiei F' in punctul x
    """
    if i == 1:
        return (3 * horner_method(F, x) - 4 * horner_method(F, x - h) + horner_method(F, x - 2 * h)) / (2 * h)
    if i == 2:
        return (- horner_method(F, x + 2 * h) + 8 * horner_method(F, x + h) - 8 * horner_method(F, x - h)
                + horner_method(F, x - 2 * h)) / (12 * h)


def F_derivat_secund(F, x, h):
    """
    Calculeaza valoarea functiei F" in punctul x
    """
    return (- horner_method(F, x + 2 * h) + 16 * horner_method(F, x + h) - 30 * horner_method(F, x)
            + 16 * horner_method(F, x - h) - horner_method(F, x - 2 * h)) / (12 * (h ** 2))


def dehghan_hajarian_method(x0, g, i, h, epsilon):
    """
     Aproximarea unui punct critic al functiei g
     Punct critic: radacina a functiei g(x) = F'(x)
    """
    k = 0
    k_maxim = 1000

    x = x0
    z = x + (F_derivat_o_data(g, x, h, i) ** 2) / \
        (F_derivat_o_data(g, x + F_derivat_o_data(g, x, h, i), h, i) - F_derivat_o_data(g, x, h, i))
    delta_x = (F_derivat_o_data(g, x, h, i) * (F_derivat_o_data(g, z, h, i) - F_derivat_o_data(g, x, h, i))) / \
              (F_derivat_o_data(g, x + F_derivat_o_data(g, x, h, i), h, i) - F_derivat_o_data(g, x, h, i))

    while epsilon <= abs(delta_x) <= 10 ** 8 and k <= k_maxim:
        if abs(F_derivat_o_data(g, x + F_derivat_o_data(g, x, h, i), h, i) - F_derivat_o_data(g, x, h, i)) <= epsilon:
            # convergenta
            print("Pentru x0 = %d, folosind G%d(x,h), obtinem un numar de %d iteratii." % (x0, i, k))
            return x
        z = x + (F_derivat_o_data(g, x, h, i) ** 2) / \
            (F_derivat_o_data(g, x + F_derivat_o_data(g, x, h, i), h, i) - F_derivat_o_data(g, x, h, i))
        delta_x = (F_derivat_o_data(g, x, h, i) * (F_derivat_o_data(g, z, h, i) - F_derivat_o_data(g, x, h, i))) / \
                  (F_derivat_o_data(g, x + F_derivat_o_data(g, x, h, i), h, i) - F_derivat_o_data(g, x, h, i))
        x = x - delta_x
        k += 1

    if abs(delta_x) < epsilon:
        # convergenta
        print("Pentru x0 = %d, folosind G%d(x,h), obtinem un numar de %d iteratii." % (x0, i, k))
        return x
    else:
        # divergenta
        return
