import methods

"""
CERINTA 1
Sa se calculeze cu Gauss-Seidel solutia sistemului Ax=f
pt A =ai.txt si f=fi.txt

CERINTA 2
Sa se verifice soultia xG, cu norma ||A*xG - f|| (se poate folosi si norma din biblioteca)
"""


# valorile lui n1, n2, ..., n5: 60630, 40420, 20210, 2021, 2020

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
norme_solutii = list()
# PERECHILE DE a si f

# 1
a1 = methods.read_matrix_from_file(a1_filename)
f1 = methods.read_vector_from_file(f1_filename)

methods.verificare_posibilitate_calul(a1[3])
n1 = a1[0]
print("n1: ", n1)
matrix = methods.convert_vectors_in_sparse_matrix_list(a1[3][0], a1[3][1], a1[3][2], a1[0], a1[1], a1[2])
# print("a1: ", matrix)
x1 = methods.gauss_seidel(matrix, f1, n1)
# print("x1: ", x1)
# print("f1: ", f1)
norma_sol1 = methods.calcul_norma(matrix, x1, f1, n1)
print("Norma 1: ", norma_sol1, "\n")
methods.write_solution_to_file("solutions/x1.txt",x1)
norme_solutii.append(norma_sol1)

# 2
a2 = methods.read_matrix_from_file(a2_filename)
f2 = methods.read_vector_from_file(f2_filename)

methods.verificare_posibilitate_calul(a2[3])
n2 = a2[0]
print("n2: ", n2)
matrix = methods.convert_vectors_in_sparse_matrix_list(a2[3][0], a2[3][1], a2[3][2], a2[0], a2[1], a2[2])
# print("a2: ", matrix)
x2 = methods.gauss_seidel(matrix, f2, n2)
# print("x2: ", x2)
# print("f2: ", f2)
norma_sol2 = methods.calcul_norma(matrix, x2, f2, n2)
print("Norma 2: ", norma_sol2, "\n")
methods.write_solution_to_file("solutions/x2.txt",x2)
norme_solutii.append(norma_sol2)

# 3
a3 = methods.read_matrix_from_file(a3_filename)
f3 = methods.read_vector_from_file(f3_filename)

methods.verificare_posibilitate_calul(a3[3])
n3 = a3[0]
print("n3: ", n3)
matrix = methods.convert_vectors_in_sparse_matrix_list(a3[3][0], a3[3][1], a3[3][2], a3[0], a3[1], a3[2])
# print("a3: ", matrix)
x3 = methods.gauss_seidel(matrix, f3, n3)
# print("x3: ", x3)
# print("f3: ", f3)
norma_sol3 = methods.calcul_norma(matrix, x3, f3, n3)
print("Norma 3: ", norma_sol3, "\n")
methods.write_solution_to_file("solutions/x3.txt",x3)
norme_solutii.append(norma_sol3)

# 4
a4 = methods.read_matrix_from_file(a4_filename)
f4 = methods.read_vector_from_file(f4_filename)

methods.verificare_posibilitate_calul(a4[3])
n4 = a4[0]
print("n4: ", n4)
matrix = methods.convert_vectors_in_sparse_matrix_list(a4[3][0], a4[3][1], a4[3][2], a4[0], a4[1], a4[2])
print("a4: ", matrix)
x4 = methods.gauss_seidel(matrix, f4, n4)
print("x4: ", x4)
print("f4: ", f4)
norma_sol4 = methods.calcul_norma(matrix, x4, f4, n4)
print("Norma 4: ", norma_sol4, "\n")
methods.write_solution_to_file("solutions/x4.txt",x4)
norme_solutii.append(norma_sol4)

# 5
a5 = methods.read_matrix_from_file(a5_filename)
f5 = methods.read_vector_from_file(f5_filename)

methods.verificare_posibilitate_calul(a5[3])
n5 = a5[0]
print("n5: ", n5)
matrix = methods.convert_vectors_in_sparse_matrix_list(a5[3][0], a5[3][1], a5[3][2], a5[0], a5[1], a5[2])
print("a5: ", matrix)
x5 = methods.gauss_seidel(matrix, f5, n5)
print("x5: ", x5)
print("f5: ", f5)
norma_sol5 = methods.calcul_norma(matrix, x5, f5, n5)
print("Norma 5: ", norma_sol5)
print(x5[1035])
methods.write_solution_to_file("solutions/x5.txt",x5)
norme_solutii.append(norma_sol5)

methods.write_solution_to_file("solutions/norme.txt",norme_solutii)
methods.gui_interface_norme(norme_solutii)