"""
Să se scrie o funcție care să calculeze produsul a două matrice
tridiagonale oarecare. Valorile (p,q) sunt oarecare şi diferite pentru fiecare
matrice: (pA, qA) şi (pB, qB).
"""

import methods

set_matrix1 = methods.read_matrix_from_file("aTestCase.txt")
set_matrix2 = methods.read_matrix_from_file("bTestCase.txt")
aorib_din_fisier = methods.read_matrix("inm1TestCase.txt")

n1 = set_matrix1[0]
n2 = set_matrix2[0]
p1 = set_matrix1[1]
q1 = set_matrix1[2]
p2 = set_matrix2[1]
q2 = set_matrix2[2]

# prima matrice tridiagonala
m = methods.convert_vectors_in_sparse_matrix(set_matrix1[3], set_matrix1[4], set_matrix1[5], n1, p1, q1)

# a doua matrice tridiagonala
a = set_matrix2[3]
b = set_matrix2[4]
c = set_matrix2[5]

# inmultirea a doua matrice tridiagonale
aorib = methods.create_empty_list_of_dicts(n1)
for i in range(0, len(m)):
    for j in range(0, len(m)):
        suma = 0
        for k in m[i].keys():
            if k == j:
                suma += m[i].get(k) * a[j]
            if j - k == q2:
                if j >= q2:
                    suma += m[i].get(k) * b[j - q2]
                else:
                    suma += 0
            if k - j == p2:
                if j < len(c):
                    suma += m[i].get(k) * c[j]
                else:
                    suma += 0
        if suma != 0:
            aorib[i].update({j: suma})

print("A * B:            ", aorib)
print("A * B din fisier: ", aorib_din_fisier)

# verificare matrici
verificare = methods.equal(aorib, aorib_din_fisier)
print("\n", verificare)


# X = [[102.5, 2.5, 0, 0, 0],
#      [3.5, 104.88, 1.05, 0, 0],
#      [0, 1.3, 100, 0.33, 0],
#      [0, 0, 0.73, 101.3, 0],
#      [0, 0, 0, 1.5, 102.23]
#      ]
# Y = [[102.5, 0, 2.5, 0, 0],
#      [0, 104.88, 0, 1.05, 0],
#      [3.5, 0, 100, 0, 0.33],
#      [0, 1.3, 0, 101.3, 0],
#      [0, 0, 0.73, 0, 102.23]
#      ]
#
# result = [[0, 0, 0, 0, 0] for i in range(0, 5)]
# # iterate through rows of X
# for i in range(len(X)):
#     # iterate through columns of Y
#     for j in range(len(Y[0])):
#         # iterate through rows of Y
#         for k in range(len(Y)):
#             result[i][j] += X[i][k] * Y[k][j]
# print(result)
