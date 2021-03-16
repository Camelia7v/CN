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

# a1 = methods.read_matrix_from_file(a1_filename)
# n1=a1[0]
# #verificare diagonale
# methods.verificare_posibilitate_calul(a1[3])
# # convertire a,b,c in matrice rara   [n, q, p, matrix]
# matrix1 = methods.convert_vectors_in_sparse_matrix(a1[3][0],a1[3][1],a1[3][2],a1[0],a1[1],a1[2])
#
# a2 = methods.read_matrix_from_file(a2_filename)
# n2=a2[0]
# methods.verificare_posibilitate_calul(a2[3])
# matrix2 = methods.convert_vectors_in_sparse_matrix(a2[3][0],a2[3][1],a2[3][2],a2[0],a2[1],a2[2])
#
# a3 = methods.read_matrix_from_file(a3_filename)
# n3=a3[0]
# methods.verificare_posibilitate_calul(a3[3])
# matrix3 = methods.convert_vectors_in_sparse_matrix(a3[3][0],a3[3][1],a3[3][2],a3[0],a3[1],a3[2])
#
# a4 = methods.read_matrix_from_file(a4_filename)
# n4=a4[0]
# methods.verificare_posibilitate_calul(a4[3])
# matrix4 = methods.convert_vectors_in_sparse_matrix(a4[3][0],a4[3][1],a4[3][2],a4[0],a4[1],a4[2])
#
# a5 = methods.read_matrix_from_file(a5_filename)
# n5=a5[0]
# methods.verificare_posibilitate_calul(a5[3])
# matrix5 = methods.convert_vectors_in_sparse_matrix(a5[3][0],a5[3][1],a5[3][2],a5[0],a5[1],a5[2])
#
# f1 = methods.read_vector_from_file(f1_filename)
# f2 = methods.read_vector_from_file(f2_filename)
# f3 = methods.read_vector_from_file(f3_filename)
# f4 = methods.read_vector_from_file(f4_filename)
# f5 = methods.read_vector_from_file(f5_filename)


# testCase din pdf
a = methods.read_matrix_from_file("testCase/test.txt")
f = methods.read_vector_from_file("testCase/f.txt")
methods.verificare_posibilitate_calul(a[3])
n = a[0]
matrix = methods.convert_vectors_in_sparse_matrix(a[3][0], a[3][1], a[3][2], a[0], a[1], a[2])

# initiere vector x
x = [0.0 for j in range(n)]
elem_a = 0.0
print(matrix)


def gauss_seidel(a, f, n):
    global x
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
            x_c = 0.0
            x_p = 0.0
            # element nenul de pe a[i][i]
            global elem_a
            x_final = 0.0
            # print(k)
            # calcularea sumelor necesare pe baza formulei
            for j in a[i].keys():
                if j <= i - 1 and 0 in a[j].keys():
                    x_c = x_c + x[j] * a[j][0]
                elif j >= i and 0 in a[j].keys():
                    x_p = x_p + a[j][0] * x[j]
                if j == i and 0 in a[j].keys():
                    elem_a += a[j][0]
            # calculate xi(k+1)
            x_final = x[i] + (f[i] - x_c - x_p) / elem_a

            # calcul norma
            norma += pow(x_final - x[i], 2)
            x[i] = x_final
            delta_x = math.sqrt(norma)
            k += 1
    return k, delta_x


def xG_solutie(a, f, x, n):
    gauss_seidel(a, f, n)
    print("\nx: ")
    print(x)
    norma_sol = methods.calcul_norma(a, f, x, n)
    print("\nNorma: ")
    print(norma_sol)
    return


xG_solutie(matrix, f, x, n)
