import math
import numpy
import PySimpleGUI as gui


def matricea_unitate(n):
    I_n = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                I_n[i][j] = 1
    return I_n


def calculeaza_p_q(A, n):
    maximum = 0
    p = 0
    q = 0
    # se cauta doar in partea strict inferior/superior triunghiulara a matricei
    for i in range(n):
        for j in range(n):
            if i < j and abs(A[i][j]) >= maximum:
                maximum = abs(A[i][j])
                p = i
                q = j
    return p, q


def calculeaza_t(A, p, q):
    # t = calculeaza_t(A, p, q)
    # c = 1 / math.sqrt(1 + t * t)
    # s = t / math.sqrt(1 + t * t)
    if A[p][q] != 0 and A[p][p] != A[q][q]:
        alfa = (A[p][p] - A[q][q]) / (2 * A[p][q])
        print(alfa)
        if alfa >= 0:
            return - alfa + math.sqrt(alfa * alfa + 1)
        else:
            return - alfa - math.sqrt(alfa * alfa + 1)
    else:
        return 0


def calculeaza_teta(A, p, q):
    if A[p][p] == A[q][q]:
        if A[p][q] > 0:
            return math.pi / 4
        else:
            return - math.pi / 4
    else:
        return 1 / 2 * math.tan(2 * A[p][q] / (A[p][p] - A[q][q]))


def este_matrice_diagonala(A):
    for i in range(len(A)):
        for j in range(len(A)):
            if i != j and abs(A[i][j]) > 10 ** (-8):
                return True
    return False


def calculeaza_R_pq(n, p, q, c, s):
    R_pq = [[0] * n for i in range(n)]
    for i in range(len(R_pq)):
        for j in range(len(R_pq)):
            if i == j != p and i == j != q:
                R_pq[i][j] = 1
            elif i == j == p or i == j == q:
                R_pq[i][j] = c
            elif i == p and j == q:
                R_pq[i][j] = s
            elif i == q and j == p:
                R_pq[i][j] = -s
            else:
                R_pq[i][j] = 0
    return R_pq


def jacobi_method(A, n):
    """
    Metoda lui Jacobi pentru aproximarea valorilor proprii ale matricelor simetrice
    """
    k = 0
    k_max = 1000
    U = matricea_unitate(n)
    p = calculeaza_p_q(A, n)[0]
    q = calculeaza_p_q(A, n)[1]
    teta = calculeaza_teta(A, p, q)
    c = math.cos(teta)
    s = math.sin(teta)
    iteratie_finala = 0
    while k <= k_max and este_matrice_diagonala(A) is True:
        R_pq = calculeaza_R_pq(n, p, q, c, s)
        A = numpy.array(A)
        R_pq = numpy.array(R_pq)
        R_pq_T = numpy.transpose(R_pq)
        inm = numpy.dot(R_pq, A)
        A = numpy.dot(inm, R_pq_T)
        U = numpy.dot(U, R_pq_T)
        p = calculeaza_p_q(A, n)[0]
        q = calculeaza_p_q(A, n)[1]
        teta = calculeaza_teta(A, p, q)
        c = math.cos(teta)
        s = math.sin(teta)
        iteratie_finala = k
        k = k + 1
    print("iteratie finala:", iteratie_finala)
    return A, U


def get_lambda(A, n):
    lambdaa = [[0] * n for i in range(n)]
    for i in range(n):
        lambdaa[i][i] = A[i][i]
    return lambdaa


def factorizarea_choleski(A):
    k = 0
    k_max = 1000

    L_numpy = numpy.linalg.cholesky(A)
    LT_numpy = numpy.transpose(L_numpy)
    print(L_numpy, LT_numpy)
    A_0 = numpy.dot(L_numpy, LT_numpy)

    A_1 = numpy.dot(LT_numpy, L_numpy)

    L_numpy = numpy.linalg.cholesky(A_1)
    LT_numpy = numpy.transpose(L_numpy)
    A_1 = numpy.dot(L_numpy, LT_numpy)

    while k <= k_max and numpy.linalg.norm(A_1 - A_0) > 10 ** (-8):
        A_0 = numpy.dot(LT_numpy, L_numpy)

        L_numpy = numpy.linalg.cholesky(A_1)
        LT_numpy = numpy.transpose(L_numpy)
        A_1 = numpy.dot(L_numpy, LT_numpy)

        k = k + 1
    print("iteratie finala:", k)
    return A_1


def gui_interface(dim, text_ex="", message="", value1="", value2="", value3="", value4="", value5="",
                  value6="", verificare=""):
    gui.theme('DarkAmber')
    layout = [[gui.Text(message, justification='center')],
              [gui.Text(str(value1), justification='center')],
              [gui.Text(str(value2), justification='center')],
              [gui.Text(str(value3), justification='center')],
              [gui.Text(str(value4), justification='center')],
              [gui.Text(str(value5), justification='center')],
              [gui.Text(str(value6), justification='center')],
              [gui.Text(str(verificare), justification='center')],
              [gui.Button("Close")]]

    # Create the window
    window = gui.Window(text_ex, layout, size=(800, dim))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == gui.WIN_CLOSED:
            break
    layout.clear()
    window.close()
