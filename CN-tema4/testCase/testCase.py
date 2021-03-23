import methods

# testCase din pdf
a = methods.read_matrix_from_file("bonus.txt")
f = methods.read_vector_from_file("f.txt")

methods.verificare_posibilitate_calul(a[3])
n = a[0]
print("n: ", n)
matrix = methods.convert_vectors_in_sparse_matrix_list(a[3][0], a[3][1], a[3][2], a[0], a[1], a[2])
print("a: ", matrix)
x = methods.gauss_seidel(matrix, f, n)
print("x: ", x)
print("f: ", f)
norma_sol = methods.calcul_norma(matrix, x, f, n)
print("Norma: ", norma_sol)
