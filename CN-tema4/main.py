a1_filename="files/a1.txt"
a2_filename="files/a2.txt"
a3_filename="files/a3.txt"
a4_filename="files/a4.txt"
a5_filename="files/a5.txt"

f1_filename="files/f1.txt"
f2_filename="files/f2.txt"
f3_filename="files/f3.txt"
f4_filename="files/f4.txt"
f5_filename="files/f5.txt"
import methods
epsilon = 10 **(-13)
a1=methods.read_matrix_from_file(a1_filename)[0]
a2=methods.read_matrix_from_file(a2_filename)[0]
a3=methods.read_matrix_from_file(a3_filename)[0]
a4=methods.read_matrix_from_file(a4_filename)[0]
a5=methods.read_matrix_from_file(a5_filename)[0]

f1=methods.read_vector_from_file(f1_filename)
f2=methods.read_vector_from_file(f2_filename)
f3=methods.read_vector_from_file(f3_filename)
f4=methods.read_vector_from_file(f4_filename)
f5=methods.read_vector_from_file(f5_filename)
# CERINTA 1
#Sa se calculeze cu Gauss-Seidel solutia sistemului Ax=f
#pt A =ai.txt si f=fi.txt
# CERINTA 2
#Sa se verifice soultia xG, cu norma  ||A*xG-f|| (se poate folosi si norma din biblioteca)

#A matrice rara
#un singur xG
# memorare matricea b

print(a1)


