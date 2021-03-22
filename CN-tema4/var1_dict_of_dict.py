import copy
import math

import methods

# CERINTA 1
# Sa se calculeze cu Gauss-Seidel solutia sistemului Ax=f
# pt A =ai.txt si f=fi.txt
# CERINTA 2
# Sa se verifice soultia xG, cu norma  ||A*xG-f|| (se poate folosi si norma din biblioteca)

# A matrice rara
# un singur xG
# memorare matricea b

a1_filename = "files/a1.txt"
a2_filename = "files/a2.txt"
a3_filename = "files/a3.txt"
a4_filename = "files/a4.txt"
a5_filename = "files/a5.txt"

f1_filename = "files/f1.txt"
f2_filename = "files/f2.txt"
f3_filename = "files/f3.txt"
f4_filename = "files/f4.txt"
f5_filename = "files/f5.txt"

#PERECHILE DE A si f

# 1
a1 = methods.read_matrix_from_file(a1_filename)
f1 = methods.read_vector_from_file(f1_filename)

# # 2
# a2 = methods.read_matrix_from_file(a2_filename)
# f2 = methods.read_vector_from_file(f2_filename)
#
#
# # 3
# a3 = methods.read_matrix_from_file(a3_filename)
# f3 = methods.read_vector_from_file(f3_filename)
#
# # 4
# a4 = methods.read_matrix_from_file(a4_filename)
# f4 = methods.read_vector_from_file(f4_filename)
#
# # 5
# a5 = methods.read_matrix_from_file(a5_filename)
# f5 = methods.read_vector_from_file(f5_filename)

# variabile globala a,n si f care iau valorile ai si fi
a = copy.deepcopy(a1)
f = copy.deepcopy(f1)
methods.verificare_posibilitate_calul(a[3])
n = a[0]
# n, q, p, matrix
matrix = methods.convert_vectors_in_sparse_matrix_dict(a[3][0], a[3][1], a[3][2], a[0], a[1], a[2])

# initiere vector x
x = [0.0 for j in range(n)]
elem_a = 0.0
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
            suma1 = 0.0
            suma2 = 0.0
            x_curent = 0.0
            # print(k)
            # calcularea sumelor necesare pe baza formulei
            for j in a[i].keys():
                if j == i - 1:
                    suma1 += x[j] * a[i][j]
                elif j == i + 1:
                    suma2 += a[i][j] * x[j]
                if j == i:
                    elem_a += a[i][j]
            # calculate xi(k+1)
            x_curent = (f[i] - suma1 - suma2) / elem_a
            x[i] = x_curent

            # calcul norma
            norma += pow(x_curent - x[i], 2)
            delta_x = math.sqrt(norma)
            k += 1
    return x


def xG_solutie(a, f, x, n):
    gauss_seidel(a, f, n)
    print("\nx: ")
    print(x)
    norma_sol = methods.calcul_norma(a, f, x, n)
    print("\nNorma: ")
    print(norma_sol)
    return


xG_solutie(matrix, f, x, n)