import math

import methods

# testCase din pdf
a = methods.read_matrix_from_file("test.txt")
f = methods.read_vector_from_file("f.txt")
methods.verificare_posibilitate_calul(a[3])
n = a[0]
matrix = methods.convert_vectors_in_sparse_matrix_list(a[3][0], a[3][1], a[3][2], a[0], a[1], a[2])
print(matrix)


def gauss_seidel(a, f, n):
    # initiere vector x
    x = [0.0 for j in range(n)]
    # element nenul de pe a[i][i]
    elem_a = 0.0
    norma = 0.0
    delta_x = 1
    # 10^(-p)
    epsilon = 10 ** (-8)
    k_max = 10000
    k = 0

    # conditiile de terminare
    while (k <= k_max) and (delta_x >= epsilon) and (delta_x <= 10 ** 8):
        norma = 0.0
        for i in range(0, n):
            # print("f : ", f[i])
            suma1 = 0.0
            suma2 = 0.0
            x_curent = 0.0
            # print(k)
            # calcularea sumelor necesare pe baza formulei
            for j in a[i].keys():
                if j == i - 1:
                    # print("a : ", a[i][j])
                    # print("x : ", x[j])
                    suma1 += x[j] * a[i][j]
                if j == i + 1:
                    # print("a : ", a[i][j])
                    # print("x : ", x[j])
                    suma2 += a[i][j] * x[j]
                if j == i:
                    # print("elem_a: ", a[i][j])
                    # print("x : ", x[j])
                    elem_a += a[i][j]
            # calculate xi(k+1)

            x_curent = (f[i] - suma1 - suma2) / elem_a
            x[i] = x_curent

            # calcul norma
            norma += pow(x_curent - x[i], 2)
            delta_x = math.sqrt(norma)
            k += 1
    return x


def xG_solutie(a, f, n):

    x = gauss_seidel(a, f,n)
    print("\nx: ")
    print(x)
    norma_sol = methods.calcul_norma(a, f, x, n)
    print("\nNorma: ")
    print(norma_sol)
    return


xG_solutie(matrix, f, n)
