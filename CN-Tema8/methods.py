import PySimpleGUI as gui


def horner_method(polinom, flag, x):
    """
    Calculeaza valoarea polinomului in punctul x
    """
    rezultat = polinom[0]

    if flag is False:
        for i in range(1, len(polinom) - 1):
            rezultat = rezultat * x + polinom[i]
        rezultat = rezultat * x + polinom[len(polinom) - 2]
    elif flag is True:
        for i in range(1, len(polinom) - 1):
            rezultat = rezultat * x + polinom[i]
        rezultat = rezultat * x - polinom[len(polinom) - 2]
    else:
        for i in range(1, len(polinom) - 1):
            rezultat = rezultat * x + polinom[i]

    return rezultat


def F_derivat_o_data(F, x, flag, h, i):
    """
    Calculeaza valoarea functiei F' in punctul x
    """
    if i == 1:
        return (3 * horner_method(F, flag, x) - 4 * horner_method(F, flag, x - h) + horner_method(F, flag,
                                                                                                  x - 2 * h)) / (2 * h)
    if i == 2:
        return (- horner_method(F, flag, x + 2 * h) + 8 * horner_method(F, flag, x + h) - 8 * horner_method(F, flag,
                                                                                                            x - h)
                + horner_method(F, flag, x - 2 * h)) / (12 * h)


def F_derivat_secund(F, flag, x, h):
    """
    Calculeaza valoarea functiei F" in punctul x
    """
    if flag != 1:
        flag = not flag
    return (- horner_method(F, flag, x + 2 * h) + 16 * horner_method(F, flag, x + h) - 30 * horner_method(F, flag, x)
            + 16 * horner_method(F, flag, x - h) - horner_method(F, flag, x - 2 * h)) / (12 * (h ** 2))


def dehghan_hajarian_method(x0, g, flag, i, h, epsilon):
    """
     Aproximarea unui punct critic al functiei g
     Punct critic: radacina a functiei g(x) = F'(x)
    """
    k = 0
    k_maxim = 1000

    x = x0
    z = x + (F_derivat_o_data(g, x, flag, h, i) ** 2) / \
        (F_derivat_o_data(g, x + F_derivat_o_data(g, x, flag, h, i), flag, h, i) - F_derivat_o_data(g, x, flag, h, i))
    delta_x = (F_derivat_o_data(g, x, flag, h, i) * (
            F_derivat_o_data(g, z, flag, h, i) - F_derivat_o_data(g, x, flag, h, i))) / \
              (F_derivat_o_data(g, x + F_derivat_o_data(g, x, flag, h, i), flag, h, i) - F_derivat_o_data(g, x, flag, h,
                                                                                                          i))

    while epsilon <= abs(delta_x) <= 10 ** 8 and k <= k_maxim:
        if abs(F_derivat_o_data(g, x + F_derivat_o_data(g, x, flag, h, i), flag, h, i) - F_derivat_o_data(g, x, flag, h,
                                                                                                          i)) <= epsilon:
            # convergenta
            print("Pentru x0 = %d, folosind G%d(x,h), obtinem un numar de %d iteratii." % (x0, i, k))
            return x, k
        z = x + (F_derivat_o_data(g, x, flag, h, i) ** 2) / \
            (F_derivat_o_data(g, x + F_derivat_o_data(g, x, flag, h, i), flag, h, i) - F_derivat_o_data(g, x, flag, h,
                                                                                                        i))
        delta_x = (F_derivat_o_data(g, x, flag, h, i) * (
                F_derivat_o_data(g, z, flag, h, i) - F_derivat_o_data(g, x, flag, h, i))) / \
                  (F_derivat_o_data(g, x + F_derivat_o_data(g, x, flag, h, i), flag, h, i) - F_derivat_o_data(g, x,
                                                                                                              flag, h,
                                                                                                              i))
        x = x - delta_x
        k += 1

    if abs(delta_x) < epsilon:
        # convergenta
        print("Pentru x0 = %d, folosind G%d(x,h), obtinem un numar de %d iteratii." % (x0, i, k))
        return x, k
    else:
        # divergenta
        return


def cerinta_interface(x0=0.0, i1=0, i2=0, k1=0, k2=0, x_stelat1=0.0, x_stelat2=0.0, message1=None, message2=None):
    gui.theme('DarkPurple6')
    layout = [[gui.Text("\n" + ("Pentru x0 = %d, folosind G%d(x,h),\n obtinem un numar de %d iteratii." % (x0, i1, k1)),
                        justification='center')],
              [gui.Text(message1 + "\n", justification='center')],
              [gui.Text(("Pentru x0 = %d, folosind G%d(x,h),\n obtinem un numar de %d iteratii." % (x0, i2, k2)),
                        justification='center')],
              [gui.Text(message2 + "\n", justification='center')],
              [gui.Button("Close")]]

    # Create the window
    window = gui.Window("Tema 8", layout, size=(700, 350))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
    window.close()
