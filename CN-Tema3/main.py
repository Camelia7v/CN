import copy
import methods

# memorare matricea b
with open("b.txt", 'r') as f:
# with open("bTestCase.txt", 'r') as f:
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
with open("a.txt", 'r') as f:
# with open("aTestCase.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    m = methods.create_empty_list_of_dicts(n)
    for i in range(2,  7108):  # 14):
        if int(lines[i].split(',')[2]) in m[int(lines[i].split(',')[1])]:
            aux = m[int(lines[i].split(',')[1])].get(int(lines[i].split(',')[2]))
            m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = aux + float(lines[i].split(',')[0])
        else:
            m[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

print("m: ", len(m), m, "\n")

# adunarea matricelor A+B
aplusb = copy.deepcopy(m)
for i in range(0, len(aplusb)):
    for j in aplusb[i].keys():
        if i == j:
            aux = aplusb[i].get(j)
            aplusb[i][j] = aux + a[i]
        if j - i == q:
            aux = aplusb[i].get(j)
            aplusb[i][j] = aux + b[i]
        if i - j == p:
            aux = aplusb[i].get(j)
            aplusb[i][j] = aux + c[j]

for i in range(0, len(a)):
    for j in aplusb[i].keys():
        if i != j and i not in aplusb[i] and a[i] != 0.0:
            aplusb[i][i] = a[i]
            break

for i in range(0, len(b)):
    for j in aplusb[i].keys():
        if i + 1 != j and i + 1 not in aplusb[i] and b[i] != 0.0:
            aplusb[i][i + 1] = b[i]
            break

for i in range(0, len(c)):
    for j in aplusb[i + 1].keys():
        if i != j and i not in aplusb[i + 1] and c[i] != 0.0:
            aplusb[i + 1][i] = c[i]
            break

# print("A + B: ", "\n", aplusb, "\n")

# sortare apusb
sorted_aplusb = methods.sort_matrix(aplusb)

print("sorted A + B", "\n", sorted_aplusb, "\n")

# memorare matricea aplusb
with open("aplusb.txt", 'r') as f:
# with open("aplusbTestCase.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    aplusb_din_fisier = methods.create_empty_list_of_dicts(n)
    for i in range(2, 11143):  # 18):
        aplusb_din_fisier[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

print("A + B din fisier: ", "\n", aplusb_din_fisier)

# verificare
methods.equal(aplusb_din_fisier, sorted_aplusb)


# inmultirea matricelor A * B
aorib = copy.deepcopy(m)
aorib = methods.sort_matrix(aorib)
m1 = methods.create_empty_list_of_dicts(n)
for i in range(0, len(m1)):
    for j in range(0, len(m1)):
        if i == j:
            m1[i][j] = a[i]
        if j - i == q:
            m1[i][j] = b[i]
        if i - j == p:
            m1[i][j] = c[j]
# print("A: ", "\n", m)
# print("B: ", "\n", m1)

# for i in range(0, len(aorib)):
#     for j in set(range(0, n)) - set(aorib[i].keys()):
#         aorib[i][j] = 0.0

for i in range(0, len(aorib)):
    for j in aorib[i].keys():
        suma = 0
        for l in m1[j].keys():
            prod = 0
            if j != l:
                continue
            for k in range(0, len(m1)):
                if j == l == k:
                    prod = aorib[i][j] * m1[k][l]
                # if j-l == q == k:
                #     prod = aorib[i][j] * m1[k][l]
                # if l-j == l == k:
                #     prod = aorib[i][j] * m1[k][l]
            suma += prod
        aorib[i].update({j: suma})
        # aorib[i][j] = suma


# for i in range(0, len(m1)):
#     for j in m1[i].keys():
#         suma = 0
#         for l in aorib[j].keys():
#             prod = 0
#             for k in range(0, len(aorib)):
#                 if j == l == k:
#                     prod = m1[i][j] * aorib[k][l]
#             suma += prod
#         if aorib[i][j] == 0.0:
#             aorib[i].update({j: suma})



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


print("A * B: ", "\n", aorib)

# memorare matricea aorib
# with open("aoribTestCase.txt", 'r') as f:
with open("aorib.txt", 'r') as f:
    lines = f.readlines()
    n = int(lines[0])
    aorib_din_fisier = methods.create_empty_list_of_dicts(n)
    for i in range(2, 21285):
        aorib_din_fisier[int(lines[i].split(',')[1])][int(lines[i].split(',')[2])] = float(lines[i].split(',')[0])

print("A * B din fisier: ", "\n", aorib_din_fisier)

methods.equal(aorib, aorib_din_fisier)
