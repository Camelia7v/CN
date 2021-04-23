import random
import numpy
import PySimpleGUI as gui

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
    # q = polynomials_gcd(p, p1, 2, epsilon)
    # p,r = numpy.polydiv(p, q)

    print("P",p)

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


def polynomials_gcd(f, g, field, epsilon):
    if len(f) < len(g):
        return polynomials_gcd(g, f, field, epsilon)

    r = [0] * len(f)
    r_mult = f[0] / g[0]
    for i in range(len(f)):
        if i < len(g):
            r[i] = f[i] - g[i] * r_mult
        else:
            r[i] = f[i]
        if field != 0:
            r[i] %= field


    # print('F',f)
    # print('G',g)
    # print('R',r)
    while abs(r[0]) < epsilon:
        r.pop(0)
        if len(r) == 0:
            return g
    return polynomials_gcd(r, g,field, epsilon)

# def polynomials_gcd(f, g, epsilon):
#     if len(f) < len(g):
#         return polynomials_gcd(g, f, epsilon)
#
#     r = [0] * len(f)
#     # r_mult = 1 / g[0] * f[0]
#     r_mult = f[0] / g[0]
#     for i in range(len(f)):
#         if i < len(g):
#             r[i] = f[i] - g[i] * r_mult
#         else:
#             r[i] = f[i]
#
#
#     print('F',f)
#     print('G',g)
#     print('R',r)
#     while abs(r[0]) < epsilon:
#         r.pop(0)
#         if len(r) == 0:
#             return g
#     return polynomials_gcd(r, g, epsilon)


def cerinta_interface(text_ex="", message="", value="", message1="", value1="", message2="", value2=""):
    gui.theme('DarkAmber')
    layout = [[gui.Text(message, justification='center')],
              [gui.Multiline(size=(105, 2), default_text=str(value), font='courier 10', background_color='black',
                            text_color='white')],
              [gui.Text(message1, justification='center')],
              [gui.Multiline(size=(105, 5), default_text=str(value1), font='courier 10',
                            background_color='black', text_color='white')],
              [gui.Text(message2, justification='center')],
              [gui.Multiline(size=(105, 5), default_text=str(value2), font='courier 10',
                             background_color='black', text_color='white')],
              [gui.Button("Close")]]

    # Create the window
    window = gui.Window(text_ex, layout, size=(800, 450))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
    window.close()


def bonus_interface(text_ex="", message="", value="", message1="", value1="", message2="", value2=""):
    gui.theme('DarkAmber')
    layout = [[gui.Text(message, justification='center')],
              [gui.Multiline(size=(105, 2), default_text=str(value), font='courier 10', background_color='black',
                             text_color='white')],
              [gui.Text(message1, justification='center')],
              [gui.Multiline(size=(105, 5), default_text=str(value1), font='courier 10',
                             background_color='black', text_color='white')],
              [gui.Text(message2, justification='center')],
              [gui.Multiline(size=(105, 5), default_text=str(value2), font='courier 10',
                             background_color='black', text_color='white')],
              [gui.Button("Close")]]

    # Create the window
    window = gui.Window(text_ex, layout, size=(800, 450))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
    window.close()

