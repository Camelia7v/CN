import math


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
    for i in range(n):
        for j in range(n):
            # se cauta doar in partea strict inferior triunghiulara a matricei
            if i > j and abs(A[i][j]) >= maximum:
                maximum = abs(A[i][j])
                p = i
                q = j
    return p, q


def calculeaza_unghiul_teta(A, p, q):
    if A[p][p] == A[q][q]:
        if A[p][q] > 0:
            return math.pi / 4
        else:
            return - math.pi / 4
    else:
        return 1 / 2 * math.tan(2 * A[p][q] / (A[p][p] - A[q][q]))


def jacobi_method(A, n):
    """
    Metoda lui Jacobi pentru aproximarea valorilor proprii ale matricelor simetrice
    """
    k = 0
    k_max = 1000
    U = matricea_unitate(n)
    p = calculeaza_p_q(A, n)[0]
    q = calculeaza_p_q(A, n)[1]
    teta = calculeaza_unghiul_teta(A, p, q)
    c = math.cos(teta)
    s = math.sin(teta)
    t = math.tan(teta)
    while k <= k_max:  # si A diferita de matricea diagonala

        k = k + 1


if __name__ == "__main__":
    A = [[4, 2, 8],
         [2, 10, 10],
         [8, 10, 21]]
    p = calculeaza_p_q(A, 3)[0]
    q = calculeaza_p_q(A, 3)[1]
    print(p, q)
    print(calculeaza_unghiul_teta(A, p, q))
