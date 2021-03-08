from math import pi


def lentz_algorithm(x, epsilon):
    b = 0
    f = b
    mic = 10 ** (-12)
    if f == 0:
        f = mic
    C = f
    D = 0
    a = x
    b = 1

    D = b + a * D
    if D == 0:
        D = mic
    C = b + a / C
    if C == 0:
        C = mic
    D = 1 / D
    delta = C * D
    f = delta * f
    if a == x:
        a = - x * x
    b += 2

    while abs(delta - 1) >= epsilon:
        D = b + a * D
        if D == 0:
            D = mic
        C = b + a / C
        if C == 0:
            C = mic
        D = 1 / D
        delta = C * D
        f = delta * f
        if a == x:
            a = - x * x
        b += 2
    return f


def maclaurin_approximation(x):
    c1 = 0.33333333333333333
    c2 = 0.133333333333333333
    c3 = 0.053968253968254
    c4 = 0.0218694885361552
    x_2 = x * x
    x_3 = x_2 * x
    x_4 = x_3 * x
    return x + c1 * x_3 + c2 * x_4 * x + c3 * x_4 * x_3 + c4 * x_4 * x_3 * x_2


def reducere_tan(x, tan_method):
    sgn = 1
    if x < 0:
        sgn = -1
        x = -x
    if x >= pi/4:
        x = pi / 2 - x
    return 1 / tan_method(sgn * x)
