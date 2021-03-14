# Să se scrie o funcție care să calculeze produsul a două matrice
# tridiagonale oarecare. Valorile (p,q) sunt oarecare şi diferite pentru fiecare
# matrice: (pA, qA) şi (pB, qB)
import copy

import methods
#n,p,q,[a,b,c]
set_matrix1=methods.read_matrix_from_file("bTestCase.txt")
set_matrix2=methods.read_matrix_from_file("bTestCase.txt")
matrix1=set_matrix1[3]
matrix2=set_matrix2[3]
n1=set_matrix1[0]
n2=set_matrix2[0]
p1=set_matrix1[1]
q1=set_matrix2[2]
p2=set_matrix1[1]
q2=set_matrix2[2]
matrix_rezultat=methods.read_matrix("inmTestCase.txt")

a=list()
b=list()
c=list()
aux=0.0

#indiferent de q si p, vectori a vor contine mereu diagonalele principale
for i in range(0, len(matrix1[0])):
    for j in range(0, len(matrix2[0])):
        aux=matrix1[0][i]*matrix2[0][j]
    a.append(aux)
aux=0.0
#ISSUE p1==q1 si p2==q2, DAR p1,p2 si respectiv q1,q2 POT fi diferite intre ele
#celelalte diagonale in functie de p si q
for i in range(0, len(matrix1[1])):
    for j in range(0, len(matrix2[1])):
        if i-j == p1:
            aux = matrix1[1][i] * matrix2[1][j]
        if j-i == q1:
            aux = matrix1[1][i] * matrix2[1][j-1]
    b.append(aux)
aux=0.0

for i in range(0, len(matrix1[2])):
    for j in range(0, len(matrix2[2])):
        if i-j == p2:
            aux = matrix1[1][i] * matrix2[2][j]
        if j - i == q2:
            aux = matrix1[2][i] * matrix2[2][j-1]
    c.append(aux)
rezultat=methods.convert_vectors_in_sparse_matrix(a,b,c,n1,q1,q2)

print("Matricea din fisier : " ,matrix_rezultat)
print("a : " ,a)
print("b : " ,b)
print("c : " ,c)
print("Matricea obtinuta : " ,rezultat)
