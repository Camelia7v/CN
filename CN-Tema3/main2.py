import copy
import methods

# memorare matricea b
with open("bTestCase.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    p = int(lines[1])
    q = int(lines[2])
    a = list()
    for i in range(4, n + 4):
        a.append(float(lines[i][:-1]))
    b = list()
    for i in range(n + 5, n + 5 + n - 1):
        b.append(float(lines[i][:-1]))
    c = list()
    for i in range(n + 5 + n - 1 + 1, n + 5 + n - 1 + 1 + n - 1):
        c.append(float(lines[i][:-1]))

print("a: ", len(a), a, "\n")
print("b: ", len(b), b, "\n")
print("c: ", len(c), c, "\n")

# memorare matricea a
with open("aTestCase.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    m = methods.create_empty_list_of_dicts(n)
    for i in range(2, 14):
        if int(lines[i].split(',')[2]) in m[int(lines[i].split(',')[1])]:
            aux = m[int(lines[i].split(',')[1])].get(int(lines[i].split(',')[2]))
            m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = aux + float(lines[i].split(',')[0])
        else:
            m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

# memorare matricea aorib
with open("aoribTestCase.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    aorib_din_fisier = methods.create_empty_list_of_dicts(n)
    for i in range(2, 23):
        aorib_din_fisier[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

aorib_fisier = methods.create_empty_dict_of_dicts(n)
for i in aorib_fisier.keys():
    for j in aorib_din_fisier[i].keys():
        aorib_fisier[i][j] = aorib_din_fisier[i][j]

# inmultirea matricelor A * B

matrix1 = methods.convert_vectors_in_sparse_matrix(a,b,c,n,q,p)
matrix = methods.create_empty_dict_of_dicts(n)
for i in matrix.keys():
    for j in m[i].keys():
        matrix[i][j] = m[i][j]
aorib = copy.deepcopy(matrix)

# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]


# luam prima linie din aorib[0]
# luam valorile din aorib[0] -> aorib[0][j] unde j=aorib[0].keys()
# count=0
# for i in aorib.keys():
#     if count == 2: break
#     print("I:", i)
#     j=0
#     index=0
#     while j < max(aorib[i].keys()):
#     # for j in aorib[i].keys():
#         print("J:", j)
#         suma=0.0
#         for k in matrix1.keys():
#             print("K:", k)
#             for l in matrix1[k].keys():
#                 print("L:", l)
#                 print("Suma ",suma)
#                 if j not in aorib[i] or j not in matrix1[i]:
#                     suma += 0.0
#                     j += 1
#                 else:
#                     suma += aorib[i][j] * matrix1[k][l]
#                     print("A*B valoare:", aorib[i][j])
#                     print("B valoare:", matrix1[k][l])
#                     index=j
#                     print("INDEX",index)
#                     j += 1
#
#                 print("Suma ",suma)
#         aorib[i].update({index: suma})
#         count+=1


for i in aorib.keys():
    # print(aorib[i])
    print("next")
    print("I:",i)
    for j in matrix1[i].keys():
        suma = 0
        print("J:",j)

        for l in matrix1.keys():
            # print("--->>")
            print("L",l)
            prod = 0
            if j == l and l in aorib[i].keys():
                # print(aorib[i][l])
                # print(matrix1[l][j])
                prod = aorib[i][l] * matrix1[l][j]
            suma += prod
            # print("=========")
        aorib[i].update({j: suma})



print("A: ", len(m), matrix, "\n")
print("B: ", len(m), matrix1, "\n")
print("A * B: ", "\n", aorib)
print("A * B din fisier: ", "\n", aorib_fisier)

verificare2 = methods.equal(aorib, aorib_fisier)


# X = [[102.5, 0, 2.5, 0, 0],
#      [3.5, 104.88, 1.05, 0, 0.33],
#      [0, 0, 100, 0, 0],
#      [0, 1.3, 0, 101.3, 0],
#      [0.73, 0, 0, 1.5, 102.23]
#      ]
# Y = [[102.5, 2.5, 0, 0, 0],
#      [3.5, 104.88, 1.05, 0, 0],
#      [0, 1.3, 100, 0.33, 0],
#      [0, 0, 0.73, 101.3, 0],
#      [0, 0, 0, 1.5, 102.23]
#      ]
#
# result = [[0, 0, 0, 0, 0] for i in range(0, 5)]
# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]
# print(result)
